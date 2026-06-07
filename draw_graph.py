"""Draw the full multi-agent architecture including all sub-agent internals.

Usage:   python draw_graph.py
Output:  graph.png  +  graph_mermaid.md
"""
import base64
import os
import re
import urllib.parse
import urllib.request

from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))

MERMAID = """\
graph TD
    USER(["User"])
    FE["Frontend · SSE Client<br/>360s timeout"]
    API["FastAPI · SSE Stream"]
    USER --> FE --> API

    PS{"Proxy Secret"}
    RL{"Rate Limiter"}
    API --> PS --> RL

    VAL["Validation Gate<br/>Gemini 3.5 Flash"]
    RL -- "text" --> VAL
    VAL -- "invalid" --> REJ(["Rejection"])
    REJ --> FE

    RESUME{"Pending interrupt?"}
    VAL -- "valid" --> RESUME
    RL -- "image" --> RESUME

    RESUME -- "new turn" --> ER
    RESUME -- "resume" --> ER

    ER{"entry_router"}
    VIS["Vision Node<br/>Gemini 3.5 Flash"]
    ER -- "image" --> VIS

    SUP["Supervisor<br/>Gemini 3.5 Flash · max 7 rounds"]
    VIS --> SUP
    ER -- "text" --> SUP

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
        SRC_T["ToolNode"]
        SRC_R(["return"])
        SRC_A -- "6 stores parallel" --> SRC_T --> SRC_A
        SRC_A -- "done" --> SRC_R
        BCL["BC Liquor"]
        EW["Everything Wine"]
        OKC["Okanagan Cellars"]
        STP["Sutton Place"]
        MRQ["Marquis Wine"]
        LGC["Legacy Liquor"]
        SRC_T -.-> BCL
        SRC_T -.-> EW
        SRC_T -.-> OKC
        SRC_T -.-> STP
        SRC_T -.-> MRQ
        SRC_T -.-> LGC
    end

    subgraph MA ["Menu Architect · ReAct · max 5 rounds · B2B"]
        MA_A["Gemini 3.1 Pro Preview"]
        MA_T["ToolNode"]
        MA_R(["return"])
        MA_A -- "tool_calls" --> MA_T --> MA_A
        MA_A -- "done" --> MA_R
        MA_SRC["sourcing_agent · A2A"]
        MA_SWG["search_web_grounded"]
        MA_T -.-> MA_SRC
        MA_T -.-> MA_SWG
    end

    SOM_R --> SUP
    SRC_R --> SUP
    MA_R --> SUP
    MA_SRC -. "A2A" .-> SRC_A

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
    class VAL,RL,PS,RESUME gate
    class SUP,SOM_A,SRC_A,MA_A,VIS agent
    class CLAR,RPW,SWG1,MA_SRC,MA_SWG tool
    class BCL,EW,OKC,STP,MRQ,LGC store
    class ERR,LS infra
"""


def render_png(mermaid_text: str) -> bytes:
    encoded = base64.b64encode(mermaid_text.encode("utf-8")).decode("ascii")
    url = f"https://mermaid.ink/img/{encoded}?type=png&bgColor=!white"
    req = urllib.request.Request(url, headers={"User-Agent": "draw_graph/1.0"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read()


def main():
    with open("graph_mermaid.md", "w", encoding="utf-8") as f:
        f.write(MERMAID)
    print(f"Mermaid saved -> graph_mermaid.md ({len(MERMAID):,} chars)")

    try:
        png = render_png(MERMAID)
        with open("graph.png", "wb") as f:
            f.write(png)
        print(f"PNG saved -> graph.png ({len(png):,} bytes)")
        print("Open graph.png to view the full architecture.")
    except Exception as e:
        print(f"PNG render failed ({type(e).__name__}: {e})")
        print("Paste graph_mermaid.md content into https://mermaid.live to view")


if __name__ == "__main__":
    main()
