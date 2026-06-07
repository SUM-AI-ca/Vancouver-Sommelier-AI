"""Supervisor Agent — routing contract (the live wiring lives in agent.py).

The Supervisor is the top of the multi-agent graph. To keep app.py's SSE streaming and
badge filters unchanged, it is wired in `agent.py` as the graph node still named
"orchestrator":

    agent.py:  TOOLS = SUPERVISOR_DIRECT_TOOLS + [sourcing_agent_tool,
                                                  sommelier_agent_tool,
                                                  menu_architect_tool]
               orchestrator_node binds TOOLS and uses prompts.SUPERVISOR_SYSTEM_PROMPT.

Flow:  entry_router → (vision) → orchestrator(=Supervisor) → tools → orchestrator → END

Each specialist tool runs its own ReAct sub-graph (agents/{sourcing,sommelier,menu_*}.py)
as an isolated invocation, so specialist-internal tool/LLM events never leak into the
Supervisor's stream — only the specialist's own badge surfaces.

This module is documentation only; the prompt is prompts.SUPERVISOR_SYSTEM_PROMPT and the
tool groupings are in agent_tools.py.
"""

# Routing summary (see prompts.SUPERVISOR_SYSTEM_PROMPT for the full contract):
#   price / stock / where-to-buy / "near me" / hours      → sourcing_agent_tool
#   what to drink / pairing / education / reviews         → sommelier_agent_tool
#   "design a drink menu" / food-menu image (B2B)         → menu_architect_tool
#   genuine ambiguity                                     → ask_user_clarification
