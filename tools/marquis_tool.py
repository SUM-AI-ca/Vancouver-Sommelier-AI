"""
Marquis Wine Cellars Search Tool for Vancouver Drinks AI (LangGraph)

Uses the BigCommerce Discovery API at discovery.marquis-wines.com.
No login required. Rich JSON response with inventory, categories, pricing.

Marquis Wine Cellars is a highly curated independent wine shop in Vancouver.
"""

import asyncio
import json
import httpx
from pydantic import BaseModel


# ── Config ──────────────────────────────────────────────────────────

BASE_URL = "https://www.marquis-wines.com"
API_URL = "https://discovery.marquis-wines.com/apis/ecommerce-service/public/discovery/v2/search"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/148.0.0.0 Safari/537.36 Edg/148.0.0.0"
    ),
    "Accept": "application/json",
    "Referer": f"{BASE_URL}/search-results/",
}

FIELDS = (
    "sku,matched_sku,provider_id,calculated_price,brand,name,"
    "category_meta,variant_options,variants,page_slug,custom_fields,"
    "out_of_stock,inventory_level,inventory_tracking,"
    "provider_specific_data,images,retail_price,price,sale_price,"
    "cost_price,date_created,categories"
)


# ── Data Model ──────────────────────────────────────────────────────

class MarquisResult(BaseModel):
    name: str
    sku: str | None = None
    price: float | None = None
    sale_price: float | None = None
    retail_price: float | None = None
    on_sale: bool = False
    in_stock: bool = True
    inventory_level: int | None = None
    categories: list[str] = []         # e.g. ["White Wine", "Chardonnay", "British Columbia", "Okanagan"]
    url: str | None = None
    image_url: str | None = None


# ── Core Search ─────────────────────────────────────────────────────

def _clean_query(q: str) -> str:
    """Strip apostrophes and smart quotes so we don't lose hits like
    'Stag's Hollow' or 'Quails' Gate' on backends sensitive to them."""
    return q.replace("'", "").replace("’", "").replace("‘", "")


async def search_marquis(
    query: str,
    limit: int = 30,
    skip: int = 0,
) -> tuple[list[MarquisResult], int]:
    """
    Search Marquis Wine Cellars inventory.

    Args:
        query: Wine name, winery, or varietal
        limit: Max results per page (default 30)
        skip:  Offset for pagination

    Returns:
        (results, total_count)
    """
    params = {
        "fields": FIELDS,
        "limit": limit,
        "skip": skip,
        "locale": "en-us",
        "include_count": "true",
        "sort_by": "relevance",
        "is_auto_spellcheck": "false",
        "is_auto_spellcheck_zero_result": "true",
        "did_you_mean_limit": 1,
        "search_term": _clean_query(query),
        "facets": "",
    }

    async with httpx.AsyncClient(timeout=20.0, headers=HEADERS) as client:
        resp = await client.get(API_URL, params=params)
        resp.raise_for_status()
        data = resp.json()

    records = data.get("Data", {}).get("records", [])
    total = data.get("Data", {}).get("_meta_", {}).get("total_count", len(records))

    results: list[MarquisResult] = []

    for item in records:
        name = item.get("name", "Unknown")
        sku = item.get("sku")
        price = item.get("price")
        sale_price = item.get("sale_price")
        retail_price = item.get("retail_price") or None
        if retail_price == 0:
            retail_price = None

        on_sale = (sale_price is not None and price is not None and sale_price < price)

        in_stock = not item.get("out_of_stock", False)
        inventory_level = item.get("inventory_level")
        categories = item.get("categories", [])

        # Product URL from page_slug
        page_slug = item.get("page_slug", "")
        url = f"{BASE_URL}{page_slug}" if page_slug else None

        # Image URL — parse from JSON string
        image_url = None
        images_raw = item.get("images", "[]")
        try:
            images = json.loads(images_raw) if isinstance(images_raw, str) else images_raw
            if images and isinstance(images, list):
                image_url = images[0].get("url_standard") or images[0].get("url_thumbnail")
        except (json.JSONDecodeError, TypeError):
            pass

        results.append(
            MarquisResult(
                name=name,
                sku=sku,
                price=price,
                sale_price=sale_price,
                retail_price=retail_price,
                on_sale=on_sale,
                in_stock=in_stock,
                inventory_level=inventory_level,
                categories=categories,
                url=url,
                image_url=image_url,
            )
        )

    return results, total


# ── Formatting ──────────────────────────────────────────────────────

def format_results(results: list[MarquisResult], query: str, total: int) -> str:
    if not results:
        return f"No products found at Marquis Wine Cellars for '{query}'."

    lines = [f"Marquis Wine Cellars: {len(results)} of {total} results for '{query}'\n"]

    for i, r in enumerate(results, 1):
        parts = [f"{i}. {r.name}"]

        if r.on_sale and r.sale_price and r.price:
            parts.append(f"   Price: ${r.sale_price:.2f} (was ${r.price:.2f} — ON SALE)")
        elif r.sale_price:
            parts.append(f"   Price: ${r.sale_price:.2f}")
        elif r.price:
            parts.append(f"   Price: ${r.price:.2f}")

        if r.categories:
            parts.append(f"   Category: {' > '.join(r.categories)}")

        stock_str = f"In Stock ({r.inventory_level})" if r.in_stock else "Out of Stock"
        parts.append(f"   Stock: {stock_str}")

        if r.url:
            parts.append(f"   URL: {r.url}")

        lines.append("\n".join(parts))

    return "\n\n".join(lines)


# ── Standalone Test ─────────────────────────────────────────────────

async def main():
    for query in ["checkmate", "martins lane", "pinot noir"]:
        print(f"Searching '{query}'...\n")
        results, total = await search_marquis(query)
        print(format_results(results, query, total))
        print("\n" + "=" * 60 + "\n")


if __name__ == "__main__":
    asyncio.run(main())
