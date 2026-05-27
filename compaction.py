"""Tool-result compaction node — runs between `tools` and `orchestrator`.

For each batch of tool results, we (1) incrementally merge raw results into
`wine_context` so synthesis already has the facts when the loop exits, and
(2) replace each compactable ToolMessage with a small projection so the next
orchestrator round attends over ~10× less context. Synthesis is unaffected —
it reads `wine_context`, never ToolMessage content directly.

Tools whose output is consumed by the synthesizer's aux-collector
(`search_tavily`, `reasoning_pair_wine`) or by the preferences harvest
(`update_preferences`) are passed through unchanged.
"""

from __future__ import annotations

import json
import re
from typing import Any

from langchain_core.messages import AIMessage, ToolMessage

from merge import _select_best_price, merge_tool_results, normalize
from state import AgentState, MergedWineRecord


MAX_COMPACT_TOP_N = 10

_COMPACTABLE_STORE_TOOLS = {
    "search_bcliquor",
    "search_marquis",
    "search_okanagan_cellars",
    "search_everything_wine",
}
_COMPACTABLE_CRITIC_TOOLS = {
    "search_winealign",
    "search_gismondi",
    "search_robert_parker",
}
_PASS_THROUGH_TOOLS = {
    "search_tavily",
    "reasoning_pair_wine",
    "update_preferences",
}


def _strip_tool_suffix(name: str | None) -> str | None:
    if not name:
        return None
    return name[:-5] if name.endswith("_tool") else name


def _vintage_of(name: str | None) -> int | None:
    if not name:
        return None
    _, _, v = normalize(name)
    return v


def _project_store_row(r: dict) -> dict:
    name = r.get("name") or r.get("display_name") or ""
    price_raw = (
        r.get("current_price")
        or r.get("sale_price")
        or r.get("price")
        or r.get("regular_price")
    )
    price: float | None
    try:
        price = float(re.sub(r"[^\d.]", "", str(price_raw))) if price_raw not in (None, "") else None
    except (ValueError, TypeError):
        price = None
    if r.get("available_units") is not None:
        in_stock = (r.get("available_units") or 0) > 0
    elif isinstance(r.get("stock"), list):
        in_stock = any(s.get("status") == "available" for s in r["stock"])
    else:
        in_stock = bool(r.get("in_stock"))
    # URL field name varies across stores: bcliquor/okanagan use `product_url`,
    # marquis/everythingwine use `url`. Coalesce. Keeping the real URL in the
    # compact projection prevents the orchestrator from fabricating plausible-
    # looking links in its draft (which synthesis was sometimes echoing).
    url = r.get("product_url") or r.get("url") or r.get("wine_url")
    return {
        "name": str(name)[:160],
        "price": price,
        "in_stock": in_stock,
        "vintage": _vintage_of(name),
        "url": url if isinstance(url, str) else None,
    }


def _project_critic_row(r: dict, tool: str) -> dict:
    url: str | None = None
    if tool == "search_winealign":
        name = r.get("wine_name") or ""
        reviews = r.get("critic_reviews") or []
        top = reviews[0] if reviews else {}
        score = top.get("score") or ""
        critic = top.get("critic_name") or ""
        url = r.get("url") or r.get("wine_url")
    elif tool == "search_gismondi":
        name = r.get("title") or ""
        score = f"{r.get('score_100', '')}/100" if r.get("score_100") else ""
        critic = r.get("taster") or "Anthony Gismondi"
        url = r.get("url")
    elif tool == "search_robert_parker":
        name = r.get("display_name") or ""
        notes = r.get("tasting_notes") or []
        top = notes[0] if notes else {}
        score = top.get("rating") or r.get("rating_display") or ""
        critic = top.get("reviewer") or r.get("last_reviewer") or "Robert Parker"
        url = r.get("url")
    else:
        name = r.get("name") or r.get("title") or r.get("display_name") or ""
        score = ""
        critic = ""
    return {
        "name": str(name)[:160],
        "score": str(score)[:32],
        "critic": str(critic)[:64],
        "vintage": _vintage_of(name),
        "url": url if isinstance(url, str) else None,
    }


def _build_compact_payload(tool: str, raw_results: list[dict]) -> dict:
    if tool in _COMPACTABLE_STORE_TOOLS:
        rows = [_project_store_row(r) for r in raw_results if isinstance(r, dict)]
    elif tool in _COMPACTABLE_CRITIC_TOOLS:
        rows = [_project_critic_row(r, tool) for r in raw_results if isinstance(r, dict)]
    else:
        rows = []
    return {
        "status": "ok",
        "tool": tool,
        "compacted": True,
        "result_count": len(raw_results),
        "top_results": rows[:MAX_COMPACT_TOP_N],
        # results=[] so any future merge_tool_results pass over this message is a no-op.
        "results": [],
    }


def _compact_tool_message(msg: ToolMessage) -> ToolMessage | None:
    """Build a same-id replacement ToolMessage carrying compact content, or
    None to pass the original through unchanged (small / aux / parse-failed)."""
    raw = msg.content if isinstance(msg.content, str) else ""
    if not raw:
        return None
    try:
        data = json.loads(raw)
    except (json.JSONDecodeError, TypeError):
        return None
    if not isinstance(data, dict):
        return None
    tool = data.get("tool") or _strip_tool_suffix(getattr(msg, "name", None))
    tool = _strip_tool_suffix(tool)
    if not tool:
        return None
    if tool in _PASS_THROUGH_TOOLS:
        return None
    if tool not in _COMPACTABLE_STORE_TOOLS and tool not in _COMPACTABLE_CRITIC_TOOLS:
        return None
    if data.get("compacted"):
        return None
    results = data.get("results")
    if not isinstance(results, list):
        return None
    payload = _build_compact_payload(tool, results)
    return ToolMessage(
        content=json.dumps(payload, ensure_ascii=False),
        tool_call_id=msg.tool_call_id,
        name=msg.name,
        id=msg.id,
    )


def _merge_into_context(
    existing: dict[str, MergedWineRecord],
    incremental: dict[str, MergedWineRecord],
) -> None:
    """Extend prices/critic_reviews on duplicate keys; insert new keys as-is.
    Recomputes best_price after extension."""
    for key, new_rec in incremental.items():
        if key in existing:
            cur = existing[key]
            cur["prices"].extend(new_rec.get("prices") or [])
            cur["critic_reviews"].extend(new_rec.get("critic_reviews") or [])
            cur["best_price"] = _select_best_price(cur["prices"])
            if new_rec.get("consumer_rating") and not cur.get("consumer_rating"):
                cur["consumer_rating"] = new_rec["consumer_rating"]
                cur["consumer_votes"] = new_rec.get("consumer_votes")
            if new_rec.get("is_bc_vqa"):
                cur["is_bc_vqa"] = True
            if new_rec.get("grape") and not cur.get("grape"):
                cur["grape"] = new_rec["grape"]
            if new_rec.get("tasting_notes_consolidated") and not cur.get("tasting_notes_consolidated"):
                cur["tasting_notes_consolidated"] = new_rec["tasting_notes_consolidated"]
        else:
            existing[key] = new_rec


def _harvest_preferences(batch: list[ToolMessage], prefs: dict) -> None:
    """Mirror merge_results_node's prefs harvest over one batch (idempotent)."""
    for msg in batch:
        content = msg.content if isinstance(msg.content, str) else ""
        if not content:
            continue
        try:
            data = json.loads(content)
        except (json.JSONDecodeError, TypeError):
            continue
        if not isinstance(data, dict) or data.get("tool") != "update_preferences":
            continue
        if data.get("budget_max"):
            prefs["budget_max"] = data["budget_max"]
        if data.get("add_varietals"):
            existing_v = prefs.get("preferred_varietals", [])
            prefs["preferred_varietals"] = list(set(existing_v + data["add_varietals"]))
        if data.get("sweetness"):
            prefs["sweetness"] = data["sweetness"]
        if data.get("style"):
            prefs["style"] = data["style"]


def compact_tool_results_node(state: AgentState) -> dict[str, Any]:
    """Between `tools` and the loop-back to `orchestrator`:

    1. Identify this round's batch of ToolMessages (since last AIMessage).
    2. Smart-merge raw results into state["wine_context"] (synthesis facts).
    3. Harvest update_preferences calls.
    4. Replace each compactable ToolMessage with a compact projection — same id
       so the LangGraph `add_messages` reducer replaces in place.
    """
    msgs = state["messages"]

    batch: list[ToolMessage] = []
    for msg in reversed(msgs):
        if isinstance(msg, AIMessage):
            break
        if isinstance(msg, ToolMessage):
            batch.append(msg)
    batch.reverse()
    if not batch:
        return {}

    incremental = merge_tool_results(batch)
    wine_ctx: dict[str, MergedWineRecord] = dict(state.get("wine_context") or {})
    _merge_into_context(wine_ctx, incremental)

    prefs = dict(state.get("user_preferences") or {})
    _harvest_preferences(batch, prefs)

    replacements: list[ToolMessage] = []
    for msg in batch:
        compact = _compact_tool_message(msg)
        if compact is not None:
            replacements.append(compact)

    out: dict[str, Any] = {"wine_context": wine_ctx}
    if replacements:
        out["messages"] = replacements
    if prefs:
        out["user_preferences"] = prefs
    return out
