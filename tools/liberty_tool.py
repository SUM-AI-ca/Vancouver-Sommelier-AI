"""
Liberty Wine Merchants Search Tool for BC Wine AI Agent (LangGraph)

Uses the WooCommerce Store REST API (public, no auth).
Rich product data with wine-specific attributes (producer, country, region,
grape, vintage), tags (Liberty Exclusive, Value Picks, Staff Picks), and stock.

Liberty Wine Merchants is a large independent wine retailer in Vancouver.
"""

import asyncio
import html
import httpx
from pydantic import BaseModel

from .query_fallback import search_with_fallback


# -- Config ------------------------------------------------------------------

BASE_URL = "https://www.libertywinemerchants.com"
API_URL = f"{BASE_URL}/wp-json/wc/store/products"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/148.0.0.0 Safari/537.36 Edg/148.0.0.0"
    ),
    "Accept": "application/json",
}


# -- Data Model --------------------------------------------------------------

class LibertyResult(BaseModel):
    name: str
    sku: str | None = None
    price: float | None = None
    regular_price: float | None = None
    on_sale: bool = False
    in_stock: bool = True
    stock_quantity: int | None = None
    category: str | None = None
    tags: list[str] = []
    producer: str | None = None
    country: str | None = None
    region: str | None = None
    grape: str | None = None
    vintage: str | None = None
    url: str | None = None


# -- Core Search -------------------------------------------------------------

def _clean_query(q: str) -> str:
    """Normalize smart quotes to plain apostrophes. Liberty's search needs the
    apostrophe to match names like Martin's Lane."""
    return q.replace("‘", "'").replace("’", "'")


def _cents_to_dollars(cents_str: str) -> float | None:
    try:
        return int(cents_str) / 100
    except (ValueError, TypeError):
        return None


def _attr_value(attributes: list[dict], name: str) -> str | None:
    for attr in attributes:
        if attr.get("name") == name:
            terms = attr.get("terms", [])
            if terms:
                return terms[0].get("name")
    return None


async def _liberty_search_once(
    client: httpx.AsyncClient, search_value: str, per_page: int,
) -> tuple[list[LibertyResult], int]:
    resp = await client.get(
        API_URL,
        params={"search": search_value, "per_page": per_page},
    )
    resp.raise_for_status()

    total = int(resp.headers.get("X-WP-Total", 0))
    items = resp.json()

    results: list[LibertyResult] = []
    for item in items:
        name = html.unescape(item.get("name", "Unknown"))
        sku = item.get("sku") or None

        prices = item.get("prices", {})
        price = _cents_to_dollars(prices.get("price", "0"))
        regular_price = _cents_to_dollars(prices.get("regular_price", "0"))
        if regular_price and regular_price == price:
            regular_price = None

        on_sale = bool(item.get("on_sale"))
        in_stock = bool(item.get("is_in_stock"))
        stock_quantity = item.get("low_stock_remaining")

        categories = item.get("categories", [])
        category = categories[0]["name"] if categories else None

        tag_names = [t["name"] for t in item.get("tags", []) if t.get("name")]

        attrs = item.get("attributes", [])
        producer = _attr_value(attrs, "Producer")
        country = _attr_value(attrs, "Country")
        region = _attr_value(attrs, "Region")
        grape = _attr_value(attrs, "Grape")
        vintage = _attr_value(attrs, "Vintage")

        url = item.get("permalink") or None

        results.append(
            LibertyResult(
                name=name,
                sku=sku,
                price=price,
                regular_price=regular_price,
                on_sale=on_sale,
                in_stock=in_stock,
                stock_quantity=stock_quantity,
                category=category,
                tags=tag_names,
                producer=producer,
                country=country,
                region=region,
                grape=grape,
                vintage=vintage,
                url=url,
            )
        )

    return results, total


async def search_liberty(
    query: str,
    limit: int = 30,
) -> tuple[list[LibertyResult], int]:
    """
    Search Liberty Wine Merchants inventory via WooCommerce Store API.

    The search AND-matches query tokens, so search_with_fallback retries with
    trimmed queries on empty results. Liberty needs the apostrophe preserved
    (Martin's Lane), so its own _clean_query is used.

    Args:
        query: Wine name, winery, or varietal
        limit: Max results (default 30)

    Returns:
        (results, total_count)
    """
    captured = {"total": 0}

    async with httpx.AsyncClient(timeout=15.0, headers=HEADERS) as client:
        async def attempt(q: str) -> list[LibertyResult]:
            items, total = await _liberty_search_once(client, q, limit)
            captured["total"] = total
            return items

        results = await search_with_fallback(attempt, query, clean=_clean_query)

    return results, captured["total"]


# -- Formatting --------------------------------------------------------------

def format_results(results: list[LibertyResult], query: str, total: int) -> str:
    if not results:
        return f"No products found at Liberty Wine Merchants for '{query}'."

    lines = [f"Liberty Wine Merchants: {len(results)} of {total} results for '{query}'\n"]

    for i, r in enumerate(results, 1):
        parts = [f"{i}. {r.name}"]

        if r.on_sale and r.regular_price and r.price:
            parts.append(f"   Price: ${r.price:.2f} (was ${r.regular_price:.2f} — ON SALE)")
        elif r.price:
            parts.append(f"   Price: ${r.price:.2f}")

        if r.tags:
            parts.append(f"   [{', '.join(r.tags)}]")

        if r.in_stock:
            stock_str = f"In Stock ({r.stock_quantity})" if r.stock_quantity is not None else "In Stock"
        else:
            stock_str = "Out of Stock"
        parts.append(f"   Stock: {stock_str}")

        origin_parts = []
        if r.grape:
            origin_parts.append(r.grape)
        if r.region:
            origin_parts.append(r.region)
        if r.country:
            origin_parts.append(r.country)
        if origin_parts:
            parts.append(f"   Origin: {', '.join(origin_parts)}")

        if r.vintage:
            parts.append(f"   Vintage: {r.vintage}")

        if r.url:
            parts.append(f"   URL: {r.url}")

        lines.append("\n".join(parts))

    return "\n\n".join(lines)


# -- Standalone Test ---------------------------------------------------------

async def main():
    for query in ["pinot noir", "tantalus", "Martin's Lane", "champagne"]:
        print(f"Searching '{query}'...\n")
        results, total = await search_liberty(query)
        print(format_results(results, query, total))
        print("\n" + "=" * 60 + "\n")


if __name__ == "__main__":
    asyncio.run(main())
