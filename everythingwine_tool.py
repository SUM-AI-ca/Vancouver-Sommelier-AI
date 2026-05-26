"""
Everything Wine Search Tool for BC Wine AI Agent (LangGraph)

Scrapes search results from everythingwine.ca/catalogsearch/result/.
No login required. Server-side rendered HTML.
"""

import asyncio
import re
import httpx
from bs4 import BeautifulSoup
from pydantic import BaseModel


# ── Config ──────────────────────────────────────────────────────────

BASE_URL = "https://www.everythingwine.ca"
SEARCH_URL = f"{BASE_URL}/catalogsearch/result/"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/148.0.0.0 Safari/537.36 Edg/148.0.0.0"
    ),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
}


# ── Data Model ──────────────────────────────────────────────────────

class StockStatus(BaseModel):
    method: str          # "Warehouse delivery", "Pick up, delivery from store", "Check other stores"
    status: str          # "available", "unavailable", "other-store"

class EverythingWineResult(BaseModel):
    name: str
    price: str | None = None
    regular_price: str | None = None
    on_sale: bool = False
    country: str | None = None
    url: str | None = None
    image_url: str | None = None
    stock: list[StockStatus] = []


# ── Core Search ─────────────────────────────────────────────────────

def _clean_query(q: str) -> str:
    """Strip apostrophes / smart quotes — some store backends silently zero-out
    results when these are present (verified on Okanagan Cellars)."""
    return q.replace("'", "").replace("’", "").replace("‘", "")


async def search_everything_wine(query: str) -> list[EverythingWineResult]:
    """
    Search Everything Wine product catalogue.

    Args:
        query: Wine name, winery, or varietal (e.g., "tantalus", "checkmate chardonnay")
    """
    async with httpx.AsyncClient(follow_redirects=True, timeout=15.0, headers=HEADERS) as client:
        resp = await client.get(SEARCH_URL, params={"q": _clean_query(query)})
        resp.raise_for_status()

    soup = BeautifulSoup(resp.text, "html.parser")
    search_div = soup.select_one("div.search.results")
    if not search_div:
        return []

    results: list[EverythingWineResult] = []

    for item in search_div.select("li.product-item"):
        # Name — <span class="product-item-link">
        name_el = item.select_one("span.product-item-link")
        if not name_el:
            continue
        name = name_el.get_text(strip=True)

        # URL — parent <a class="product-item-info"> href
        link_el = item.select_one("a.product-item-info")
        url = link_el.get("href") if link_el else None

        # Price — <span data-price-amount="30.98">
        price = None
        regular_price = None
        on_sale = False

        price_wrapper = item.select_one("span.price-wrapper[data-price-amount]")
        if price_wrapper:
            price = price_wrapper.get("data-price-amount")

        # Check for sale / old price
        old_price_el = item.select_one(".old-price span.price-wrapper[data-price-amount]")
        if old_price_el:
            regular_price = old_price_el.get("data-price-amount")
            on_sale = True

        sale_div = item.select_one("div.product-item-discount")
        if sale_div and "hide" not in " ".join(sale_div.get("class", [])):
            on_sale = True

        # Country — <span class="product-item-attributes"><span>Canada</span></span>
        country = None
        attr_el = item.select_one("span.product-item-attributes span")
        if attr_el:
            country = attr_el.get_text(strip=True)

        # Image
        img_el = item.select_one("img.product-image-photo")
        image_url = img_el.get("src") if img_el else None

        # Availability — parse stock status from nested spans
        # Structure: <span class="stock product-item-stock">
        #              <span class="stock available">...</span>        ✅
        #              <span class="stock unavailable">...</span>      ❌
        #              <span class="stock store available">...</span>  ✅
        #              <span class="stock other-store">...</span>      ⚠️
        stock: list[StockStatus] = []
        stock_container = item.select_one("span.product-item-stock")
        if stock_container:
            for child in stock_container.find_all("span", class_="stock", recursive=False):
                classes = child.get("class", [])
                text = child.get_text(strip=True)
                if not text or "product-item-stock" in classes:
                    continue

                if "unavailable" in classes:
                    status = "unavailable"
                elif "other-store" in classes:
                    status = "other-store"
                elif "available" in classes:
                    status = "available"
                else:
                    status = "unknown"

                stock.append(StockStatus(method=text, status=status))

        results.append(
            EverythingWineResult(
                name=name,
                price=price,
                regular_price=regular_price,
                on_sale=on_sale,
                country=country,
                url=url,
                image_url=image_url,
                stock=stock,
            )
        )

    return results


# ── Formatting ──────────────────────────────────────────────────────

def format_results(results: list[EverythingWineResult], query: str) -> str:
    if not results:
        return f"No products found at Everything Wine for '{query}'."

    lines = [f"Everything Wine: {len(results)} results for '{query}'\n"]

    for i, r in enumerate(results, 1):
        parts = [f"{i}. {r.name}"]

        if r.on_sale and r.price and r.regular_price:
            parts.append(f"   Price: ${r.price} (was ${r.regular_price} — ON SALE)")
        elif r.price:
            parts.append(f"   Price: ${r.price}")

        if r.country:
            parts.append(f"   Country: {r.country}")
        if r.stock:
            stock_lines = []
            for s in r.stock:
                if s.status == "available":
                    stock_lines.append(f"✅ {s.method}")
                elif s.status == "unavailable":
                    stock_lines.append(f"❌ {s.method}")
                elif s.status == "other-store":
                    stock_lines.append(f"⚠️ {s.method}")
                else:
                    stock_lines.append(f"❓ {s.method}")
            parts.append(f"   Stock: {' | '.join(stock_lines)}")
        if r.url:
            parts.append(f"   URL: {r.url}")

        lines.append("\n".join(parts))

    return "\n\n".join(lines)


# ── Standalone Test ─────────────────────────────────────────────────

async def main():
    for query in ["martins", "synchromesh"]:
        print(f"Searching '{query}'...\n")
        results = await search_everything_wine(query)
        print(format_results(results, query))
        print("\n" + "=" * 60 + "\n")


if __name__ == "__main__":
    asyncio.run(main())
