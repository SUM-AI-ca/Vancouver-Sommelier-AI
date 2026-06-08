"""Helpers for Vancouver Drinks AI quality eval.

Content extraction and tool result summarization used by quality_eval.py
and judge.py. All scoring is done by LLM-as-Judge (judge.py).
"""

from __future__ import annotations

import json
from typing import Any

from langchain_core.messages import AIMessage, ToolMessage


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
    """Walk state['messages'] backwards to find the last AIMessage with no tool_calls."""
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


# =====================================================================
# Tool result summarization for the judge
# =====================================================================
#
# Design goal: the judge must see *exactly everything the agent saw* — nothing cut.
# The agent composes its answer from the full, raw tool results, so any lossy compaction
# here creates an information asymmetry that makes the judge flag correctly-grounded facts
# as hallucinations. We therefore apply NO per-item caps: every result, the full grounding
# answer, every product field, and the full web snippet are passed through verbatim. The
# only limit is a single overall ceiling sized near the judge model's context capacity, and
# it exists purely as a crash-guard so an extreme payload degrades gracefully (fair
# truncation + a `truncated` flag) instead of failing the API call. For this workload it is
# never reached. See HYPERPARAMETERS.md.

# Crash-guard ceiling only — set near the judge model's input capacity (Gemini 3.x Pro is
# ~1M tokens). ~2M chars (~500k tokens) leaves ample headroom and is never hit in practice.
EVIDENCE_BUDGET_CHARS = 2_000_000

_KNOWN_PRODUCT_FIELDS = frozenset({
    "name", "title", "current_price", "price", "sale_price", "regular_price",
    "retail_price", "product_url", "url", "available_units", "stock_qty",
    "inventory_level", "store_count", "store_stock", "on_sale", "consumer_rating",
    "vintage",
})


def _fair_allocate(sizes: list[int], budget: int) -> list[int]:
    """Max-min fair allocation of `budget` across items of the given `sizes`.

    Small blocks are never starved by large ones: each block first gets up to an equal
    share; whatever a small block doesn't use is redistributed to the larger blocks.
    Returns the allowed size for each block (sum <= budget).
    """
    n = len(sizes)
    if n == 0:
        return []
    allowed = [0] * n
    active = set(range(n))
    remaining = budget
    while active:
        share = remaining // len(active)
        if share <= 0:
            break
        progressed = False
        for i in list(active):
            if sizes[i] <= share:
                allowed[i] = sizes[i]
                remaining -= sizes[i]
                active.discard(i)
                progressed = True
        if not progressed:
            # Every remaining block is larger than the equal share — cap each at `share`.
            for i in active:
                allowed[i] = share
            break
    return allowed


def _compact_product(product: dict) -> str:
    """One-line summary of a product from a store tool."""
    name = product.get("name") or product.get("title", "?")
    price = (product.get("current_price") or product.get("price")
             or product.get("sale_price"))
    regular = product.get("regular_price") or product.get("retail_price")
    url = product.get("product_url") or product.get("url", "")
    stock = (product.get("available_units") or product.get("stock_qty")
             or product.get("inventory_level"))
    store_count = product.get("store_count")
    store_stock = product.get("store_stock")
    on_sale = product.get("on_sale")
    consumer_rating = product.get("consumer_rating")
    vintage = product.get("vintage")

    parts = [name]
    if price is not None:
        p = f"${price}"
        if on_sale and regular:
            p += f" (reg ${regular})"
        parts.append(p)
    if vintage:
        parts.append(str(vintage))
    if stock is not None:
        parts.append(f"stock={stock}")
    if store_count:
        parts.append(f"in {store_count} stores")
    if store_stock and isinstance(store_stock, list):
        detail = ", ".join(
            f"{s.get('store', '?')}:{s.get('quantity', '?')}"
            for s in store_stock if isinstance(s, dict)
        )
        if detail:
            parts.append(f"[{detail}]")
    if consumer_rating:
        parts.append(f"rating={consumer_rating}")
    if url:
        parts.append(url)

    # Fallback: surface EVERY other non-empty field verbatim (description, varietal,
    # country, abv, review source, …) so nothing the agent could have cited is invisible.
    extras = []
    for k, v in product.items():
        if k in _KNOWN_PRODUCT_FIELDS or v in (None, "", [], {}):
            continue
        sval = (json.dumps(v, ensure_ascii=False, default=str)
                if isinstance(v, (dict, list)) else str(v))
        extras.append(f"{k}={sval}")
    if extras:
        parts.append("{" + "; ".join(extras) + "}")
    return " | ".join(parts)


def _summarize_inner_tool(tool_name: str, content) -> str:
    """Render one inner tool result from a sub-agent's inner_tools array — verbatim.

    No per-item caps: every result, the full grounding answer/recommendation, and full
    web snippets are passed through so the judge sees exactly what the agent saw.
    """
    if isinstance(content, str):
        try:
            parsed = json.loads(content)
        except (json.JSONDecodeError, TypeError):
            return f"#### {tool_name}\n{content}"
    elif isinstance(content, dict):
        parsed = content
    else:
        return f"#### {tool_name}\n{str(content)}"

    status = parsed.get("status", "?")
    results = parsed.get("results", []) or []

    lines = [f"#### {tool_name} (status={status}, {len(results)} results)"]

    answer = parsed.get("answer")
    if answer:
        lines.append(f"Search answer: {answer}")

    rec = parsed.get("recommendation")
    if rec:
        lines.append(f"Recommendation: {rec}")

    for r in results:
        if not isinstance(r, dict):
            continue
        is_web = ("content" in r
                  and not any(k in r for k in ("price", "current_price", "sale_price", "stock_qty")))
        if is_web:
            title = r.get("title", "?")
            url = r.get("url", "")
            snippet = r.get("content") or ""
            lines.append(f"  - [{title}]({url}): {snippet}")
        else:
            lines.append(f"  - {_compact_product(r)}")

    return "\n".join(lines)


def _build_tool_block(tm: ToolMessage) -> str:
    """Render one ToolMessage into a full (untruncated) markdown evidence block."""
    name = getattr(tm, "name", "?")
    raw = to_text(tm.content)

    try:
        parsed = json.loads(raw)
    except (json.JSONDecodeError, TypeError):
        return f"### {name}\n{raw}"

    status = parsed.get("status", "?")
    inner_tools = parsed.get("inner_tools")

    if isinstance(inner_tools, list):
        lines = [f"### {name} (status={status})"]
        answer = parsed.get("answer", "")
        if answer:
            lines.append(f"**Sub-agent synthesis:**\n{answer}")
        lines.append("")
        for it in inner_tools:
            if isinstance(it, dict):
                lines.append(_summarize_inner_tool(
                    it.get("tool", "?"), it.get("content", ""),
                ))
                lines.append("")
        return "\n".join(lines)

    results = parsed.get("results", []) or []
    lines = [f"### {name} (status={status})"]
    for key in ("answer", "recommendation", "question", "user_reply"):
        val = parsed.get(key)
        if val:
            lines.append(f"{key}: {val}")
    if results:
        lines.append(f"({len(results)} results)")
        for r in results:
            if isinstance(r, dict):
                lines.append(f"  - {_compact_product(r)}")
    return "\n".join(lines)


def summarize_tool_results(
    tool_messages: list[ToolMessage],
    budget_chars: int = EVIDENCE_BUDGET_CHARS,
    wine_context: dict | None = None,
) -> tuple[str, dict]:
    """Render tool results for the judge prompt — complete, with no per-item caps.

    Builds a full evidence block per ToolMessage (every result, full grounding answers,
    full product fields, full web snippets). ``budget_chars`` is only a crash-guard sized
    near the judge model's context capacity; for this workload it is never reached so
    ``meta['truncated']`` is False. If an extreme payload ever exceeds it, max-min fair
    allocation truncates the largest blocks proportionally (never dropping a whole tool)
    and sets ``truncated=True`` so a low score can be told apart from a real failure.
    Returns ``(summary, meta)``.
    """
    blocks: list[str] = [_build_tool_block(tm) for tm in tool_messages]

    if isinstance(wine_context, dict) and wine_context:
        ctx_blob = json.dumps(wine_context, indent=2, default=str, ensure_ascii=False)
        blocks.append(f"### wine_context\n{ctx_blob}")

    total_full = sum(len(b) for b in blocks)
    sizes = [len(b) for b in blocks]
    allowed = _fair_allocate(sizes, budget_chars)

    out_blocks: list[str] = []
    truncated = False
    for block, cap in zip(blocks, allowed):
        if len(block) > cap:
            truncated = True
            out_blocks.append(block[:cap] + "\n[... this tool's evidence truncated ...]")
        else:
            out_blocks.append(block)

    meta = {
        "truncated": truncated,
        "n_tool_messages": len(tool_messages),
        "total_evidence_chars": total_full,
        "budget_chars": budget_chars,
    }
    return "\n\n".join(out_blocks), meta
