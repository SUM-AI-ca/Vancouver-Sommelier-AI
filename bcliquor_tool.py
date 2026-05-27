"""
BC Liquor Store Search Tool for BC Wine AI Agent (LangGraph)

Uses the public Elasticsearch JSON API at bcliquorstores.com.
No login required.
"""

import asyncio
import httpx
from pydantic import BaseModel, field_validator


# ── Config ──────────────────────────────────────────────────────────

BASE_URL = "https://www.bcliquorstores.com"
BROWSE_URL = f"{BASE_URL}/ajax/browse"
INVENTORY_URL = f"{BASE_URL}/ajax/get-product-inventory-sum"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/125.0.0.0 Safari/537.36"
    ),
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "X-Requested-With": "XMLHttpRequest",
    "Referer": f"{BASE_URL}/product-catalogue",
}

PAGE_SIZE = 24


# ── Data Model ──────────────────────────────────────────────────────

class BCLiquorResult(BaseModel):
    name: str
    sku: str
    current_price: str | None = None
    regular_price: str | None = None
    on_sale: bool = False
    product_type: str | None = None       # "Red Wine", "White Wine", etc.
    grape_type: str | None = None          # "PINOT NOIR", "RIESLING", etc.
    country: str | None = None
    volume: str | None = None              # "0.750"
    alcohol_pct: float | None = None
    sweetness: str | None = None           # "00" = dry
    tasting_notes: str | None = None
    consumer_rating: float | None = None   # e.g., 4.4
    consumer_votes: int | None = None
    store_count: int | None = None         # number of stores carrying it
    available_units: int | None = None     # total units across all stores
    is_bc_vqa: bool = False
    image_url: str | None = None
    product_url: str | None = None
    certificates: list[str] = []

    # BC Liquor's Elasticsearch payload sometimes returns explicit nulls for
    # isBCVQA (observed on Fort Berens 2024 listings, broader Pinot Noir queries).
    # dict.get(key, default) only falls back when the key is missing — an
    # explicit null passes None through and trips Pydantic's strict bool check.
    # Same for `certificates` returning null. Coerce both at validation time so
    # construction sites stay simple.
    @field_validator("is_bc_vqa", mode="before")
    @classmethod
    def _is_bc_vqa_null_to_false(cls, v):
        return False if v is None else v

    @field_validator("certificates", mode="before")
    @classmethod
    def _certificates_null_to_empty(cls, v):
        return [] if v is None else v


# ── Core Search ─────────────────────────────────────────────────────

def _clean_query(q: str) -> str:
    """Strip apostrophes / smart quotes for consistency with other store
    backends (Okanagan Cellars in particular returns 0 hits when an ASCII
    apostrophe is present)."""
    return q.replace("'", "").replace("’", "").replace("‘", "")


async def search_bcliquor(
    query: str,
    max_pages: int = 2,
    category: str | None = None,
) -> list[BCLiquorResult]:
    """
    Search BC Liquor Store products.

    Args:
        query:      Search term (wine name, winery, varietal)
        max_pages:  Max pages to fetch (24 results per page)
        category:   Optional filter: "wine", "beer", "spirits"
    """
    all_results: list[BCLiquorResult] = []

    async with httpx.AsyncClient(timeout=15.0, headers=HEADERS) as client:
        for page in range(1, max_pages + 1):
            params = {
                "search": _clean_query(query),
                "sort": "_score:desc",
                "size": PAGE_SIZE,
                "page": page,
            }
            if category:
                params["category"] = category

            resp = await client.get(BROWSE_URL, params=params)
            resp.raise_for_status()
            data = resp.json()

            hits = data.get("hits", {})
            items = hits.get("hits", [])
            total_pages = int(hits.get("total_pages", 1))

            for item in items:
                src = item.get("_source", {})

                current = src.get("currentPrice")
                regular = src.get("regularPrice")
                on_sale = (current != regular) if current and regular else False

                tasting = src.get("tastingDescription")
                if tasting is False:  # API returns `false` when no notes
                    tasting = None

                sku = src.get("sku", item.get("_id", ""))

                all_results.append(
                    BCLiquorResult(
                        name=src.get("name", "Unknown"),
                        sku=sku,
                        current_price=current,
                        regular_price=regular,
                        on_sale=on_sale,
                        product_type=src.get("productType"),
                        grape_type=src.get("grapeType"),
                        country=src.get("countryName"),
                        volume=src.get("volume"),
                        alcohol_pct=src.get("alcoholPercentage"),
                        sweetness=src.get("sweetness"),
                        tasting_notes=tasting,
                        consumer_rating=src.get("consumerRating"),
                        consumer_votes=src.get("votes"),
                        store_count=src.get("storeCount"),
                        available_units=src.get("availableUnits"),
                        is_bc_vqa=src.get("isBCVQA", False),
                        image_url=src.get("image"),
                        product_url=f"{BASE_URL}/product/{sku}",
                        certificates=src.get("certificates", []),
                    )
                )

            # Stop if no more pages
            if page >= total_pages:
                break

    return all_results


# ── LangGraph Tool Wrapper ─────────────────────────────────────────

def format_results(results: list[BCLiquorResult], query: str) -> str:
    """Format results as readable string for the LLM."""
    if not results:
        return f"No products found at BC Liquor Store for '{query}'."

    lines = [f"BC Liquor Store: {len(results)} results for '{query}'\n"]

    for i, r in enumerate(results, 1):
        parts = [f"{i}. {r.name}"]

        # Price
        if r.on_sale and r.current_price and r.regular_price:
            parts.append(f"   Price: ${r.current_price} (was ${r.regular_price} — ON SALE)")
        elif r.current_price:
            parts.append(f"   Price: ${r.current_price}")

        if r.grape_type:
            parts.append(f"   Varietal: {r.grape_type}")
        if r.product_type:
            parts.append(f"   Type: {r.product_type}")
        if r.country:
            parts.append(f"   Country: {r.country}")
        if r.volume:
            parts.append(f"   Volume: {r.volume}L")
        if r.alcohol_pct:
            parts.append(f"   ABV: {r.alcohol_pct}%")
        if r.is_bc_vqa:
            parts.append(f"   BC VQA: Yes")
        if r.consumer_rating:
            parts.append(f"   Rating: {r.consumer_rating}/5 ({r.consumer_votes or 0} votes)")
        if r.store_count is not None:
            parts.append(f"   Available at: {r.store_count} stores ({r.available_units or 0} units)")
        if r.tasting_notes:
            parts.append(f"   Tasting Notes: {r.tasting_notes.strip()}")
        if r.product_url:
            parts.append(f"   URL: {r.product_url}")

        lines.append("\n".join(parts))

    return "\n\n".join(lines)


# ── Standalone Test ─────────────────────────────────────────────────

async def main():
    print("Searching BC Liquor Store for 'tantalus'...\n")
    results = await search_bcliquor("tantalus")
    print(format_results(results, "tantalus"))

    print("\n" + "=" * 60)
    print("\nSearching for 'checkmate'...\n")
    results2 = await search_bcliquor("checkmate", category="wine")
    print(format_results(results2, "checkmate"))


if __name__ == "__main__":
    asyncio.run(main())
