"""Shared LangChain @tool wrappers for the AI Drinks Concierge.

Extracted from agent.py so both the legacy single orchestrator (agent.py) and the
multi-agent specialists (agents/) can import the same tools without a circular import.

Grouped lists declare specialist ownership:
  - SOURCING_TOOLS   — store search + Google Maps locator
  - SOMMELIER_TOOLS  — pairing reasoning + Google Search grounding
  - SUPERVISOR_DIRECT_TOOLS — clarification + preferences (the Supervisor binds these)
  - ALL_TOOLS — the flat set the legacy orchestrator binds (kept working until P0-3 swap)
"""
from __future__ import annotations

import json

from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.tools import tool
from langgraph.types import interrupt

from models import get_llm
from prompts import PAIRING_SYSTEM_PROMPT
from tools.bcliquor_tool import search_bcliquor
from tools.everythingwine_tool import search_everything_wine
from tools.google_maps_tool import search_google_maps
from tools.google_search_tool import search_web_grounded
from tools.legacy_tool import search_legacy as search_legacy_liquor_store
from tools.marquis_tool import search_marquis
from tools.okanagan_cellars_tool import search_okanagan_cellars
from tools.suttonplace_tool import search_suttonplace


def _extract_text(content) -> str:
    """Flatten Gemini's list-of-parts content into plain text.

    Gemini returns response.content as a list of dicts like
    [{"type": "text", "text": "..."}] when thinking/signing is active; str() on that
    leaks the Python repr into the UI. This picks out the text fields in order.
    """
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        parts: list[str] = []
        for item in content:
            if isinstance(item, dict):
                text = item.get("text")
                if isinstance(text, str):
                    parts.append(text)
            elif isinstance(item, str):
                parts.append(item)
        return "".join(parts)
    return str(content)


# ── Store search tools ───────────────────────────────────────────

@tool
async def search_bcliquor_tool(query: str, max_pages: int = 2, category: str | None = None) -> str:
    """Search BC Liquor Stores (government retailer, province-wide; serves Vancouver).
    Largest selection and ALL categories — wine, beer, spirits, cider. Also returns
    consumer ratings and BC VQA status.
    """
    results = await search_bcliquor(query, max_pages=max_pages, category=category)
    return json.dumps({"status": "ok", "tool": "search_bcliquor", "results": [r.model_dump() for r in results]})


@tool
async def search_everything_wine_tool(query: str) -> str:
    """Search Everything Wine for prices and availability across Lower Mainland stores
    (Vancouver, North Vancouver, South Surrey, Langley).
    Also shows home-delivery status and exact per-store stock quantities.
    """
    results = await search_everything_wine(query)
    return json.dumps({"status": "ok", "tool": "search_everything_wine", "results": [r.model_dump() for r in results]})


@tool
async def search_okanagan_cellars_tool(query: str) -> str:
    """Search Okanagan Cellars (Vancouver, 2 locations) for prices and availability.
    Often competitive pricing on BC wines. Also shows exact stock quantities and unit sizes.
    """
    results = await search_okanagan_cellars(query)
    return json.dumps({"status": "ok", "tool": "search_okanagan_cellars", "results": [r.model_dump() for r in results]})


@tool
async def search_suttonplace_tool(query: str) -> str:
    """Search Sutton Place Wine Merchant (Vancouver, Yaletown) for prices and availability.
    Also shows vintage, varietal, country, alcohol %, and staff picks.
    """
    results = await search_suttonplace(query)
    return json.dumps({"status": "ok", "tool": "search_suttonplace", "results": [r.model_dump() for r in results]})


@tool
async def search_marquis_tool(query: str, limit: int = 20, skip: int = 0) -> str:
    """Search Marquis Wine Cellars (Vancouver, curated boutique) for prices and availability.
    Boutique selection with hierarchical categories and MSRP pricing.
    """
    results, total = await search_marquis(query, limit=limit, skip=skip)
    return json.dumps({"status": "ok", "tool": "search_marquis", "total": total, "results": [r.model_dump() for r in results]})


@tool
async def search_legacy_liquor_store_tool(
    query: str,
    limit: int = 20,
    price_min: float | None = None,
    price_max: float | None = None,
    on_sale: bool | None = None,
    staff_pick: bool | None = None,
) -> str:
    """Search Legacy Liquor Store (Vancouver, full-line liquor: wine, beer, spirits).
    Supports price_min/price_max filtering, on_sale for deals, and staff_pick for expert recommendations.
    """
    results, total = await search_legacy_liquor_store(
        query, limit=limit, price_min=price_min, price_max=price_max,
        on_sale=on_sale, staff_pick=staff_pick,
    )
    return json.dumps({"status": "ok", "tool": "search_legacy_liquor_store", "total": total, "results": [r.model_dump() for r in results]})


@tool
async def search_google_maps_tool(query: str) -> str:
    """Find liquor / wine stores near a place in Vancouver — address, opening
    hours, rating, and a Google Maps link. Use for "where can I buy near X", "store near
    me", or store-hours questions. Example query: "BC Liquor Store near Yaletown, Vancouver"
    or "wine shop near Kitsilano, Vancouver". Not for product prices — use the store tools.
    """
    results = await search_google_maps(query)
    return json.dumps({"status": "ok", "tool": "search_google_maps", "results": [r.model_dump() for r in results]})


# ── Knowledge / reasoning tools ──────────────────────────────────

@tool
async def search_web_grounded_tool(query: str) -> str:
    """Web search with Google Search grounding — cited, up-to-date facts.
    Use for: drinks education, regions/producers/breweries/distilleries, reviews and
    scores (ATTRIBUTE to the source and summarize — never reproduce full review text;
    always include source links), and disambiguation when store tools come back empty.
    NOT a first-line tool for inventory/pricing.
    """
    results, answer = await search_web_grounded(query)
    return json.dumps({
        "status": "ok",
        "tool": "search_web_grounded",
        "answer": answer,
        "results": [r.model_dump() for r in results],
    })


@tool
async def reasoning_pair_wine_tool(dish: str) -> str:
    """Sommelier sub-LLM for non-trivial food-and-drink pairings across all categories
    (wine, beer, spirits, cider, sake, cocktails). Use for non-Western cuisines or complex
    dishes. Do NOT use for common pairings (steak + Cabernet, salmon + Pinot) — answer
    those from built-in knowledge.
    """
    llm = get_llm(temperature=0.3)
    resp = await llm.ainvoke([
        SystemMessage(content=PAIRING_SYSTEM_PROMPT),
        HumanMessage(content=f"What drink pairs best with: {dish}"),
    ])
    content = _extract_text(resp.content)
    return json.dumps({"status": "ok", "tool": "reasoning_pair_wine", "recommendation": content})


# ── Cross-cutting tools (Supervisor-owned) ───────────────────────

@tool
async def ask_user_clarification_tool(
    question: str,
    options: list[str] | None = None,
) -> str:
    """Ask the user a clarifying question when the request or available data is genuinely ambiguous.

    Use ONLY when:
    - The user query has multiple plausible interpretations that would yield very different answers
      (e.g. "good wine" with no budget/style/occasion hint).
    - Tool results have several closely-matched products and the user's preference would break the tie.
    - Essential information is missing (food pairing request with no dish; "the second one" with no
      prior context in conversation history).

    Do NOT use when:
    - A reasonable default answer exists from conversation history.
    - The query is vague but answerable (e.g. "recommend a red" — just pick ~5 across styles).
    - You are stalling instead of making a judgment call.

    Args:
        question: The clarifying question, written in the SAME language as the user. One sentence.
        options: Up to 7 short option strings the user can click. Leave empty for free-form replies.

    Returns the user's clarification reply as a string. The user may type free text instead of
    choosing one of the options.
    """
    user_reply = interrupt({
        "type": "clarification_request",
        "question": question,
        "options": options or [],
    })
    return json.dumps({
        "status": "ok",
        "tool": "ask_user_clarification",
        "question": question,
        "user_reply": str(user_reply),
    })


@tool
async def update_preferences_tool(
    budget_max: float | None = None,
    add_varietals: list[str] | None = None,
    sweetness: str | None = None,
    style: str | None = None,
) -> str:
    """Record a stable user preference for use in future turns.
    Call when the user expresses a preference that should persist
    (e.g., "I always want to stay under $50", "I prefer dry whites").
    Do NOT call for one-off filters within a single query.
    """
    return json.dumps({
        "status": "ok",
        "tool": "update_preferences",
        "budget_max": budget_max,
        "add_varietals": add_varietals,
        "sweetness": sweetness,
        "style": style,
    })


# ── Tool groupings ───────────────────────────────────────────────

SOURCING_TOOLS = [
    search_bcliquor_tool,
    search_everything_wine_tool,
    search_okanagan_cellars_tool,
    search_suttonplace_tool,
    search_marquis_tool,
    search_legacy_liquor_store_tool,
    search_google_maps_tool,
]

SOMMELIER_TOOLS = [
    reasoning_pair_wine_tool,
    search_web_grounded_tool,
]

SUPERVISOR_DIRECT_TOOLS = [
    ask_user_clarification_tool,
    update_preferences_tool,
]

# Flat set bound by the legacy single orchestrator (agent.py) until the Supervisor lands.
ALL_TOOLS = SOURCING_TOOLS + SOMMELIER_TOOLS + SUPERVISOR_DIRECT_TOOLS
