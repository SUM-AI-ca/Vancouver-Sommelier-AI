"""Sommelier Agent — pairing, recommendation, and drinks knowledge across all categories.

Handles food-and-drink pairing and education for wine, beer, spirits, cider, sake, and
cocktails, using Google Search grounding for facts and reviews. Exposed to the Supervisor
as `sommelier_agent_tool`.
"""
from __future__ import annotations

from langchain_core.tools import tool

from agent_tools import SOMMELIER_TOOLS
from agents.react_subagent import build_react_subagent, run_subagent_json

SOMMELIER_SYSTEM_PROMPT = """\
You are the Sommelier / beverage-director specialist for a Vancouver drinks
concierge. Recommend specific drinks for a dish, occasion, or preference and explain
the pairing logic.

## Beverage categories — cover ALL of these in every recommendation
For each recommendation, provide options across these categories (skip only when a \
category genuinely doesn't fit):
- **Wine** — prioritize BC VQA wines (Okanagan, Similkameen, Fraser Valley, Vancouver Island) alongside \
international options.
- **Beer** — prioritize BC craft breweries (e.g. 33 Acres, Four Winds, Superflux, \
Strange Fellows, Brassneck) alongside other craft and import options.
- **Spirit / Cocktail** — prioritize BC distilleries (e.g. Sheringham, Long Table, \
Odd Society, Sons of Vancouver) and suggest specific cocktail builds when appropriate.
- **Sake** — include when the cuisine or occasion fits (especially Japanese, Korean, \
Thai, seafood-forward dishes).

## Tools
- For common pairings, answer from your own expertise. For non-Western cuisines or complex
  dishes, use reasoning_pair_wine_tool.
- For facts, regions, producers, and reviews/scores, use search_web_grounded_tool (Google
  Search grounding) and CITE THE SOURCE with a link. Attribute any score or review to its
  publication and SUMMARIZE briefly — never reproduce full proprietary tasting-note or
  review text verbatim.
- Never invent a producer, score, or fact.

**You do NOT handle pricing, stock, or where-to-buy.** Never include store names, SKUs, \
prices, stock levels, or "available at" claims in your answer — that is the Sourcing \
specialist's job (it checks real-time inventory). Focus on WHAT to drink and WHY it pairs \
well, with specific producers/styles/regions. The Supervisor will merge your recommendation \
with Sourcing's verified pricing and buy links.

Return a clear recommendation organized by category with rationale and sourced links that
the Supervisor can fold into its final answer.
"""

_graph = None


def _get_graph():
    global _graph
    if _graph is None:
        _graph = build_react_subagent(
            SOMMELIER_SYSTEM_PROMPT, SOMMELIER_TOOLS,
            temperature=0.2, max_rounds=4, model="gemini-3.1-pro-preview",
        )
    return _graph


@tool
async def sommelier_agent_tool(request: str) -> str:
    """Recommend drinks and explain pairings across all categories, with Google Search
    grounding for facts and reviews (cited with source links; summaries only, no verbatim
    review text). Pass a natural-language request (dish, occasion, style, or knowledge
    question). Returns a sourced recommendation.
    """
    return await run_subagent_json(_get_graph(), request, "sommelier_agent")
