# Hyperparameters

## LLM Temperatures

| Where | Value | Purpose |
|---|---|---|
| `models.py:11` `get_llm()` default | 0.1 | Base default (not used directly — callers override) |
| `models.py:20` `get_grounded_llm()` default | 0.1 | Google Search grounding calls |
| `models.py:36` `get_judge_llm()` | 0.0 | Eval judge |
| `agent.py:68` Supervisor orchestrator | 0.1 | Routing & final answer |
| `agents/react_subagent.py:29` Sub-agent default | 0.1 | All 3 specialist agents (none override) |
| `agent_tools.py:147` `reasoning_pair_wine` | 0.15 | Wine pairing sub-LLM (creative) |
| `validation.py:24` Query validation | 0.0 | Safety/topic check |
| `vision.py:217` Vision structured output | 0.0 | Image transcription |
| `vision.py:234` Vision raw fallback | 0.0 | Image transcription fallback |

## Agent Limits

| Where | Value | Purpose |
|---|---|---|
| `agent.py:95` `MAX_TOOL_ROUNDS` | 7 | Supervisor max tool-call rounds per turn |
| `agent.py:38` `MAX_CLARIFICATIONS_PER_TURN` | 3 | Max clarification questions before forced answer |
| `agents/sourcing_agent.py:34` | max_rounds=4 | Sourcing sub-agent tool rounds |
| `agents/sommelier_agent.py:43` | max_rounds=4 | Sommelier sub-agent tool rounds |
| `agents/menu_architect.py:58` | max_rounds=5 | Menu architect sub-agent tool rounds |
| `agents/react_subagent.py:30` | max_rounds=5 | Sub-agent default (overridden above) |
| `agent.py:162` tool_call_log | [-50:] | Keep last 50 tool call log entries |

## Timeouts

| Where | Value | Purpose |
|---|---|---|
| `vision.py:182` `_VISION_TIMEOUT` | 45s | Vision LLM call (both paths) |
| `tools/bcliquor_tool.py:98` | 20s | HTTP client |
| `tools/everythingwine_tool.py:147` | 20s | HTTP client |
| `tools/legacy_tool.py:245` | 20s | HTTP client |
| `tools/marquis_tool.py:94` | 20s | HTTP client |
| `tools/okanagan_cellars_tool.py:120` | 20s | HTTP client |
| `tools/suttonplace_tool.py:140` | 20s | HTTP client |

## Rate & Size Limits

| Where | Value | Purpose |
|---|---|---|
| `app.py:375` | 20/hour | API chat endpoint rate limit (per IP) |
| `app.py:81` / `frontend/app.js:93` | MAX_IMAGES=2 | Max images per chat turn |
| `frontend/app.js:94` | MAX_DIM=2048px | Image downscale longest edge |

## Tool-Specific Defaults

| Where | Value | Purpose |
|---|---|---|
| `agent_tools.py:56` BC Liquor | max_pages=3 | 2 pages x 24 results = ~48 max |
| `agent_tools.py:94` Marquis | limit=20 | Max search results |
| `agent_tools.py:105` Legacy | limit=20 | Max search results |
| `tools/legacy_tool.py:195` raw search | limit=30 | Internal search default |
| `tools/marquis_tool.py:66` raw search | limit=30 | Internal search default |
| `tools/everythingwine_tool.py:134` | max_store_lookups=12 | Cap on per-product stock lookups |

## Models

| Where | Value |
|---|---|
| `models.py:7` `MODEL` | gemini-3.5-flash |
| `models.py:8` `JUDGE_MODEL` | gemini-3.1-pro-preview |

## Missing (no explicit setting)

- **`recursion_limit`** — LangGraph default (25)
- **Supervisor LLM `max_output_tokens`** — 설정 없음 (model default)
- **Sub-agent LLM `max_output_tokens`** — 설정 없음