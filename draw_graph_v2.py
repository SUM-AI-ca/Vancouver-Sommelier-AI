"""Draw the full multi-agent architecture (same as draw_graph.py).

Only difference: individual store names are not shown. Instead the MCP
server is depicted fetching the stores' live data (real-time inventory
& pricing) on demand.

Usage:   python draw_graph_v2.py
Output:  graph_v2.png  +  graph_v2_mermaid.md
"""
import base64
import os
import urllib.request

from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))

MERMAID = """\
graph TD
    USER(["User"])
    FE["Frontend · SSE Client<br/>60min timeout"]
    API["FastAPI · SSE Stream"]
    USER --> FE --> API

    PS{"Proxy Secret"}
    RL{"Rate Limiter"}
    API --> PS --> RL

    RESUME{"Pending interrupt?"}
    RL --> RESUME

    VAL["Validation Gate<br/>Gemini 3.5 Flash"]
    REJ(["Rejection"])
    RESUME -- "new turn · text" --> VAL
    RESUME -- "new turn · image" --> ER
    VAL -- "invalid" --> REJ
    REJ --> FE
    VAL -- "valid" --> ER

    ER{"entry_router"}
    VIS["Vision Node<br/>Gemini 3.5 Flash"]
    ER -- "image" --> VIS

    SUP["Supervisor<br/>Gemini 3.5 Flash · max 7 rounds"]
    VIS --> SUP
    ER -- "text" --> SUP
    RESUME -. "resume · clarification reply" .-> SUP

    MEM[("InMemorySaver<br/>thread_id state")]
    SUP -. "checkpoint" .-> MEM

    CLAR["ask_user_clarification<br/>interrupt · max 3/turn"]
    SUP -- "ambiguous" --> CLAR
    CLAR -- "resume" --> SUP

    SUP --> SOM_A
    SUP --> SRC_A
    SUP --> MA_A

    subgraph SOM ["Sommelier · ReAct · max 4 rounds"]
        SOM_A["Gemini 3.1 Pro Preview"]
        SOM_T["ToolNode"]
        SOM_R(["return"])
        SOM_A -- "tool_calls" --> SOM_T --> SOM_A
        SOM_A -- "done" --> SOM_R
        RPW["reasoning_pair_wine"]
        SWG1["search_web_grounded"]
        SOM_T -.-> RPW
        SOM_T -.-> SWG1
    end

    subgraph SRC ["Sourcing · ReAct · max 4 rounds"]
        SRC_A["Gemini 3.5 Flash"]
        SRC_T["ToolNode · MCP client"]
        SRC_R(["return"])
        SRC_A -- "stores in parallel" --> SRC_T --> SRC_A
        SRC_A -- "done" --> SRC_R
    end

    MCPS["MCP Server · vancouver-retailers<br/>/mcp · Streamable HTTP"]
    SRC_T -- "MCP tools/call" --> MCPS

    EXTMCP(["External MCP clients<br/>MCP Inspector · Claude · ADK"])
    EXTMCP -. "wineaiagent.com/mcp" .-> MCPS

    LIVE[("Stores' live data<br/>real-time inventory & pricing<br/>fetched on demand")]
    MCPS == "fetches live store data" ==> LIVE

    subgraph MA ["Menu Architect · ReAct · max 5 rounds · B2B"]
        MA_A["Gemini 3.1 Pro Preview"]
        MA_T["ToolNode"]
        MA_R(["return"])
        MA_A -- "tool_calls" --> MA_T --> MA_A
        MA_A -- "done" --> MA_R
        MA_SRC["sourcing_agent (delegate)"]
        MA_SWG["search_web_grounded"]
        MA_T -.-> MA_SRC
        MA_T -.-> MA_SWG
    end

    SOM_R --> SUP
    SRC_R --> SUP
    MA_R --> SUP
    MA_SRC -. "delegates" .-> SRC_A

    ERR["tool_error_to_json"]
    SOM_T -. "err" .-> ERR
    SRC_T -. "err" .-> ERR
    MA_T -. "err" .-> ERR

    SSE["SSE Events<br/>token · tool_start · tool_result<br/>clarification · done"]
    SUP -- "final answer" --> SSE --> FE --> USER

    LS["LangSmith"]
    API -. "traces" .-> LS

    classDef gate fill:#fff3cd,stroke:#856404,color:#856404
    classDef agent fill:#d4edda,stroke:#155724,color:#155724
    classDef tool fill:#cce5ff,stroke:#004085,color:#004085
    classDef infra fill:#f8d7da,stroke:#721c24,color:#721c24
    classDef store fill:#e2e3e5,stroke:#383d41,color:#383d41
    classDef mcp fill:#e7d8f7,stroke:#5a2d82,color:#5a2d82
    class VAL,RL,PS,RESUME gate
    class SUP,SOM_A,SRC_A,MA_A,VIS agent
    class CLAR,RPW,SWG1,MA_SRC,MA_SWG tool
    class LIVE store
    class ERR,LS infra
    class MCPS,EXTMCP mcp
"""


def render_png(mermaid_text: str) -> bytes:
    encoded = base64.b64encode(mermaid_text.encode("utf-8")).decode("ascii")
    url = f"https://mermaid.ink/img/{encoded}?type=png&bgColor=!white"
    req = urllib.request.Request(url, headers={"User-Agent": "draw_graph/1.0"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read()


def main():
    with open("graph_v2_mermaid.md", "w", encoding="utf-8") as f:
        f.write(MERMAID)
    print(f"Mermaid saved -> graph_v2_mermaid.md ({len(MERMAID):,} chars)")

    try:
        png = render_png(MERMAID)
        with open("graph_v2.png", "wb") as f:
            f.write(png)
        print(f"PNG saved -> graph_v2.png ({len(png):,} bytes)")
        print("Open graph_v2.png to view the full architecture.")
    except Exception as e:
        print(f"PNG render failed ({type(e).__name__}: {e})")
        print("Paste graph_v2_mermaid.md content into https://mermaid.live to view")


if __name__ == "__main__":
    main()
