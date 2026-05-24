"""Debug: dump Everything Wine search results HTML structure."""

import asyncio
import httpx
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/148.0.0.0 Safari/537.36 Edg/148.0.0.0"
    ),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
}

async def main():
    async with httpx.AsyncClient(follow_redirects=True, timeout=15.0, headers=HEADERS) as client:
        resp = await client.get(
            "https://www.everythingwine.ca/catalogsearch/result/",
            params={"q": "tantalus"},
        )

    print(f"Status: {resp.status_code}")
    print(f"URL: {resp.url}")

    soup = BeautifulSoup(resp.text, "html.parser")

    # Find search results container
    search_div = soup.select_one("div.search.results")
    print(f"\ndiv.search.results found: {search_div is not None}")

    if not search_div:
        # Try alternatives
        for sel in ["div.search-results", "ol.product-items", "div.products", "ul.product-items"]:
            el = soup.select_one(sel)
            if el:
                print(f"  Alternative found: {sel}")
                search_div = el
                break

    if not search_div:
        print("\nNo search results container found.")
        print("Page title:", soup.select_one("title").get_text() if soup.select_one("title") else "?")
        print("First 2000 chars:")
        print(soup.get_text(strip=True)[:2000])
        return

    # Find product items
    product_items = search_div.select("li.product-item, li.item, div.product-item")
    print(f"Product items found: {len(product_items)}")

    if not product_items:
        # Try broader
        product_items = search_div.select("li, div.product")
        print(f"  (broader search): {len(product_items)}")

    # Dump first product's structure
    if product_items:
        first = product_items[0]
        print("\n=== FIRST PRODUCT RAW HTML (first 2000 chars) ===")
        print(str(first)[:2000])

        print("\n=== PARSED FIELDS ===")
        for i, item in enumerate(product_items[:3]):
            print(f"\nProduct #{i+1}:")

            # Name
            for sel in ["a.product-item-link", "a.product-name", ".product-name a", ".product-item-name a", "h2 a", "h3 a"]:
                el = item.select_one(sel)
                if el:
                    print(f"  Name ({sel}): {el.get_text(strip=True)}")
                    print(f"  URL: {el.get('href', '?')}")
                    break

            # Price
            for sel in ["span.price", ".price-wrapper", "[data-price-amount]"]:
                el = item.select_one(sel)
                if el:
                    price = el.get("data-price-amount") or el.get_text(strip=True)
                    print(f"  Price ({sel}): {price}")
                    break

            # Country/Region
            for sel in [".product-item-country", ".country", "[data-country]", ".product-attribute"]:
                el = item.select_one(sel)
                if el:
                    print(f"  Country ({sel}): {el.get_text(strip=True)}")
                    break

            # Image
            img = item.select_one("img.product-image-photo, img")
            if img:
                print(f"  Image: {img.get('src', '?')[:100]}")

            # Availability
            for sel in [".stock", ".availability", ".delivery-status", "[class*='delivery']", "[class*='avail']"]:
                els = item.select(sel)
                for el in els:
                    print(f"  Availability ({sel}): {el.get_text(strip=True)[:80]}")

asyncio.run(main())
