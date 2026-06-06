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
    START(["START"])
    ER{"entry_router"}

    START --> ER

    VIS["Vision Node<br/>Gemini 3.5 Flash"]
    ER -- "image" --> VIS

    SUP["Supervisor<br/>Gemini 3.5 Flash<br/>Route + Synthesize"]
    VIS --> SUP
    ER -- "text" --> SUP

    CLAR["ask_user_clarification"]
    PREF["update_preferences"]
    SUP -.-> CLAR
    SUP -.-> PREF

    SUP -- "sommelier_agent_tool" --> SOM_A
    SUP -- "sourcing_agent_tool" --> SRC_A
    SUP -- "menu_architect_tool" --> MA_A

    subgraph SOM ["Sommelier Agent - ReAct max 3 rounds"]
        SOM_A["agent LLM"]
        SOM_T["tools"]
        SOM_R(["return"])
        SOM_A -- "tool_calls" --> SOM_T --> SOM_A
        SOM_A -- "done" --> SOM_R
        RPW["reasoning_pair_wine"]
        SWG1["search_web_grounded"]
        SOM_T -.-> RPW
        SOM_T -.-> SWG1
    end

    subgraph SRC ["Sourcing Agent - ReAct max 3 rounds"]
        SRC_A["agent LLM"]
        SRC_T["tools"]
        SRC_R(["return"])
        SRC_A -- "tool_calls" --> SRC_T --> SRC_A
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

    subgraph MA ["Menu Architect - ReAct max 4 rounds - B2B"]
        MA_A["agent LLM"]
        MA_T["tools"]
        MA_R(["return"])
        MA_A -- "tool_calls" --> MA_T --> MA_A
        MA_A -- "done" --> MA_R
        MA_SRC["sourcing_agent_tool<br/>A2A hand-off"]
        MA_SWG["search_web_grounded"]
        MA_T -.-> MA_SRC
        MA_T -.-> MA_SWG
    end

    SOM_R --> SUP
    SRC_R --> SUP
    MA_R --> SUP

    MA_SRC -. "calls" .-> SRC_A

    FINISH(["END - SSE to user"])
    SUP -- "final answer" --> FINISH
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
