"""LangGraph agent — build_graph() wires the ReAct orchestrator, tools, merge, and synthesis."""

import json
from datetime import datetime, timezone

from langchain_core.messages import AIMessage, HumanMessage, SystemMessage, ToolMessage
from langchain_core.tools import tool
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph import END, StateGraph
from langgraph.prebuilt import ToolNode
from langgraph.types import interrupt

from models import get_llm
from prompts import ORCHESTRATOR_SYSTEM_PROMPT, PAIRING_SYSTEM_PROMPT
from safety import tool_error_to_json
from state import AgentState
from tools.bcliquor_tool import search_bcliquor
from tools.everythingwine_tool import search_everything_wine
from tools.gismondi_tool import search_gismondi
from tools.legacy_tool import search_legacy as search_legacy_liquor_store
from tools.marquis_tool import search_marquis
from tools.okanagan_cellars_tool import search_okanagan_cellars
from tools.suttonplace_tool import search_suttonplace
from tools.robert_parker_tool import search_robert_parker
from tools.tavily_tool import search_tavily
from tools.winealign_tool import search_winealign
from vision import (
    extract_image_urls,
    extract_text,
    extract_vision,
    format_extraction,
    latest_human_message,
    message_has_image,
)


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
    Slow (3-10s). Always attribute by critic name.
    """
    results = await search_winealign(query, max_pages=max_pages, include_reviews=include_reviews)
    return json.dumps({"status": "ok", "tool": "search_winealign", "results": [r.model_dump() for r in results]})


@tool
async def search_everything_wine_tool(query: str) -> str:
    """Search Everything Wine for delivery and per-store pickup availability.
    Returns warehouse-delivery status plus exact per-store stock quantities for the
    Lower Mainland stores (Vancouver, North Vancouver, South Surrey, Langley).
    Use when the user wants home delivery, in-store pickup, or which specific store has a wine.
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
async def search_suttonplace_tool(query: str) -> str:
    """Search Sutton Place Wine Merchant (Vancouver, Yaletown) for wines with stock, vintage, varietal, and staff picks.
    Use when checking Yaletown wine shop availability or vintage-specific inventory.
    """
    results = await search_suttonplace(query)
    return json.dumps({"status": "ok", "tool": "search_suttonplace", "results": [r.model_dump() for r in results]})


@tool
async def search_marquis_tool(query: str, limit: int = 20, skip: int = 0) -> str:
    """Search Marquis Wine Cellars (Vancouver, curated boutique shop) for wines with hierarchical categories and MSRP.
    Use for curated/boutique selections or MSRP vs sale price comparison.
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
    """Search Legacy Liquor Store (Vancouver, premium selection) for wines with price filtering and staff picks.
    Use for premium/curated selections, sale items, or staff-recommended wines.
    Supports price_min/price_max for budget queries and staff_pick=True for expert recommendations.
    """
    results, total = await search_legacy_liquor_store(
        query, limit=limit, price_min=price_min, price_max=price_max,
        on_sale=on_sale, staff_pick=staff_pick,
    )
    return json.dumps({"status": "ok", "tool": "search_legacy_liquor_store", "total": total, "results": [r.model_dump() for r in results]})


@tool
async def search_gismondi_tool(
    query: str,
    limit: int = 25,
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
    Authenticated.
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
    Never as a first-line tool for inventory/pricing.
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
      prior context in conversation history).

    Do NOT use when:
    - A reasonable default answer exists from conversation history.
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
    search_suttonplace_tool,
    search_marquis_tool,
    search_legacy_liquor_store_tool,
    search_gismondi_tool,
    search_robert_parker_tool,
    search_tavily_tool,
    reasoning_pair_wine_tool,
    update_preferences_tool,
    ask_user_clarification_tool,
]

MAX_CLARIFICATIONS_PER_TURN = 3


# ── Graph nodes ──────────────────────────────────────────────────

def _filter_previous_turns(messages: list) -> list:
    """Keep only Human + final AI answer from previous turns.
    Current turn (after last HumanMessage) is kept in full."""
    last_human_idx = -1
    for i in range(len(messages) - 1, -1, -1):
        if isinstance(messages[i], HumanMessage):
            last_human_idx = i
            break

    if last_human_idx <= 0:
        return messages

    filtered = []
    for msg in messages[:last_human_idx]:
        if isinstance(msg, HumanMessage):
            filtered.append(msg)
        elif isinstance(msg, AIMessage) and not msg.tool_calls:
            filtered.append(msg)

    filtered.extend(messages[last_human_idx:])
    return filtered


async def orchestrator_node(state: AgentState) -> dict:
    over_budget = _count_tool_rounds_this_turn(state["messages"]) >= MAX_TOOL_ROUNDS
    llm = get_llm(temperature=0.2)
    if not over_budget:
        llm = llm.bind_tools(TOOLS)

    system_parts = [ORCHESTRATOR_SYSTEM_PROMPT]

    if over_budget:
        system_parts.append(
            "\n\n## Tool budget reached\n"
            "You have used the maximum data-tool rounds this turn. Do NOT request "
            "more data — write the FINAL answer to the user NOW using the tool "
            "results already gathered."
        )
    elif _count_clarifications_this_turn(state["messages"]) >= MAX_CLARIFICATIONS_PER_TURN:
        system_parts.append(
            "\n\n## Clarification cap reached\n"
            f"You have already asked {MAX_CLARIFICATIONS_PER_TURN} clarifying questions this turn. "
            "Do NOT call ask_user_clarification_tool again. Proceed with the best answer you can."
        )

    system_msg = SystemMessage(content="\n".join(system_parts))
    messages = [system_msg] + _filter_previous_turns(state["messages"])

    response = await llm.ainvoke(messages)
    return {"messages": [response]}


MAX_TOOL_ROUNDS = 6  # safety net for prompts.py C3 (≤5 rounds expected, +1 buffer)


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
    # handle_tool_errors routes every tool exception through tool_error_to_json so a
    # single failing tool returns a status="error" result instead of crashing the
    # turn — the orchestrator keeps the other tools' results and answers from them.
    # (GraphInterrupt from ask_user_clarification_tool is re-raised by ToolNode
    # before this handler, so clarifications still work.)
    tool_node = ToolNode(TOOLS, handle_tool_errors=tool_error_to_json)
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


# ── Vision node ──────────────────────────────────────────────────

async def vision_node(state: AgentState) -> dict:
    """Multimodal pass that runs before the orchestrator when the user's latest
    message carries an image. It transcribes the wine label / wine list into a
    structured record, then folds that read into the user turn as text.

    The replacement HumanMessage reuses the original message id, so add_messages
    swaps it in place — stripping the (token-heavy) image from context for this
    turn and every future turn. From here the orchestrator runs text-only."""
    human = latest_human_message(state["messages"])
    if human is None or not message_has_image(human):
        return {}  # defensive: entry_router shouldn't route here without an image

    image_urls = extract_image_urls(human)
    user_text = extract_text(human)

    extraction = await extract_vision(image_urls, user_text)
    summary = format_extraction(extraction)

    base_text = user_text or "(The user attached an image with no text.)"
    replacement = HumanMessage(
        id=human.id,
        content=f"{base_text}\n\n[Image analysis — vision]\n{summary}",
    )
    return {
        "messages": [replacement],
        "vision_extractions": [extraction.model_dump()],
    }


def entry_router(state: AgentState) -> str:
    """Route the turn to vision_node first when an image is attached, else
    straight to the orchestrator."""
    human = latest_human_message(state["messages"])
    return "vision" if message_has_image(human) else "orchestrator"


# ── Graph builder ────────────────────────────────────────────────

def build_graph(checkpointer=None):
    builder = StateGraph(AgentState)

    builder.add_node("vision", vision_node)
    builder.add_node("orchestrator", orchestrator_node)
    builder.add_node("tools", tool_node_with_logging)

    builder.set_conditional_entry_point(entry_router, {
        "vision": "vision",
        "orchestrator": "orchestrator",
    })
    builder.add_edge("vision", "orchestrator")
    builder.add_conditional_edges("orchestrator", should_continue, {
        "tools": "tools",
        "end": END,
    })
    builder.add_edge("tools", "orchestrator")

    return builder.compile(checkpointer=checkpointer)


def get_graph():
    checkpointer = InMemorySaver()
    return build_graph(checkpointer=checkpointer)
