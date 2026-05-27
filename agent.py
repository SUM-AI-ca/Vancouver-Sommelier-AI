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
from merge import merge_tool_results
from models import get_llm
from okanagan_cellars_tool import search_okanagan_cellars
from prompts import ORCHESTRATOR_SYSTEM_PROMPT, PAIRING_SYSTEM_PROMPT, SYNTHESIS_SYSTEM_PROMPT
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
    - The query is vague but answerable (e.g. "recommend a red" — just pick 2-3 BC reds across styles).
    - You are stalling instead of making a judgment call.

    Args:
        question: The clarifying question, written in the SAME language as the user. One sentence.
        options: 2-4 short option strings the user can click. Leave empty for free-form replies.

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
    llm = get_llm(temperature=0.2).bind_tools(TOOLS)

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

    if _count_clarifications_this_turn(state["messages"]) >= MAX_CLARIFICATIONS_PER_TURN:
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


MAX_TOOL_ROUNDS = 3  # safety net for prompts.py Rule 12 (≤2 rounds expected, +1 buffer)


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
    last = state["messages"][-1]
    if isinstance(last, AIMessage) and last.tool_calls:
        # Safety net: if the orchestrator has already issued MAX_TOOL_ROUNDS rounds
        # of tool calls this turn, stop and force synthesis with whatever data we have.
        # Without this, malformed queries can drive the agent to recursion_limit (e.g.
        # SOM-003 hit 30 rounds in run 20260525-225130). The user gets a partial answer
        # instead of an error.
        if _count_tool_rounds_this_turn(state["messages"]) >= MAX_TOOL_ROUNDS:
            return "merge_results"
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

    # wine_context is now incrementally populated by compact_tool_results_node
    # during the ReAct loop; `merged` here is empty for compacted ToolMessages
    # (results=[]). Derive last_recommendations from wine_context's tail so
    # reference resolution still has the freshest entries.
    last_recs = list((existing or {}).keys())[-10:]

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


def _compact_wine_record(rec: dict) -> dict:
    """Strip a MergedWineRecord down to fields the synthesizer actually uses.

    Splits prices into two lists:
    - retail_prices: real store inventory rows that go in the Where-to-buy table
    - reference_prices: critic-quoted prices (Gismondi review snapshots) — these
      go in a separate "Reference price" note, NEVER in the Where-to-buy table
    """
    all_prices = rec.get("prices") or []
    retail = [p for p in all_prices if not p.get("is_reference")][:10]
    refs = [p for p in all_prices if p.get("is_reference")][:3]
    critics = rec.get("critic_reviews") or []
    return {
        "display_name": rec.get("display_name"),
        "producer": rec.get("producer"),
        "vintage": rec.get("vintage"),
        "grape": rec.get("grape"),
        "is_bc_vqa": rec.get("is_bc_vqa"),
        "consumer_rating": rec.get("consumer_rating"),
        "avg_critic_score": rec.get("avg_critic_score"),
        "best_price": rec.get("best_price"),
        "retail_prices": retail,
        "reference_prices": refs,
        "critic_reviews": critics[:6],
        "tasting_notes_consolidated": rec.get("tasting_notes_consolidated"),
    }


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


def _collect_aux_tool_outputs(messages: list) -> list[dict]:
    """Pick up reasoning_pair_wine and tavily outputs — tools whose value isn't captured
    in the merged wine_context but is needed by the synthesizer for pairing logic and
    educational/disambiguation context.
    """
    aux: list[dict] = []
    for msg in messages:
        if not isinstance(msg, ToolMessage):
            continue
        content = msg.content if isinstance(msg.content, str) else ""
        if not content:
            continue
        try:
            data = json.loads(content)
        except (json.JSONDecodeError, TypeError):
            continue
        if not isinstance(data, dict):
            continue
        tool = data.get("tool", "")
        if tool == "reasoning_pair_wine":
            rec = data.get("recommendation", "")
            if rec:
                aux.append({"tool": "reasoning_pair_wine", "recommendation": rec[:2000]})
        elif tool == "search_tavily":
            ans = data.get("answer", "")
            if ans:
                aux.append({"tool": "search_tavily", "answer": ans[:1500]})
    return aux[-4:]


async def format_response_node(state: AgentState) -> dict:
    """Synthesis pass — reformat the orchestrator's wine selection into the markdown skeleton.

    The orchestrator's draft provides the *intent signal* (which wines to feature,
    which to omit as fuzzy-search noise). The wine_context blob provides the *facts*
    (prices, stores, URLs, critic scores). Synthesis combines them: it follows the
    orchestrator's recommendations but pulls all numbers and links from wine_context.

    Replaces the orchestrator's last AIMessage in-place (same id) so streaming and
    downstream consumers see only the synthesized response. Off-topic turns (no tool
    results, empty wine_context AND no aux outputs) are passed through untouched
    to avoid latency cost on queries that don't need the skeleton.
    """
    msgs = state["messages"]
    last_ai: AIMessage | None = None
    last_ai_any: AIMessage | None = None
    user_query = ""
    # Walk backwards within this turn only — stop at the most recent HumanMessage
    # so multi-turn conversations don't bleed an earlier turn's draft into synthesis.
    for msg in reversed(msgs):
        if isinstance(msg, HumanMessage):
            if not user_query:
                user_query = msg.content if isinstance(msg.content, str) else str(msg.content)
            break
        if isinstance(msg, AIMessage):
            if last_ai_any is None:
                last_ai_any = msg
            if last_ai is None and not msg.tool_calls:
                last_ai = msg

    # If the orchestrator was short-circuited by MAX_TOOL_ROUNDS, the most recent
    # AIMessage still has tool_calls and no clean draft. Use it anyway (it has the
    # orchestrator's intent in any text it managed to produce) and let synthesis
    # write the final response from data.
    if last_ai is None:
        last_ai = last_ai_any
    if last_ai is None:
        return {}

    wine_ctx = state.get("wine_context") or {}
    aux_outputs = _collect_aux_tool_outputs(msgs)

    if not wine_ctx and not aux_outputs:
        return {}

    last_recs = state.get("last_recommendations") or []
    ordered_keys: list[str] = []
    for k in last_recs:
        if k in wine_ctx and k not in ordered_keys:
            ordered_keys.append(k)
    for k in wine_ctx.keys():
        if k not in ordered_keys:
            ordered_keys.append(k)
        if len(ordered_keys) >= 8:
            break
    ordered_keys = ordered_keys[:8]

    context_blob = {k: _compact_wine_record(wine_ctx[k]) for k in ordered_keys}

    orchestrator_draft = _extract_text(last_ai.content)

    synthesis_input = (
        f"## User query\n{user_query}\n\n"
        f"## Orchestrator's wine selection (FOLLOW this — it knows which wines actually "
        f"answer the user's question vs. which are fuzzy-search noise)\n"
        f"{orchestrator_draft}\n\n"
        f"## Wine data (the FACTS — pull prices, stores, URLs, scores from here. "
        f"Do NOT introduce wines that are not in the orchestrator's selection above.)\n"
        f"{json.dumps(context_blob, default=str, ensure_ascii=False)}\n\n"
        f"## Supplementary tool outputs (pairing logic, web answers — use as context, "
        f"do NOT copy their formatting)\n"
        f"{json.dumps(aux_outputs, default=str, ensure_ascii=False)}\n"
    )

    llm = get_llm(temperature=0.0)
    response = await llm.ainvoke([
        SystemMessage(content=SYNTHESIS_SYSTEM_PROMPT),
        HumanMessage(content=synthesis_input),
    ])

    content = _extract_text(response.content)
    final_msg = AIMessage(content=content, id=last_ai.id)
    return {"messages": [final_msg]}


# ── Graph builder ────────────────────────────────────────────────

def build_graph(checkpointer=None):
    builder = StateGraph(AgentState)

    builder.add_node("orchestrator", orchestrator_node)
    builder.add_node("tools", tool_node_with_logging)
    builder.add_node("compact_tool_results", compact_tool_results_node)
    builder.add_node("merge_results", merge_results_node)
    builder.add_node("format_response", format_response_node)

    builder.set_entry_point("orchestrator")
    builder.add_conditional_edges("orchestrator", should_continue, {
        "tools": "tools",
        "merge_results": "merge_results",
    })
    # Between rounds: tools → compact → orchestrator. Compaction shrinks the
    # ToolMessage payload the next orchestrator round attends over, while
    # populating wine_context incrementally so synthesis has facts ready.
    builder.add_edge("tools", "compact_tool_results")
    builder.add_edge("compact_tool_results", "orchestrator")
    builder.add_edge("merge_results", "format_response")
    builder.add_edge("format_response", END)

    return builder.compile(checkpointer=checkpointer)


def get_graph():
    checkpointer = InMemorySaver()
    return build_graph(checkpointer=checkpointer)
