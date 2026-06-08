"""Sourcing Agent — inventory, pricing, and where-to-buy across the Vancouver market.

Owns the six retail store tools. Runs as an independent ReAct sub-graph and is
surfaced to the Supervisor as one `@tool`: `sourcing_agent_tool(request)`.
"""
from __future__ import annotations

from langchain_core.tools import tool

from agent_tools import SOURCING_TOOLS
from agents.react_subagent import build_react_subagent, run_subagent_json

SOURCING_SYSTEM_PROMPT = """\
You are the Sourcing specialist for a Vancouver drinks concierge. Given a
product or need, find real availability, prices, and where to buy.

## CRITICAL — search ALL stores every time
You have 6 retailer tools. In your VERY FIRST tool call, you MUST call ALL 6 retailers \
simultaneously (6 parallel tool_calls in one step). Do NOT call just one or two \
and stop — even if BC Liquor returns results, the user needs price comparison across \
retailers. A response citing only one retailer is a failure.

The 6 retailers: search_bcliquor_tool, search_everything_wine_tool, \
search_okanagan_cellars_tool, search_suttonplace_tool, search_marquis_tool, \
search_legacy_liquor_store_tool.

## Categories
Cover ALL categories: wine, beer, spirits, cider. BC Liquor and Legacy carry beer and \
spirits; the wine shops will simply return nothing for those — that's fine.

## Rules
- NEVER invent a price, stock level, store, or URL — cite only what a tool returned, and \
include the product/store link whenever the tool provided one. If a specific (price, stock, \
store) isn't in any tool result, omit it — never approximate or guess a price range.
- **"Available at <store>" only when that store's tool shows stock > 0.** A product a store \
lists but shows as zero / unavailable is NOT available there — say "out of stock" rather \
than claiming availability.
- **Keep each price, stock, and store bound to its exact product** — never attach one \
product's price, stock, or store to a different product.
- If every store is empty, say so plainly; do not fabricate stock.
- When multiple stores carry the same product, list ALL with prices so the user can compare.

Return a compact, well-sourced summary (products, prices, stores, links) that the
Supervisor can fold into its final answer.
"""

_graph = None


def _get_graph():
    global _graph
    if _graph is None:
        _graph = build_react_subagent(SOURCING_SYSTEM_PROMPT, SOURCING_TOOLS, max_rounds=4)
    return _graph


@tool
async def sourcing_agent_tool(request: str) -> str:
    """Find availability, prices, and where-to-buy across Vancouver stores.
    Pass a natural-language request describing the product(s) and any constraints
    (budget, category). Returns a sourced summary with prices and links; never
    invents stock or prices.
    """
    return await run_subagent_json(_get_graph(), request, "sourcing_agent")
