# Quality Eval — Local Runbook

Golden-query eval pipeline for Vancouver Drinks AI. Run on your own machine.

## What it does

For each query in `golden_queries.py`:

1. Invokes the LangGraph (`agent.get_graph().ainvoke`) on a fresh thread.
2. Captures the resulting `state` — messages, `tool_call_log`.
3. Runs **deterministic metrics** (`metrics.py`):
   - Tool orchestration (precision / recall / F1, forbidden-call check, per-turn limit check)
   - Hallucination check against raw tool output
   - Coverage (distinct stores / critics cited)
   - Output-contract score (Lead / Why / Where-to-buy / Pairing skeleton)
   - Multi-turn reference resolution + preferences-active checks
4. (Optional) **LLM-as-judge** (`judge.py`) — Gemini 3.5 Flash, temp=0, rubric scores 1–5 for accuracy / citation / completeness / style / helpfulness / structure / overall.
5. Writes a per-query transcript (`transcripts/<id>.md`), the full `results.json`, and a Claude-readable `summary.md` with TL;DR.

Output lands in `tests/results/<YYYYMMDD-HHMMSS>/` (gitignored).

## Pre-flight (one-time setup)

```bash
# From project root
gcloud auth application-default login        # Vertex AI ADC for Gemini
```

The runner prints warnings for anything missing but doesn't block — the rest of the suite continues.

## Run it

All commands from the **project root** (not `tests/`):

```bash
# See what's available, group by category, no LLM calls
python -m tests.quality_eval --list

# Quickest sanity check — 2 queries, no judge (~1-2 min)
python -m tests.quality_eval --dry-run --skip-judge

# One specific query (fast feedback loop on a single regression)
python -m tests.quality_eval --id INV-001

# Category subset (INV = inventory/fan-out, CRI = critic, PAIR-* = pairings,
# MT-REF / MT-PREF = multi-turn, OFF = off-topic, etc.)
python -m tests.quality_eval --only INV,CRI

# First N queries after filters (helpful with --only for incremental testing)
python -m tests.quality_eval --only PAIR-W --limit 2

# Deterministic-only sweep across the whole suite (~10-12 min, no judge cost)
python -m tests.quality_eval --skip-judge

# Full suite with judge (~25-30 min)
python -m tests.quality_eval
```

**Ctrl-C is safe.** Whatever queries have completed are written to a partial `results.json` + `summary.md` before exit. Exit code 130 indicates interruption.

## Reading the output

```
tests/results/20260526-184500/
├── results.json            # full structured data (load with json.load)
├── summary.md              # human-readable; start here
└── transcripts/
    ├── INV-001.md          # per-query: tool calls, response, metrics, judge
    ├── CRI-001.md
    └── …
```

`summary.md` order:

1. **TL;DR — Top Issues for Next Session** — auto-derived list of code targets (e.g. "Output contract avg 1.8/4 — synthesis prompt skeleton not enforced").
2. **Aggregate Metrics** — orchestration F1, hallucination rate, judge scores, latency, coverage, structure score.
3. **Per-Category Breakdown** — pass-rate + judge overall per `INV`/`CRI`/`PAIR-*`/etc.
4. **Suspected Hallucinations** — flagged tokens with the originating query ID for code review.
5. **Per-Query Detail** — one row per turn, with pass/fail flags + judge overall.
6. **Suggested Code Targets** — file:line pointers for likely root causes.

Iteration history lives in `docs/AGENT_DESIGN.md` §16.5.

## Categories (golden_queries.py)

| Code | Meaning |
|---|---|
| `INV` | Inventory / "where can I buy" — must parallel-fan-out 4 store tools |
| `CRI` | Critic reviews — must cite by critic name + source |
| `PAIR-W` | Western pairing — answer from built-in knowledge |
| `PAIR-C` | Complex pairing — may invoke `reasoning_pair_wine` |
| `PAIR-N` | Non-Western pairing — web grounding allowed |
| `EDU` | Regional / educational |
| `DISC` | Open-ended discovery |
| `BEG` | Beginner-tier — friendly, jargon-light |
| `SOM` | Sommelier-tier — full critic detail |
| `MT-REF` | Multi-turn reference resolution ("the second one") |
| `MT-PREF` | Multi-turn preference inference |
| `FB` | Fallback — wine not in stock anywhere |
| `OFF` | Off-topic — should be intercepted by `validation.py` gate |

## Common workflows

**"Did my prompt/code change regress anything?"** — run `--skip-judge` first for a fast deterministic sweep, then run full suite if structure / hallucination / orchestration metrics look clean.

**"Why did one query fail?"** — open `transcripts/<id>.md`. Tool I/O, final response, and all metrics are there.

**"I want to compare runs."** — both runs live in `tests/results/<timestamp>/`. Diff their `summary.md` files (or load both `results.json` and diff the `aggregate` blocks).

## Files

- `quality_eval.py` — the runner. CLI + per-query loop + aggregation + summary rendering.
- `metrics.py` — pure-Python deterministic checks (no LLM).
- `judge.py` — single LLM call per turn with the rubric.
- `golden_queries.py` — golden queries across multiple categories. Each entry sets `expected_tools_all_of` / `forbidden_tools` / `must_mention` / `min_distinct_stores_cited` / `hallucination_check_fields` / `max_latency_s`.
- `__init__.py` — empty; just makes `tests` a package.
- `results/` — gitignored output directory.
