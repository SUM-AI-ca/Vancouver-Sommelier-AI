"""MCP smoke test — exercises the exact production tool-loading path.

Run while the app is serving (python -m uvicorn app:app --port 8080), or against
a standalone server (python mcp_server.py → port 3001):

    python scripts/mcp_smoke.py                          # default self URL :8080
    python scripts/mcp_smoke.py http://127.0.0.1:3001/   # standalone server
"""
import asyncio
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


async def main() -> None:
    if len(sys.argv) > 1:
        os.environ["MCP_SELF_URL"] = sys.argv[1]

    from agent_tools import SOURCING_TOOLS
    from mcp_client import EXPECTED_TOOL_NAMES, load_sourcing_tools

    tools = await load_sourcing_tools()
    assert tools is not SOURCING_TOOLS, (
        "FAIL: fell back to direct in-process tools — MCP endpoint unreachable "
        "(is the app running on the expected port?)"
    )
    names = {t.name for t in tools}
    assert names == EXPECTED_TOOL_NAMES, f"FAIL: unexpected toolset {sorted(names)}"

    marquis = next(t for t in tools if t.name == "search_marquis_tool")
    out = await marquis.ainvoke({"query": "pinot noir", "limit": 3})
    assert isinstance(out, str), f"FAIL: expected flattened str output, got {type(out)}"
    data = json.loads(out)
    assert data.get("tool") == "search_marquis", f"FAIL: bad envelope {data.keys()}"
    assert isinstance(data.get("results"), list), "FAIL: envelope missing results list"

    print(
        f"OK — 6 tools via MCP; search_marquis status={data['status']}, "
        f"{len(data['results'])} results"
    )


asyncio.run(main())
