"""LangGraph agent — build_graph() wires the ReAct orchestrator, tools, merge, and synthesis."""

from datetime import datetime, timezone

from langchain_core.messages import AIMessage, HumanMessage, SystemMessage, ToolMessage
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph import END, StateGraph
from langgraph.prebuilt import ToolNode

from agent_tools import SUPERVISOR_DIRECT_TOOLS
from agents.menu_architect import menu_architect_tool
from agents.sommelier_agent import sommelier_agent_tool
from agents.sourcing_agent import sourcing_agent_tool
from models import get_llm
from prompts import SUPERVISOR_SYSTEM_PROMPT
from safety import tool_error_to_json
from state import AgentState
from vision import (
    extract_image_urls,
    extract_text,
    extract_vision,
    format_extraction,
    latest_human_message,
    message_has_image,
)


# The Supervisor routes to specialist sub-agents (each a @tool over its own ReAct
# sub-graph in agents/) plus the cross-cutting clarification/preferences tools. The graph
# node is still named "orchestrator" so app.py's SSE streaming/badge filters are unchanged.
SUPERVISOR_TOOLS = SUPERVISOR_DIRECT_TOOLS + [
    sourcing_agent_tool,
    sommelier_agent_tool,
    menu_architect_tool,
]
TOOLS = SUPERVISOR_TOOLS

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
    llm = get_llm(temperature=0.1)
    if not over_budget:
        llm = llm.bind_tools(TOOLS)

    system_parts = [SUPERVISOR_SYSTEM_PROMPT]

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


MAX_TOOL_ROUNDS = 7


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
