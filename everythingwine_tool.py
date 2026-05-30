"""
Everything Wine Search Tool for BC Wine AI Agent (LangGraph)

Scrapes search results from everythingwine.ca/catalogsearch/result/ (server-side
rendered HTML, no login), then enriches each hit with per-store pickup availability.

Per-store stock comes from Magento's public In-Store Pickup REST API
(/rest/V1/inventory/in-store-pickup/pickup-locations) — guest-accessible, no auth.
It needs the product SKU, which Everything Wine embeds as the image filename prefix
(`<SKU>_<slug>.jpg`), so we extract it from the search HTML with no extra page fetch.
Each search hit then costs one lightweight JSON call (run in parallel, capped).
"""

import asyncio
import re
import httpx
from bs4 import BeautifulSoup
from pydantic import BaseModel

from query_fallback import search_with_fallback


# ── Config ──────────────────────────────────────────────────────────

BASE_URL = "https://www.everythingwine.ca"
SEARCH_URL = f"{BASE_URL}/catalogsearch/result/"
PICKUP_URL = f"{BASE_URL}/rest/V1/inventory/in-store-pickup/pickup-locations"

# Huge radius so a single call returns ALL stores regardless of the coords passed.
# The lat/lng only orders results by distance; the radius makes it exhaustive.
_PICKUP_RADIUS = "20000000"
_PICKUP_LAT = "49.2"   # Metro Vancouver — only affects ordering, not which stores
_PICKUP_LNG = "-123.0"

# Keep only the Lower Mainland stores (by stable pickup_location_code); the API also
# returns Abbotsford and Victoria, which we drop. Set to None to keep every store.
LOWER_MAINLAND_STORE_CODES = {
    "riverdistrict",   # Vancouver
    "northvancouver",  # North Vancouver
    "southsurrey",     # South Surrey
    "langleystore",    # Langley Store
}

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

class StoreAvailability(BaseModel):
    store: str           # "Vancouver", "North Vancouver", "South Surrey", "Langley Store", ...
    code: str | None = None     # pickup_location_code, e.g. "northvancouver"
    status: str          # "available" | "unavailable"
    quantity: int = 0    # exact units in stock at that store

class EverythingWineResult(BaseModel):
    name: str
    sku: str | None = None
    price: str | None = None
    regular_price: str | None = None
    on_sale: bool = False
    country: str | None = None
    url: str | None = None
    image_url: str | None = None
    stock: list[StockStatus] = []
    # Per-store pickup availability for the Lower Mainland stores (Vancouver,
    # North Vancouver, South Surrey, Langley) from the In-Store Pickup API. Empty
    # if the SKU couldn't be resolved or the lookup was skipped/failed.
    store_stock: list[StoreAvailability] = []


# ── Core Search ─────────────────────────────────────────────────────

def _sku_from_image(src: str | None) -> str | None:
    """Everything Wine names product images `<SKU>_<slug>.jpg`, so the SKU is the
    leading numeric run of the filename — extracted with no extra request."""
    if not src:
        return None
    filename = src.split("/")[-1].split("?")[0]
    m = re.match(r"^(\d{3,})[_.]", filename)
    return m.group(1) if m else None


async def _fetch_store_stock(client: httpx.AsyncClient, sku: str) -> list[StoreAvailability]:
    """Query the public In-Store Pickup API for per-store availability of one SKU.
    Returns [] on any failure so a stock lookup never breaks the search itself."""
    params = {
        "searchRequest[scopeCode]": "base",
        "searchRequest[extensionAttributes][productsInfo][0][sku]": sku,
        "searchRequest[extensionAttributes][strategy]": "point-of-sale-based",
        "searchRequest[extensionAttributes][lat]": _PICKUP_LAT,
        "searchRequest[extensionAttributes][lng]": _PICKUP_LNG,
        "searchRequest[area][radius]": _PICKUP_RADIUS,
        "searchRequest[area][searchTerm]": "",
    }
    try:
        # Force JSON: the shared client's Accept header prefers application/xml,
        # which Magento honors and would otherwise return XML for this REST call.
        resp = await client.get(PICKUP_URL, params=params, headers={"Accept": "application/json"})
        resp.raise_for_status()
        data = resp.json()
    except (httpx.HTTPError, ValueError):
        return []

    out: list[StoreAvailability] = []
    for loc in data.get("items", []):
        code = loc.get("pickup_location_code")
        if LOWER_MAINLAND_STORE_CODES is not None and code not in LOWER_MAINLAND_STORE_CODES:
            continue
        inv = (loc.get("extension_attributes") or {}).get("inventory_status") or {}
        out.append(StoreAvailability(
            store=loc.get("name", ""),
            code=code,
            status="available" if inv.get("status") == 1 else "unavailable",
            quantity=int(inv.get("quantity") or 0),
        ))
    return out


async def search_everything_wine(
    query: str,
    with_store_stock: bool = True,
    max_store_lookups: int = 12,
) -> list[EverythingWineResult]:
    """
    Search Everything Wine product catalogue, with per-store pickup availability.

    Args:
        query: Wine name, winery, or varietal (e.g., "tantalus", "checkmate chardonnay")
        with_store_stock: If True (default), enrich each hit with Lower Mainland
            per-store stock (Vancouver, North Vancouver, South Surrey, Langley)
            via the public In-Store Pickup API.
        max_store_lookups: Cap on how many hits get the per-store lookup (one parallel
            API call each), to bound latency on large result sets.
    """
    async with httpx.AsyncClient(follow_redirects=True, timeout=15.0, headers=HEADERS) as client:
        # The Elasticsuite search AND-matches every token, so a full label string
        # ("Mission Hill Perpetua 2022 Chardonnay") can return 0 even when the wine is
        # stocked. search_with_fallback retries with trimmed queries (see query_fallback).
        async def attempt(q: str) -> list[EverythingWineResult]:
            resp = await client.get(SEARCH_URL, params={"q": q})
            resp.raise_for_status()
            search_div = BeautifulSoup(resp.text, "html.parser").select_one("div.search.results")
            return _parse_results(search_div) if search_div else []

        results = await search_with_fallback(attempt, query)

        # Enrich top hits with per-store availability (parallel; failures → []).
        if with_store_stock and results:
            targets = [r for r in results if r.sku][:max_store_lookups]
            if targets:
                stocks = await asyncio.gather(
                    *(_fetch_store_stock(client, r.sku) for r in targets)
                )
                for r, st in zip(targets, stocks):
                    r.store_stock = st

    return results


def _parse_results(search_div) -> list[EverythingWineResult]:
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

        # Image — also the SKU source (filename is `<SKU>_<slug>.jpg`).
        img_el = item.select_one("img.product-image-photo")
        image_url = (img_el.get("src") or img_el.get("data-src")) if img_el else None
        sku = _sku_from_image(image_url)

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
                sku=sku,
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
        if r.store_stock:
            avail = [f"{s.store} ({s.quantity})" for s in r.store_stock if s.status == "available"]
            oos = [s.store for s in r.store_stock if s.status != "available"]
            if avail:
                parts.append(f"   Pickup in stock: {', '.join(avail)}")
            if oos:
                parts.append(f"   Pickup out of stock: {', '.join(oos)}")
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
