"""Collapsed variant of the architecture diagram.

Identical to draw_graph.py except that the six retailers are not named — the MCP
server is shown fetching the stores' live data (real-time inventory & pricing) on
demand. The Mermaid source comes from `draw_graph.build_mermaid(show_stores=False)`
so this variant can never describe a different system than the full one.

Usage:   python draw_graph_v2.py
Output:  graph_v2.png  +  graph_v2_mermaid.md
"""
import os

from dotenv import load_dotenv

from draw_graph import build_mermaid, render_png

load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))

MERMAID = build_mermaid(show_stores=False)


def main():
    with open("graph_v2_mermaid.md", "w", encoding="utf-8") as f:
        f.write(MERMAID)
    print(f"Mermaid saved -> graph_v2_mermaid.md ({len(MERMAID):,} chars)")

    try:
        png = render_png(MERMAID)
    except Exception as e:
        print(f"PNG render failed ({type(e).__name__}: {e})")
        print("Paste graph_v2_mermaid.md content into https://mermaid.live to view")
        return

    with open("graph_v2.png", "wb") as f:
        f.write(png)
    print(f"PNG saved -> graph_v2.png ({len(png):,} bytes)")


if __name__ == "__main__":
    main()
