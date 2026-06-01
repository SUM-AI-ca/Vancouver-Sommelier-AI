"""
Sutton Place Wine Merchant Search Tool for BC Wine AI Agent (LangGraph)

Uses the public JSON API at store.suttonplacewinemerchant.com (Barnet Network).
Same platform as Okanagan Cellars — identical API structure, different shop ID.
No login required.

Store location:
- 1168 Hamilton St, Vancouver, BC (Yaletown)
"""

import asyncio
import time
import httpx
from pydantic import BaseModel

from .query_fallback import search_with_fallback


# ── Config ──────────────────────────────────────────────────────────

BASE_URL = "https://store.suttonplacewinemerchant.com"
API_URL = f"{BASE_URL}/api/shop/124-229/products"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/125.0.0.0 Safari/537.36"
    ),
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "X-Requested-With": "XMLHttpRequest",
    "Referer": f"{BASE_URL}/products",
}


# ── Data Model ──────────────────────────────────────────────────────

class SuttonPlaceResult(BaseModel):
    name: str
    category: str | None = None          # "RED USA", "WHITE BC"
    sale_price: str | None = None
    regular_price: str | None = None
    on_sale: bool = False
    in_stock: bool = False
    stock_qty: int | None = None
    unit_size: str | None = None         # "750ML Bottle"
    product_url: str | None = None
    image_url: str | None = None
    country: str | None = None           # "USA", "CANADA", "FRANCE"
    varietal: str | None = None          # "Pinot Noir", "Riesling"
    vintage: int | None = None           # 2014
    alcohol_pct: str | None = None       # "14.40"
    is_staff_pick: bool = False
    is_featured: bool = False


# ── Core Search ─────────────────────────────────────────────────────

async def _search_once(client: httpx.AsyncClient, query: str) -> list[SuttonPlaceResult]:
    """One API call + parse for an already-cleaned query string."""
    params = {
        "q": query,
        "show_on_web": "true",
        "varital_name": "",
        "no_item_found": "No item found.",
        "avail_for_sale": "false",
        "_dc": str(int(time.time() * 1000)),
    }

    resp = await client.get(API_URL, params=params)
    resp.raise_for_status()
    data = resp.json()

    items = data.get("items", [])
    results: list[SuttonPlaceResult] = []

    for item in items:
        sale = item.get("sale_price", "0")
        regular = item.get("regular_price", "0")
        on_sale = item.get("is_sale", False)

        def fmt_price(p: str | None) -> str | None:
            if not p:
                return None
            try:
                return f"{float(p):.2f}"
            except (ValueError, TypeError):
                return p

        on_hand = item.get("on_hand", 0)
        image_path = item.get("image", "")
        image_url = f"{BASE_URL}/static/{image_path}" if image_path else None

        raw_vintage = item.get("vintage")
        vintage = None
        if raw_vintage is not None:
            try:
                vintage = int(raw_vintage)
                if vintage == 0:
                    vintage = None
            except (ValueError, TypeError):
                vintage = None

        results.append(
            SuttonPlaceResult(
                name=item.get("description", "Unknown"),
                category=item.get("category_name"),
                sale_price=fmt_price(sale),
                regular_price=fmt_price(regular),
                on_sale=on_sale,
                in_stock=on_hand > 0,
                stock_qty=on_hand,
                unit_size=item.get("unit_name"),
                product_url=item.get("url"),
                image_url=image_url,
                country=item.get("country_name"),
                varietal=item.get("varital_name"),
                vintage=vintage,
                alcohol_pct=fmt_price(item.get("alcohol")),
                is_staff_pick=item.get("is_staff_picks", False),
                is_featured=item.get("is_featured", False),
            )
        )

    return results


async def search_suttonplace(query: str) -> list[SuttonPlaceResult]:
    """
    Search Sutton Place Wine Merchant inventory.

    Same Barnet Network backend as Okanagan Cellars — AND-matches all tokens.
    search_with_fallback retries with progressively trimmed queries.
    Apostrophes are stripped by the default clean_query (e.g. "martin's lane" → "martins lane").

    Args:
        query: Wine name, winery, or varietal (e.g., "pinot noir", "mission hill")
    """
    async with httpx.AsyncClient(timeout=15.0, headers=HEADERS) as client:
        return await search_with_fallback(lambda q: _search_once(client, q), query)


# ── Formatting ──────────────────────────────────────────────────────

def format_results(results: list[SuttonPlaceResult], query: str) -> str:
    if not results:
        return f"No products found at Sutton Place Wine Merchant for '{query}'."

    lines = [f"Sutton Place Wine Merchant: {len(results)} results for '{query}'\n"]

    for i, r in enumerate(results, 1):
        parts = [f"{i}. {r.name}"]

        if r.on_sale and r.sale_price and r.regular_price:
            parts.append(f"   Price: ${r.sale_price} (was ${r.regular_price} — ON SALE)")
        elif r.sale_price:
            parts.append(f"   Price: ${r.sale_price}")

        if r.category:
            parts.append(f"   Category: {r.category}")
        if r.varietal:
            parts.append(f"   Varietal: {r.varietal}")
        if r.vintage:
            parts.append(f"   Vintage: {r.vintage}")
        if r.country:
            parts.append(f"   Country: {r.country}")
        if r.unit_size:
            parts.append(f"   Size: {r.unit_size}")
        if r.alcohol_pct:
            parts.append(f"   Alcohol: {r.alcohol_pct}%")

        stock_str = f"In Stock ({r.stock_qty})" if r.in_stock else "Out of Stock"
        parts.append(f"   Stock: {stock_str}")

        flags = []
        if r.is_staff_pick:
            flags.append("Staff Pick")
        if r.is_featured:
            flags.append("Featured")
        if flags:
            parts.append(f"   Tags: {', '.join(flags)}")

        if r.product_url:
            parts.append(f"   URL: {r.product_url}")

        lines.append("\n".join(parts))

    return "\n\n".join(lines)


# ── Standalone Test ─────────────────────────────────────────────────

async def main():
    for query in ["pinot noir", "tantalus", "martin's lane"]:
        print(f"Searching '{query}'...\n")
        results = await search_suttonplace(query)
        print(format_results(results, query))
        print("\n" + "=" * 60 + "\n")


if __name__ == "__main__":
    asyncio.run(main())
