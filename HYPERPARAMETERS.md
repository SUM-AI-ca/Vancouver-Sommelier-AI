# Hyperparameters

## LLM Temperatures

| Where | Value | Purpose |
|---|---|---|
| `models.py:17` `get_llm()` default | 0.1 | Base default (not used directly — callers override) |
| `models.py:26` `get_grounded_llm()` default | 0.1 | Google Search grounding calls |
| `models.py:42` `get_judge_llm()` | 0.0 | Eval judge |
| `agent.py:91` Supervisor orchestrator | 0.1 | Routing & final answer |
| `agents/react_subagent.py:29` Sub-agent default | 0.1 | Used by Sourcing only — the other two override |
| `agents/sommelier_agent.py:83` Sommelier | 0.2 | Pairing rationale |
| `agents/menu_architect.py:76` Menu Architect | 0.3 | Menu design (most creative) |
| `agent_tools.py:150` `reasoning_pair_wine` | 0.15 | Wine pairing sub-LLM (creative) |
| `validation.py:24` Query validation | 0.0 | Safety/topic check |
| `vision.py:220` Vision structured output | 0.0 | Image transcription |
| `vision.py:237` Vision raw fallback | 0.0 | Image transcription fallback |

## Agent Limits

| Where | Value | Purpose |
|---|---|---|
| `agent.py:124` `MAX_TOOL_ROUNDS` | 7 | Supervisor max tool-call rounds per turn |
| `agent.py:38` `MAX_CLARIFICATIONS_PER_TURN` | 3 | Max clarification questions before forced answer |
| `agent.py:86` `EMPTY_RESPONSE_RETRIES` | 3 | Supervisor blank-response re-invokes |
| `agents/sourcing_agent.py:64` | max_rounds=4 | Sourcing sub-agent tool rounds |
| `agents/sommelier_agent.py:83` | max_rounds=3 | Sommelier sub-agent tool rounds (trimmed 4 → 3 with single-round batching) |
| `agents/menu_architect.py:76` | max_rounds=5 | Menu architect sub-agent tool rounds |
| `agents/react_subagent.py:30` | max_rounds=5 | Sub-agent default (overridden above) |
| `agent.py:191` tool_call_log | [-50:] | Keep last 50 tool call log entries |

## Timeouts

| Where | Value | Purpose |
|---|---|---|
| `vision.py:185` `_VISION_TIMEOUT` | 45s | Vision LLM call (both paths) |
| `app.py:213` `HEARTBEAT_SECONDS` | 15s | SSE keepalive ping when the stream is idle |
| `mcp_client.py:94` MCP `timeout` | 120s | Retailer `tools/call` over MCP (slow scrapes exceed the 30s default) |
| `mcp_client.py:95` MCP `sse_read_timeout` | 300s | MCP stream read |
| `tools/bcliquor_tool.py:98` | 20s | HTTP client |
| `tools/everythingwine_tool.py:147` | 20s | HTTP client |
| `tools/legacy_tool.py:245` | 20s | HTTP client |
| `tools/marquis_tool.py:94` | 20s | HTTP client |
| `tools/okanagan_cellars_tool.py:120` | 20s | HTTP client |
| `tools/suttonplace_tool.py:140` | 20s | HTTP client |

## Rate & Size Limits

| Where | Value | Purpose |
|---|---|---|
| `app.py:544` | 30/hour | API chat endpoint rate limit (per IP) |
| `app.py:151` / `frontend/app.js:56` | MAX_IMAGES=2 | Max images per chat turn |
| `frontend/app.js:57` | MAX_DIM=2048px | Image downscale longest edge |

## Tool-Specific Defaults

| Where | Value | Purpose |
|---|---|---|
| `agent_tools.py:56` BC Liquor | max_pages=2 | 2 pages x 24 results = ~48 max |
| `agent_tools.py:93` Marquis | limit=20 | Max search results |
| `agent_tools.py:104` Legacy | limit=20 | Max search results |
| `tools/legacy_tool.py:195` raw search | limit=30 | Internal search default |
| `tools/marquis_tool.py:66` raw search | limit=30 | Internal search default |
| `tools/everythingwine_tool.py:134` | max_store_lookups=12 | Cap on per-product stock lookups |

## Models

| Where | Value |
|---|---|
| `models.py:13` `MODEL` | gemini-3.6-flash |
| `models.py:14` `JUDGE_MODEL` | gemini-3.1-pro-preview |
| `agents/sommelier_agent.py:83` | gemini-3.6-flash |
| `agents/menu_architect.py:76` | gemini-3.6-flash |

`tests/quality_eval.py` reads both ids from `models.py` rather than repeating them, so a swap
can't silently mislabel a whole eval run.

## Transient LLM Retry

Gemini returns `499 CANCELLED` intermittently. It is a 4xx, so the SDK does not retry it, and
one blip would otherwise drop a whole specialist's contribution for the turn.

| Where | Value | Purpose |
|---|---|---|
| `models.py` `LLM_MAX_ATTEMPTS` | 3 | Total attempts per specialist LLM call |
| `models.py` `LLM_RETRY_BASE_DELAY` | 1.0s | Doubled each retry (1s, 2s) |
| `models.py` `_TRANSIENT_HINTS` | 429/499/5xx, cancelled, deadline, timeout, unavailable, … | Same list `tests/judge.py` uses for the judge |

Non-transient errors re-raise on the first attempt. `asyncio.CancelledError` is a
`BaseException` and passes through untouched, so a disconnected client is never retried against.

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