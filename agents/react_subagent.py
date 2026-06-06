"""Shared ReAct sub-graph builder for specialist agents.

Each specialist (Sourcing, Sommelier, …) is a small ReAct loop — `agent → tools → agent
→ END` — over its own tool set and system prompt. The Supervisor calls each specialist
as a single `@tool` via `run_subagent`. Specialists do NOT own the clarification tool,
so their graphs run to completion without interrupts.
"""
from __future__ import annotations

import json

from langchain_core.messages import AIMessage, HumanMessage, SystemMessage, ToolMessage
from langgraph.graph import END, StateGraph
from langgraph.prebuilt import ToolNode

from models import get_llm
from safety import tool_error_to_json
from state import AgentState


def _count_tool_rounds(messages: list) -> int:
    return sum(1 for m in messages if isinstance(m, AIMessage) and m.tool_calls)


def build_react_subagent(
    system_prompt: str,
    tools: list,
    *,
    temperature: float = 0.1,
    max_rounds: int = 5,
    model: str | None = None,
):
    """Compile a bounded ReAct sub-graph over `tools` with `system_prompt`.

    Once `max_rounds` tool rounds are used, the agent node binds no tools and is forced
    to write its final answer — the same budget pattern as the legacy orchestrator.
    """

    async def agent_node(state: AgentState) -> dict:
        llm = get_llm(temperature=temperature, model=model)
        if _count_tool_rounds(state["messages"]) < max_rounds:
            llm = llm.bind_tools(tools)
        messages = [SystemMessage(content=system_prompt)] + state["messages"]
        response = await llm.ainvoke(messages)
        return {"messages": [response]}

    def should_continue(state: AgentState) -> str:
        last = state["messages"][-1]
        return "tools" if isinstance(last, AIMessage) and last.tool_calls else "end"

    builder = StateGraph(AgentState)
    builder.add_node("agent", agent_node)
    builder.add_node("tools", ToolNode(tools, handle_tool_errors=tool_error_to_json))
    builder.set_entry_point("agent")
    builder.add_conditional_edges("agent", should_continue, {"tools": "tools", "end": END})
    builder.add_edge("tools", "agent")
    return builder.compile()


def _flatten_text(content) -> str:
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        return "".join(p.get("text", "") for p in content if isinstance(p, dict))
    return str(content) if content is not None else ""


async def run_subagent(graph, request: str) -> str:
    """Run a specialist sub-graph on `request` and return its final answer text.

    The sub-graph runs as an isolated invocation (no parent config/callbacks), so its
    internal tool/LLM events do NOT bubble into the Supervisor's SSE stream — only the
    specialist's single tool badge surfaces, and its inner reasoning never leaks.
    """
    final_state = await graph.ainvoke({"messages": [HumanMessage(content=request)]})
    return _flatten_text(final_state["messages"][-1].content).strip()


def _extract_inner_tools(messages: list) -> list[dict]:
    """Walk a sub-agent's message history and pull out each ToolMessage's raw output."""
    tools: list[dict] = []
    for m in messages:
        if isinstance(m, ToolMessage) and m.content:
            tools.append({"tool": m.name or "", "content": m.content})
    return tools


async def run_subagent_json(graph, request: str, tool_name: str) -> str:
    """run_subagent wrapped in the standard tool JSON envelope.

    Returns `{"status": "ok", "tool": <tool_name>, "answer": <text>,
    "inner_tools": [...]}` so app.py can render per-tool breakdowns in the
    agent box UI. On failure, returns a status="error" envelope.
    """
    try:
        final_state = await graph.ainvoke({"messages": [HumanMessage(content=request)]})
        answer = _flatten_text(final_state["messages"][-1].content).strip()
        inner_tools = _extract_inner_tools(final_state["messages"])
        return json.dumps({
            "status": "ok",
            "tool": tool_name,
            "answer": answer,
            "inner_tools": inner_tools,
        })
    except Exception as e:  # noqa: BLE001 — a specialist failure must not crash the turn
        return json.dumps({"status": "error", "tool": tool_name, "message": f"{type(e).__name__}: {e}"})
