"""
Okanagan Cellars Search Tool for BC Wine AI Agent (LangGraph)

Uses the public JSON API at okanagancellars.com.
No login required.

Store locations:
- 1811 West 1st Ave, Vancouver, BC
- 3669 West 4th Ave, Vancouver, BC
"""

import asyncio
import time
import httpx
from pydantic import BaseModel


# ── Config ──────────────────────────────────────────────────────────

BASE_URL = "https://okanagancellars.com"
API_URL = f"{BASE_URL}/api/shop/131-41/products"

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

class OkanaganCellarsResult(BaseModel):
    name: str
    category: str | None = None        # "Red Wine", "White Wine", "L/S Format Wines"
    sale_price: str | None = None
    regular_price: str | None = None
    on_sale: bool = False
    in_stock: bool = False
    stock_qty: int | None = None
    unit_size: str | None = None       # "750ml", "1.5L"
    product_url: str | None = None
    image_url: str | None = None


# ── Core Search ─────────────────────────────────────────────────────

async def search_okanagan_cellars(query: str) -> list[OkanaganCellarsResult]:
    """
    Search Okanagan Cellars wine inventory.

    Args:
        query: Wine name, winery, or varietal (e.g., "tantalus", "checkmate", "pinot noir")
    """
    params = {
        "q": query,
        "show_on_web": "true",
        "varital_name": "",
        "no_item_found": "No item found.",
        "avail_for_sale": "false",  # show all, including out-of-stock
        "_dc": str(int(time.time() * 1000)),
    }

    async with httpx.AsyncClient(timeout=15.0, headers=HEADERS) as client:
        resp = await client.get(API_URL, params=params)
        resp.raise_for_status()
        data = resp.json()

    items = data.get("items", [])
    results: list[OkanaganCellarsResult] = []

    for item in items:
        sale = item.get("sale_price", "0")
        regular = item.get("regular_price", "0")
        on_sale = item.get("is_sale", False)

        # Format price: "105.9900" → "105.99"
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

        results.append(
            OkanaganCellarsResult(
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
            )
        )

    return results


# ── Formatting ──────────────────────────────────────────────────────

def format_results(results: list[OkanaganCellarsResult], query: str) -> str:
    if not results:
        return f"No products found at Okanagan Cellars for '{query}'."

    lines = [f"Okanagan Cellars: {len(results)} results for '{query}'\n"]

    for i, r in enumerate(results, 1):
        parts = [f"{i}. {r.name}"]

        if r.on_sale and r.sale_price and r.regular_price:
            parts.append(f"   Price: ${r.sale_price} (was ${r.regular_price} — ON SALE)")
        elif r.sale_price:
            parts.append(f"   Price: ${r.sale_price}")

        if r.category:
            parts.append(f"   Category: {r.category}")
        if r.unit_size:
            parts.append(f"   Size: {r.unit_size}")

        stock_str = f"In Stock ({r.stock_qty})" if r.in_stock else "Out of Stock"
        parts.append(f"   Stock: {stock_str}")

        if r.product_url:
            parts.append(f"   URL: {r.product_url}")

        lines.append("\n".join(parts))

    return "\n\n".join(lines)


# ── Standalone Test ─────────────────────────────────────────────────

async def main():
    for query in ["checkmate", "tantalus", "cedar creek"]:
        print(f"Searching '{query}'...\n")
        results = await search_okanagan_cellars(query)
        print(format_results(results, query))
        print("\n" + "=" * 60 + "\n")


if __name__ == "__main__":
    asyncio.run(main())
