"""Shared query fallback for store-inventory search tools.

Several store backends AND-match every query token against the product title, so a
full label string ("Mission Hill Perpetua 2022 Chardonnay") returns 0 results even
when the wine is stocked (its title is "MISSION HILL - PERPETUA 2022", with no
"Chardonnay"). This happens whenever a wine is searched from a label/vision extraction
that tacks on the varietal and vintage.

`search_with_fallback` runs the query, and on an empty result retries with progressively
trimmed queries (varietal/vintage stripped first, then trailing tokens dropped), returning
the first non-empty match. Verified to help okanagan_cellars, everything_wine, and legacy.
(bcliquor's search is lenient and never needs it; marquis over-matches — a separate
precision problem the fallback can't fix.)
"""

import re
from collections.abc import Awaitable, Callable


# Refinement tokens that often appear in a label/extraction but NOT in a store's
# product title. The backend AND-matches every token, so one of these can zero out
# an otherwise-valid search. Dropped on fallback retries.
_VARIETAL_NOISE = {
    "chardonnay", "pinot", "noir", "gris", "grigio", "blanc", "fumé", "fume",
    "riesling", "cabernet", "sauvignon", "merlot", "syrah", "shiraz", "gamay",
    "viognier", "semillon", "sémillon", "malbec", "zinfandel", "tempranillo",
    "sangiovese", "nebbiolo", "grenache", "mourvedre", "mourvèdre", "petit",
    "verdot", "franc", "gewurztraminer", "gewürztraminer", "muscat", "sparkling",
    "brut", "rosé", "rose", "red", "white", "wine", "vqa", "bc",
}


def clean_query(q: str) -> str:
    """Default cleaner: strip apostrophes / smart quotes. Some backends silently
    zero-out results when these are present (e.g. "Quails' Gate" → 0). Note: Legacy
    is the exception (it NEEDS the apostrophe) and passes its own cleaner instead."""
    return q.replace("'", "").replace("’", "").replace("‘", "")


def _strip_refinements(cleaned: str) -> str:
    """Drop 4-digit vintage years and varietal/style words (see _VARIETAL_NOISE),
    keeping the distinctive producer + cuvée tokens."""
    kept = [
        t for t in cleaned.split()
        if not re.fullmatch(r"(19|20)\d{2}", t) and t.lower() not in _VARIETAL_NOISE
    ]
    return " ".join(kept)


def query_variants(cleaned: str) -> list[str]:
    """Progressively-broader fallback queries, most-specific first, for when the full
    query returns nothing.

    The targeted strip (varietal/vintage removed) comes first and may go as low as one
    distinctive token ("perpetua") since those words are safe to drop. The blind
    trailing-drop that follows stops at 3 tokens, so it never collapses to a bare
    producer name and dumps an unrelated catalog (e.g. 'mission hill' → 15 wines)."""
    variants: list[str] = []
    toks = cleaned.split()

    stripped = _strip_refinements(cleaned)
    if stripped and stripped != cleaned:
        variants.append(stripped)

    # Drop trailing tokens one at a time, down to (but not below) 3 tokens.
    for end in range(len(toks) - 1, 2, -1):
        cand = " ".join(toks[:end])
        if cand and cand != cleaned and cand not in variants:
            variants.append(cand)

    return variants


async def search_with_fallback(
    attempt: Callable[[str], Awaitable[list]],
    query: str,
    *,
    clean: Callable[[str], str] | None = clean_query,
) -> list:
    """Run `attempt(query)`; if it returns an empty list, retry with each
    `query_variants` until one yields results. Returns the first non-empty result
    list (or the final empty one).

    Args:
        attempt: async callable taking a (cleaned) query string → list of results.
        query:   the raw user/orchestrator query.
        clean:   cleaner applied once to `query` before searching; pass a store's own
                 cleaner (Legacy) or None to skip. Variants are derived from the
                 cleaned string and need no further cleaning.
    """
    cleaned = clean(query) if clean else query

    results = await attempt(cleaned)
    if results:
        return results

    for variant in query_variants(cleaned):
        results = await attempt(variant)
        if results:
            return results

    return results
