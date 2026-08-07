"""Menu Architect Agent — B2B beverage-menu designer for F&B businesses.

The differentiator use case: a restaurant/bar gives a FOOD menu (via the vision node's
`food_menu` extraction, or as text) and this agent designs a fitting beverage menu —
by course/dish — then sources real products and prices by delegating to the Sourcing
specialist (an agent-to-agent hand-off). Output is a structured drink menu the operator
can adopt without hiring a sommelier.

Exposed to the Supervisor as `menu_architect_tool`.
"""
from __future__ import annotations

from langchain_core.tools import tool

from agent_tools import search_web_grounded_tool
from agents.react_subagent import build_react_subagent, run_subagent_json
from agents.sourcing_agent import sourcing_agent_tool

# Collaborators: the Menu Architect designs pairings with its own expertise, calls
# search_web_grounded_tool for ideas/facts, and hands real-product sourcing to the
# Sourcing specialist (in-process delegation within the multi-agent system).
MENU_ARCHITECT_TOOLS = [
    sourcing_agent_tool,
    search_web_grounded_tool,
]

MENU_ARCHITECT_SYSTEM_PROMPT = """\
You are the Menu Architect for F&B businesses in the Vancouver area. Given a
restaurant's food menu (dishes, optionally courses and prices), design a coherent
beverage menu.

## Beverage categories — every course must cover ALL of these
For each course or dish group, provide options across these categories (skip only when \
a category genuinely doesn't fit):
- **Wine** — prioritize BC VQA wines (Okanagan, Similkameen, Fraser Valley, Vancouver Island) alongside international options.
- **Beer** — prioritize BC craft breweries alongside other craft and import options.
- **Spirit / Cocktail** — prioritize BC distilleries and suggest specific cocktail builds.
- **Sake** — include when the cuisine fits (especially Asian, seafood-forward menus).
Offer 3-4 price tiers within each category where possible.

## Process
1. Group the dishes by course/section. For each course or signature dish, choose
   beverage pairings across ALL four categories above, with a one-line rationale for each.
2. Call sourcing_agent_tool to find REAL local products, prices, and buy links.
   **Split your sourcing into 2-4 separate calls by course group** (e.g. one call for \
   starters pairings, another for mains, another for desserts). Do NOT dump all products \
   into a single sourcing call — smaller, focused requests give better coverage across \
   all Vancouver retailers.
   **Emit those sourcing calls TOGETHER in ONE response — batch them as parallel \
   tool_calls in a single turn.** The course groups do not depend on each other and run \
   concurrently, so issuing them one per round makes the menu take several times longer \
   for no gain. Only hold a call back for a later round when it genuinely needs an \
   earlier call's result.
3. Use search_web_grounded_tool only for pairing ideas or facts you're unsure of — cite
   sources, summarize, never reproduce full review text.

## Rules
- Respect any stated cuisine, budget, list size, or "by the glass" needs.
- NEVER invent a product, price, or availability — every concrete bottle/can must come
  from the Sourcing specialist's results, with its link.
- If sourcing returns nothing for a pick, say so and offer an alternative.
- Include results from MULTIPLE stores when available — price comparison is valuable.

Output a clean, structured beverage menu (grouped by course, with pairing rationale and
sourced products/prices/links) the operator can adopt as-is.
"""

_graph = None


def _get_graph():
    global _graph
    if _graph is None:
        _graph = build_react_subagent(
            MENU_ARCHITECT_SYSTEM_PROMPT, MENU_ARCHITECT_TOOLS,
            temperature=0.3, max_rounds=5, model="gemini-3.6-flash",
            name="menu_architect",
        )
    return _graph


@tool
async def menu_architect_tool(food_menu: str) -> str:
    """(B2B) Design a beverage menu for a restaurant/bar from its FOOD menu, then source
    real local products and prices. Pass the food menu as text (dish names, optionally
    courses/prices) or the vision `food_menu` extraction. Use this when the user wants to
    build / design a drink or wine menu for their venue, or uploads a food menu photo.
    Returns a structured, sourced beverage menu grouped by course.
    """
    return await run_subagent_json(_get_graph(), food_menu, "menu_architect")
