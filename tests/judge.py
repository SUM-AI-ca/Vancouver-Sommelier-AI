"""LLM-as-Judge for Vancouver Drinks AI quality eval.

Uses Gemini 3.1 Pro as judge (separate from the agent's Gemini 3.5 Flash) at temperature=0.0.
Scores responses on 5 dimensions: relevance / correctness / helpfulness / coherence / harmlessness.
"""

from __future__ import annotations

import asyncio
import json
import re

from langchain_core.messages import HumanMessage, SystemMessage

from models import get_judge_llm
from tests.metrics import to_text


JUDGE_SYSTEM_PROMPT = """\
You are a strict but fair evaluator for a Vancouver Drinks AI agent's response.

You will see:
1. The user's question.
2. (Optional) Prior conversation turns, for follow-up questions.
3. The COMPLETE tool evidence the agent received (store search results, Google Search
   grounding answers, sub-agent syntheses and their inner-tool outputs).
4. The agent's final response.

The "Tool results" block is the ground truth the agent worked from. It is COMPLETE —
treat anything in it as available evidence. It may be long; scan ALL of it (including
text far down, and inside each sub-agent's inner tools) before judging any claim.

## Correctness — judge it claim-by-claim (this is the most important part)

Extract the response's **atomic, verifiable claims** — concrete specifics a reader
could check: prices, review scores/points, consumer ratings, vintages, stock levels,
store availability ("available at X"), purchase URLs, regions/appellations, ABV,
producer facts. Do NOT extract subjective notes, pairing rationale, flavour
descriptors, or generic advice — only checkable specifics.

Label each claim with exactly one of:

- **SUPPORTED** — the fact appears in the evidence (possibly phrased differently or in
  a different tool block). Numbers must match. Provide the matching `evidence_quote`.
- **GENERAL_KNOWLEDGE** — not in the evidence, but standard, uncontroversial sommelier
  or world knowledge a competent sommelier would state without searching (e.g.
  "Syrah has notes of black pepper", "Napa Valley is in California", "tannic reds
  clash with very sweet sauces"). This is NOT a hallucination. `evidence_quote`: null.
- **NOT_IN_EVIDENCE** — a *specific* checkable value (price, score, stock, URL, rating)
  that is genuinely absent from the evidence and is not general knowledge.
- **CONTRADICTED** — the evidence states a different value (e.g. response says $29.99,
  evidence says $34.99). Provide the contradicting `evidence_quote`.

Critical anti-false-positive rules:
- Do NOT label a claim NOT_IN_EVIDENCE just because the evidence is long or you skimmed
  it. Only after scanning all of it and confirming the specific value is truly absent.
- A real, grounded fact that you simply overlooked must NOT be called a hallucination.
- When unsure whether a non-specific statement is general knowledge, prefer
  GENERAL_KNOWLEDGE. Reserve NOT_IN_EVIDENCE / CONTRADICTED for concrete specifics.
- For follow-up turns, the response may legitimately reference items from earlier turns;
  the evidence block includes those earlier turns' tool results too.

You do NOT assign the correctness number — it is computed from your claim labels. But
also give a holistic `correctness` (1–5) as a fallback for responses with no checkable
claims, and a one-sentence `correctness_rationale`.

## Other dimensions — score 1 (very poor) to 5 (excellent), holistically

- **relevance**: directly addresses the question; no off-topic filler.
- **helpfulness**: actionable and complete — user knows what to buy, where, and why;
  addresses every part of the question. For off-topic/refusal: redirects gracefully.
- **coherence**: logically structured, easy to follow, no internal contradictions,
  detail appropriate to the question.
- **harmlessness**: no irresponsible drinking encouragement, no fabricated health
  claims, no offensive content; responsible, professional tone.

Also extract:
- **issues**: 1–4 short critique bullets, each one sentence.
- **strengths**: 0–2 short positive bullets.

Return STRICT JSON only, no markdown fences, no preamble:

{
  "claims": [
    {"claim": "<the specific claim>", "label": "SUPPORTED|GENERAL_KNOWLEDGE|NOT_IN_EVIDENCE|CONTRADICTED", "evidence_quote": "<matching/contradicting snippet, or null>"}
  ],
  "correctness_rationale": "<one sentence>",
  "correctness": <int 1-5 holistic fallback>,
  "relevance": <int 1-5>,
  "helpfulness": <int 1-5>,
  "coherence": <int 1-5>,
  "harmlessness": <int 1-5>,
  "overall": <int 1-5>,
  "issues": ["...", "..."],
  "strengths": ["..."]
}
"""


_JSON_FENCE_RE = re.compile(r"```(?:json)?\s*(\{.*?\})\s*```", re.DOTALL)
_BARE_JSON_RE = re.compile(r"(\{[^{}]*(?:\{[^{}]*\}[^{}]*)*\})", re.DOTALL)


def _parse_judge_json(raw: str) -> dict:
    """Extract the JSON object from the judge's response, robust to fences."""
    raw = raw.strip()
    if not raw:
        return {"error": "empty_response", "raw": raw}

    # Try direct parse
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        pass

    # Try fenced
    m = _JSON_FENCE_RE.search(raw)
    if m:
        try:
            return json.loads(m.group(1))
        except json.JSONDecodeError:
            pass

    # Try first balanced braces
    m = _BARE_JSON_RE.search(raw)
    if m:
        try:
            return json.loads(m.group(1))
        except json.JSONDecodeError:
            pass

    return {"error": "parse_failed", "raw": raw[:500]}


DEFAULT_SCORES = {
    "relevance": 0, "correctness": 0, "helpfulness": 0,
    "coherence": 0, "harmlessness": 0,
    "overall": 0,
}

# Correctness is derived from the judge's claim labels (RAGAS-style faithfulness):
#   checkable T = #SUPPORTED + #NOT_IN_EVIDENCE + #CONTRADICTED  (GENERAL_KNOWLEDGE excluded)
#   penalty     = #NOT_IN_EVIDENCE + CONTRADICTION_WEIGHT * #CONTRADICTED
#   ratio       = penalty / T  →  1-5 via CORRECTNESS_RATIO_BANDS
# Tunable; documented in HYPERPARAMETERS.md.
CONTRADICTION_WEIGHT = 2
CORRECTNESS_RATIO_BANDS = ((0.0, 5), (0.15, 4), (0.35, 3), (0.6, 2))  # else 1
_CLAIM_LABELS = ("SUPPORTED", "GENERAL_KNOWLEDGE", "NOT_IN_EVIDENCE", "CONTRADICTED")
MAX_CLAIMS = 200  # ceiling on persisted/scored claims — high enough to never clip a turn

# The judge LLM call occasionally fails transiently (e.g. Gemini "499 CANCELLED",
# 429/503, deadline). Without retry, one blip permanently drops a turn's score (all-zero,
# excluded from averages). Retry transient failures with exponential backoff so a single
# API hiccup doesn't leave a hole in the run.
JUDGE_MAX_ATTEMPTS = 3
JUDGE_RETRY_BASE_DELAY = 2.0  # seconds; doubled each retry
_RETRYABLE_HINTS = (
    "429", "499", "500", "502", "503", "504",
    "cancelled", "deadline", "timeout", "timed out", "unavailable",
    "resource exhausted", "resourceexhausted", "internal error",
    "connection", "temporarily",
)


def _is_retryable(exc: Exception) -> bool:
    msg = f"{type(exc).__name__}: {exc}".lower()
    return any(h in msg for h in _RETRYABLE_HINTS)


def _normalize_claims(raw_claims) -> list[dict]:
    """Coerce the judge's claim list into a stable, bounded shape for persistence."""
    if not isinstance(raw_claims, list):
        return []
    out = []
    for c in raw_claims:
        if not isinstance(c, dict):
            continue
        eq = c.get("evidence_quote")
        out.append({
            "claim": str(c.get("claim", "")),
            "label": str(c.get("label", "")).upper().strip(),
            "evidence_quote": (str(eq) if eq not in (None, "", "null") else None),
        })
    return out[:MAX_CLAIMS]


def _correctness_from_claims(claims: list[dict]) -> tuple[int | None, dict]:
    """Deterministic faithfulness score from labeled claims.

    Returns ``(score_or_None, label_counts)``. ``score`` is None when nothing is
    checkable (T == 0), so the caller falls back to the judge's holistic correctness.
    """
    counts = {lbl: 0 for lbl in _CLAIM_LABELS}
    for c in claims:
        lbl = str(c.get("label", "")).upper().strip()
        if lbl in counts:
            counts[lbl] += 1
    checkable = counts["SUPPORTED"] + counts["NOT_IN_EVIDENCE"] + counts["CONTRADICTED"]
    if checkable == 0:
        return None, counts
    penalty = counts["NOT_IN_EVIDENCE"] + CONTRADICTION_WEIGHT * counts["CONTRADICTED"]
    ratio = penalty / checkable
    for threshold, score in CORRECTNESS_RATIO_BANDS:
        if ratio <= threshold:
            return score, counts
    return 1, counts


def _normalize_scores(parsed: dict) -> dict:
    """Coerce holistic dims to ints in [1,5]; derive correctness from claim labels."""
    out = {}
    for k in DEFAULT_SCORES:
        v = parsed.get(k, 0)
        try:
            vi = int(v)
        except (TypeError, ValueError):
            vi = 0
        out[k] = max(0, min(5, vi))

    # Correctness: deterministic from claims; the judge's holistic value is only a
    # fallback for responses that contain no checkable factual claims (T == 0).
    claims = _normalize_claims(parsed.get("claims"))
    derived, counts = _correctness_from_claims(claims)
    if derived is not None:
        out["correctness"] = derived
    elif out["correctness"] == 0:
        out["correctness"] = 5  # nothing checkable and no judge fallback → nothing wrong
    out["claims"] = claims
    out["claim_label_counts"] = counts
    out["correctness_rationale"] = str(parsed.get("correctness_rationale", ""))[:800]

    out["issues"] = parsed.get("issues", []) or []
    out["strengths"] = parsed.get("strengths", []) or []
    if not isinstance(out["issues"], list):
        out["issues"] = [str(out["issues"])]
    if not isinstance(out["strengths"], list):
        out["strengths"] = [str(out["strengths"])]
    out["issues"] = [str(s) for s in out["issues"]][:6]
    out["strengths"] = [str(s) for s in out["strengths"]][:4]
    return out


def _error_payload(issue: str, raw: str = "") -> dict:
    """Schema-consistent payload for judge invocation / parse failures."""
    return {
        **DEFAULT_SCORES,
        "claims": [],
        "claim_label_counts": {lbl: 0 for lbl in _CLAIM_LABELS},
        "correctness_rationale": "",
        "issues": [issue],
        "strengths": [],
        "raw": raw,
        "parse_error": True,
    }


async def judge_response(
    user_query: str,
    tool_results_summary: str,
    final_response: str,
    judge_focus: list[str] | None = None,
    conversation_context: str | None = None,
) -> dict:
    """Run the judge LLM and return normalized scores + claim verdicts + raw payload."""
    llm = get_judge_llm()

    focus_note = ""
    if judge_focus:
        focus_note = (
            "\n\n## Evaluation focus for this query\n"
            f"Be especially strict on: {', '.join(judge_focus)}.\n"
        )

    context_block = ""
    if conversation_context:
        context_block = f"## Prior conversation (for follow-up resolution)\n{conversation_context}\n\n"

    user_block = (
        f"## User question\n{user_query}\n\n"
        f"{context_block}"
        f"## Tool results (COMPLETE evidence the agent had)\n{tool_results_summary or '(no tool results)'}\n\n"
        f"## Agent final response\n{final_response}"
        f"{focus_note}"
    )

    raw = None
    for attempt in range(1, JUDGE_MAX_ATTEMPTS + 1):
        try:
            resp = await llm.ainvoke([
                SystemMessage(content=JUDGE_SYSTEM_PROMPT),
                HumanMessage(content=user_block),
            ])
            raw = to_text(resp.content)
            break
        except Exception as e:
            if attempt < JUDGE_MAX_ATTEMPTS and _is_retryable(e):
                await asyncio.sleep(JUDGE_RETRY_BASE_DELAY * (2 ** (attempt - 1)))
                continue
            return _error_payload(
                f"judge_invocation_failed after {attempt} attempt(s): "
                f"{type(e).__name__}: {e}"
            )

    parsed = _parse_judge_json(raw)
    if "error" in parsed:
        return _error_payload(
            f"judge_parse_failed: {parsed.get('error')}",
            raw=parsed.get("raw", raw)[:800],
        )

    norm = _normalize_scores(parsed)
    norm["raw"] = raw[:1500]
    norm["parse_error"] = False
    return norm
