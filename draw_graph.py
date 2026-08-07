"""Draw the full multi-agent architecture, including every sub-agent's internals.

The diagram is generated from this file, so it is the one place to edit when the
architecture changes. Three artifacts are written, and they must not drift apart:

    graph_mermaid.md                     the Mermaid source (paste into mermaid.live)
    graph.png                            the rendered diagram
    frontend/images/architecture-diagram.png   the copy the site serves (diagram.html)

`draw_graph_v2.py` imports `build_mermaid()` from here and renders the collapsed
variant (retailer names replaced by a single "live store data" node), so the two
diagrams cannot describe different systems.

Usage:   python draw_graph.py
"""
import base64
import json
import os
import shutil
import urllib.request
import zlib

from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))

# The site the frontend is deployed to is unlisted — its host is shared privately
# and deliberately not written into this repo, so the diagram says <host> instead.
_EXTERNAL_MCP_LABEL = "&lt;host&gt;/mcp via the worker"


_EDGE_AND_GATES = """\
---
config:
  flowchart:
    curve: basis
    nodeSpacing: 40
    rankSpacing: 55
    padding: 12
  themeVariables:
    fontSize: 15px
---
graph TD
    %% ── Edge: browser → Cloudflare → Cloud Run ──────────────────────────
    USER(["User · 19+ age gate"])
    FE["Frontend · Cloudflare Pages<br/>vanilla JS SSE client · 60 min timeout<br/>unlisted: robots.txt + meta noindex"]
    CFW["Cloudflare Worker · _worker.js<br/>404s probe paths · injects X-Proxy-Secret<br/>CF-Connecting-IP → X-Client-IP · X-Robots-Tag<br/>proxies /api/* and /mcp"]
    API["Cloud Run · FastAPI · app.py<br/>POST /api/chat → text/event-stream"]
    USER --> FE --> CFW --> API

    %% ── Per-request gates, in the order app.py applies them ─────────────
    PS{"Proxy secret<br/>403 on direct Cloud Run"}
    RL{"Rate limiter<br/>30 / hour / IP"}
    TS{"Turnstile<br/>when secret is set"}
    RESUME{"Pending interrupt?"}
    API --> PS --> RL --> TS --> RESUME

    VAL["Validation gate · validation.py<br/>Gemini 3.6 Flash · temp 0.0<br/>structured is_valid + rejection"]
    REJ(["Rejection<br/>in the user's language"])
    RESUME -- "new turn · text" --> VAL
    RESUME -- "new turn · image · gate skipped" --> ER
    VAL -- "invalid" --> REJ
    REJ -. "streamed as tokens" .-> SSE
    VAL -- "valid · fails open" --> ER

    %% ── LangGraph · agent.py build_graph() ──────────────────────────────
    ER{"entry_router"}
    VIS["vision_node · Gemini 3.6 Flash<br/>temp 0.0 · 45 s timeout<br/>structured output → raw fallback<br/>label · drink_list · food_menu · other"]
    ER -- "image" --> VIS

    SUP["Supervisor · node 'orchestrator'<br/>Gemini 3.6 Flash · temp 0.1<br/>max 7 tool rounds · blank-response retry ×3<br/>keeps every category a specialist returned"]
    VIS --> SUP
    ER -- "text" --> SUP
    RESUME -. "resume · Command(resume=…)" .-> SUP

    CKPT[("AsyncPostgresSaver · Cloud SQL Postgres 16<br/>per-thread checkpoint · survives instance restarts<br/>InMemorySaver when DATABASE_URL is unset")]
    SUP -. "checkpoint · restore" .-> CKPT

    CLAR["ask_user_clarification_tool<br/>interrupt() · max 3 / turn"]
    SUP -- "ambiguous" --> CLAR
    CLAR -. "clarification_request" .-> SSE

    SUP --> SOM_A
    SUP --> SRC_A
    SUP --> MA_A

    %% ── Specialists: independent ReAct sub-graphs (react_subagent.py) ───
    subgraph SOM ["Sommelier · ReAct · temp 0.2 · max 3 rounds · lookups batched into one round"]
        SOM_A["Gemini 3.6 Flash"]
        SOM_T["ToolNode"]
        SOM_R(["return JSON"])
        SOM_A -- "tool_calls" --> SOM_T --> SOM_A
        SOM_A -- "done" --> SOM_R
        RPW["reasoning_pair_wine<br/>sub-LLM · temp 0.15<br/>only for a dish the user named"]
        SWG1["search_web_grounded<br/>Google Search grounding + citations"]
        SOM_T -.-> RPW
        SOM_T -.-> SWG1
    end

    subgraph SRC ["Sourcing · ReAct · temp 0.1 · max 4 rounds"]
        SRC_A["Gemini 3.6 Flash"]
        SRC_T["ToolNode · MCP client<br/>mcp_client.py"]
        SRC_R(["return JSON"])
        SRC_A -- "all 6 retailers in parallel" --> SRC_T --> SRC_A
        SRC_A -- "done" --> SRC_R
    end

    subgraph MA ["Menu Architect · B2B · ReAct · temp 0.3 · max 5 rounds · course groups batched into ONE round"]
        MA_A["Gemini 3.6 Flash"]
        MA_T["ToolNode"]
        MA_R(["return JSON"])
        MA_A -- "tool_calls" --> MA_T --> MA_A
        MA_A -- "done" --> MA_R
        MA_SRC["sourcing_agent_tool<br/>(delegate)"]
        MA_SWG["search_web_grounded"]
        MA_T -.-> MA_SRC
        MA_T -.-> MA_SWG
    end

    SOM_R --> SUP
    SRC_R --> SUP
    MA_R --> SUP
    MA_SRC -. "in-process delegation<br/>no Supervisor round-trip" .-> SRC_A

    %% ── MCP: the retailer tools travel over the protocol ────────────────
    MCPS["MCP server · vancouver-retailers<br/>FastMCP · Streamable HTTP · stateless JSON<br/>mounted by app.py at /mcp"]
    SRC_T -- "tools/call · one session per call<br/>timeout 120 s · read 300 s" --> MCPS

    FALL["Fallback · in-process SOURCING_TOOLS<br/>only when /mcp is unreachable<br/>same tools, different transport"]
    SRC_T -. "MCP load failed" .-> FALL

    EXTMCP(["External MCP clients<br/>MCP Inspector · Claude Desktop · ADK"])
    EXTMCP -. "{EXTERNAL_MCP_LABEL}" .-> MCPS
"""

_STORES_FULL = """\
    subgraph STORES ["6 Vancouver retail chains — live product search · 20 s HTTP timeout"]
        BCL["BC Liquor Stores<br/>200+ locations · max 2 pages"]
        EW["Everything Wine<br/>4 stores · ≤ 12 stock lookups"]
        OKC["Okanagan Cellars"]
        STP["Sutton Place Wine Merchant"]
        MRQ["Marquis Wine Cellars<br/>limit 20"]
        LGC["Legacy Liquor Store<br/>limit 20"]
    end
    MCPS -.-> BCL
    MCPS -.-> EW
    MCPS -.-> OKC
    MCPS -.-> STP
    MCPS -.-> MRQ
    MCPS -.-> LGC
"""

_STORES_COLLAPSED = """\
    LIVE[("Stores' live data<br/>real-time inventory & pricing<br/>fetched on demand · 20 s HTTP timeout")]
    MCPS == "fetches live store data" ==> LIVE
"""

_RESILIENCE_AND_OUT = """\
    %% ── Resilience: every specialist is wrapped in both ─────────────────
    RETRY["ainvoke_with_retry · models.py<br/>3 attempts · 1 s → 2 s backoff<br/>429 · 499 · 5xx · cancelled · timeout<br/>CancelledError passes through untouched"]
    SOM_A -. "transient" .-> RETRY
    SRC_A -. "transient" .-> RETRY
    MA_A -. "transient" .-> RETRY

    ERR["tool_error_to_json<br/>exception → status:error envelope<br/>the turn continues"]
    SOM_T -. "err" .-> ERR
    SRC_T -. "err" .-> ERR
    MA_T -. "err" .-> ERR

    %% ── Response stream ─────────────────────────────────────────────────
    SSE["SSE events · app.py<br/>token · tool_start · tool_end · error · done<br/>vision_start · vision_result · clarification_request<br/>15 s heartbeat ping · nested runs suppressed via parent_ids<br/>tool_end carries error → red 'failed' badge"]
    SUP -- "final answer · streamed from the orchestrator node only" --> SSE
    SSE --> FE

    %% ── Ops ─────────────────────────────────────────────────────────────
    LS["LangSmith tracing<br/>optional"]
    API -. "traces" .-> LS

    ENDS["POST /api/session/:id/end<br/>deletes the thread now"]
    FE -. "chat closed · pagehide sendBeacon" .-> ENDS --> CKPT

    SCHED["Cloud Scheduler<br/>daily 04:00 America/Vancouver"]
    CLEAN["POST /internal/cleanup<br/>shared-secret guard · raw SQL over the pool<br/>sweeps threads idle &gt; 7 days"]
    SCHED --> CLEAN --> CKPT

    %% ── Palette ─────────────────────────────────────────────────────────
    classDef gate fill:#fff3cd,stroke:#856404,color:#856404
    classDef agent fill:#d4edda,stroke:#155724,color:#155724
    classDef tool fill:#cce5ff,stroke:#004085,color:#004085
    classDef infra fill:#f8d7da,stroke:#721c24,color:#721c24
    classDef store fill:#e2e3e5,stroke:#383d41,color:#383d41
    classDef mcp fill:#e7d8f7,stroke:#5a2d82,color:#5a2d82
    classDef edge fill:#d1ecf1,stroke:#0c5460,color:#0c5460
    class PS,RL,TS,RESUME,VAL gate
    class SUP,SOM_A,SRC_A,MA_A,VIS agent
    class CLAR,RPW,SWG1,MA_SRC,MA_SWG tool
    class ERR,LS,RETRY,FALL infra
    class MCPS,EXTMCP mcp
    class FE,CFW,API,SSE edge
"""


def build_mermaid(show_stores: bool = True) -> str:
    """Assemble the diagram source.

    show_stores=True  names the six retail chains (draw_graph.py)
    show_stores=False collapses them into one "live store data" node (draw_graph_v2.py)
    """
    stores = _STORES_FULL if show_stores else _STORES_COLLAPSED
    body = _EDGE_AND_GATES.replace("{EXTERNAL_MCP_LABEL}", _EXTERNAL_MCP_LABEL)
    parts = [body, stores, _RESILIENCE_AND_OUT]
    mermaid = "\n".join(parts)
    if show_stores:
        return mermaid
    # The collapsed variant has no STORES subgraph, so drop its class assignment.
    return mermaid.replace(
        "    classDef store fill:#e2e3e5,stroke:#383d41,color:#383d41\n",
        "    classDef store fill:#e2e3e5,stroke:#383d41,color:#383d41\n    class LIVE store\n",
    )


MERMAID = build_mermaid()


def render_png(mermaid_text: str) -> bytes:
    """Render via mermaid.ink's `pako:` form (deflate + base64url).

    The plain-base64 form puts the whole diagram in the URL and this one now
    exceeds nginx's request-URI limit there (HTTP 414). Deflating first cuts it
    to roughly a third, which fits comfortably.
    """
    payload = json.dumps(
        {"code": mermaid_text, "mermaid": {"theme": "default"}}
    ).encode("utf-8")
    compressor = zlib.compressobj(9, zlib.DEFLATED, 15)
    deflated = compressor.compress(payload) + compressor.flush()
    encoded = base64.urlsafe_b64encode(deflated).decode("ascii").rstrip("=")
    url = f"https://mermaid.ink/img/pako:{encoded}?type=png&bgColor=!white"
    req = urllib.request.Request(url, headers={"User-Agent": "draw_graph/1.0"})
    with urllib.request.urlopen(req, timeout=120) as resp:
        return resp.read()


# The copy diagram.html serves. Written from the same render so the published
# diagram can never fall behind the one in the repo root.
SITE_DIAGRAM = os.path.join("frontend", "images", "architecture-diagram.png")


def main():
    with open("graph_mermaid.md", "w", encoding="utf-8") as f:
        f.write(MERMAID)
    print(f"Mermaid saved -> graph_mermaid.md ({len(MERMAID):,} chars)")

    try:
        png = render_png(MERMAID)
    except Exception as e:
        print(f"PNG render failed ({type(e).__name__}: {e})")
        print("Paste graph_mermaid.md content into https://mermaid.live to view")
        return

    with open("graph.png", "wb") as f:
        f.write(png)
    print(f"PNG saved -> graph.png ({len(png):,} bytes)")

    if os.path.isdir(os.path.dirname(SITE_DIAGRAM)):
        shutil.copyfile("graph.png", SITE_DIAGRAM)
        print(f"PNG copied -> {SITE_DIAGRAM} (served by frontend/diagram.html)")


if __name__ == "__main__":
    main()
