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

## Eval — LLM-as-Judge (tests/)

Evidence shown to the judge is **complete — nothing is cut**. The agent answers from the
full raw tool results, so any per-item compaction makes correctly-grounded facts look
hallucinated. Every result, the full grounding answer/recommendation, every product field,
and full web snippets are passed through verbatim. There are **no per-item caps**; the only
limit is one overall crash-guard ceiling sized near the judge model's context capacity.

| Where | Value | Purpose |
|---|---|---|
| `tests/metrics.py` `EVIDENCE_BUDGET_CHARS` | 2_000_000 | **Crash-guard only** (~500k tokens, near Gemini 3.x Pro's ~1M-token input). Never reached for this workload, so nothing is truncated. If ever exceeded, max-min fair allocation truncates the largest blocks proportionally — never dropping a whole tool — and sets `truncated=True` |
| `tests/judge.py` `MAX_CLAIMS` | 200 | Ceiling on persisted/scored claims per turn — high enough to never clip a turn |
| `tests/judge.py` `CONTRADICTION_WEIGHT` | 2 | A `CONTRADICTED` claim counts double a `NOT_IN_EVIDENCE` one |
| `tests/judge.py` `CORRECTNESS_RATIO_BANDS` | 0→5, ≤0.15→4, ≤0.35→3, ≤0.6→2, else 1 | Maps faithfulness penalty ratio to a 1-5 correctness score |

No per-item caps exist anymore (the earlier `MAX_RESULTS_PER_TOOL` / `WEB_SNIPPET_CHARS` /
`SEARCH_ANSWER_CHARS` / `RECOMMENDATION_CHARS` / `EXTRA_FIELD_CHARS` were removed). The
`truncated` flag in `summary.md` should always be 0; if it isn't, the workload grew past the
crash-guard and `EVIDENCE_BUDGET_CHARS` should be raised.

**Correctness scoring** is derived deterministically from the judge's per-claim labels
(RAGAS-style faithfulness), not a holistic guess:

```
ratio = (#NOT_IN_EVIDENCE + CONTRADICTION_WEIGHT·#CONTRADICTED)
        / (#SUPPORTED + #NOT_IN_EVIDENCE + #CONTRADICTED)
correctness = CORRECTNESS_RATIO_BANDS(ratio)
```

`GENERAL_KNOWLEDGE` claims are excluded from the denominator (standard sommelier/world
knowledge is not a grounding failure). When nothing is checkable (T == 0), it falls back
to the judge's holistic `correctness`. `summary.md` reports an **Evidence & Claim Health**
block: turns with truncated evidence (should be 0) and the global claim-label distribution
(`NOT_IN_EVIDENCE + CONTRADICTED` is the real hallucination signal).

## Missing (no explicit setting)

- **`recursion_limit`** — LangGraph default (25)
- **Supervisor LLM `max_output_tokens`** — 설정 없음 (model default)
- **Sub-agent LLM `max_output_tokens`** — 설정 없음