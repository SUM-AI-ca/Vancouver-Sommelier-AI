"""Sourcing Agent — inventory, pricing, and where-to-buy across the Vancouver market.

Owns the six retail store tools plus the Google Maps Places store-locator. Runs as an
independent ReAct sub-graph and is surfaced to the Supervisor as one `@tool`:
`sourcing_agent_tool(request)`.
"""
from __future__ import annotations

from langchain_core.tools import tool

from agent_tools import SOURCING_TOOLS
from agents.react_subagent import build_react_subagent, run_subagent_json

SOURCING_SYSTEM_PROMPT = """\
You are the Sourcing specialist for a Vancouver drinks concierge. Given a
product or need, find real availability, prices, and where to buy.

- Cover ALL categories: wine, beer, spirits, cider. BC Liquor and Legacy carry beer and
  spirits; the wine shops will simply return nothing for those — that's fine.
- Fan the store tools out in PARALLEL (emit multiple tool_calls in one step) to save latency.
- Use search_google_maps_tool for "near me" / store-location / opening-hours questions.
- NEVER invent a price, stock level, store, or URL — cite only what a tool returned, and
  include the product/store link whenever the tool provided one.
- If every store is empty, say so plainly; do not fabricate stock.

Return a compact, well-sourced summary (products, prices, stores, links) that the
Supervisor can fold into its final answer.
"""

_graph = None


def _get_graph():
    global _graph
    if _graph is None:
        _graph = build_react_subagent(SOURCING_SYSTEM_PROMPT, SOURCING_TOOLS, max_rounds=3)
    return _graph


@tool
async def sourcing_agent_tool(request: str) -> str:
    """Find availability, prices, and where-to-buy across Vancouver stores plus a
    Google Maps store locator. Pass a natural-language request describing the product(s)
    and any constraints (budget, category, "near <place>"). Returns a sourced summary with
    prices and links; never invents stock or prices.
    """
    return await run_subagent_json(_get_graph(), request, "sourcing_agent")
