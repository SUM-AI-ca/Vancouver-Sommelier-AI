"""
WineAlign Search Tool for BC Wine AI Agent (LangGraph)

Features:
- Session-based login (authenticity_token + person_credentials cookie)
- Pagination support (all pages or capped)
- Critic reviews from wine detail pages
"""

import os
import re
import asyncio
import httpx
from bs4 import BeautifulSoup, Tag
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()

# ── Config ──────────────────────────────────────────────────────────

WINEALIGN_EMAIL = os.getenv("WINEALIGN_EMAIL", "")
WINEALIGN_PASSWORD = os.getenv("WINEALIGN_PASSWORD", "")
BASE_URL = "https://www.winealign.com"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/125.0.0.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
}

# Polite delay between requests (seconds)
REQUEST_DELAY = 0.5


# ── Data Models ─────────────────────────────────────────────────────

class CriticReview(BaseModel):
    critic_name: str
    score: str | None = None
    tasting_notes: str | None = None
    value_rating: int | None = None  # number of stars (0-5)
    drink_window: str | None = None

class WineAlignResult(BaseModel):
    wine_name: str
    appellation: str | None = None
    score: str | None = None          # aggregate/display score from search
    price: str | None = None
    url: str | None = None
    thumbnail_url: str | None = None
    critic_reviews: list[CriticReview] = []


# ── Session Manager ────────────────────────────────────────────────

class WineAlignSession:
    def __init__(self):
        self._client: httpx.AsyncClient | None = None
        self._logged_in = False

    async def _ensure_client(self) -> httpx.AsyncClient:
        if self._client is None:
            self._client = httpx.AsyncClient(
                follow_redirects=False,  # We handle redirects manually
                timeout=15.0,
                headers=HEADERS,
            )
        if not self._logged_in:
            await self._login()
        return self._client

    async def _login(self):
        if not WINEALIGN_EMAIL or not WINEALIGN_PASSWORD:
            raise ValueError("Set WINEALIGN_EMAIL and WINEALIGN_PASSWORD in .env")

        client = self._client

        # GET /login → grab authenticity_token
        r = await client.get(f"{BASE_URL}/login")
        soup = BeautifulSoup(r.text, "html.parser")
        form = soup.select_one("form#login_form")
        if not form:
            raise ValueError("Login form not found")
        token_el = form.select_one('input[name="authenticity_token"]')
        token = token_el["value"] if token_el else ""

        # POST /login → get person_credentials cookie (ignore 302 redirect)
        await client.post(
            f"{BASE_URL}/login",
            data={
                "utf8": "✓",
                "authenticity_token": token,
                "email": WINEALIGN_EMAIL,
                "password": WINEALIGN_PASSWORD,
            },
            headers={
                **HEADERS,
                "Content-Type": "application/x-www-form-urlencoded",
                "Referer": f"{BASE_URL}/login",
                "Origin": BASE_URL,
            },
        )

        if "person_credentials" not in dict(client.cookies):
            raise ValueError("Login failed — no person_credentials cookie. Check credentials.")

        self._logged_in = True

    async def _get(self, url: str, **kwargs) -> httpx.Response:
        """GET with auto-relogin on session expiry."""
        client = await self._ensure_client()
        resp = await client.get(url, **kwargs)

        # Follow one redirect if not back to login
        if resp.status_code in (301, 302, 303):
            location = resp.headers.get("location", "")
            if "/login" in location:
                # Session expired — relogin
                self._logged_in = False
                client = await self._ensure_client()
                resp = await client.get(url, **kwargs)
            else:
                if not location.startswith("http"):
                    location = f"{BASE_URL}{location}"
                resp = await client.get(location)

        return resp

    async def close(self):
        if self._client:
            await self._client.aclose()
            self._client = None
            self._logged_in = False


# ── Parsers ─────────────────────────────────────────────────────────

def _parse_appellation(alt_text: str) -> str | None:
    if not alt_text:
        return None
    match = re.search(r",\s*(.+?)(?:\s+Bottle)?$", alt_text)
    return match.group(1).strip() if match else None


def _parse_drink_window(text: str) -> str | None:
    """Extract 'Drink 2025-2032' pattern from tasting notes."""
    match = re.search(r"[Dd]rink\s+(\d{4}\s*[-–]\s*\d{4})", text)
    return match.group(0).strip() if match else None


def _parse_search_page(html: str) -> tuple[list[WineAlignResult], int]:
    """
    Parse a single search results page.
    Returns (results, total_count).
    """
    soup = BeautifulSoup(html, "html.parser")

    # Total count: "Displaying results 1 - 10 of 9853 in total"
    total = 0
    pagination_el = soup.select_one("div.pg_pagination")
    if pagination_el:
        text = pagination_el.get_text()
        match = re.search(r"of\s+([\d,]+)\s+in total", text)
        if match:
            total = int(match.group(1).replace(",", ""))

    container = soup.select_one("div.container.winelist")
    if not container:
        return [], total

    results: list[WineAlignResult] = []

    for row in container.select("a.row"):
        name_el = row.select_one("h5.link")
        if not name_el:
            continue

        wine_name = name_el.get_text(strip=True)

        # URL
        href = row.get("href", "")
        url = href if href.startswith("http") else f"{BASE_URL}{href}"

        # Thumbnail & Appellation
        thumb_el = row.select_one("div.bottle_thumbnail img")
        thumbnail_url = thumb_el.get("src") if thumb_el else None
        alt_text = thumb_el.get("alt", "") if thumb_el else ""
        appellation = _parse_appellation(alt_text)

        # Score
        score_el = row.select_one("div.score")
        score = None
        if score_el:
            score_img = score_el.select_one("img")
            if score_img:
                score = score_img.get("title") or score_img.get("alt")
            if not score:
                score = score_el.get_text(strip=True) or None

        # Price
        price_el = row.select_one("div.price")
        price = price_el.get_text(strip=True) if price_el else None

        results.append(
            WineAlignResult(
                wine_name=wine_name,
                appellation=appellation,
                score=score,
                price=price,
                url=url,
                thumbnail_url=thumbnail_url,
            )
        )

    return results, total


def _parse_critic_reviews(html: str) -> list[CriticReview]:
    """Parse critic reviews from a wine detail page."""
    soup = BeautifulSoup(html, "html.parser")
    reviews: list[CriticReview] = []

    for review_div in soup.select("div.person-review"):
        # Skip empty placeholder divs
        if not review_div.find_all(True):
            continue

        # Critic name
        name_el = review_div.select_one("div.copy a")
        if not name_el:
            continue
        critic_name = name_el.get_text(strip=True)

        # Tasting notes — grab entire paywalled div text (may have multiple <p> tags)
        paywalled_el = review_div.select_one("div.paywalled")
        tasting_notes = None
        if paywalled_el:
            # Get all <p> text, exclude the value_rating div
            paragraphs = paywalled_el.select("p")
            if paragraphs:
                tasting_notes = " ".join(p.get_text(strip=True) for p in paragraphs)

        # Drink window (extracted from tasting notes)
        drink_window = _parse_drink_window(tasting_notes) if tasting_notes else None

        # Score
        score_el = review_div.select_one("div.rating img")
        score = None
        if score_el:
            score = score_el.get("title") or score_el.get("alt")

        # Value rating (star count)
        value_div = review_div.select_one("div.review_value_rating")
        value_rating = None
        if value_div:
            stars = value_div.select("span.fa-star")
            value_rating = len(stars)

        reviews.append(
            CriticReview(
                critic_name=critic_name,
                score=score,
                tasting_notes=tasting_notes,
                value_rating=value_rating,
                drink_window=drink_window,
            )
        )

    return reviews


# ── Main Search Function ───────────────────────────────────────────

_session = WineAlignSession()


def _clean_query(q: str) -> str:
    """Strip apostrophes / smart quotes for consistency with the store tools."""
    return q.replace("'", "").replace("’", "").replace("‘", "")


async def search_winealign(
    query: str,
    max_pages: int = 3,
    include_reviews: bool = True,
) -> list[WineAlignResult]:
    """
    Search WineAlign with pagination and optional critic reviews.

    Args:
        query:           Search term (wine name, winery, varietal)
        max_pages:       Max pages to fetch (10 results per page)
        include_reviews: If True, fetch each wine's detail page for critic reviews
    """
    all_results: list[WineAlignResult] = []
    total_count = 0

    for page in range(1, max_pages + 1):
        resp = await _session._get(
            f"{BASE_URL}/search",
            params={"q": _clean_query(query), "page": page},
        )

        if resp.status_code != 200:
            break

        results, total = _parse_search_page(resp.text)
        if page == 1:
            total_count = total

        if not results:
            break

        all_results.extend(results)

        # Stop if we've collected all results
        if len(all_results) >= total_count:
            break

        await asyncio.sleep(REQUEST_DELAY)

    # Fetch critic reviews for each wine
    if include_reviews and all_results:
        for wine in all_results:
            if not wine.url:
                continue
            try:
                detail_resp = await _session._get(wine.url)
                if detail_resp.status_code == 200:
                    wine.critic_reviews = _parse_critic_reviews(detail_resp.text)
            except Exception as e:
                print(f"  [Warning] Failed to fetch reviews for {wine.wine_name}: {e}")
            await asyncio.sleep(REQUEST_DELAY)

    return all_results


async def get_wine_reviews(wine_url: str) -> list[CriticReview]:
    """Fetch critic reviews for a single wine by URL."""
    resp = await _session._get(wine_url)
    if resp.status_code != 200:
        return []
    return _parse_critic_reviews(resp.text)


# ── LangGraph Tool Wrapper ─────────────────────────────────────────

def format_results(results: list[WineAlignResult], query: str) -> str:
    """Format results as a readable string for the LLM."""
    if not results:
        return f"No results found on WineAlign for '{query}'."

    lines = [f"WineAlign: {len(results)} results for '{query}'\n"]

    for i, r in enumerate(results, 1):
        parts = [f"{i}. {r.wine_name}"]
        if r.score:
            parts.append(f"   Score: {r.score}")
        if r.price:
            parts.append(f"   Price: {r.price}")
        if r.appellation:
            parts.append(f"   Appellation: {r.appellation}")
        if r.url:
            parts.append(f"   URL: {r.url}")

        if r.critic_reviews:
            parts.append(f"   --- Critic Reviews ({len(r.critic_reviews)}) ---")
            for cr in r.critic_reviews:
                parts.append(f"   [{cr.critic_name}] Score: {cr.score or 'N/A'}")
                if cr.tasting_notes:
                    parts.append(f"   {cr.tasting_notes}")
                if cr.drink_window:
                    parts.append(f"   {cr.drink_window}")
                if cr.value_rating is not None:
                    parts.append(f"   Value: {'★' * cr.value_rating}{'☆' * (5 - cr.value_rating)}")

        lines.append("\n".join(parts))

    return "\n\n".join(lines)


# ── Standalone Test ─────────────────────────────────────────────────

async def main():
    try:
        print("Searching 'orofino' with reviews...\n")
        results = await search_winealign("orofino", max_pages=2, include_reviews=True)
        print(format_results(results, "orofino"))
    finally:
        await _session.close()


if __name__ == "__main__":
    asyncio.run(main())
