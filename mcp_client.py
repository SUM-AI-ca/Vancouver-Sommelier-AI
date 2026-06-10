"""Loads the Sourcing Agent's toolset over MCP, with a loud in-process fallback.

The Sourcing Agent does not import the retailer tools directly — it consumes them
from the `vancouver-retailers` MCP server (mcp_server.py, mounted at /mcp by
app.py) through langchain-mcp-adapters. Each tool invocation opens its own
short-lived MCP session, so the agent's 6-way parallel fan-out stays parallel.

If the MCP endpoint is unreachable (e.g. tests/quality_eval.py runs the graph
without uvicorn, or local dev on a non-8080 port without MCP_SELF_URL), the
loader logs an ERROR and falls back to the legacy in-process SOURCING_TOOLS —
the agent keeps working, only the transport differs.

Env vars:
    SOURCING_VIA_MCP  "1" (default) load tools over MCP; "0" force direct tools.
    MCP_SELF_URL      MCP endpoint; default http://127.0.0.1:${PORT:-8080}/mcp/
"""
from __future__ import annotations

import logging
import os

from langchain_core.tools import StructuredTool

log = logging.getLogger("bc-wine-agent.mcp")

EXPECTED_TOOL_NAMES = {
    "search_bcliquor_tool",
    "search_everything_wine_tool",
    "search_okanagan_cellars_tool",
    "search_suttonplace_tool",
    "search_marquis_tool",
    "search_legacy_liquor_store_tool",
}


def _flatten(content) -> str:
    """Restore an MCP tool result to the raw JSON envelope string.

    langchain-mcp-adapters >= 0.2 returns tool output as a list of content
    blocks ([{"type": "text", "text": ...}]). The agent prompt, the inner-tool
    log, and app.py's badge summarizer all expect the plain JSON string the
    legacy tools returned.
    """
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        return "".join(
            block.get("text", "")
            for block in content
            if isinstance(block, dict) and block.get("type") == "text"
        )
    return str(content)


def _flat_tool(mcp_tool: StructuredTool) -> StructuredTool:
    """Re-wrap an adapter tool so it returns the flattened string content."""

    async def _run(**kwargs) -> str:
        return _flatten(await mcp_tool.ainvoke(kwargs))

    return StructuredTool(
        name=mcp_tool.name,
        description=mcp_tool.description,
        args_schema=mcp_tool.args_schema,
        coroutine=_run,
        metadata=mcp_tool.metadata,
    )


async def load_sourcing_tools() -> list:
    from agent_tools import SOURCING_TOOLS  # late import — also the fallback set

    if os.getenv("SOURCING_VIA_MCP", "1") != "1":
        log.info("SOURCING_VIA_MCP disabled — using direct in-process tools")
        return SOURCING_TOOLS

    try:
        from langchain_mcp_adapters.client import MultiServerMCPClient

        url = os.getenv("MCP_SELF_URL") or f"http://127.0.0.1:{os.getenv('PORT', '8080')}/mcp/"
        headers = {}
        if os.getenv("PROXY_SECRET"):
            # /mcp sits behind the same proxy-secret guard as /api/* in production.
            headers["X-Proxy-Secret"] = os.environ["PROXY_SECRET"]

        client = MultiServerMCPClient({
            "vancouver_retailers": {
                "transport": "streamable_http",
                "url": url,
                "headers": headers,
                # tools/call blocks until the retailer scrape finishes; the
                # slowest path (bcliquor 2 pages + query fallback retries) can
                # exceed the 30s default.
                "timeout": 120,
                "sse_read_timeout": 300,
            }
        })
        tools = await client.get_tools()
        names = {t.name for t in tools}
        if names != EXPECTED_TOOL_NAMES:
            raise RuntimeError(f"unexpected MCP toolset: {sorted(names)}")
        log.info("Sourcing tools loaded via MCP at %s: %s", url, sorted(names))
        return [_flat_tool(t) for t in tools]
    except Exception as e:
        log.error(
            "MCP tool loading FAILED (%s: %s) — FALLING BACK to direct in-process tools",
            type(e).__name__, e,
        )
        return SOURCING_TOOLS
