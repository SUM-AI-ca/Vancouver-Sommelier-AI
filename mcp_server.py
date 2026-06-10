"""MCP server — `vancouver-retailers`.

Serves the six Vancouver retailer search tools over the Model Context Protocol
(Streamable HTTP). This is the canonical tool host for the Sourcing Agent, which
consumes these tools as an MCP client (see mcp_client.py). app.py mounts this
server at /mcp, so the same endpoint is reachable by any external MCP client
(MCP Inspector, Claude Desktop, ADK agents) at https://wineaiagent.com/mcp.

Tool names, signatures, docstrings, and JSON envelopes are kept identical to the
legacy in-process wrappers in agent_tools.py — the LLM-facing schema and the
frontend tool badges do not change when tools travel over MCP.

Standalone (for development / external use without the FastAPI app):

    python mcp_server.py      # serves http://127.0.0.1:3001/
"""
from __future__ import annotations

import json

from mcp.server.fastmcp import FastMCP

from safety import tool_error_to_json
from tools.bcliquor_tool import search_bcliquor
from tools.everythingwine_tool import search_everything_wine
from tools.legacy_tool import search_legacy as search_legacy_liquor_store
from tools.marquis_tool import search_marquis
from tools.okanagan_cellars_tool import search_okanagan_cellars
from tools.suttonplace_tool import search_suttonplace

mcp = FastMCP(
    "vancouver-retailers",
    # Mounted at /mcp by app.py; "/" here keeps the endpoint at /mcp/ (not /mcp/mcp).
    streamable_http_path="/",
    # Every request is self-contained — safe for the Sourcing Agent's 6-way
    # parallel fan-out, where each tool call runs in its own short-lived session.
    stateless_http=True,
    json_response=True,
)

# structured_output=False on every tool: the return value is already a JSON string
# envelope; without it FastMCP would re-wrap the string in structuredContent.


@mcp.tool(structured_output=False)
async def search_bcliquor_tool(query: str, max_pages: int = 2, category: str | None = None) -> str:
    """Search BC Liquor Stores (government retailer, Vancouver).
    Wine, beer, spirits, cider. Also returns consumer ratings and BC VQA status.
    """
    try:
        results = await search_bcliquor(query, max_pages=max_pages, category=category)
        return json.dumps({"status": "ok", "tool": "search_bcliquor", "results": [r.model_dump() for r in results]})
    except Exception as e:
        return tool_error_to_json(e)


@mcp.tool(structured_output=False)
async def search_everything_wine_tool(query: str) -> str:
    """Search Everything Wine for prices and availability across Lower Mainland stores
    (Vancouver, North Vancouver, South Surrey, Langley).
    Also shows home-delivery status and exact per-store stock quantities.
    """
    try:
        results = await search_everything_wine(query)
        return json.dumps({"status": "ok", "tool": "search_everything_wine", "results": [r.model_dump() for r in results]})
    except Exception as e:
        return tool_error_to_json(e)


@mcp.tool(structured_output=False)
async def search_okanagan_cellars_tool(query: str) -> str:
    """Search Okanagan Cellars (Vancouver, 2 locations) for prices and availability.
    Often competitive pricing on BC wines. Also shows exact stock quantities and unit sizes.
    """
    try:
        results = await search_okanagan_cellars(query)
        return json.dumps({"status": "ok", "tool": "search_okanagan_cellars", "results": [r.model_dump() for r in results]})
    except Exception as e:
        return tool_error_to_json(e)


@mcp.tool(structured_output=False)
async def search_suttonplace_tool(query: str) -> str:
    """Search Sutton Place Wine Merchant (Vancouver, Yaletown) for prices and availability.
    Also shows vintage, varietal, country, alcohol %, and staff picks.
    """
    try:
        results = await search_suttonplace(query)
        return json.dumps({"status": "ok", "tool": "search_suttonplace", "results": [r.model_dump() for r in results]})
    except Exception as e:
        return tool_error_to_json(e)


@mcp.tool(structured_output=False)
async def search_marquis_tool(query: str, limit: int = 20, skip: int = 0) -> str:
    """Search Marquis Wine Cellars (Vancouver, curated boutique) for prices and availability.
    Boutique selection with hierarchical categories and MSRP pricing.
    """
    try:
        results, total = await search_marquis(query, limit=limit, skip=skip)
        return json.dumps({"status": "ok", "tool": "search_marquis", "total": total, "results": [r.model_dump() for r in results]})
    except Exception as e:
        return tool_error_to_json(e)


@mcp.tool(structured_output=False)
async def search_legacy_liquor_store_tool(
    query: str,
    limit: int = 20,
    price_min: float | None = None,
    price_max: float | None = None,
    on_sale: bool | None = None,
    staff_pick: bool | None = None,
) -> str:
    """Search Legacy Liquor Store (Vancouver). Wine, beer, spirits, cider.
    Supports price_min/price_max filtering, on_sale for deals, and staff_pick for expert recommendations.
    """
    try:
        results, total = await search_legacy_liquor_store(
            query, limit=limit, price_min=price_min, price_max=price_max,
            on_sale=on_sale, staff_pick=staff_pick,
        )
        return json.dumps({"status": "ok", "tool": "search_legacy_liquor_store", "total": total, "results": [r.model_dump() for r in results]})
    except Exception as e:
        return tool_error_to_json(e)


if __name__ == "__main__":
    # Port 3001: the FastMCP default (8000) collides with the local app server.
    mcp.settings.host = "127.0.0.1"
    mcp.settings.port = 3001
    mcp.run(transport="streamable-http")
