"""LangGraph agent — build_graph() wires the ReAct orchestrator, tools, merge, and synthesis."""

import json
from datetime import datetime, timezone

from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_core.tools import tool
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph import END, StateGraph
from langgraph.prebuilt import ToolNode

from bcliquor_tool import search_bcliquor
from everythingwine_tool import search_everything_wine
from gismondi_tool import search_gismondi
from marquis_tool import search_marquis
from merge import merge_tool_results
from models import get_llm
from okanagan_cellars_tool import search_okanagan_cellars
from prompts import ORCHESTRATOR_SYSTEM_PROMPT, PAIRING_SYSTEM_PROMPT
from robert_parker_tool import search_robert_parker
from safety import safe_tool
from state import AgentState, UserPreferences
from tavily_tool import search_tavily
from winealign_tool import search_winealign


# ── LangChain @tool wrappers ─────────────────────────────────────

@tool
async def search_bcliquor_tool(query: str, max_pages: int = 2, category: str | None = None) -> str:
    """Search BC Liquor Stores for prices, availability, consumer ratings, and BC VQA status.
    Use when the user asks about price, availability, "where can I buy", consumer sentiment, or BC VQA wines.
    """
    results = await search_bcliquor(query, max_pages=max_pages, category=category)
    return json.dumps({"status": "ok", "tool": "search_bcliquor", "results": [r.model_dump() for r in results]})


@tool
async def search_winealign_tool(query: str, max_pages: int = 3, include_reviews: bool = True) -> str:
    """Search WineAlign for multi-critic professional reviews with scores, tasting notes, value ratings, and drink windows.
    Use when the user asks "what do critics think", "is this worth buying", or wants aging guidance.
    Slow (3-10s). Do not call more than twice per turn. Always attribute by critic name.
    """
    results = await search_winealign(query, max_pages=max_pages, include_reviews=include_reviews)
    return json.dumps({"status": "ok", "tool": "search_winealign", "results": [r.model_dump() for r in results]})


@tool
async def search_everything_wine_tool(query: str) -> str:
    """Search Everything Wine (Vancouver) for delivery and pickup availability.
    Returns 3-level stock status: warehouse delivery, in-store pickup, check other stores.
    Use when the user wants Vancouver-area pickup or home delivery.
    """
    results = await search_everything_wine(query)
    return json.dumps({"status": "ok", "tool": "search_everything_wine", "results": [r.model_dump() for r in results]})


@tool
async def search_okanagan_cellars_tool(query: str) -> str:
    """Search Okanagan Cellars (Vancouver, 2 locations) for exact stock quantities and unit sizes.
    Use when the user wants precise bottle counts or non-standard sizes (750ml, 1.5L).
    """
    results = await search_okanagan_cellars(query)
    return json.dumps({"status": "ok", "tool": "search_okanagan_cellars", "results": [r.model_dump() for r in results]})


@tool
async def search_marquis_tool(query: str, limit: int = 30, skip: int = 0) -> str:
    """Search Marquis Wine Cellars (Vancouver, curated boutique shop) for wines with hierarchical categories and MSRP.
    Use for curated/boutique selections or MSRP vs sale price comparison.
    """
    results, total = await search_marquis(query, limit=limit, skip=skip)
    return json.dumps({"status": "ok", "tool": "search_marquis", "total": total, "results": [r.model_dump() for r in results]})


@tool
async def search_gismondi_tool(
    query: str,
    limit: int = 10,
    score_min: int = 0,
    price_max: float | None = None,
    bc_only: bool = True,
) -> str:
    """Search Anthony Gismondi's wine reviews from local database. Deep tasting notes for Canadian wines.
    Sub-100ms latency. Use for Gismondi's specific opinion or BC wine discovery queries.
    Supports score_min and price_max filters. bc_only=True biases to BC wines.
    """
    results = await search_gismondi(query, limit=limit, score_min=score_min, price_max=price_max, bc_only=bc_only)
    return json.dumps({"status": "ok", "tool": "search_gismondi", "results": [r.model_dump() for r in results]})


@tool
async def search_robert_parker_tool(
    query: str,
    rating_min: int = 50,
    hits_per_page: int = 10,
    country: str | None = None,
    region: str | None = None,
    color: str | None = None,
    variety: str | None = None,
) -> str:
    """Search Robert Parker Wine Advocate for world-class 100-point ratings, tasting notes, and drink windows.
    Use when the user asks for Robert Parker/RP scores, internationally recognized ratings, or global comparisons.
    Authenticated. Do not call more than once per turn.
    """
    results = await search_robert_parker(
        query, rating_min=rating_min, hits_per_page=hits_per_page,
        country=country, region=region, color=color, variety=variety,
    )
    return json.dumps({"status": "ok", "tool": "search_robert_parker", "results": [r.model_dump() for r in results]})


@tool
async def search_tavily_tool(
    query: str,
    max_results: int = 5,
    search_depth: str = "basic",
    include_answer: bool = True,
) -> str:
    """Web search fallback with AI-generated answer summary.
    Use ONLY for: (1) non-Western cuisine pairings, (2) educational/regional questions,
    or (3) disambiguation when all store tools return empty.
    Paid per request. Call at most once per turn. Never as a first-line tool for inventory/pricing.
    """
    results, answer = await search_tavily(query, max_results=max_results, search_depth=search_depth, include_answer=include_answer)
    return json.dumps({"status": "ok", "tool": "search_tavily", "answer": answer, "results": [r.model_dump() for r in results]})


@tool
async def reasoning_pair_wine_tool(dish: str) -> str:
    """Sommelier sub-LLM for non-trivial food-wine pairings.
    Use for non-Western cuisines or complex dishes. Do NOT use for common pairings
    (steak + Cabernet, salmon + Pinot) — answer those from built-in knowledge.
    """
    llm = get_llm(temperature=0.5)
    resp = await llm.ainvoke([
        SystemMessage(content=PAIRING_SYSTEM_PROMPT),
        HumanMessage(content=f"What BC wine pairs best with: {dish}"),
    ])
    content = resp.content if isinstance(resp.content, str) else str(resp.content)
    return json.dumps({"status": "ok", "tool": "reasoning_pair_wine", "recommendation": content})


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


# ── Tool list ────────────────────────────────────────────────────

TOOLS = [
    search_bcliquor_tool,
    search_winealign_tool,
    search_everything_wine_tool,
    search_okanagan_cellars_tool,
    search_marquis_tool,
    search_gismondi_tool,
    search_robert_parker_tool,
    search_tavily_tool,
    reasoning_pair_wine_tool,
    update_preferences_tool,
]

SAFE_TOOLS = [safe_tool(t) for t in TOOLS]


# ── Graph nodes ──────────────────────────────────────────────────

async def orchestrator_node(state: AgentState) -> dict:
    llm = get_llm().bind_tools(TOOLS)

    system_parts = [ORCHESTRATOR_SYSTEM_PROMPT]

    prefs = state.get("user_preferences")
    if prefs:
        system_parts.append(f"\n\n## Active User Preferences\n{json.dumps(prefs)}")

    wine_ctx = state.get("wine_context")
    if wine_ctx:
        keys = list(wine_ctx.keys())[:20]
        summary = {k: {"name": wine_ctx[k]["display_name"], "best_price": wine_ctx[k].get("best_price")} for k in keys}
        system_parts.append(f"\n\n## Wine Context (cached)\n{json.dumps(summary, default=str)}")

    last_recs = state.get("last_recommendations")
    if last_recs:
        system_parts.append(f"\n\n## Last Recommendations (ordered)\n{json.dumps(last_recs)}")

    system_msg = SystemMessage(content="\n".join(system_parts))
    messages = [system_msg] + state["messages"]

    response = await llm.ainvoke(messages)
    return {"messages": [response]}


def should_continue(state: AgentState) -> str:
    last = state["messages"][-1]
    if isinstance(last, AIMessage) and last.tool_calls:
        return "tools"
    return "merge_results"


async def tool_node_with_logging(state: AgentState) -> dict:
    tool_node = ToolNode(TOOLS)
    result = await tool_node.ainvoke(state)

    log_entries = state.get("tool_call_log", [])
    last_msg = state["messages"][-1]
    if isinstance(last_msg, AIMessage) and last_msg.tool_calls:
        for tc in last_msg.tool_calls:
            log_entries.append({
                "tool": tc["name"],
                "query": str(tc.get("args", {})),
                "ts": datetime.now(timezone.utc).isoformat(),
            })

    new_state = {**result, "tool_call_log": log_entries[-50:]}
    return new_state


def merge_results_node(state: AgentState) -> dict:
    merged = merge_tool_results(state["messages"])
    existing = state.get("wine_context", {})
    existing.update(merged)

    last_recs = list(merged.keys())[:10]

    prefs = state.get("user_preferences", {})
    for msg in state["messages"]:
        if isinstance(msg, AIMessage):
            continue
        content = msg.content if hasattr(msg, "content") and isinstance(msg.content, str) else ""
        if not content:
            continue
        try:
            data = json.loads(content)
            if isinstance(data, dict) and data.get("tool") == "update_preferences":
                if data.get("budget_max"):
                    prefs["budget_max"] = data["budget_max"]
                if data.get("add_varietals"):
                    existing_v = prefs.get("preferred_varietals", [])
                    prefs["preferred_varietals"] = list(set(existing_v + data["add_varietals"]))
                if data.get("sweetness"):
                    prefs["sweetness"] = data["sweetness"]
                if data.get("style"):
                    prefs["style"] = data["style"]
        except (json.JSONDecodeError, TypeError):
            pass

    return {
        "wine_context": existing,
        "last_recommendations": last_recs,
        "user_preferences": prefs if prefs else state.get("user_preferences"),
    }


async def format_response_node(state: AgentState) -> dict:
    return {}


# ── Graph builder ────────────────────────────────────────────────

def build_graph(checkpointer=None):
    builder = StateGraph(AgentState)

    builder.add_node("orchestrator", orchestrator_node)
    builder.add_node("tools", tool_node_with_logging)
    builder.add_node("merge_results", merge_results_node)
    builder.add_node("format_response", format_response_node)

    builder.set_entry_point("orchestrator")
    builder.add_conditional_edges("orchestrator", should_continue, {
        "tools": "tools",
        "merge_results": "merge_results",
    })
    builder.add_edge("tools", "orchestrator")
    builder.add_edge("merge_results", "format_response")
    builder.add_edge("format_response", END)

    return builder.compile(checkpointer=checkpointer)


def get_graph():
    checkpointer = InMemorySaver()
    return build_graph(checkpointer=checkpointer)
