"""
Gismondi Tool for BC Wine AI Agent (LangGraph)

Searches Anthony Gismondi's Canadian wine review archive via a local
SQLite database with FTS5 full-text search. The DB is built by
`build_db.py` from the `gismondi-canada-wines` git submodule.

Indexed fields (FTS5): title, region, tasting_notes, grape, producer.
"""

import asyncio
import re
import sqlite3
from pathlib import Path

from pydantic import BaseModel


# ── Config ──────────────────────────────────────────────────────────

DB_PATH = Path(__file__).resolve().parent.parent / "data" / "wines.db"


# ── Data Model ──────────────────────────────────────────────────────

class GismondiResult(BaseModel):
    note_id: int
    title: str
    score_100: int
    score_20: str
    region: str
    tasting_notes: str
    tasting_date: str
    taster: str
    price: float | None = None
    price_format: str | None = None
    price_channel: str | None = None
    producer: str
    grape: list[str] = []
    distributor: str | None = None
    cspc: str | None = None
    upc: str | None = None
    url: str


# ── FTS5 Query Sanitization ─────────────────────────────────────────

def _sanitize_fts_query(query: str) -> str:
    """Strip FTS5-significant characters and collapse whitespace.

    Multiple bareword tokens are implicitly AND-ed by FTS5, so we just
    need to keep word characters and spaces.
    """
    sanitized = re.sub(r"[^\w\s]", " ", query)
    sanitized = " ".join(sanitized.split())
    return sanitized


# ── Core Search ─────────────────────────────────────────────────────

def _search_sync(
    query: str,
    limit: int,
    score_min: int,
    price_max: float | None,
    bc_only: bool,
) -> list[GismondiResult]:
    if not DB_PATH.exists():
        raise FileNotFoundError(
            f"Database not built: {DB_PATH}. Run: python build_db.py"
        )

    fts_query = _sanitize_fts_query(query)
    if not fts_query:
        return []

    sql = """
    SELECT
        w.note_id, w.title, w.score_100, w.score_20, w.region,
        w.tasting_notes, w.tasting_date, w.taster, w.price,
        w.price_format, w.price_channel, w.producer,
        w.distributor, w.grape, w.cspc, w.upc, w.url
    FROM wines w
    JOIN wines_fts f ON w.note_id = f.rowid
    WHERE wines_fts MATCH ?
      AND w.score_100 >= ?
    """
    params: list = [fts_query, score_min]

    if price_max is not None:
        sql += " AND w.price IS NOT NULL AND w.price <= ?"
        params.append(price_max)

    if bc_only:
        sql += " AND w.region LIKE '%British Columbia%'"

    sql += " ORDER BY w.score_100 DESC, w.tasting_date DESC LIMIT ?"
    params.append(limit)

    conn = sqlite3.connect(DB_PATH)
    try:
        cursor = conn.execute(sql, params)
        rows = cursor.fetchall()
    finally:
        conn.close()

    results: list[GismondiResult] = []
    for row in rows:
        (
            note_id, title, score_100, score_20, region, tasting_notes,
            tasting_date, taster, price, price_format, price_channel,
            producer, distributor, grape, cspc, upc, url,
        ) = row

        grape_list = [g.strip() for g in (grape or "").split(" - ") if g.strip()]

        results.append(
            GismondiResult(
                note_id=note_id,
                title=title,
                score_100=score_100 or 0,
                score_20=score_20 or "",
                region=region or "",
                tasting_notes=tasting_notes or "",
                tasting_date=tasting_date or "",
                taster=taster or "",
                price=price,
                price_format=price_format,
                price_channel=price_channel,
                producer=producer or "",
                grape=grape_list,
                distributor=distributor,
                cspc=cspc,
                upc=upc,
                url=url or "",
            )
        )

    return results


async def search_gismondi(
    query: str,
    limit: int = 10,
    score_min: int = 0,
    price_max: float | None = None,
    bc_only: bool = True,
) -> list[GismondiResult]:
    """
    Search Anthony Gismondi's Canadian wine review archive (SQLite + FTS5).

    Args:
        query:      Wine name, varietal, region, producer, or tasting-note keyword.
        limit:      Max rows returned (default 10).
        score_min:  Minimum /100 score; default 0 (no filter).
        price_max:  CAD price ceiling; None disables (default None). NULL-priced
                    rows are excluded when this is set.
        bc_only:    If True (default), restrict to British Columbia wines.

    Returns:
        list[GismondiResult] ordered by score_100 desc, tasting_date desc.
    """
    return await asyncio.to_thread(
        _search_sync, query, limit, score_min, price_max, bc_only
    )


# ── Formatting ──────────────────────────────────────────────────────

def format_results(results: list[GismondiResult], query: str) -> str:
    if not results:
        return f"No Gismondi reviews found for '{query}'."

    lines = [f"Gismondi Reviews: {len(results)} results for '{query}'\n"]

    for i, r in enumerate(results, 1):
        parts = [f"{i}. {r.title}  ({r.score_100}/100 — {r.taster})"]

        if r.region:
            parts.append(f"   Region: {r.region}")

        if r.grape:
            parts.append(f"   Grape: {' / '.join(r.grape)}")

        if r.price is not None:
            price_str = f"${r.price:.2f}"
            if r.price_format:
                price_str += f" ({r.price_format})"
            if r.price_channel:
                price_str += f" — {r.price_channel}"
            parts.append(f"   Price: {price_str}")

        if r.tasting_notes:
            note = r.tasting_notes.strip()
            if len(note) > 220:
                note = note[:220].rstrip() + "..."
            parts.append(f"   Notes: {note}")

        if r.tasting_date:
            parts.append(f"   Reviewed: {r.tasting_date}")

        if r.url:
            parts.append(f"   URL: {r.url}")

        lines.append("\n".join(parts))

    return "\n\n".join(lines)


# ── Standalone Test ─────────────────────────────────────────────────

async def main():
    test_cases = [
        ("pinot noir", {"score_min": 90, "limit": 5}),
        ("riesling", {"score_min": 89, "price_max": 40.0, "limit": 5}),
        ("chardonnay", {"score_min": 92, "limit": 5}),
        ("quails gate", {"limit": 5}),
        ("syrah okanagan", {"score_min": 88, "limit": 5}),
        ("checkmate", {"limit": 5}),
    ]
    for query, kwargs in test_cases:
        print(f"Searching '{query}' with filters {kwargs}...\n")
        results = await search_gismondi(query, **kwargs)
        print(format_results(results, query))
        print("\n" + "=" * 70 + "\n")


if __name__ == "__main__":
    asyncio.run(main())
