# Quality Eval — Local Runbook

Golden-query eval pipeline for Vancouver Drinks AI. Run on your own machine.

## What it does

For each query in `golden_queries.py`:

1. Invokes the LangGraph (`agent.get_graph().ainvoke`) on a fresh thread.
2. Captures the resulting `state` — messages, tool calls, `wine_context`.
3. **LLM-as-Judge** (`judge.py`) — Gemini 3.1 Pro Preview, temp=0, scores 1–5 on: relevance / correctness / helpfulness / coherence / harmlessness / overall. Also extracts 1–4 issue bullets and 0–2 strength bullets.
4. Writes a per-query transcript (`transcripts/<id>.md`), the full `results.json`, and a Claude-readable `summary.md` with TL;DR.

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

# Quickest sanity check — 2 queries (~2 min)
python -m tests.quality_eval --dry-run

# One specific query (fast feedback loop on a single regression)
python -m tests.quality_eval --id INV-001

# Category subset (INV = inventory, CRI = critic, PAIR-* = pairings,
# MT-REF / MT-PREF = multi-turn, OFF = off-topic, etc.)
python -m tests.quality_eval --only INV,CRI

# First N queries after filters
python -m tests.quality_eval --only PAIR-W --limit 2

# Full suite (~25-30 min)
python -m tests.quality_eval
```

**Ctrl-C is safe.** Whatever queries have completed are written to a partial `results.json` + `summary.md` before exit. Exit code 130 indicates interruption.

## Reading the output

```
tests/results/20260526-184500/
├── results.json            # full structured data (load with json.load)
├── summary.md              # human-readable; start here
└── transcripts/
    ├── INV-001.md          # per-query: tool calls, response, judge scores
    ├── CRI-001.md
    └── …
```

`summary.md` order:

1. **TL;DR — Top Issues for Next Session** — auto-derived from low judge dimension averages.
2. **Judge Scores** — per-dimension averages (relevance, correctness, helpfulness, coherence, harmlessness, overall).
3. **Latency** — avg, median, p95, max.
4. **Per-Category Breakdown** — judge overall average per category.
5. **Per-Query Detail** — one row per turn with all 6 judge dimensions + issue summary.
6. **Suggested Code Targets** — file pointers for likely root causes of low scores.

## Categories (golden_queries.py)

| Code | Meaning |
|---|---|
| `INV` | Inventory / "where can I buy" |
| `CRI` | Critic reviews via grounding |
| `PAIR-W` | Western pairing — built-in knowledge |
| `PAIR-C` | Complex pairing — reasoning depth |
| `PAIR-N` | Non-Western pairing — cultural awareness |
| `EDU` | Regional / educational |
| `DISC` | Open-ended discovery |
| `BEG` | Beginner-tier — friendly, jargon-light |
| `SOM` | Sommelier-tier — technical depth |
| `B2B` | Beverage-menu design for F&B |
| `ML` | Multilingual (Chinese, Japanese) |
| `MT-REF` | Multi-turn reference resolution ("the second one") |
| `MT-PREF` | Multi-turn preference inference |
| `FB` | Fallback — wine not in stock anywhere |
| `OFF` | Off-topic / prompt injection — should refuse |

## Common workflows

**"Did my prompt/code change regress anything?"** — run `--dry-run` or `--only INV,CRI` for a quick spot check, then full suite if those look clean.

**"Why did one query score low?"** — open `transcripts/<id>.md`. Tool calls, final response, and full judge output (scores + issues + strengths) are there.

**"I want to compare runs."** — both runs live in `tests/results/<timestamp>/`. Diff their `summary.md` files (or load both `results.json` and diff the `aggregate` blocks).

## Files

- `quality_eval.py` — the runner. CLI + per-query loop + aggregation + summary rendering.
- `metrics.py` — content extraction helpers (no scoring logic).
- `judge.py` — single LLM call per turn with the rubric.
- `golden_queries.py` — 29 golden queries across 16 categories. Each entry has `judge_focus` to weight specific dimensions.
- `__init__.py` — empty; just makes `tests` a package.
- `results/` — gitignored output directory.
