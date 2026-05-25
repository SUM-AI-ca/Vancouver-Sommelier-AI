"""
Robert Parker Wine Search Tool for BC Wine AI Agent (LangGraph)

Searches Robert Parker's wine database via their Algolia-backed REST API.
Returns professional ratings, detailed tasting notes, drink windows, and pricing
from one of the world's most authoritative wine review publications.

Requires an active Robert Parker subscription. Set in .env:
  ROBERT_PARKER_EMAIL    — login email
  ROBERT_PARKER_PASSWORD — login password
  ROBERT_PARKER_API_KEY  — public API key (rarely changes)
"""

import asyncio
import os
from datetime import datetime

import httpx
from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()


# ── Config ──────────────────────────────────────────────────────────

RP_API_BASE = "https://api.robertparker.com/v2/v2"
RP_API_KEY = os.getenv("ROBERT_PARKER_API_KEY", "")
RP_EMAIL = os.getenv("ROBERT_PARKER_EMAIL", "")
RP_PASSWORD = os.getenv("ROBERT_PARKER_PASSWORD", "")

HEADERS_BASE = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/148.0.0.0 Safari/537.36 Edg/148.0.0.0"
    ),
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Origin": "https://www.robertparker.com",
    "Referer": "https://www.robertparker.com/",
    "x-api-key": RP_API_KEY,
    "authorizationtoken": "allow",
}


# ── Data Models ────────────────────────────────────────────────────

class RobertParkerTastingNote(BaseModel):
    reviewer: str
    rating: str
    content: str
    published_at: str | None = None
    article_title: str | None = None
    producer_note: str | None = None


class RobertParkerResult(BaseModel):
    wine_id: str
    display_name: str
    producer: str
    name: str
    vintage: int | None = None
    color_class: str
    country: str
    region: str
    sub_region: str | None = None
    appellation: str | None = None
    sub_appellation: str | None = None
    varieties: list[str] = []
    rating_display: str
    rating_computed: float
    price_low: float | None = None
    price_high: float | None = None
    drink_date_low: int | None = None
    drink_date_high: int | None = None
    dryness: str | None = None
    wine_type: str | None = None
    certified: list[str] = []
    last_reviewer: str | None = None
    tasting_notes: list[RobertParkerTastingNote] = []
    slug: str | None = None


# ── Session Manager ────────────────────────────────────────────────

class _RobertParkerSession:
    def __init__(self):
        self._token: str | None = None
        self._client: httpx.AsyncClient | None = None

    async def _ensure_client(self) -> httpx.AsyncClient:
        if self._client is None:
            self._client = httpx.AsyncClient(timeout=20.0)
        if not self._token:
            await self._login()
        return self._client

    def _auth_headers(self) -> dict:
        return {
            **HEADERS_BASE,
            "authorization": f"Bearer {self._token}",
        }

    async def _login(self):
        if not RP_EMAIL or not RP_PASSWORD:
            raise ValueError(
                "Set ROBERT_PARKER_EMAIL and ROBERT_PARKER_PASSWORD in .env"
            )

        client = self._client or httpx.AsyncClient(timeout=20.0)
        if self._client is None:
            self._client = client

        csrf_resp = await client.get(
            f"{RP_API_BASE}/users/csrf-token",
            headers=HEADERS_BASE,
        )
        csrf_resp.raise_for_status()
        csrf_token = csrf_resp.json()["data"]["token"]

        login_resp = await client.post(
            f"{RP_API_BASE}/users/login",
            json={
                "username": RP_EMAIL,
                "password": RP_PASSWORD,
                "device": "Web | python-tool",
            },
            headers={**HEADERS_BASE, "xsrf-token": csrf_token},
        )

        if login_resp.status_code != 200:
            raise ValueError(
                f"Robert Parker login failed ({login_resp.status_code}). "
                "Check ROBERT_PARKER_EMAIL / ROBERT_PARKER_PASSWORD in .env."
            )

        data = login_resp.json().get("data", {})
        access = data.get("accessDetails", {})
        self._token = access.get("accessToken")

        if not self._token:
            raise ValueError(
                "Robert Parker login succeeded but no accessToken returned. "
                "Check subscription status."
            )

    async def request(
        self, method: str, path: str, **kwargs
    ) -> httpx.Response:
        client = await self._ensure_client()
        url = f"{RP_API_BASE}{path}"
        resp = await client.request(
            method, url, headers=self._auth_headers(), **kwargs
        )

        if resp.status_code == 401:
            self._token = None
            await self._login()
            resp = await client.request(
                method, url, headers=self._auth_headers(), **kwargs
            )

        return resp

    async def close(self):
        if self._client:
            await self._client.aclose()
            self._client = None
            self._token = None


_session = _RobertParkerSession()


# ── Response Parser ────────────────────────────────────────────────

def _parse_hit(hit: dict) -> RobertParkerResult:
    tasting_notes: list[RobertParkerTastingNote] = []
    for tn in hit.get("tasting_notes_history", []):
        reviewer_name = tn.get("reviewer", {}).get("name", "Unknown")
        rating = tn.get("rating_display", "")
        content = tn.get("content", "")
        published_ts = tn.get("published_at")
        published_at = None
        if published_ts:
            try:
                published_at = datetime.fromtimestamp(
                    published_ts / 1000
                ).strftime("%Y-%m-%d")
            except (ValueError, OSError):
                pass
        articles = tn.get("article", [])
        article_title = articles[0].get("title") if articles else None
        producer_note = tn.get("producer_note")

        tasting_notes.append(
            RobertParkerTastingNote(
                reviewer=reviewer_name,
                rating=rating,
                content=content,
                published_at=published_at,
                article_title=article_title,
                producer_note=producer_note,
            )
        )

    return RobertParkerResult(
        wine_id=hit.get("_id", ""),
        display_name=hit.get("display_name", ""),
        producer=hit.get("producer", ""),
        name=hit.get("name", ""),
        vintage=hit.get("vintage"),
        color_class=hit.get("color_class", ""),
        country=hit.get("country", ""),
        region=hit.get("region", ""),
        sub_region=hit.get("sub_region") or None,
        appellation=hit.get("appellation") or None,
        sub_appellation=hit.get("sub_appellation") or None,
        varieties=hit.get("varieties", []),
        rating_display=hit.get("rating_display", ""),
        rating_computed=hit.get("rating_computed", 0),
        price_low=hit.get("price_low"),
        price_high=hit.get("price_high"),
        drink_date_low=hit.get("drink_date_low"),
        drink_date_high=hit.get("drink_date_high"),
        dryness=hit.get("dryness"),
        wine_type=hit.get("type"),
        certified=hit.get("certified", []),
        last_reviewer=hit.get("last_reviewer"),
        tasting_notes=tasting_notes,
        slug=hit.get("slug") or None,
    )


# ── Filter Builder ─────────────────────────────────────────────────

def _build_filters(
    rating_min: int,
    country: str | None,
    region: str | None,
    color: str | None,
    variety: str | None,
) -> str:
    parts = [f"rating_computed:{rating_min} TO 100"]
    if country:
        parts.append(f"country:{country}")
    if region:
        parts.append(f"region:'{region}'")
    if color:
        parts.append(f"color_class:{color}")
    if variety:
        parts.append(f"varieties:'{variety}'")
    return " AND ".join(parts)


# ── Core Search ────────────────────────────────────────────────────

async def search_robert_parker(
    query: str,
    rating_min: int = 50,
    hits_per_page: int = 10,
    page: int = 0,
    sort: str = "relevancy",
    country: str | None = None,
    region: str | None = None,
    color: str | None = None,
    variety: str | None = None,
) -> list[RobertParkerResult]:
    """
    Search Robert Parker's wine database (Algolia-backed API).

    Args:
        query:         Wine name, producer, region, or grape
                       (e.g. "pinot noir okanagan", "martin's lane")
        rating_min:    Minimum RP rating (50–100, default 50)
        hits_per_page: Results per page (default 10, max 50)
        page:          Zero-based page number for pagination
        sort:          "relevancy" (default) or "rating" or "vintage" or "price"
        country:       Filter — e.g. "Canada"
        region:        Filter — e.g. "British Columbia" (quote-wrapped automatically)
        color:         Filter — e.g. "Red", "White", "Rosé"
        variety:       Filter — e.g. "Pinot Noir", "Riesling" (quote-wrapped automatically)

    Returns:
        list[RobertParkerResult] with tasting notes, ratings, drink windows.
    """
    payload = {
        "query": query,
        "filters": _build_filters(rating_min, country, region, color, variety),
        "page": page,
        "facets": ["*"],
        "facetFilters": [],
        "hitsPerPage": min(hits_per_page, 50),
        "sortFacetValuesBy": "count",
    }

    resp = await _session.request(
        "POST",
        f"/algolia?sort={sort}&type=wine",
        json=payload,
    )
    resp.raise_for_status()
    data = resp.json()

    hits = data.get("data", {}).get("hits", [])
    return [_parse_hit(h) for h in hits]


# ── Formatting ─────────────────────────────────────────────────────

def format_results(results: list[RobertParkerResult], query: str) -> str:
    if not results:
        return f"No Robert Parker reviews found for '{query}'."

    lines = [f"Robert Parker: {len(results)} results for '{query}'\n"]

    for i, r in enumerate(results, 1):
        parts = [f"{i}. {r.display_name}  (RP {r.rating_display})"]

        if r.region:
            region_str = r.region
            if r.sub_region:
                region_str += f" > {r.sub_region}"
            if r.appellation:
                region_str += f" > {r.appellation}"
            parts.append(f"   Region: {region_str}")

        if r.varieties:
            parts.append(f"   Grape: {', '.join(r.varieties)}")

        if r.price_low is not None:
            if r.price_low == r.price_high:
                parts.append(f"   Price: ${r.price_low:.0f}")
            else:
                parts.append(
                    f"   Price: ${r.price_low:.0f}–${r.price_high:.0f}"
                )

        if r.drink_date_low and r.drink_date_high:
            parts.append(
                f"   Drink: {r.drink_date_low}–{r.drink_date_high}"
            )

        if r.certified:
            parts.append(f"   Certified: {', '.join(r.certified)}")

        for tn in r.tasting_notes:
            parts.append(
                f"   --- {tn.reviewer} ({tn.rating}) "
                f"[{tn.published_at or 'N/A'}] ---"
            )
            note = tn.content.strip()
            if len(note) > 300:
                note = note[:300].rstrip() + "..."
            parts.append(f"   {note}")

        lines.append("\n".join(parts))

    return "\n\n".join(lines)


# ── Standalone Test ────────────────────────────────────────────────

async def main():
    test_cases = [
        ("martin's lane", {}),
        (
            "pinot noir",
            {
                "country": "Canada",
                "region": "British Columbia",
                "rating_min": 90,
                "hits_per_page": 5,
            },
        ),
        ("riesling", {"country": "Canada", "rating_min": 90, "hits_per_page": 5}),
    ]
    for query, kwargs in test_cases:
        print(f"Searching '{query}' with filters {kwargs}...\n")
        try:
            results = await search_robert_parker(query, **kwargs)
            print(format_results(results, query))
        except Exception as e:
            print(f"  Error: {e}")
        print("\n" + "=" * 70 + "\n")


if __name__ == "__main__":
    asyncio.run(main())
