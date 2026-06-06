"""
Legacy Liquor Store Search Tool for Vancouver Drinks AI (LangGraph)

Uses a GraphQL API (Apollo Server on Google Cloud Run).
No login required. Rich product data with price filtering and staff picks.

Legacy Liquor Store is a premium independent wine shop in Vancouver.
"""

import asyncio
import httpx
from pydantic import BaseModel

from .query_fallback import search_with_fallback


# -- Config ------------------------------------------------------------------

BASE_URL = "https://www.legacyliquorstore.com"
API_URL = "https://production-retail-store-api-hagnfhf3sq-uc.a.run.app/graphql"
STORE_ID = "LL"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/148.0.0.0 Safari/537.36 Edg/148.0.0.0"
    ),
    "Content-Type": "application/json",
    "Accept": "application/json",
}

PRODUCTS_QUERY = """
query SearchProducts(
  $storeId: String!
  $searchValue: String
  $priceMin: Float
  $priceMax: Float
  $pageLimit: Int
  $pageCursor: String
  $sortBy: String
  $sortOrder: String
  $countries: [String]
  $regions: [String]
  $isOnSale: Boolean
  $isStaffPick: Boolean
  $anyTags: [String]
) {
  products(
    storeId: $storeId
    searchValue: $searchValue
    priceMin: $priceMin
    priceMax: $priceMax
    pageLimit: $pageLimit
    pageCursor: $pageCursor
    sortBy: $sortBy
    sortOrder: $sortOrder
    countries: $countries
    regions: $regions
    isOnSale: $isOnSale
    isStaffPick: $isStaffPick
    anyTags: $anyTags
  ) {
    totalCount
    nextPageCursor
    items {
      id
      name
      brand
      slug
      country
      region
      priceFrom
      priceTo
      retailPriceFrom
      retailPriceTo
      isOnSale
      isFeatured
      isNewArrival
      isStaffPick
      bestSellerScore
      tags {
        name
        slug
      }
      variants {
        quantity
      }
    }
  }
}
"""


# -- Data Model --------------------------------------------------------------

class LegacyResult(BaseModel):
    name: str
    brand: str | None = None
    slug: str | None = None
    price: float | None = None
    retail_price: float | None = None
    on_sale: bool = False
    is_staff_pick: bool = False
    is_new_arrival: bool = False
    country: str | None = None
    region: str | None = None
    in_stock: bool = True
    stock_qty: int | None = None
    tags: list[str] = []
    url: str | None = None


# -- Core Search -------------------------------------------------------------

def _clean_query(q: str) -> str:
    """Normalize smart quotes to plain apostrophes. Unlike other store backends,
    Legacy’s search engine needs the apostrophe to match names like Martin’s Lane."""
    return q.replace("‘", "’").replace("’", "’")


async def _legacy_search_once(
    client: httpx.AsyncClient, base_variables: dict, search_value: str
) -> tuple[list[LegacyResult], int]:
    """One GraphQL search for an already-cleaned searchValue, reusing the caller's
    filter variables (price, tags, ...). Returns (results, total_count)."""
    variables = {**base_variables, "searchValue": search_value}

    resp = await client.post(
        API_URL,
        json={"query": PRODUCTS_QUERY, "variables": variables},
    )
    resp.raise_for_status()
    data = resp.json()

    if "errors" in data:
        error_msg = data["errors"][0].get("message", "Unknown GraphQL error")
        raise ValueError(f"Legacy Liquor GraphQL error: {error_msg}")

    products_data = data.get("data", {}).get("products", {})
    total = products_data.get("totalCount", 0)
    items = products_data.get("items", [])

    results: list[LegacyResult] = []

    for item in items:
        name = item.get("name", "Unknown")
        brand = item.get("brand") or None
        slug = item.get("slug") or None

        price_from = item.get("priceFrom")
        retail_from = item.get("retailPriceFrom")
        if retail_from and retail_from == price_from:
            retail_from = None

        is_on_sale = bool(item.get("isOnSale"))
        is_staff_pick = bool(item.get("isStaffPick"))
        is_new_arrival = bool(item.get("isNewArrival"))

        tags_raw = item.get("tags") or []
        tag_names = [t["name"] for t in tags_raw if t.get("name")]
        tag_slugs = [t["slug"] for t in tags_raw if t.get("slug")]
        category = tag_slugs[0] if tag_slugs else "wine"

        variants = item.get("variants") or []
        stock_qty = sum(v.get("quantity", 0) for v in variants)
        in_stock = stock_qty > 0

        url = f"{BASE_URL}/product/{category}/{slug}" if slug else None

        results.append(
            LegacyResult(
                name=name,
                brand=brand,
                slug=slug,
                price=price_from,
                retail_price=retail_from,
                on_sale=is_on_sale,
                is_staff_pick=is_staff_pick,
                is_new_arrival=is_new_arrival,
                country=item.get("country") or None,
                region=item.get("region") or None,
                in_stock=in_stock,
                stock_qty=stock_qty,
                tags=tag_names,
                url=url,
            )
        )

    return results, total


async def search_legacy(
    query: str,
    limit: int = 30,
    price_min: float | None = None,
    price_max: float | None = None,
    on_sale: bool | None = None,
    staff_pick: bool | None = None,
    country: str | None = None,
    region: str | None = None,
    tags: list[str] | None = None,
) -> tuple[list[LegacyResult], int]:
    """
    Search Legacy Liquor Store inventory via GraphQL.

    The search AND-matches query tokens, so a full label string can return 0 even when
    the wine is stocked; search_with_fallback retries with trimmed queries (see
    query_fallback). Legacy needs the apostrophe preserved (Martin's Lane), so its own
    _clean_query — which normalizes smart quotes rather than stripping them — is used.

    Args:
        query:      Wine name, winery, or varietal
        limit:      Max results (default 30)
        price_min:  Minimum price filter
        price_max:  Maximum price filter
        on_sale:    Only sale items
        staff_pick: Only staff picks
        country:    Filter by country
        region:     Filter by region
        tags:       Filter by tag slugs (e.g. ["pinot-noir", "red-wine"])

    Returns:
        (results, total_count)
    """
    base_variables: dict = {"storeId": STORE_ID, "pageLimit": limit}
    if price_min is not None:
        base_variables["priceMin"] = price_min
    if price_max is not None:
        base_variables["priceMax"] = price_max
    if on_sale is not None:
        base_variables["isOnSale"] = on_sale
    if staff_pick is not None:
        base_variables["isStaffPick"] = staff_pick
    if country is not None:
        base_variables["countries"] = [country]
    if region is not None:
        base_variables["regions"] = [region]
    if tags is not None:
        base_variables["anyTags"] = tags

    # The fallback returns only the result list; capture the matching total via a holder.
    captured = {"total": 0}

    async with httpx.AsyncClient(timeout=20.0, headers=HEADERS) as client:
        async def attempt(q: str) -> list[LegacyResult]:
            items, total = await _legacy_search_once(client, base_variables, q)
            captured["total"] = total
            return items

        results = await search_with_fallback(attempt, query, clean=_clean_query)

    return results, captured["total"]


# -- Formatting --------------------------------------------------------------

def format_results(results: list[LegacyResult], query: str, total: int) -> str:
    if not results:
        return f"No products found at Legacy Liquor Store for '{query}'."

    lines = [f"Legacy Liquor Store: {len(results)} of {total} results for '{query}'\n"]

    for i, r in enumerate(results, 1):
        parts = [f"{i}. {r.name}"]

        if r.on_sale and r.retail_price and r.price:
            parts.append(f"   Price: ${r.price:.2f} (was ${r.retail_price:.2f} — ON SALE)")
        elif r.price:
            parts.append(f"   Price: ${r.price:.2f}")

        badges = []
        if r.is_staff_pick:
            badges.append("Staff Pick")
        if r.is_new_arrival:
            badges.append("New Arrival")
        if badges:
            parts.append(f"   [{', '.join(badges)}]")

        stock_str = f"In Stock ({r.stock_qty})" if r.in_stock else "Out of Stock"
        parts.append(f"   Stock: {stock_str}")

        if r.country or r.region:
            origin = ", ".join(filter(None, [r.region, r.country]))
            parts.append(f"   Origin: {origin}")

        if r.tags:
            parts.append(f"   Tags: {', '.join(r.tags)}")

        if r.url:
            parts.append(f"   URL: {r.url}")

        lines.append("\n".join(parts))

    return "\n\n".join(lines)


# -- Standalone Test ---------------------------------------------------------

async def main():
    for query in ["pinot noir", "chardonnay BC", "champagne"]:
        print(f"Searching '{query}'...\n")
        results, total = await search_legacy(query)
        print(format_results(results, query, total))
        print("\n" + "=" * 60 + "\n")


if __name__ == "__main__":
    asyncio.run(main())
