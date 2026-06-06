"""Google Maps Places (New) store-locator tool.

Finds liquor / wine stores near a place in Vancouver with address,
opening hours, rating, and a Google Maps link, via the Places API (New) `searchText`
endpoint. Powers the agent's "where can I buy this near me?" answers.

Requires GOOGLE_MAPS_API_KEY in .env (enable "Places API (New)" on the GCP project).
"""
from __future__ import annotations

import os

import httpx
from pydantic import BaseModel

GOOGLE_MAPS_API_KEY = os.getenv("GOOGLE_MAPS_API_KEY", "")
PLACES_SEARCH_URL = "https://places.googleapis.com/v1/places:searchText"

# Bias results to the City of Vancouver (downtown center), ~12 km radius.
_VANCOUVER = {"latitude": 49.2827, "longitude": -123.1207}
_BIAS_RADIUS_M = 12000.0

# Only request the fields we use, to keep the response small and cheap.
_FIELD_MASK = ",".join([
    "places.displayName",
    "places.formattedAddress",
    "places.location",
    "places.rating",
    "places.userRatingCount",
    "places.googleMapsUri",
    "places.currentOpeningHours.openNow",
    "places.regularOpeningHours.weekdayDescriptions",
    "places.primaryType",
])


class PlaceResult(BaseModel):
    name: str | None = None
    address: str | None = None
    rating: float | None = None
    rating_count: int | None = None
    open_now: bool | None = None
    hours: list[str] | None = None
    maps_url: str | None = None
    lat: float | None = None
    lng: float | None = None


async def search_google_maps(query: str, max_results: int = 8) -> list[PlaceResult]:
    """Text-search for stores (e.g. "BC Liquor Store near Yaletown, Vancouver").

    Biased to the City of Vancouver. Returns up to `max_results` places.
    """
    if not GOOGLE_MAPS_API_KEY:
        raise ValueError("GOOGLE_MAPS_API_KEY not set in .env")

    payload = {
        "textQuery": query,
        "maxResultCount": max(1, min(max_results, 20)),
        "locationBias": {
            "circle": {"center": _VANCOUVER, "radius": _BIAS_RADIUS_M},
        },
    }
    headers = {
        "Content-Type": "application/json",
        "X-Goog-Api-Key": GOOGLE_MAPS_API_KEY,
        "X-Goog-FieldMask": _FIELD_MASK,
    }

    async with httpx.AsyncClient(timeout=15) as client:
        resp = await client.post(PLACES_SEARCH_URL, json=payload, headers=headers)
        resp.raise_for_status()
        data = resp.json()

    results: list[PlaceResult] = []
    for p in data.get("places", []):
        loc = p.get("location") or {}
        results.append(PlaceResult(
            name=(p.get("displayName") or {}).get("text"),
            address=p.get("formattedAddress"),
            rating=p.get("rating"),
            rating_count=p.get("userRatingCount"),
            open_now=(p.get("currentOpeningHours") or {}).get("openNow"),
            hours=(p.get("regularOpeningHours") or {}).get("weekdayDescriptions"),
            maps_url=p.get("googleMapsUri"),
            lat=loc.get("latitude"),
            lng=loc.get("longitude"),
        ))
    return results


if __name__ == "__main__":
    import asyncio

    async def _smoke() -> None:
        places = await search_google_maps("liquor store near Yaletown, Vancouver BC")
        for pl in places:
            status = "open" if pl.open_now else "closed/unknown"
            print(f"- {pl.name} ({status}) — {pl.address} — {pl.maps_url}")

    asyncio.run(_smoke())
