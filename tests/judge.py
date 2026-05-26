"""LLM-as-Judge for BC Wine AI quality eval.

Same model as the agent (Gemini 3.5 Flash) but temperature=0.0.
Scores responses on 6 dimensions: accuracy / citation / completeness / style / helpfulness / structure.

Note: self-judging has mild favorable bias, but the goal is relative regression
tracking, not absolute scoring — same-model + temp=0 is documented as the
canonical setup in AGENT_DESIGN.md §16.3.
"""

from __future__ import annotations

import json
import re

from langchain_core.messages import HumanMessage, SystemMessage

from models import get_llm
from tests.metrics import to_text


JUDGE_SYSTEM_PROMPT = """\
You are a strict evaluator for a BC Wine AI Agent's response.

You will see:
1. The user's question.
2. A compact summary of the tool results the agent received.
3. The agent's final response.

Score the response on each dimension from 1 (very poor) to 5 (excellent).
Be strict and specific. Lower scores are appropriate when the response cuts corners,
hallucinates facts, omits requested information, or fails the markdown skeleton.

Dimensions:

- **accuracy**: Every factual claim (price, score, vintage, winery, region) is
  supported by the tool results OR is general knowledge that a sommelier would
  know without searching. Fabricated facts → 1.

- **citation**: Critics are named when reviews are cited (e.g., "John Szabo MS rated
  it 93"); stores are named when prices are cited ("BC Liquor: $29.99"). Vague
  attributions ("critics say", "available in stores") → low score.

- **completeness**: Addresses every distinct part of the user's question. If the
  user asks "where to buy AND how much", a response that gives only one is incomplete.
  For pairing questions, includes WHY the pairing works.

- **style**: Clear, concise English; no rambling. For beginners, jargon is explained.
  For sommeliers, technical depth is appropriate. Pacing matches the question's complexity.

- **helpfulness**: Actionable — user can act on the answer (knows what to buy, where,
  and why). For off-topic / refusal cases: gracefully redirects without being curt.

- **structure**: Follows the markdown skeleton when appropriate:
    Lead sentence → **Why this wine** section → **Where to buy** table → Pairing note.
  For non-recommendation responses (educational, off-topic), structure should be
  appropriate to the question (don't penalize for missing a table when the user
  asked a definition question).

Also extract:
- **issues**: 1–4 short critique bullets, each one sentence.
- **strengths**: 0–2 short positive bullets.

Return STRICT JSON only, no markdown fences, no preamble:

{
  "accuracy": <int 1-5>,
  "citation": <int 1-5>,
  "completeness": <int 1-5>,
  "style": <int 1-5>,
  "helpfulness": <int 1-5>,
  "structure": <int 1-5>,
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
    "accuracy": 0, "citation": 0, "completeness": 0,
    "style": 0, "helpfulness": 0, "structure": 0,
    "overall": 0,
}


def _normalize_scores(parsed: dict) -> dict:
    """Coerce dimension values to ints in [1,5]; missing → 0."""
    out = {}
    for k in DEFAULT_SCORES:
        v = parsed.get(k, 0)
        try:
            vi = int(v)
        except (TypeError, ValueError):
            vi = 0
        out[k] = max(0, min(5, vi))
    out["issues"] = parsed.get("issues", []) or []
    out["strengths"] = parsed.get("strengths", []) or []
    if not isinstance(out["issues"], list):
        out["issues"] = [str(out["issues"])]
    if not isinstance(out["strengths"], list):
        out["strengths"] = [str(out["strengths"])]
    out["issues"] = [str(s) for s in out["issues"]][:6]
    out["strengths"] = [str(s) for s in out["strengths"]][:4]
    return out


async def judge_response(
    user_query: str,
    tool_results_summary: str,
    final_response: str,
    judge_focus: list[str] | None = None,
) -> dict:
    """Run the judge LLM and return normalized scores + raw payload."""
    llm = get_llm(temperature=0.0)

    focus_note = ""
    if judge_focus:
        focus_note = (
            "\n\n## Evaluation focus for this query\n"
            f"Be especially strict on: {', '.join(judge_focus)}.\n"
        )

    user_block = (
        f"## User question\n{user_query}\n\n"
        f"## Tool results summary\n{tool_results_summary or '(no tool results)'}\n\n"
        f"## Agent final response\n{final_response}"
        f"{focus_note}"
    )

    try:
        resp = await llm.ainvoke([
            SystemMessage(content=JUDGE_SYSTEM_PROMPT),
            HumanMessage(content=user_block),
        ])
        raw = to_text(resp.content)
    except Exception as e:
        return {
            **DEFAULT_SCORES,
            "issues": [f"judge_invocation_failed: {type(e).__name__}: {e}"],
            "strengths": [],
            "raw": "",
            "parse_error": True,
        }

    parsed = _parse_judge_json(raw)
    if "error" in parsed:
        return {
            **DEFAULT_SCORES,
            "issues": [f"judge_parse_failed: {parsed.get('error')}"],
            "strengths": [],
            "raw": parsed.get("raw", raw)[:800],
            "parse_error": True,
        }

    norm = _normalize_scores(parsed)
    norm["raw"] = raw[:1500]
    norm["parse_error"] = False
    return norm
