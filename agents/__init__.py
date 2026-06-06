"""Multi-agent layer for the AI Drinks Concierge.

Target architecture (CHALLENGE_PLAN.md v2 — Supervisor + 3 Specialists):

    Supervisor  → routes, synthesizes, owns clarification + preferences
      ├─ Sourcing Agent   — 6 store tools (price / stock / where-to-buy)
      ├─ Sommelier Agent  — pairing + all-category drinks knowledge + Google grounding
      └─ Menu Architect   — (B2B) food menu → beverage menu design + sourcing

Each specialist is an independent mini ReAct sub-graph exposed to the Supervisor as a
single `@tool` (same pattern as the legacy `reasoning_pair_wine_tool`). This Day-1
scaffold defines module structure and tool ownership; sub-graph wiring lands in P0-3.
"""
