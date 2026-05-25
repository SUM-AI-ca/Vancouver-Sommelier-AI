"""Build SQLite database from gismondi-canada-wines CSV with FTS5 full-text search."""

import csv
import sqlite3
from pathlib import Path

CSV_PATH = Path(__file__).parent / "gismondi-canada-wines" / "canada_wines.csv"
DB_PATH = Path(__file__).parent / "data" / "wines.db"

SCHEMA = """
CREATE TABLE IF NOT EXISTS wines (
    note_id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    score_100 INTEGER,
    score_20 TEXT,
    region TEXT,
    tasting_notes TEXT,
    tasting_date TEXT,
    taster TEXT,
    price REAL,
    price_region TEXT,
    price_format TEXT,
    price_channel TEXT,
    producer TEXT,
    distributor TEXT,
    grape TEXT,
    cspc TEXT,
    upc TEXT,
    url TEXT,
    updated_at TEXT
);

CREATE VIRTUAL TABLE IF NOT EXISTS wines_fts USING fts5(
    title, region, tasting_notes, grape, producer,
    content='wines',
    content_rowid='note_id'
);

CREATE TRIGGER IF NOT EXISTS wines_ai AFTER INSERT ON wines BEGIN
    INSERT INTO wines_fts(rowid, title, region, tasting_notes, grape, producer)
    VALUES (new.note_id, new.title, new.region, new.tasting_notes, new.grape, new.producer);
END;

CREATE TRIGGER IF NOT EXISTS wines_ad AFTER DELETE ON wines BEGIN
    INSERT INTO wines_fts(wines_fts, rowid, title, region, tasting_notes, grape, producer)
    VALUES ('delete', old.note_id, old.title, old.region, old.tasting_notes, old.grape, old.producer);
END;

CREATE TRIGGER IF NOT EXISTS wines_au AFTER UPDATE ON wines BEGIN
    INSERT INTO wines_fts(wines_fts, rowid, title, region, tasting_notes, grape, producer)
    VALUES ('delete', old.note_id, old.title, old.region, old.tasting_notes, old.grape, old.producer);
    INSERT INTO wines_fts(rowid, title, region, tasting_notes, grape, producer)
    VALUES (new.note_id, new.title, new.region, new.tasting_notes, new.grape, new.producer);
END;
"""

COLUMNS = [
    "note_id", "title", "score_100", "score_20", "region",
    "tasting_notes", "tasting_date", "taster", "price",
    "price_region", "price_format", "price_channel", "producer",
    "distributor", "grape", "cspc", "upc", "url", "updated_at",
]


def parse_price(val: str) -> float | None:
    if not val:
        return None
    cleaned = val.replace("$", "").replace(",", "").strip()
    try:
        return float(cleaned)
    except ValueError:
        return None


def parse_int(val: str) -> int | None:
    if not val:
        return None
    try:
        return int(val)
    except ValueError:
        return None


def build():
    if not CSV_PATH.exists():
        raise FileNotFoundError(f"CSV not found: {CSV_PATH}")

    DB_PATH.parent.mkdir(parents=True, exist_ok=True)

    if DB_PATH.exists():
        DB_PATH.unlink()

    conn = sqlite3.connect(DB_PATH)
    conn.executescript(SCHEMA)

    with open(CSV_PATH, encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        rows = []
        for row in reader:
            rows.append((
                parse_int(row["note_id"]),
                row["title"].strip(),
                parse_int(row["score_100"]),
                row["score_20"].strip() or None,
                row["region"].strip() or None,
                row["tasting_notes"].strip() or None,
                row["tasting_date"].strip() or None,
                row["taster"].strip() or None,
                parse_price(row["price"]),
                row["price_region"].strip() or None,
                row["price_format"].strip() or None,
                row["price_channel"].strip() or None,
                row["producer"].strip() or None,
                row["distributor"].strip() or None,
                row["grape"].strip() or None,
                row["cspc"].strip() or None,
                row["upc"].strip() or None,
                row["url"].strip() or None,
                row["updated_at"].strip() or None,
            ))

    placeholders = ", ".join(["?"] * len(COLUMNS))
    conn.executemany(f"INSERT INTO wines ({', '.join(COLUMNS)}) VALUES ({placeholders})", rows)
    conn.commit()

    count = conn.execute("SELECT COUNT(*) FROM wines").fetchone()[0]
    conn.close()
    print(f"Built {DB_PATH} with {count} wines")


if __name__ == "__main__":
    build()
