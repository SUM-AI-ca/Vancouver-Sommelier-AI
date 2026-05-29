"""LangGraph agent — build_graph() wires the ReAct orchestrator, tools, merge, and synthesis."""

import json
from datetime import datetime, timezone

from langchain_core.messages import AIMessage, HumanMessage, SystemMessage, ToolMessage
from langchain_core.tools import tool
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph import END, StateGraph
from langgraph.prebuilt import ToolNode
from langgraph.types import interrupt

from bcliquor_tool import search_bcliquor
from compaction import compact_tool_results_node
from everythingwine_tool import search_everything_wine
from gismondi_tool import search_gismondi
from marquis_tool import search_marquis
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
    limit: int = 20,
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
    max_results: int = 8,
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
    llm = get_llm(temperature=0.3)
    resp = await llm.ainvoke([
        SystemMessage(content=PAIRING_SYSTEM_PROMPT),
        HumanMessage(content=f"What BC wine pairs best with: {dish}"),
    ])
    # Gemini returns content as a list of typed parts; str() on that emits the
    # Python repr ([{'type': 'text', 'text': '...'}]) which leaks into the UI.
    # _extract_text flattens the list into clean text.
    content = _extract_text(resp.content)
    return json.dumps({"status": "ok", "tool": "reasoning_pair_wine", "recommendation": content})


@tool
async def ask_user_clarification_tool(
    question: str,
    options: list[str] | None = None,
) -> str:
    """Ask the user a clarifying question when the request or available data is genuinely ambiguous.

    Use ONLY when:
    - The user query has multiple plausible interpretations that would yield very different answers
      (e.g. "good wine" with no budget/style/occasion hint).
    - Tool results have several closely-matched wines and the user's preference would break the tie.
    - Essential information is missing (food pairing request with no dish; "the second one" with no
      prior context in wine_context).

    Do NOT use when:
    - A reasonable default answer exists from user_preferences or wine_context.
    - The query is vague but answerable (e.g. "recommend a red" — just pick ~5 BC reds across styles).
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
    ask_user_clarification_tool,
]

MAX_CLARIFICATIONS_PER_TURN = 3

SAFE_TOOLS = [safe_tool(t) for t in TOOLS]


# ── Graph nodes ──────────────────────────────────────────────────

async def orchestrator_node(state: AgentState) -> dict:
    # Once the data-tool round budget is spent, bind NO tools so the model must
    # answer in prose instead of calling more tools. This is the turn's
    # termination guarantee now that there's no separate synthesis node to write
    # a final answer when the loop is force-stopped.
    over_budget = _count_tool_rounds_this_turn(state["messages"]) >= MAX_TOOL_ROUNDS
    llm = get_llm(temperature=0.2)
    if not over_budget:
        llm = llm.bind_tools(TOOLS)

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

    if over_budget:
        system_parts.append(
            "\n\n## Tool budget reached\n"
            "You have used the maximum data-tool rounds this turn. Do NOT request "
            "more data — write the FINAL answer to the user NOW, using wine_context, "
            "the tool results already gathered, and user_preferences."
        )
    elif _count_clarifications_this_turn(state["messages"]) >= MAX_CLARIFICATIONS_PER_TURN:
        system_parts.append(
            "\n\n## Clarification cap reached\n"
            f"You have already asked {MAX_CLARIFICATIONS_PER_TURN} clarifying questions this turn. "
            "Do NOT call ask_user_clarification_tool again. Proceed with the best answer you can "
            "give from the user's replies, wine_context, and user_preferences."
        )

    system_msg = SystemMessage(content="\n".join(system_parts))
    messages = [system_msg] + state["messages"]

    response = await llm.ainvoke(messages)
    return {"messages": [response]}


MAX_TOOL_ROUNDS = 5  # safety net for prompts.py C3 (≤4 rounds expected, +1 buffer)


def _count_tool_rounds_this_turn(messages: list) -> int:
    """Count AIMessage tool-call rounds since the most recent HumanMessage.

    Each AIMessage with .tool_calls counts as one round (the AIMessage may emit
    multiple parallel tool_calls, but it is one orchestrator decision).

    Rounds that ONLY call ask_user_clarification_tool are excluded — clarifications
    are not data-gathering rounds and shouldn't push the orchestrator toward the
    MAX_TOOL_ROUNDS safety stop."""
    rounds = 0
    for msg in reversed(messages):
        if isinstance(msg, HumanMessage):
            break
        if isinstance(msg, AIMessage) and msg.tool_calls:
            names = {tc.get("name") for tc in msg.tool_calls}
            if names == {"ask_user_clarification_tool"}:
                continue
            rounds += 1
    return rounds


def _count_clarifications_this_turn(messages: list) -> int:
    """Count completed clarifications since the most recent HumanMessage.

    A clarification is a ToolMessage produced by ask_user_clarification_tool.
    Used to enforce MAX_CLARIFICATIONS_PER_TURN."""
    count = 0
    for msg in reversed(messages):
        if isinstance(msg, HumanMessage):
            break
        if isinstance(msg, ToolMessage) and getattr(msg, "name", "") == "ask_user_clarification_tool":
            count += 1
    return count


def should_continue(state: AgentState) -> str:
    # Pending tool_calls must be executed; the loop is bounded because once
    # MAX_TOOL_ROUNDS is reached the orchestrator binds no tools (see
    # orchestrator_node) and is forced to answer, so the next pass returns "end".
    last = state["messages"][-1]
    if isinstance(last, AIMessage) and last.tool_calls:
        return "tools"
    return "end"


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


def _extract_text(content) -> str:
    """Flatten Gemini's list-of-parts content into plain text.

    Gemini 3.5 returns response.content as a list of dicts like
    [{"type": "text", "text": "...", "extras": {"signature": "..."}}]
    when thinking/signing is active. Calling str() on that list leaks
    the Python repr into the user-facing response. This helper picks
    out only the text fields, in order.
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


# ── Graph builder ────────────────────────────────────────────────

def build_graph(checkpointer=None):
    builder = StateGraph(AgentState)

    builder.add_node("orchestrator", orchestrator_node)
    builder.add_node("tools", tool_node_with_logging)
    builder.add_node("compact_tool_results", compact_tool_results_node)

    builder.set_entry_point("orchestrator")
    builder.add_conditional_edges("orchestrator", should_continue, {
        "tools": "tools",
        "end": END,
    })
    # Between rounds: tools → compact → orchestrator. Compaction shrinks the
    # ToolMessage payload the next orchestrator round attends over, and populates
    # wine_context incrementally (+ last_recommendations for multi-turn refs).
    # When the orchestrator answers with no tool_calls, its message is the final
    # response shown to the user — there is no separate synthesis pass.
    builder.add_edge("tools", "compact_tool_results")
    builder.add_edge("compact_tool_results", "orchestrator")

    return builder.compile(checkpointer=checkpointer)


def get_graph():
    checkpointer = InMemorySaver()
    return build_graph(checkpointer=checkpointer)
