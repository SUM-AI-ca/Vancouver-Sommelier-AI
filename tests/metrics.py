"""Deterministic metrics for BC Wine AI quality eval.

Pure functions, no LLM. Used by quality_eval.py to score each query's response
along orchestration / hallucination / coverage / structure dimensions.
"""

from __future__ import annotations

import json
import re
from typing import Any

from langchain_core.messages import AIMessage, ToolMessage

from tests.golden_queries import KNOWN_BC_WINERIES, KNOWN_CRITICS, KNOWN_STORES


# =====================================================================
# Content extraction helpers
# =====================================================================

def to_text(content: Any) -> str:
    """Robustly extract text from a LangChain message content (str | list[str|dict]).
    Handles Gemini 3.x parts-style content where content is a list of dicts with 'text'.
    """
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        parts = []
        for item in content:
            if isinstance(item, str):
                parts.append(item)
            elif isinstance(item, dict):
                parts.append(item.get("text", ""))
            else:
                parts.append(getattr(item, "text", str(item)))
        return "".join(parts)
    return str(content)


def extract_final_response(state: dict) -> str:
    """Walk state['messages'] backwards to find the last AIMessage with no tool_calls.
    That message is the agent's final answer for this turn.
    """
    msgs = state.get("messages", []) if isinstance(state, dict) else []
    for msg in reversed(msgs):
        if isinstance(msg, AIMessage) and not msg.tool_calls:
            return to_text(msg.content)
    return ""


def extract_tool_messages(state: dict) -> list[ToolMessage]:
    msgs = state.get("messages", []) if isinstance(state, dict) else []
    return [m for m in msgs if isinstance(m, ToolMessage)]


def extract_tool_call_records(state: dict) -> list[dict]:
    """Extract tool calls as (name, args) records from AIMessage.tool_calls in order."""
    records = []
    msgs = state.get("messages", []) if isinstance(state, dict) else []
    for msg in msgs:
        if isinstance(msg, AIMessage) and msg.tool_calls:
            for tc in msg.tool_calls:
                records.append({
                    "name": tc.get("name", ""),
                    "args": tc.get("args", {}),
                })
    return records


def collect_tool_results_text(tool_messages: list[ToolMessage]) -> str:
    """Concatenate all ToolMessage contents into a single searchable blob (lowercased)."""
    parts = []
    for tm in tool_messages:
        content = to_text(tm.content)
        parts.append(content)
    return "\n".join(parts).lower()


def collect_wine_context_text(state: dict) -> str:
    """Flatten state['wine_context'] into a searchable, lowercased blob.

    Necessary because `compact_tool_results_node` projects each ToolMessage down
    to top-N rows — so facts that survive only in `wine_context` (full merged
    record set: tasting notes, consumer ratings, all prices/critic reviews,
    URLs across all stores, etc.) would otherwise be invisible to
    `hallucination_check`, producing false positives on facts the synthesizer
    legitimately drew from cumulative state.
    """
    ctx = state.get("wine_context") if isinstance(state, dict) else None
    if not isinstance(ctx, dict):
        return ""
    return json.dumps(ctx, default=str, ensure_ascii=False).lower()


# =====================================================================
# Tool orchestration metrics
# =====================================================================

# Per-turn call limits from prompts.py / AGENT_DESIGN.md §3
TOOL_CALL_LIMITS = {
    "search_tavily": 1,
}


def _strip_tool_suffix(name: str) -> str:
    """Normalize LangChain @tool-bound names ("search_bcliquor_tool") down to
    the canonical bare form ("search_bcliquor") that golden_queries uses."""
    return name[:-5] if isinstance(name, str) and name.endswith("_tool") else name


def tool_orchestration_metrics(
    tool_calls_in_turn: list[dict],   # records from extract_tool_call_records (scoped to this turn)
    expected: dict,                   # the golden query entry
) -> dict:
    """Compare actual tool calls against expected_tools_all_of / any_of / forbidden,
    and check per-turn call limits.

    Returns a dict with deterministic flags and counts.
    """
    called_names = [_strip_tool_suffix(tc["name"]) for tc in tool_calls_in_turn]
    called_set = set(called_names)

    all_of = {_strip_tool_suffix(n) for n in (expected.get("expected_tools_all_of") or [])}
    any_of = {_strip_tool_suffix(n) for n in (expected.get("expected_tools_any_of") or [])}
    forbidden = {_strip_tool_suffix(n) for n in (expected.get("forbidden_tools") or [])}

    missing_all_of = sorted(all_of - called_set)
    has_any_of = bool(any_of & called_set) if any_of else True
    forbidden_called = sorted(forbidden & called_set)

    per_call_counts: dict[str, int] = {}
    for name in called_names:
        per_call_counts[name] = per_call_counts.get(name, 0) + 1

    limit_violations = []
    for tool_name, max_per_turn in TOOL_CALL_LIMITS.items():
        count = per_call_counts.get(tool_name, 0)
        if count > max_per_turn:
            limit_violations.append({
                "tool": tool_name,
                "count": count,
                "limit": max_per_turn,
            })

    expected_universe = all_of | any_of
    if called_set and expected_universe:
        precision = len(called_set & expected_universe) / len(called_set)
    else:
        precision = 1.0 if not called_set else 0.0

    if all_of:
        recall = len(called_set & all_of) / len(all_of)
    elif any_of:
        recall = 1.0 if (called_set & any_of) else 0.0
    else:
        recall = 1.0

    parallel_fan_out = False
    if all_of and "expected_tools_all_of" in expected:
        # all_of fully called AND no intermediate user message between them
        parallel_fan_out = (not missing_all_of) and len(tool_calls_in_turn) >= len(all_of)

    return {
        "called": sorted(called_set),
        "call_sequence": called_names,
        "per_call_counts": per_call_counts,
        "missing_all_of": missing_all_of,
        "has_any_of": has_any_of,
        "forbidden_called": forbidden_called,
        "limit_violations": limit_violations,
        "precision": round(precision, 3),
        "recall": round(recall, 3),
        "f1": round(2 * precision * recall / (precision + recall), 3) if (precision + recall) else 0.0,
        "parallel_fan_out_satisfied": parallel_fan_out,
        "pass": (
            not missing_all_of
            and has_any_of
            and not forbidden_called
            and not limit_violations
        ),
    }


# =====================================================================
# Hallucination checks
# =====================================================================

# Match $XX or $XX.XX (allow ,XXX or commas for thousands)
PRICE_RE = re.compile(r"\$\s?(\d{1,3}(?:,\d{3})*(?:\.\d{1,2})?)")

# Vintages 1900-2039
VINTAGE_RE = re.compile(r"\b(19[0-9]{2}|20[0-3][0-9])\b")

# Score patterns — be strict to avoid false positives.
# "94/100", "94 points", "94 pts", "scored 94", "rated 94", "rating: 94"
SCORE_PATTERNS = [
    re.compile(r"\b(\d{2,3})\s*/\s*100\b"),
    re.compile(r"\b(\d{2,3})\s*(?:points?|pts)\b", re.I),
    re.compile(r"\b(?:scored|rated|rating[: ])\s*(\d{2,3})\b", re.I),
]


def _extract_numbers(text: str, patterns: list[re.Pattern]) -> list[str]:
    found = []
    for pat in patterns:
        for m in pat.finditer(text):
            found.append(m.group(1))
    return found


def _normalize_price(s: str) -> str:
    return s.replace(",", "").rstrip(".0").rstrip(".")


def hallucination_check(
    response_text: str,
    tool_results_blob_lower: str,
    fields: list[str],
) -> dict:
    """Extract factual tokens from response and verify each appears in tool results.

    Unsupported tokens are returned per category. This is the spine of the
    factual-grounding dimension — Claude reads these on the round-trip to
    locate concrete code-level issues.
    """
    unsupported: dict[str, list[str]] = {}

    if "price" in fields:
        prices = PRICE_RE.findall(response_text)
        bad = []
        for p in set(prices):
            norm = _normalize_price(p)
            # tool_results may store as "29.99" without $; try both
            if (
                norm.lower() not in tool_results_blob_lower
                and f"${norm}".lower() not in tool_results_blob_lower
            ):
                bad.append(f"${p}")
        if bad:
            unsupported["price"] = sorted(bad)

    if "vintage" in fields:
        vintages = VINTAGE_RE.findall(response_text)
        bad = []
        for v in set(vintages):
            if v not in tool_results_blob_lower:
                bad.append(v)
        if bad:
            unsupported["vintage"] = sorted(bad)

    if "score" in fields:
        scores = _extract_numbers(response_text, SCORE_PATTERNS)
        bad = []
        for s in set(scores):
            if s not in tool_results_blob_lower:
                bad.append(s)
        if bad:
            unsupported["score"] = sorted(bad)

    if "winery" in fields:
        # Conservative: only flag candidates that end with an unambiguous winery suffix
        # ("Vineyards" / "Winery" / "Vineyard" / "Estate"/"Estates"). We deliberately
        # exclude "Cellars" because it collides with stores (Marquis Wine Cellars,
        # Okanagan Cellars). False positives on winery names are very expensive for
        # the human reading the report, so we err on the side of caution.
        winery_suffix_re = re.compile(
            r"\b([A-Z][A-Za-z'’]+(?:\s+[A-Z][A-Za-z'’]+){0,3}\s+"
            r"(?:Vineyards|Winery|Wineries|Vineyard|Estates|Estate))\b"
        )
        candidates = set(winery_suffix_re.findall(response_text))
        known_lower = {w.lower() for w in KNOWN_BC_WINERIES}
        # Also accept the prefix portion alone (e.g. "Tantalus" if response says "Tantalus Vineyards")
        bad = []
        suffix_strip_re = re.compile(
            r"\s+(?:Vineyards|Winery|Wineries|Vineyard|Estates|Estate)$", re.I
        )
        for c in candidates:
            cl = c.lower()
            if cl in known_lower or cl in tool_results_blob_lower:
                continue
            prefix = suffix_strip_re.sub("", c).strip()
            pl = prefix.lower()
            if pl in known_lower or pl in tool_results_blob_lower:
                continue
            bad.append(c)
        if bad:
            unsupported["winery"] = sorted(bad)[:10]  # cap noise

    total_unsupported = sum(len(v) for v in unsupported.values())
    return {
        "unsupported": unsupported,
        "total_unsupported": total_unsupported,
        "pass": total_unsupported == 0,
    }


# =====================================================================
# Coverage metrics
# =====================================================================

def count_distinct_stores_cited(response_text: str) -> tuple[int, list[str]]:
    rl = response_text.lower()
    hit_codes: set[str] = set()
    for label, code in KNOWN_STORES.items():
        if label.lower() in rl:
            hit_codes.add(code)
    return len(hit_codes), sorted(hit_codes)


def count_distinct_critics_cited(response_text: str) -> tuple[int, list[str]]:
    rl = response_text.lower()
    canonical_seen: set[str] = set()
    detail = []
    canonical_map = {
        "john szabo": "John Szabo",
        "sara d'amato": "Sara d'Amato",
        "sara d amato": "Sara d'Amato",
        "sara damato": "Sara d'Amato",
        "anthony gismondi": "Anthony Gismondi",
        "gismondi": "Anthony Gismondi",
        "robert parker": "Robert Parker",
        "parker": "Robert Parker",
        "mark squires": "Mark Squires",
        "david lawrason": "David Lawrason",
        "rhys pender": "Rhys Pender",
        "treve ring": "Treve Ring",
    }
    for key, canonical in canonical_map.items():
        if key in rl and canonical not in canonical_seen:
            canonical_seen.add(canonical)
            detail.append(canonical)
    return len(canonical_seen), sorted(detail)


MD_LINK_RE = re.compile(r"\[[^\]]+\]\([^)]+\)")


def markdown_link_count(response_text: str) -> int:
    return len(MD_LINK_RE.findall(response_text))


# =====================================================================
# Output contract compliance
# =====================================================================

def output_contract_score(response_text: str) -> dict:
    """Check adherence to SYNTHESIS_SYSTEM_PROMPT skeleton (prompts.py:131).
    Each present section adds 1 to score (max 4).
    """
    rl = response_text
    rl_lower = rl.lower()

    # Lead = first non-empty line that is not a markdown heading or bullet
    lead_present = False
    for line in rl.splitlines():
        s = line.strip()
        if not s:
            continue
        if s.startswith("#") or s.startswith("-") or s.startswith("*"):
            break
        lead_present = True
        break

    why_present = bool(
        re.search(r"\*\*why\b|^#+ *why\b|why this (wine|pairing|works)", rl_lower, re.M)
    )

    table_present = (
        "| store" in rl_lower
        or "| price" in rl_lower
        or bool(re.search(r"\|\s*store\s*\|", rl_lower))
        or (rl.count("\n|") >= 2 and "|---" in rl)
    )
    # Also accept narrative "where to buy" sections that cite ≥2 known stores
    # with prices — Judge consistently grades these as well-structured even
    # without a literal markdown table.
    if not table_present:
        where_section_match = re.search(
            r"(where to buy|where can (you|i) buy|available at|currently in stock|in stock at)",
            rl_lower,
        )
        if where_section_match:
            tail = rl_lower[where_section_match.start():]
            store_hits = sum(
                1 for s in ("bc liquor", "marquis", "everything wine", "okanagan cellars")
                if s in tail
            )
            has_price = bool(re.search(r"\$\s?\d", tail))
            if store_hits >= 2 and has_price:
                table_present = True

    pairing_present = bool(
        re.search(
            r"\*\*pairing\b|^#+ *pairing\b|pair[a-z]*\s+(well\s+)?with|food pairing|"
            r"this (pairing|wine) (works|pairs)|why this pairing",
            rl_lower,
            re.M,
        )
    )

    score = sum([lead_present, why_present, table_present, pairing_present])
    return {
        "lead_present": lead_present,
        "why_present": why_present,
        "where_to_buy_table_present": table_present,
        "pairing_present": pairing_present,
        "score_of_4": score,
    }


# =====================================================================
# Multi-turn reference resolution check
# =====================================================================

def reference_resolution_check(
    turn_state: dict,
    prev_turn_state: dict,
    response_text: str,
) -> dict:
    """For multi-turn queries that reference prior recommendations, check that the
    response either (a) mentions a wine from prev turn's last_recommendations,
    or (b) clearly resolved against wine_context.
    """
    prev_recs = prev_turn_state.get("last_recommendations", []) if prev_turn_state else []
    prev_ctx = prev_turn_state.get("wine_context", {}) if prev_turn_state else {}

    rl = response_text.lower()

    mentioned_keys = []
    for key in prev_recs:
        record = prev_ctx.get(key, {})
        display = record.get("display_name", "") if isinstance(record, dict) else ""
        producer = record.get("producer", "") if isinstance(record, dict) else ""

        candidates = [display, producer]
        if isinstance(record, dict):
            candidates.append(key.split("|")[0])

        for cand in candidates:
            if cand and len(cand) > 2 and cand.lower() in rl:
                mentioned_keys.append(key)
                break

    return {
        "prev_last_recommendations_count": len(prev_recs),
        "mentioned_from_prev_recs": sorted(set(mentioned_keys)),
        "any_referenced": bool(mentioned_keys),
    }


# =====================================================================
# Preference enforcement check
# =====================================================================

def preferences_active_check(
    state: dict,
    expected_prefs: dict,
) -> dict:
    """For MT-PREF turns, verify state['user_preferences'] contains the expected pairs."""
    actual = state.get("user_preferences") or {} if isinstance(state, dict) else {}
    discrepancies = []
    for k, v in expected_prefs.items():
        actual_v = actual.get(k)
        if actual_v != v:
            discrepancies.append({"key": k, "expected": v, "actual": actual_v})
    return {
        "actual_preferences": dict(actual) if actual else {},
        "discrepancies": discrepancies,
        "pass": not discrepancies,
    }


# =====================================================================
# Must-mention / must-not-mention
# =====================================================================

def mention_check(
    response_text: str,
    must_mention: list[str],
    must_not_mention: list[str],
) -> dict:
    rl = response_text.lower()
    missing = [s for s in must_mention if s.lower() not in rl]
    appeared = [s for s in must_not_mention if s.lower() in rl]
    return {
        "missing_required": missing,
        "forbidden_appeared": appeared,
        "pass": not missing and not appeared,
    }


# =====================================================================
# Tool result summary for the judge / transcript
# =====================================================================

def summarize_tool_results(
    tool_messages: list[ToolMessage],
    max_chars: int = 8000,
    wine_context: dict | None = None,
) -> str:
    """Compact summary of tool results for the judge prompt + transcript files.

    After in-loop compaction the ToolMessage blobs are projections (top_results
    with name/price/score/url only). The full merged record set lives in
    `wine_context`. Surface a compact view of both so the judge can verify
    citations against the same data the synthesizer saw.
    """
    chunks = []
    used = 0
    for tm in tool_messages:
        name = getattr(tm, "name", "?")
        raw = to_text(tm.content)
        try:
            parsed = json.loads(raw)
            results_field = parsed.get("results", []) or []
            top_results = parsed.get("top_results", []) or []
            n_results = len(top_results) if parsed.get("compacted") else len(results_field)
            status = parsed.get("status", "?")
            compacted_marker = "  [compacted]" if parsed.get("compacted") else ""
            preview = json.dumps(parsed, indent=2, default=str)[:1500]
        except (json.JSONDecodeError, TypeError):
            n_results = -1
            status = "?"
            compacted_marker = ""
            preview = raw[:1500]
        header = f"### {name}  (status={status}, n_results={n_results}){compacted_marker}"
        block = f"{header}\n{preview}"
        if used + len(block) > max_chars:
            chunks.append("\n[... tool results truncated ...]")
            break
        chunks.append(block)
        used += len(block)

    if isinstance(wine_context, dict) and wine_context:
        keys = list(wine_context.keys())[:12]
        ctx_view = {}
        for k in keys:
            rec = wine_context[k]
            if not isinstance(rec, dict):
                continue
            ctx_view[k] = {
                "display_name": rec.get("display_name"),
                "best_price": rec.get("best_price"),
                "n_prices": len(rec.get("prices") or []),
                "n_critic_reviews": len(rec.get("critic_reviews") or []),
                "is_bc_vqa": rec.get("is_bc_vqa"),
            }
        ctx_blob = json.dumps(ctx_view, indent=2, default=str, ensure_ascii=False)[:2000]
        chunks.append(f"### wine_context (cumulative merged; top {len(ctx_view)} entries)\n{ctx_blob}")

    return "\n\n".join(chunks)
