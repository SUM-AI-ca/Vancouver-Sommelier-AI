# Vancouver Drinks AI Quality Eval — 20260608-093835

- Model under test: `gemini-3.5-flash`
- Judge model: `gemini-3.1-pro-preview (temp=0)` (temperature=0)
- Total queries: **28**  |  Total invocations: **34**  |  Completed: **34**  |  Errored: **0**
- Run duration: **5928.1s** (98.8 min)

## TL;DR — Top Issues for Next Session

- No major issues auto-detected. Inspect per-query details below.

## Judge Scores (LLM-as-Judge)

| Dimension | Average | N |
|---|---|---|
| relevance | 5 | 34 |
| correctness | 4.82 | 34 |
| helpfulness | 5 | 34 |
| coherence | 4.97 | 34 |
| harmlessness | 5 | 34 |
| overall | 4.88 | 34 |

_correctness is derived from per-claim faithfulness labels (see judge.py), not a holistic guess._

## Evidence & Claim Health

- Turns with **truncated** evidence: **0** / 34 (should be 0 — >0 means raise `EVIDENCE_BUDGET_CHARS` in `tests/metrics.py`; low correctness on those turns may be a measurement artifact, not a real hallucination)
- Claim labels across all turns — SUPPORTED: 523, GENERAL_KNOWLEDGE: 12, NOT_IN_EVIDENCE: 5, CONTRADICTED: 2 (NOT_IN_EVIDENCE + CONTRADICTED = the real hallucination signal)

## Latency

| Stat | Value |
|---|---|
| avg | 147.23s |
| median | 107.0s |
| p95 | 362.62s |
| max | 458.98s |

## Per-Category Breakdown

| Category | Turns | Completed | Judge overall avg |
|---|---|---|---|
| B2B | 2 | 2 | 5 |
| BEG | 1 | 1 | 5 |
| CRI | 2 | 2 | 5 |
| DISC | 2 | 2 | 4.5 |
| EDU | 2 | 2 | 5 |
| FB | 2 | 2 | 5 |
| INV | 2 | 2 | 5 |
| ML | 2 | 2 | 5 |
| MT-PREF | 6 | 6 | 4.83 |
| MT-REF | 4 | 4 | 4.5 |
| OFF | 2 | 2 | 5 |
| PAIR-C | 2 | 2 | 5 |
| PAIR-N | 2 | 2 | 5 |
| PAIR-W | 1 | 1 | 5 |
| SOM | 2 | 2 | 5 |

## Per-Query Detail

| ID | Cat | Turn | Latency | Rel | Corr | Help | Coh | Harm | Ovr | Issues |
|---|---|---|---|---|---|---|---|---|---|---|
| INV-001 | INV | 0 | 32.74s | 5 | 5 | 5 | 5 | 5 | 5 |  |
| INV-003 | INV | 0 | 279.31s | 5 | 5 | 5 | 5 | 5 | 5 |  |
| CRI-001 | CRI | 0 | 72.74s | 5 | 5 | 5 | 5 | 5 | 5 |  |
| CRI-003 | CRI | 0 | 103.78s | 5 | 5 | 5 | 5 | 5 | 5 |  |
| PAIR-W-001 | PAIR-W | 0 | 83.18s | 5 | 5 | 5 | 5 | 5 | 5 |  |
| PAIR-C-001 | PAIR-C | 0 | 110.23s | 5 | 5 | 5 | 5 | 5 | 5 |  |
| PAIR-C-003 | PAIR-C | 0 | 182.92s | 5 | 5 | 5 | 5 | 5 | 5 |  |
| PAIR-N-001 | PAIR-N | 0 | 101.49s | 5 | 5 | 5 | 5 | 5 | 5 |  |
| PAIR-N-002 | PAIR-N | 0 | 139.3s | 5 | 5 | 5 | 5 | 5 | 5 |  |
| EDU-001 | EDU | 0 | 257.42s | 5 | 5 | 5 | 5 | 5 | 5 |  |
| EDU-002 | EDU | 0 | 362.62s | 5 | 4 | 5 | 5 | 5 | 5 | Incorrectly attributes the tasting notes of honey, apricot, and poached pear to  |
| MT-REF-001 | MT-REF | 0 | 435.41s | 5 | 5 | 5 | 5 | 5 | 5 |  |
| MT-REF-001 | MT-REF | 1 | 57.46s | 5 | 4 | 5 | 5 | 5 | 4 | The agent hallucinated the name of the winemaker ('Janice Stevens'), which is no |
| MT-REF-003 | MT-REF | 0 | 101.3s | 5 | 3 | 5 | 5 | 5 | 4 | The agent states Blue Mountain Gold Label Brut is a blend of Pinot Noir, Chardon |
| MT-REF-003 | MT-REF | 1 | 89.96s | 5 | 5 | 5 | 5 | 5 | 5 |  |
| MT-PREF-001 | MT-PREF | 0 | 4.24s | 5 | 5 | 5 | 5 | 5 | 5 |  |
| MT-PREF-001 | MT-PREF | 1 | 100.21s | 5 | 4 | 5 | 5 | 5 | 4 | The agent hallucinated the specific 5-grape blend (Cabernet Sauvignon, Merlot, C |
| MT-PREF-001 | MT-PREF | 2 | 147.88s | 5 | 5 | 5 | 5 | 5 | 5 |  |
| MT-PREF-002 | MT-PREF | 0 | 5.33s | 5 | 5 | 5 | 5 | 5 | 5 |  |
| MT-PREF-002 | MT-PREF | 1 | 78.59s | 5 | 5 | 5 | 5 | 5 | 5 |  |
| MT-PREF-002 | MT-PREF | 2 | 136.32s | 5 | 5 | 5 | 5 | 5 | 5 |  |
| FB-001 | FB | 0 | 458.98s | 5 | 5 | 5 | 5 | 5 | 5 |  |
| FB-003 | FB | 0 | 290.9s | 5 | 5 | 5 | 5 | 5 | 5 |  |
| DISC-001 | DISC | 0 | 132.88s | 5 | 4 | 5 | 5 | 5 | 4 | The agent states Quails' Gate Dry Riesling consistently lands in the 89-92 point |
| DISC-002 | DISC | 0 | 102.74s | 5 | 5 | 5 | 5 | 5 | 5 |  |
| BEG-001 | BEG | 0 | 102.73s | 5 | 5 | 5 | 5 | 5 | 5 |  |
| SOM-001 | SOM | 0 | 168.79s | 5 | 5 | 5 | 4 | 5 | 5 | The agent lists 'Scout Light Syrah' and 'Scout Vineyard 2022 Syrah Blend' under  |
| SOM-003 | SOM | 0 | 222.07s | 5 | 5 | 5 | 5 | 5 | 5 |  |
| B2B-001 | B2B | 0 | 208.71s | 5 | 5 | 5 | 5 | 5 | 5 |  |
| B2B-002 | B2B | 0 | 163.73s | 5 | 5 | 5 | 5 | 5 | 5 |  |
| ML-ZH-001 | ML | 0 | 172.5s | 5 | 5 | 5 | 5 | 5 | 5 |  |
| ML-JA-001 | ML | 0 | 92.69s | 5 | 5 | 5 | 5 | 5 | 5 |  |
| OFF-001 | OFF | 0 | 3.96s | 5 | 5 | 5 | 5 | 5 | 5 |  |
| OFF-003 | OFF | 0 | 2.87s | 5 | 5 | 5 | 5 | 5 | 5 |  |

## Suggested Code Targets (auto-derived)

- No high-confidence targets identified. Inspect per-query transcripts.

## Files in This Run

- `results.json` — full structured data (machine-readable; load with `json.load`)
- `transcripts/<ID>.md` — per-query transcripts with tool I/O + final response + judge scores