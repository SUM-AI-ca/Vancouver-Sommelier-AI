"""Wine name normalization and cross-store deduplication."""

import json
import re

from langchain_core.messages import BaseMessage, ToolMessage
from rapidfuzz import fuzz

from state import CriticReviewMerged, MergedWineRecord, StorePrice

VINTAGE_RE = re.compile(r"\b(19|20)\d{2}\b")
NOISE_WORDS = {"vineyards", "winery", "estate", "cellars", "wines", "vineyard", "wine"}


def normalize(
    name: str, producer: str | None = None
) -> tuple[str, str, int | None]:
    vintage_match = VINTAGE_RE.search(name)
    vintage = int(vintage_match.group()) if vintage_match else None
    cleaned = VINTAGE_RE.sub("", name)
    cleaned = re.sub(r"[^\w\s]", " ", cleaned).lower()
    tokens = [t for t in cleaned.split() if t and t not in NOISE_WORDS]
    wine_slug = " ".join(tokens)
    prod_slug = ""
    if producer:
        prod_slug = producer.lower().strip()
        prod_slug = " ".join(t for t in prod_slug.split() if t not in NOISE_WORDS)
    return prod_slug, wine_slug, vintage


def _make_key(prod_slug: str, wine_slug: str, vintage: int | None) -> str:
    v = str(vintage) if vintage else "nv"
    return f"{prod_slug}|{wine_slug}|{v}"


def _find_match(
    key: str,
    prod_slug: str,
    wine_slug: str,
    vintage: int | None,
    existing: dict[str, MergedWineRecord],
) -> str | None:
    if key in existing:
        return key
    for ek, ev in existing.items():
        ep, ew, ev_parts = ek.split("|", 2)
        ev_int = int(ev_parts) if ev_parts != "nv" else None
        if ev_int != vintage:
            continue
        if ep != prod_slug:
            continue
        if fuzz.token_set_ratio(ew, wine_slug) >= 88:
            return ek
    return None


def _parse_price(raw: str | float | None) -> float | None:
    if raw is None:
        return None
    if isinstance(raw, (int, float)):
        return float(raw)
    cleaned = re.sub(r"[^\d.]", "", str(raw))
    try:
        return float(cleaned)
    except (ValueError, TypeError):
        return None


def _select_best_price(prices: list[StorePrice]) -> StorePrice | None:
    # Reference prices (Gismondi review quotes) are NOT real inventory — exclude
    # them from best_price selection entirely. They are still kept in `prices`
    # for the synthesizer to render as a "Reference price" footnote.
    real = [p for p in prices if not p.get("is_reference")]
    if not real:
        return None
    in_stock = [p for p in real if p.get("in_stock")]
    pool = in_stock if in_stock else real
    return min(pool, key=lambda p: (p["price"], not p.get("on_sale", False), p["store"]))


def _extract_bcliquor(results: list[dict]) -> list[tuple[MergedWineRecord, str, str, int | None]]:
    out = []
    for r in results:
        name = r.get("name", "")
        prod_slug, wine_slug, vintage = normalize(name)
        price = _parse_price(r.get("current_price"))
        if price is None:
            continue
        sp: StorePrice = {
            "store": "bcliquor",
            "price": price,
            "on_sale": r.get("on_sale", False),
            "in_stock": (r.get("available_units") or 0) > 0,
            "url": r.get("product_url"),
            "stock_qty": r.get("available_units"),
        }
        rec: MergedWineRecord = {
            "normalized_key": "",
            "display_name": name,
            "producer": "",
            "vintage": vintage,
            "grape": [r["grape_type"]] if r.get("grape_type") else [],
            "prices": [sp],
            "best_price": None,
            "critic_reviews": [],
            "avg_critic_score": None,
            "consumer_rating": r.get("consumer_rating"),
            "consumer_votes": r.get("consumer_votes"),
            "is_bc_vqa": r.get("is_bc_vqa", False),
            "tasting_notes_consolidated": r.get("tasting_notes") if isinstance(r.get("tasting_notes"), str) else None,
        }
        out.append((rec, prod_slug, wine_slug, vintage))
    return out


def _extract_marquis(results: list[dict]) -> list[tuple[MergedWineRecord, str, str, int | None]]:
    out = []
    for r in results:
        name = r.get("name", "")
        prod_slug, wine_slug, vintage = normalize(name)
        price = _parse_price(r.get("sale_price") or r.get("price"))
        if price is None:
            continue
        sp: StorePrice = {
            "store": "marquis",
            "price": price,
            "on_sale": r.get("on_sale", False),
            "in_stock": r.get("in_stock", True),
            "url": r.get("url"),
            "stock_qty": r.get("inventory_level"),
        }
        rec: MergedWineRecord = {
            "normalized_key": "",
            "display_name": name,
            "producer": "",
            "vintage": vintage,
            "grape": [],
            "prices": [sp],
            "best_price": None,
            "critic_reviews": [],
            "avg_critic_score": None,
            "consumer_rating": None,
            "consumer_votes": None,
            "is_bc_vqa": False,
            "tasting_notes_consolidated": None,
        }
        out.append((rec, prod_slug, wine_slug, vintage))
    return out


def _extract_legacy(results: list[dict]) -> list[tuple[MergedWineRecord, str, str, int | None]]:
    out = []
    for r in results:
        name = r.get("name", "")
        prod_slug, wine_slug, vintage = normalize(name, r.get("brand"))
        price = _parse_price(r.get("price"))
        if price is None:
            continue
        sp: StorePrice = {
            "store": "legacy",
            "price": price,
            "on_sale": r.get("on_sale", False),
            "in_stock": r.get("in_stock", True),
            "url": r.get("url"),
            "stock_qty": r.get("stock_qty"),
        }
        rec: MergedWineRecord = {
            "normalized_key": "",
            "display_name": name,
            "producer": r.get("brand", ""),
            "vintage": vintage,
            "grape": [],
            "prices": [sp],
            "best_price": None,
            "critic_reviews": [],
            "avg_critic_score": None,
            "consumer_rating": None,
            "consumer_votes": None,
            "is_bc_vqa": False,
            "tasting_notes_consolidated": None,
        }
        out.append((rec, prod_slug, wine_slug, vintage))
    return out


def _extract_okanagan(results: list[dict]) -> list[tuple[MergedWineRecord, str, str, int | None]]:
    out = []
    for r in results:
        name = r.get("name", "")
        prod_slug, wine_slug, vintage = normalize(name)
        price = _parse_price(r.get("sale_price") or r.get("regular_price"))
        if price is None:
            continue
        sp: StorePrice = {
            "store": "okanagan",
            "price": price,
            "on_sale": r.get("on_sale", False),
            "in_stock": r.get("in_stock", False),
            "url": r.get("product_url"),
            "stock_qty": r.get("stock_qty"),
        }
        rec: MergedWineRecord = {
            "normalized_key": "",
            "display_name": name,
            "producer": "",
            "vintage": vintage,
            "grape": [],
            "prices": [sp],
            "best_price": None,
            "critic_reviews": [],
            "avg_critic_score": None,
            "consumer_rating": None,
            "consumer_votes": None,
            "is_bc_vqa": False,
            "tasting_notes_consolidated": None,
        }
        out.append((rec, prod_slug, wine_slug, vintage))
    return out


def _extract_everythingwine(results: list[dict]) -> list[tuple[MergedWineRecord, str, str, int | None]]:
    out = []
    for r in results:
        name = r.get("name", "")
        prod_slug, wine_slug, vintage = normalize(name)
        price = _parse_price(r.get("price"))
        if price is None:
            continue
        stocks = r.get("stock", [])
        in_stock = any(s.get("status") == "available" for s in stocks)
        sp: StorePrice = {
            "store": "everythingwine",
            "price": price,
            "on_sale": r.get("on_sale", False),
            "in_stock": in_stock,
            "url": r.get("url"),
            "stock_qty": None,
        }
        rec: MergedWineRecord = {
            "normalized_key": "",
            "display_name": name,
            "producer": "",
            "vintage": vintage,
            "grape": [],
            "prices": [sp],
            "best_price": None,
            "critic_reviews": [],
            "avg_critic_score": None,
            "consumer_rating": None,
            "consumer_votes": None,
            "is_bc_vqa": False,
            "tasting_notes_consolidated": None,
        }
        out.append((rec, prod_slug, wine_slug, vintage))
    return out


def _extract_winealign(
    results: list[dict],
) -> list[tuple[str, str, int | None, list[CriticReviewMerged], list[StorePrice]]]:
    out = []
    for r in results:
        name = r.get("wine_name", "")
        prod_slug, wine_slug, vintage = normalize(name)
        reviews: list[CriticReviewMerged] = []
        for cr in r.get("critic_reviews", []):
            reviews.append({
                "source": "winealign",
                "critic_name": cr.get("critic_name", "Unknown"),
                "score": cr.get("score", ""),
                "tasting_notes": cr.get("tasting_notes", ""),
                "value_rating": cr.get("value_rating"),
                "drink_window": cr.get("drink_window"),
            })
        if reviews:
            out.append((prod_slug, wine_slug, vintage, reviews, []))
    return out


def _extract_gismondi(
    results: list[dict],
) -> list[tuple[str, str, int | None, list[CriticReviewMerged], list[StorePrice]]]:
    out = []
    for r in results:
        name = r.get("title", "")
        prod_slug, wine_slug, vintage = normalize(name, r.get("producer"))
        review: CriticReviewMerged = {
            "source": "gismondi",
            "critic_name": r.get("taster", "Anthony Gismondi"),
            "score": f"{r.get('score_100', '')}/100",
            "tasting_notes": r.get("tasting_notes", ""),
            "value_rating": None,
            "drink_window": None,
        }
        # Gismondi reviews include the price + channel observed at review time.
        # These are NOT live inventory checks — Gismondi is a critic, not a
        # retailer. We still promote them so price-constrained queries
        # ("BC Riesling under $30") have something to render, but they are
        # tagged `is_reference=True` so synthesis renders them as a "Reference
        # price (per Gismondi review)" note rather than as a row in the
        # Where-to-buy table. The URL points at the review.
        prices: list[StorePrice] = []
        price = r.get("price")
        if price is not None:
            try:
                price_f = float(price)
            except (TypeError, ValueError):
                price_f = None
            if price_f is not None:
                channel = (r.get("price_channel") or "").strip()
                prices.append({
                    "store": "gismondi_ref",
                    "price": price_f,
                    "on_sale": False,
                    "in_stock": False,    # unknown — never claim stock from a review
                    "url": r.get("url"),  # link back to the Gismondi review
                    "stock_qty": None,
                    "is_reference": True,
                    "ref_channel": channel or None,  # raw channel string for the note
                })
        out.append((prod_slug, wine_slug, vintage, [review], prices))
    return out


def _extract_robert_parker(
    results: list[dict],
) -> list[tuple[str, str, int | None, list[CriticReviewMerged], list[StorePrice]]]:
    out = []
    for r in results:
        name = r.get("display_name", "")
        prod_slug, wine_slug, vintage = normalize(name, r.get("producer"))
        reviews: list[CriticReviewMerged] = []
        drink_window = None
        if r.get("drink_date_low") and r.get("drink_date_high"):
            drink_window = f"{r['drink_date_low']}–{r['drink_date_high']}"
        for tn in r.get("tasting_notes", []):
            reviews.append({
                "source": "robert_parker",
                "critic_name": tn.get("reviewer", "Unknown"),
                "score": tn.get("rating", r.get("rating_display", "")),
                "tasting_notes": tn.get("content", ""),
                "value_rating": None,
                "drink_window": drink_window,
            })
        if not reviews and r.get("rating_display"):
            reviews.append({
                "source": "robert_parker",
                "critic_name": r.get("last_reviewer", "Robert Parker"),
                "score": r.get("rating_display", ""),
                "tasting_notes": "",
                "value_rating": None,
                "drink_window": drink_window,
            })
        if reviews:
            out.append((prod_slug, wine_slug, vintage, reviews, []))
    return out


TOOL_TO_EXTRACTOR = {
    "search_bcliquor": ("store", _extract_bcliquor),
    "search_marquis": ("store", _extract_marquis),
    "search_legacy_liquor_store": ("store", _extract_legacy),
    "search_okanagan_cellars": ("store", _extract_okanagan),
    "search_everything_wine": ("store", _extract_everythingwine),
    "search_winealign": ("critic", _extract_winealign),
    "search_gismondi": ("critic", _extract_gismondi),
    "search_robert_parker": ("critic", _extract_robert_parker),
}


def _parse_tool_content(content: str) -> tuple[str | None, list[dict]]:
    try:
        data = json.loads(content)
    except (json.JSONDecodeError, TypeError):
        return None, []
    if isinstance(data, dict):
        tool_name = data.get("tool")
        results = data.get("results", [])
        return tool_name, results if isinstance(results, list) else []
    if isinstance(data, list):
        return None, data
    return None, []


def merge_tool_results(messages: list[BaseMessage]) -> dict[str, MergedWineRecord]:
    merged: dict[str, MergedWineRecord] = {}

    for msg in messages:
        if not isinstance(msg, ToolMessage):
            continue
        tool_name = getattr(msg, "name", None)
        content = msg.content if isinstance(msg.content, str) else str(msg.content)
        parsed_tool, results = _parse_tool_content(content)
        # Prefer the tool name embedded in the JSON payload (set by our @tool
        # wrappers to the canonical bare name, e.g. "search_bcliquor"). Fall back
        # to msg.name, which arrives with the LangChain binding suffix
        # ("search_bcliquor_tool") and must be stripped before lookup.
        effective_tool = parsed_tool or tool_name
        if effective_tool and effective_tool.endswith("_tool"):
            effective_tool = effective_tool[:-5]
        if not effective_tool or effective_tool not in TOOL_TO_EXTRACTOR:
            continue
        kind, extractor = TOOL_TO_EXTRACTOR[effective_tool]

        if kind == "store":
            items = extractor(results)
            for rec, ps, ws, v in items:
                key = _make_key(ps, ws, v)
                match_key = _find_match(key, ps, ws, v, merged)
                if match_key:
                    existing = merged[match_key]
                    existing["prices"].extend(rec["prices"])
                    if rec.get("consumer_rating") and not existing.get("consumer_rating"):
                        existing["consumer_rating"] = rec["consumer_rating"]
                        existing["consumer_votes"] = rec.get("consumer_votes")
                    if rec.get("is_bc_vqa"):
                        existing["is_bc_vqa"] = True
                    if rec.get("grape") and not existing.get("grape"):
                        existing["grape"] = rec["grape"]
                    if rec.get("tasting_notes_consolidated") and not existing.get("tasting_notes_consolidated"):
                        existing["tasting_notes_consolidated"] = rec["tasting_notes_consolidated"]
                else:
                    rec["normalized_key"] = key
                    merged[key] = rec

        elif kind == "critic":
            critic_items = extractor(results)
            for ps, ws, v, reviews, crit_prices in critic_items:
                key = _make_key(ps, ws, v)
                match_key = _find_match(key, ps, ws, v, merged)
                if match_key:
                    merged[match_key]["critic_reviews"].extend(reviews)
                    if crit_prices:
                        merged[match_key]["prices"].extend(crit_prices)
                else:
                    rec: MergedWineRecord = {
                        "normalized_key": key,
                        "display_name": ws.title(),
                        "producer": ps.title() if ps else "",
                        "vintage": v,
                        "grape": [],
                        "prices": list(crit_prices),
                        "best_price": None,
                        "critic_reviews": reviews,
                        "avg_critic_score": None,
                        "consumer_rating": None,
                        "consumer_votes": None,
                        "is_bc_vqa": False,
                        "tasting_notes_consolidated": None,
                    }
                    merged[key] = rec

    for rec in merged.values():
        rec["best_price"] = _select_best_price(rec["prices"])
        tn = [r["tasting_notes"] for r in rec["critic_reviews"] if r["tasting_notes"]]
        if tn and not rec["tasting_notes_consolidated"]:
            rec["tasting_notes_consolidated"] = max(tn, key=len)

    return merged
