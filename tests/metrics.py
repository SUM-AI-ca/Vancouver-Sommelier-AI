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
    return " | ".join(parts)


def _summarize_inner_tool(tool_name: str, content) -> str:
    """Summarize one inner tool result from a sub-agent's inner_tools array."""
    if isinstance(content, str):
        try:
            parsed = json.loads(content)
        except (json.JSONDecodeError, TypeError):
            return f"#### {tool_name}\n{content[:2000]}"
    elif isinstance(content, dict):
        parsed = content
    else:
        return f"#### {tool_name}\n{str(content)[:2000]}"

    status = parsed.get("status", "?")
    results = parsed.get("results", []) or []

    lines = [f"#### {tool_name} (status={status}, {len(results)} results)"]

    answer = parsed.get("answer")
    if answer:
        lines.append(f"Search answer: {answer[:4000]}")

    rec = parsed.get("recommendation")
    if rec:
        lines.append(f"Recommendation: {rec[:3000]}")

    for r in results[:20]:
        if not isinstance(r, dict):
            continue
        is_web = ("content" in r
                  and not any(k in r for k in ("price", "current_price", "sale_price", "stock_qty")))
        if is_web:
            title = r.get("title", "?")
            url = r.get("url", "")
            snippet = (r.get("content") or "")[:300]
            lines.append(f"  - [{title}]({url}): {snippet}")
        else:
            lines.append(f"  - {_compact_product(r)}")

    return "\n".join(lines)


def summarize_tool_results(
    tool_messages: list[ToolMessage],
    max_chars: int = 30000,
    wine_context: dict | None = None,
) -> str:
    """Summarize tool results for the judge prompt.

    Handles sub-agent responses (with inner_tools) by extracting product-level
    data from each inner tool, ensuring the judge can see the prices, URLs, and
    stock levels that the agent actually used to compose its response.
    """
    chunks = []
    used = 0

    for tm in tool_messages:
        name = getattr(tm, "name", "?")
        raw = to_text(tm.content)

        try:
            parsed = json.loads(raw)
        except (json.JSONDecodeError, TypeError):
            block = f"### {name}\n{raw[:3000]}"
            if used + len(block) > max_chars:
                chunks.append("\n[... tool results truncated ...]")
                break
            chunks.append(block)
            used += len(block)
            continue

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
            block = "\n".join(lines)
        else:
            results = parsed.get("results", []) or []
            lines = [f"### {name} (status={status})"]
            for key in ("answer", "recommendation", "question", "user_reply"):
                val = parsed.get(key)
                if val:
                    lines.append(f"{key}: {val}")
            if results:
                lines.append(f"({len(results)} results)")
                for r in results[:20]:
                    if isinstance(r, dict):
                        lines.append(f"  - {_compact_product(r)}")
            block = "\n".join(lines)

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
        chunks.append(f"### wine_context (top {len(ctx_view)} entries)\n{ctx_blob}")

    return "\n\n".join(chunks)
