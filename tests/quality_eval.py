"""Main runner for BC Wine AI quality eval.

Run from the project root:

    python -m tests.quality_eval                          # full suite (~25 min)
    python -m tests.quality_eval --only INV,CRI           # category filter
    python -m tests.quality_eval --id INV-001             # single query
    python -m tests.quality_eval --dry-run                # first 2 queries only
    python -m tests.quality_eval --skip-judge             # deterministic only
    python -m tests.quality_eval --limit 5                # first N queries
    python -m tests.quality_eval --list                   # print all queries, exit
    python -m tests.quality_eval --skip-preflight         # skip credential checks

Outputs to tests/results/<YYYYMMDD-HHMMSS>/:
    results.json          # full structured data
    summary.md            # Claude-readable summary with TL;DR
    transcripts/<id>.md   # per-query full transcript

Ctrl-C is handled gracefully — partial results are written before exit so
nothing is lost on a long run.

The flow is:
  golden query → graph.ainvoke → capture state → deterministic metrics
                                              → LLM-as-judge (optional)
                                              → write transcript + result entry
After all queries: aggregate → summary.md.
"""

from __future__ import annotations

import argparse
import asyncio
import json
import os
import sys
import time
import traceback
from datetime import datetime, timezone
from pathlib import Path
from statistics import mean, median
from typing import Any
from uuid import uuid4

# Ensure project root is on sys.path so `from agent import ...` works
_PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))

from dotenv import load_dotenv  # noqa: E402

load_dotenv(_PROJECT_ROOT / ".env")

from agent import get_graph  # noqa: E402
from tests.golden_queries import GOLDEN_QUERIES, total_invocations  # noqa: E402
from tests.judge import judge_response  # noqa: E402
from tests.metrics import (  # noqa: E402
    collect_tool_results_text,
    collect_wine_context_text,
    count_distinct_critics_cited,
    count_distinct_stores_cited,
    extract_final_response,
    extract_tool_call_records,
    extract_tool_messages,
    hallucination_check,
    markdown_link_count,
    mention_check,
    output_contract_score,
    preferences_active_check,
    reference_resolution_check,
    summarize_tool_results,
    tool_orchestration_metrics,
)


# =====================================================================
# Per-turn invocation
# =====================================================================

async def invoke_turn(
    graph,
    thread_id: str,
    query: str,
    eval_id: str,
    prev_msg_count: int,
) -> tuple[dict, list, float, str]:
    """One graph.ainvoke. Returns (full_state, new_messages_for_this_turn, latency_s, error_str_or_empty)."""
    config = {
        "configurable": {"thread_id": thread_id},
        "tags": ["bc-wine-quality-eval"],
        "metadata": {"thread_id": thread_id, "eval_id": eval_id},
        "recursion_limit": 30,
    }
    inputs = {"messages": [("user", query)]}

    t0 = time.time()
    try:
        state = await graph.ainvoke(inputs, config=config)
        err = ""
    except Exception as e:
        latency = time.time() - t0
        return {}, [], latency, f"{type(e).__name__}: {e}\n{traceback.format_exc()}"
    latency = time.time() - t0

    all_msgs = state.get("messages", [])
    new_msgs = all_msgs[prev_msg_count:]
    return state, new_msgs, latency, err


# =====================================================================
# Metric assembly for a single turn
# =====================================================================

async def evaluate_turn(
    turn_expected: dict,
    full_state: dict,
    new_msgs: list,
    prev_state: dict | None,
    latency_s: float,
    error_str: str,
    skip_judge: bool,
) -> dict:
    """Compute all metrics for one turn. Returns a turn-result dict."""
    if error_str:
        return {
            "query": turn_expected.get("query", ""),
            "latency_s": round(latency_s, 2),
            "error": error_str,
            "tool_calls": [],
            "final_response": "",
            "metrics": {},
            "judge": None,
            "pass_summary": {"agent_completed": False},
        }

    scoped_state = {**full_state, "messages": new_msgs}

    tool_call_records = extract_tool_call_records(scoped_state)
    tool_messages = extract_tool_messages(scoped_state)
    # Build the supporting-text blob from BOTH the (post-compaction) ToolMessages
    # AND wine_context — compaction projects each ToolMessage down to top-N rows,
    # so facts the synthesizer drew from cumulative wine_context would otherwise
    # be falsely flagged as unsupported.
    tool_results_blob = collect_tool_results_text(tool_messages)
    wine_ctx_blob = collect_wine_context_text(full_state)
    support_blob = tool_results_blob + "\n" + wine_ctx_blob
    final_response = extract_final_response(scoped_state)

    orch = tool_orchestration_metrics(tool_call_records, turn_expected)
    hallu = hallucination_check(
        final_response,
        support_blob,
        turn_expected.get("hallucination_check_fields", []) or [],
    )
    stores_n, stores_hit = count_distinct_stores_cited(final_response)
    critics_n, critics_hit = count_distinct_critics_cited(final_response)
    n_links = markdown_link_count(final_response)
    contract = output_contract_score(final_response)
    mention = mention_check(
        final_response,
        turn_expected.get("must_mention", []) or [],
        turn_expected.get("must_not_mention", []) or [],
    )

    ref_resolution = None
    if turn_expected.get("must_reference_cached_wine") and prev_state is not None:
        ref_resolution = reference_resolution_check(full_state, prev_state, final_response)

    prefs_check = None
    if turn_expected.get("preferences_should_be_active"):
        prefs_check = preferences_active_check(
            full_state, turn_expected["preferences_should_be_active"]
        )

    judge_scores: dict | None = None
    if not skip_judge:
        tr_summary = summarize_tool_results(
            tool_messages,
            max_chars=6000,
            wine_context=full_state.get("wine_context") if isinstance(full_state, dict) else None,
        )
        judge_scores = await judge_response(
            user_query=turn_expected.get("query", ""),
            tool_results_summary=tr_summary,
            final_response=final_response,
            judge_focus=turn_expected.get("judge_focus"),
        )

    min_stores = int(turn_expected.get("min_distinct_stores_cited", 0) or 0)
    min_critics = int(turn_expected.get("min_distinct_critics_cited", 0) or 0)
    require_link = bool(turn_expected.get("require_markdown_link", False))
    pass_summary = {
        "agent_completed": True,
        "orchestration": orch["pass"],
        "hallucination": hallu["pass"],
        "mention": mention["pass"],
        "coverage_stores": stores_n >= min_stores,
        "coverage_critics": critics_n >= min_critics,
        "link_inclusion": (n_links >= 1) if require_link else True,
        "structure_min": contract["score_of_4"] >= 1,
    }
    if ref_resolution is not None:
        pass_summary["reference_resolution"] = ref_resolution["any_referenced"]
    if prefs_check is not None:
        pass_summary["preferences_active"] = prefs_check["pass"]

    return {
        "query": turn_expected.get("query", ""),
        "latency_s": round(latency_s, 2),
        "error": "",
        "tool_calls": tool_call_records,
        "tool_messages_count": len(tool_messages),
        "final_response": final_response,
        "metrics": {
            "orchestration": orch,
            "hallucination": hallu,
            "stores_cited": {"count": stores_n, "stores": stores_hit, "required_min": min_stores},
            "critics_cited": {"count": critics_n, "critics": critics_hit, "required_min": min_critics},
            "markdown_links": n_links,
            "output_contract": contract,
            "mention": mention,
            "reference_resolution": ref_resolution,
            "preferences_active": prefs_check,
        },
        "judge": judge_scores,
        "pass_summary": pass_summary,
    }


# =====================================================================
# Per-query runner (single + multi-turn)
# =====================================================================

async def run_query(graph, entry: dict, skip_judge: bool, console_prefix: str = "") -> dict:
    is_multi = "turns" in entry
    eval_id = entry["id"]
    thread_id = f"eval-{eval_id}-{uuid4().hex[:8]}"

    print(f"{console_prefix}▶ {eval_id} ({entry['category']})  thread={thread_id[:18]}…", flush=True)

    turn_results: list[dict] = []
    prev_state: dict | None = None
    prev_msg_count = 0

    if is_multi:
        for i, turn_expected in enumerate(entry["turns"]):
            full_state, new_msgs, latency, err = await invoke_turn(
                graph, thread_id, turn_expected["query"], eval_id, prev_msg_count
            )
            r = await evaluate_turn(
                turn_expected, full_state, new_msgs, prev_state, latency, err, skip_judge
            )
            r["turn_index"] = i
            turn_results.append(r)
            _print_turn_summary(console_prefix + "    ", i, r)

            # Always advance prev_msg_count when the checkpointer has any state,
            # so a partial-error turn doesn't pollute the next turn's slicing.
            if isinstance(full_state, dict) and full_state.get("messages"):
                prev_msg_count = len(full_state["messages"])
            if not err:
                prev_state = full_state
    else:
        full_state, new_msgs, latency, err = await invoke_turn(
            graph, thread_id, entry["query"], eval_id, 0
        )
        r = await evaluate_turn(entry, full_state, new_msgs, None, latency, err, skip_judge)
        r["turn_index"] = 0
        turn_results.append(r)
        _print_turn_summary(console_prefix + "  ", 0, r)

    return {
        "id": eval_id,
        "category": entry["category"],
        "type": "multi" if is_multi else "single",
        "thread_id": thread_id,
        "notes": entry.get("notes", ""),
        "turns": turn_results,
    }


def _print_turn_summary(prefix: str, idx: int, r: dict) -> None:
    if r.get("error"):
        print(f"{prefix}T{idx} ✗ ERROR ({r['error'].splitlines()[0][:80]})", flush=True)
        return
    ps = r["pass_summary"]
    flags = []
    for k, v in ps.items():
        flags.append(f"{k}={'✓' if v else '✗'}")
    judge = r.get("judge") or {}
    j_overall = judge.get("overall", "-")
    tools = [tc["name"] for tc in r.get("tool_calls", [])]
    print(
        f"{prefix}T{idx}  {r['latency_s']:>5.1f}s  judge={j_overall}/5  tools={tools[:6]}",
        flush=True,
    )
    fails = [k for k, v in ps.items() if not v]
    if fails:
        print(f"{prefix}      fails: {', '.join(fails)}", flush=True)


# =====================================================================
# Aggregation
# =====================================================================

def _flatten_turns(results: list[dict]) -> list[dict]:
    out = []
    for q in results:
        for t in q["turns"]:
            out.append({"id": q["id"], "category": q["category"], **t})
    return out


def aggregate(results: list[dict]) -> dict:
    turns = _flatten_turns(results)
    n_turns = len(turns)
    completed = [t for t in turns if not t.get("error")]

    judge_scores = {k: [] for k in ("relevance", "correctness", "helpfulness", "coherence", "harmlessness", "overall")}
    for t in completed:
        j = t.get("judge") or {}
        for k in judge_scores:
            v = j.get(k, 0)
            if isinstance(v, (int, float)) and v > 0:
                judge_scores[k].append(v)

    judge_avg = {k: round(mean(vs), 2) if vs else None for k, vs in judge_scores.items()}
    judge_n = {k: len(vs) for k, vs in judge_scores.items()}

    latencies = [t["latency_s"] for t in completed]
    if latencies:
        latencies_sorted = sorted(latencies)
        p95_idx = max(0, int(0.95 * len(latencies_sorted)) - 1)
        latency_stats = {
            "avg": round(mean(latencies), 2),
            "median": round(median(latencies), 2),
            "p95": round(latencies_sorted[p95_idx], 2),
            "max": round(max(latencies), 2),
        }
    else:
        latency_stats = {"avg": None, "median": None, "p95": None, "max": None}

    orch_pass_n = sum(1 for t in completed if t["metrics"]["orchestration"]["pass"])
    forbidden_violations = sum(
        1 for t in completed if t["metrics"]["orchestration"]["forbidden_called"]
    )
    limit_violations = sum(
        1 for t in completed if t["metrics"]["orchestration"]["limit_violations"]
    )
    precision_avg = round(mean([t["metrics"]["orchestration"]["precision"] for t in completed]), 3) if completed else None
    recall_avg = round(mean([t["metrics"]["orchestration"]["recall"] for t in completed]), 3) if completed else None
    f1_avg = round(mean([t["metrics"]["orchestration"]["f1"] for t in completed]), 3) if completed else None

    n_with_unsupported = sum(1 for t in completed if t["metrics"]["hallucination"]["total_unsupported"] > 0)
    total_unsupported_tokens = sum(t["metrics"]["hallucination"]["total_unsupported"] for t in completed)

    n_with_link = sum(1 for t in completed if t["metrics"]["markdown_links"] >= 1)

    stores_in_buyability = [
        t["metrics"]["stores_cited"]["count"]
        for t in completed
        if t["metrics"]["stores_cited"]["required_min"] >= 1
    ]
    critics_in_review = [
        t["metrics"]["critics_cited"]["count"]
        for t in completed
        if t["metrics"]["critics_cited"]["required_min"] >= 1
    ]

    structure_scores = [t["metrics"]["output_contract"]["score_of_4"] for t in completed]
    structure_avg = round(mean(structure_scores), 2) if structure_scores else None

    # Per-category breakdown
    by_cat: dict[str, dict] = {}
    for t in turns:
        cat = t["category"]
        bc = by_cat.setdefault(cat, {"n_turns": 0, "n_passed_all": 0, "judge_overall": []})
        bc["n_turns"] += 1
        if t.get("error"):
            continue
        ps = t["pass_summary"]
        if all(ps.values()):
            bc["n_passed_all"] += 1
        j = t.get("judge") or {}
        if isinstance(j.get("overall"), int) and j["overall"] > 0:
            bc["judge_overall"].append(j["overall"])
    for cat, bc in by_cat.items():
        bc["judge_overall_avg"] = round(mean(bc["judge_overall"]), 2) if bc["judge_overall"] else None
        bc["pass_rate"] = round(bc["n_passed_all"] / bc["n_turns"], 2) if bc["n_turns"] else 0
        del bc["judge_overall"]

    # Suspected hallucinations (collected for the round-trip Claude analysis)
    suspected_hallucinations = []
    for t in completed:
        h = t["metrics"]["hallucination"]
        if h["total_unsupported"] > 0:
            suspected_hallucinations.append({
                "id": t["id"],
                "category": t["category"],
                "turn_index": t.get("turn_index", 0),
                "unsupported": h["unsupported"],
                "query": t["query"],
            })

    # Top issues — automated TL;DR for the next-session Claude
    top_issues: list[str] = []
    if structure_avg is not None and structure_avg < 2.5:
        below = sum(1 for s in structure_scores if s < 2)
        top_issues.append(
            f"**Output structure 평균 {structure_avg}/4** — {below}/{len(structure_scores)} 응답이 마크다운 skeleton(Lead/Why/Where-to-buy 표/Pairing)을 부분 이상 미충족. "
            "`agent.py:273` `format_response_node` 가 no-op 인 게 원인일 가능성 — synthesis LLM call 활성화 검토."
        )
    if n_with_unsupported:
        top_issues.append(
            f"**Hallucination 의심 {n_with_unsupported}/{len(completed)} 응답** (총 unsupported 토큰 {total_unsupported_tokens}건). "
            "`prompts.py` Behavioral Rule 2 ('Never invent') 가 약하게 작동. 아래 Suspected Hallucinations 섹션 참조."
        )
    link_rate = n_with_link / len(completed) if completed else 0
    if link_rate < 0.5:
        top_issues.append(
            f"**Markdown 링크 포함률 {round(link_rate*100)}%** — `prompts.py` Behavioral Rule 11 (\"Always include links\") 가 거의 무시됨. "
            "프롬프트에서 우선순위를 더 명확히 하거나 합성 단계에서 강제 검증 필요."
        )
    if forbidden_violations:
        top_issues.append(
            f"**Forbidden tool 호출 {forbidden_violations}건** — 금지된 툴 호출 발생. `prompts.py` 의 'when to call' 트리거 어휘 강화 또는 negative example 추가 검토."
        )
    if limit_violations:
        top_issues.append(
            f"**Per-turn 호출 한도 초과 {limit_violations}건** — tavily(≤1) 초과. `prompts.py` 의 한도 문구를 더 강하게 표현 필요."
        )
    judge_relevance = judge_avg.get("relevance")
    if judge_relevance is not None and judge_relevance < 3.5:
        top_issues.append(
            f"**Judge 'relevance' 평균 {judge_relevance}/5** — 응답이 질문과 관련 없는 내용을 포함하거나 핵심을 벗어남. orchestrator 프롬프트에서 질문 재확인 단계 강화 필요."
        )
    judge_correctness = judge_avg.get("correctness")
    if judge_correctness is not None and judge_correctness < 3.5:
        top_issues.append(
            f"**Judge 'correctness' 평균 {judge_correctness}/5** — 사실 정확도가 낮음. `prompts.py` Behavioral Rule 2 ('Never invent') 강화 또는 tool 결과 외 주장 금지 규칙 추가 필요."
        )
    judge_coherence = judge_avg.get("coherence")
    if judge_coherence is not None and judge_coherence < 3.5:
        top_issues.append(
            f"**Judge 'coherence' 평균 {judge_coherence}/5** — 응답 내 논리적 일관성 부족. 응답 구조화 또는 synthesis 단계 개선 필요."
        )

    return {
        "n_queries": len(results),
        "n_turns": n_turns,
        "n_completed": len(completed),
        "n_errored": n_turns - len(completed),
        "judge_avg": judge_avg,
        "judge_n": judge_n,
        "latency": latency_stats,
        "orchestration": {
            "pass_rate": round(orch_pass_n / len(completed), 3) if completed else None,
            "precision_avg": precision_avg,
            "recall_avg": recall_avg,
            "f1_avg": f1_avg,
            "forbidden_violations_count": forbidden_violations,
            "limit_violations_count": limit_violations,
        },
        "hallucination": {
            "responses_with_unsupported": n_with_unsupported,
            "total_unsupported_tokens": total_unsupported_tokens,
            "rate": round(n_with_unsupported / len(completed), 3) if completed else None,
        },
        "coverage": {
            "avg_stores_when_buyability": round(mean(stores_in_buyability), 2) if stores_in_buyability else None,
            "avg_critics_when_reviews": round(mean(critics_in_review), 2) if critics_in_review else None,
            "link_inclusion_rate": round(link_rate, 3),
        },
        "structure_contract": {
            "avg_score_of_4": structure_avg,
            "distribution": {str(i): structure_scores.count(i) for i in range(5)} if structure_scores else {},
        },
        "by_category": by_cat,
        "suspected_hallucinations": suspected_hallucinations,
        "top_issues_for_next_session": top_issues,
    }


# =====================================================================
# Output rendering
# =====================================================================

def render_summary_md(meta: dict, agg: dict, results: list[dict]) -> str:
    lines: list[str] = []
    add = lines.append
    add(f"# BC Wine AI Quality Eval — {meta['timestamp']}")
    add("")
    add(f"- Model under test: `{meta['model']}`")
    add(f"- Judge model: `{meta['judge_model']}` (temperature=0)")
    add(f"- Total queries: **{agg['n_queries']}**  |  Total invocations: **{agg['n_turns']}**  |  Completed: **{agg['n_completed']}**  |  Errored: **{agg['n_errored']}**")
    add(f"- Run duration: **{meta['duration_s']:.1f}s** ({meta['duration_s']/60:.1f} min)")
    add("")

    add("## TL;DR — Top Issues for Next Session")
    add("")
    if not agg["top_issues_for_next_session"]:
        add("- No major issues auto-detected. Inspect per-query details below.")
    else:
        for i, issue in enumerate(agg["top_issues_for_next_session"], 1):
            add(f"{i}. {issue}")
    add("")

    add("## Aggregate Metrics")
    add("")
    add("| Dimension | Value |")
    add("|---|---|")
    add(f"| Tool-orchestration pass rate | {agg['orchestration']['pass_rate']} |")
    add(f"| Tool-orchestration F1 (avg) | {agg['orchestration']['f1_avg']} |")
    add(f"| Tool-orchestration precision (avg) | {agg['orchestration']['precision_avg']} |")
    add(f"| Tool-orchestration recall (avg) | {agg['orchestration']['recall_avg']} |")
    add(f"| Forbidden-tool violations | {agg['orchestration']['forbidden_violations_count']} |")
    add(f"| Per-turn limit violations | {agg['orchestration']['limit_violations_count']} |")
    add(f"| Hallucination rate (responses) | {agg['hallucination']['rate']} |")
    add(f"| Total unsupported tokens | {agg['hallucination']['total_unsupported_tokens']} |")
    j = agg["judge_avg"]
    add(f"| Judge — relevance | {j['relevance']} |")
    add(f"| Judge — correctness | {j['correctness']} |")
    add(f"| Judge — helpfulness | {j['helpfulness']} |")
    add(f"| Judge — coherence | {j['coherence']} |")
    add(f"| Judge — harmlessness | {j['harmlessness']} |")
    add(f"| Judge — overall | {j['overall']} |")
    lat = agg["latency"]
    add(f"| Latency avg | {lat['avg']}s |")
    add(f"| Latency median | {lat['median']}s |")
    add(f"| Latency p95 | {lat['p95']}s |")
    add(f"| Latency max | {lat['max']}s |")
    cov = agg["coverage"]
    add(f"| Avg distinct stores cited (buyability) | {cov['avg_stores_when_buyability']} |")
    add(f"| Avg distinct critics cited (review) | {cov['avg_critics_when_reviews']} |")
    add(f"| Markdown-link inclusion rate | {cov['link_inclusion_rate']} |")
    add(f"| Output-contract avg score | {agg['structure_contract']['avg_score_of_4']}/4 |")
    add("")

    add("## Per-Category Breakdown")
    add("")
    add("| Category | Turns | Pass-all rate | Judge overall avg |")
    add("|---|---|---|---|")
    for cat in sorted(agg["by_category"].keys()):
        bc = agg["by_category"][cat]
        add(f"| {cat} | {bc['n_turns']} | {bc['pass_rate']} | {bc.get('judge_overall_avg')} |")
    add("")

    add("## Suspected Hallucinations (Need Code Review)")
    add("")
    if not agg["suspected_hallucinations"]:
        add("- None flagged.")
    else:
        for h in agg["suspected_hallucinations"]:
            add(f"### {h['id']} (turn {h['turn_index']}) — {h['category']}")
            add(f"- **Query:** {h['query']}")
            for kind, toks in h["unsupported"].items():
                add(f"- **{kind} unsupported:** {', '.join(toks)}")
            add(f"- See: `transcripts/{h['id']}.md`")
            add("")
    add("")

    add("## Per-Query Detail")
    add("")
    add("| ID | Cat | Turn | Latency | Orch | Hallu | Cov-S | Cov-C | Link | Struct | Judge ovr | Notable Fail |")
    add("|---|---|---|---|---|---|---|---|---|---|---|---|")
    for q in results:
        for t in q["turns"]:
            if t.get("error"):
                add(f"| {q['id']} | {q['category']} | {t['turn_index']} | — | — | — | — | — | — | — | — | ERROR |")
                continue
            ps = t["pass_summary"]
            j = t.get("judge") or {}
            fails = [k for k, v in ps.items() if not v]
            short = ", ".join(fails)[:60]
            add(
                f"| {q['id']} | {q['category']} | {t['turn_index']} "
                f"| {t['latency_s']}s "
                f"| {'✓' if ps.get('orchestration') else '✗'} "
                f"| {'✓' if ps.get('hallucination') else '✗'} "
                f"| {t['metrics']['stores_cited']['count']}/{t['metrics']['stores_cited']['required_min']} "
                f"| {t['metrics']['critics_cited']['count']}/{t['metrics']['critics_cited']['required_min']} "
                f"| {t['metrics']['markdown_links']} "
                f"| {t['metrics']['output_contract']['score_of_4']}/4 "
                f"| {j.get('overall', '—')}/5 "
                f"| {short} |"
            )
    add("")

    add("## Suggested Code Targets (auto-derived)")
    add("")
    targets = _suggest_code_targets(agg)
    if not targets:
        add("- No high-confidence targets identified. Inspect per-query transcripts.")
    else:
        for t in targets:
            add(f"- {t}")
    add("")

    add("## Files in This Run")
    add("")
    add("- `results.json` — full structured data (machine-readable; load with `json.load`)")
    add("- `transcripts/<ID>.md` — per-query transcripts with tool I/O + final response + metrics")
    return "\n".join(lines)


def _suggest_code_targets(agg: dict) -> list[str]:
    targets = []
    if agg["structure_contract"]["avg_score_of_4"] is not None and agg["structure_contract"]["avg_score_of_4"] < 2.5:
        targets.append("`agent.py:273` — `format_response_node` is currently a no-op. Activate a synthesis LLM call using `SYNTHESIS_SYSTEM_PROMPT` from `prompts.py` to enforce the markdown skeleton.")
    if agg["hallucination"]["rate"] and agg["hallucination"]["rate"] > 0.05:
        targets.append("`prompts.py` Behavioral Rule 2 — strengthen 'Never invent' with explicit examples of what NOT to do (fabricated prices/scores).")
    if agg["coverage"]["link_inclusion_rate"] < 0.5:
        targets.append("`prompts.py` Behavioral Rule 11 — link inclusion is poorly followed. Move it earlier in the rules list, or add an output-format example.")
    if agg["orchestration"]["forbidden_violations_count"]:
        targets.append("`prompts.py` Tool Catalog — tighten 'when to call' triggers. Several forbidden tool calls observed.")
    if agg["orchestration"]["limit_violations_count"]:
        targets.append("`prompts.py` — per-turn call limits exceeded. Re-emphasize the '≤N per turn' constraints; consider adding a guard in `agent.py` to drop excess calls.")
    judge = agg["judge_avg"]
    if judge.get("correctness") is not None and judge["correctness"] < 3.5:
        targets.append("`prompts.py` Behavioral Rule 2 — strengthen 'Never invent' and require all claims to be grounded in tool results.")
    if judge.get("relevance") is not None and judge["relevance"] < 3.5:
        targets.append("`prompts.py` orchestrator system prompt — add instruction to re-read the user query and confirm all parts addressed before emitting final response.")
    if judge.get("coherence") is not None and judge["coherence"] < 3.5:
        targets.append("`prompts.py` — response coherence is low. Consider activating synthesis step or adding explicit structuring instructions.")
    return targets


def render_transcript_md(q: dict) -> str:
    lines = [f"# {q['id']} — {q['category']}"]
    lines.append("")
    if q.get("notes"):
        lines.append(f"_Notes:_ {q['notes']}")
        lines.append("")
    lines.append(f"- Thread ID: `{q['thread_id']}`")
    lines.append(f"- Turns: {len(q['turns'])}")
    lines.append("")

    for t in q["turns"]:
        idx = t.get("turn_index", 0)
        lines.append(f"---")
        lines.append(f"## Turn {idx}")
        lines.append("")
        lines.append(f"### Query")
        lines.append("")
        lines.append(f"> {t['query']}")
        lines.append("")
        if t.get("error"):
            lines.append("### ERROR")
            lines.append("")
            lines.append(f"```\n{t['error']}\n```")
            lines.append("")
            continue
        lines.append(f"### Tool Calls (in order)")
        lines.append("")
        if not t["tool_calls"]:
            lines.append("_(no tool calls)_")
        else:
            for i, tc in enumerate(t["tool_calls"], 1):
                args = json.dumps(tc.get("args", {}), default=str)
                lines.append(f"{i}. `{tc['name']}` args={args}")
        lines.append("")
        lines.append(f"### Final Response")
        lines.append("")
        lines.append("```markdown")
        lines.append(t["final_response"] or "(empty)")
        lines.append("```")
        lines.append("")
        lines.append(f"### Deterministic Metrics")
        lines.append("")
        lines.append("```json")
        lines.append(json.dumps(t["metrics"], indent=2, default=str))
        lines.append("```")
        lines.append("")
        lines.append(f"### Judge Scores")
        lines.append("")
        if t.get("judge"):
            lines.append("```json")
            j = dict(t["judge"])
            j.pop("raw", None)  # raw can be very long
            lines.append(json.dumps(j, indent=2, default=str))
            lines.append("```")
        else:
            lines.append("_(judge skipped)_")
        lines.append("")
        lines.append(f"### Pass Summary")
        lines.append("")
        for k, v in t["pass_summary"].items():
            lines.append(f"- {k}: {'✓ PASS' if v else '✗ FAIL'}")
        lines.append(f"- latency: {t['latency_s']}s")
        lines.append("")
    return "\n".join(lines)


# =====================================================================
# CLI
# =====================================================================

def _filter_queries(
    queries: list[dict],
    only: str | None,
    only_id: str | None,
    dry_run: bool,
    limit: int | None,
) -> list[dict]:
    if only_id:
        return [q for q in queries if q["id"] == only_id]
    if only:
        cats = {c.strip().upper() for c in only.split(",") if c.strip()}
        out = [q for q in queries if q["category"].upper() in cats]
    elif dry_run:
        out = queries[:2]
    else:
        out = list(queries)
    if limit is not None and limit > 0:
        out = out[:limit]
    return out


def _preflight_check() -> list[str]:
    """Soft check for credentials / common setup issues. Returns a list of
    human-readable warnings — empty list means everything looks fine. Never
    blocks; the eval still runs and individual tools degrade per their own
    error handling.
    """
    warnings: list[str] = []

    # .env file presence
    env_path = _PROJECT_ROOT / ".env"
    if not env_path.exists():
        warnings.append(
            f".env file not found at {env_path}. "
            "Auth-gated tools (Tavily) will return 'unavailable'."
        )

    # Vertex AI / Gemini ADC
    try:
        import google.auth  # type: ignore
        try:
            google.auth.default()
        except Exception as e:
            warnings.append(
                f"Vertex AI credentials not resolvable (`{type(e).__name__}: {e}`). "
                "Run `gcloud auth application-default login` before kicking off the eval."
            )
    except ImportError:
        warnings.append("google-auth not installed — cannot pre-check Vertex AI credentials.")

    # Per-tool env keys (warn-only)
    optional_keys = {
        "TAVILY_API_KEY": "Tavily web fallback",
    }
    missing = [(k, v) for k, v in optional_keys.items() if not os.environ.get(k)]
    if missing:
        for k, label in missing:
            warnings.append(f"{k} not set — {label} will be unavailable.")

    # Gismondi DB
    db_path = _PROJECT_ROOT / "data" / "wines.db"
    if not db_path.exists():
        warnings.append(
            f"Gismondi DB not built at {db_path}. Run `python build_db.py` first."
        )

    return warnings


def _print_query_list(queries: list[dict]) -> None:
    by_cat: dict[str, list[dict]] = {}
    for q in queries:
        by_cat.setdefault(q["category"], []).append(q)
    print(f"\nAvailable golden queries ({len(queries)} total, "
          f"{sum(len(q.get('turns', [None])) for q in queries)} invocations):\n")
    for cat in sorted(by_cat.keys()):
        rows = by_cat[cat]
        print(f"  [{cat}]  ({len(rows)} queries)")
        for q in rows:
            is_multi = "turns" in q
            if is_multi:
                first = q["turns"][0].get("query", "(no query)")
                tag = f"  ({len(q['turns'])} turns)"
            else:
                first = q.get("query", "(no query)")
                tag = ""
            print(f"    {q['id']:<14} {first[:72]}{tag}")
        print()


def _format_eta(seconds: float) -> str:
    if seconds < 60:
        return f"{seconds:.0f}s"
    m, s = divmod(int(seconds), 60)
    if m < 60:
        return f"{m}m{s:02d}s"
    h, m = divmod(m, 60)
    return f"{h}h{m:02d}m"


async def amain(args) -> int:
    if args.list:
        _print_query_list(GOLDEN_QUERIES)
        return 0

    selected = _filter_queries(
        GOLDEN_QUERIES, args.only, args.id, args.dry_run, args.limit,
    )
    if not selected:
        print("No queries matched filter. Available IDs:", flush=True)
        for q in GOLDEN_QUERIES:
            print(f"  {q['id']}  ({q['category']})", flush=True)
        return 2

    # Pre-flight credential / dep check (soft — warnings only, never blocks).
    if not args.skip_preflight:
        warns = _preflight_check()
        if warns:
            print("\n⚠  Pre-flight warnings (eval will still run, but some tools may degrade):", flush=True)
            for w in warns:
                print(f"   - {w}", flush=True)
            print("", flush=True)

    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    out_dir = _PROJECT_ROOT / "tests" / "results" / timestamp
    (out_dir / "transcripts").mkdir(parents=True, exist_ok=True)

    n_invocations = sum(len(q.get("turns", [None])) for q in selected)
    # Rough ETA: ~50s avg per invocation (with judge), ~30s without.
    eta_per = 50.0 if not args.skip_judge else 30.0
    est_total = n_invocations * eta_per

    print("=" * 78, flush=True)
    print(f"BC Wine AI Quality Eval", flush=True)
    print(f"Output dir:    {out_dir}", flush=True)
    print(f"Selected:      {len(selected)} queries ({n_invocations} invocations)", flush=True)
    print(f"Skip judge:    {args.skip_judge}", flush=True)
    print(f"Estimated:     ~{_format_eta(est_total)} "
          f"(at ~{eta_per:.0f}s/invocation; varies by tool latency)", flush=True)
    print("=" * 78, flush=True)

    graph = get_graph()

    started_at = datetime.now(timezone.utc)
    t0 = time.time()

    results: list[dict] = []
    interrupted = False
    for i, entry in enumerate(selected, 1):
        # Live ETA based on running average of completed queries.
        elapsed = time.time() - t0
        if i > 1 and results:
            avg = elapsed / (i - 1)
            remaining = avg * (len(selected) - i + 1)
            eta_str = f"  ETA ~{_format_eta(remaining)}"
        else:
            eta_str = ""
        prefix = f"[{i:>2}/{len(selected)}{eta_str}] "
        try:
            r = await run_query(graph, entry, args.skip_judge, console_prefix=prefix)
        except KeyboardInterrupt:
            interrupted = True
            print(f"\n⚠  Interrupted on {entry['id']} — saving partial results…", flush=True)
            break
        except Exception as e:
            print(f"{prefix}FATAL on {entry['id']}: {type(e).__name__}: {e}", flush=True)
            traceback.print_exc()
            r = {
                "id": entry["id"],
                "category": entry["category"],
                "type": "multi" if "turns" in entry else "single",
                "thread_id": "fatal-error",
                "notes": entry.get("notes", ""),
                "turns": [{
                    "turn_index": 0,
                    "query": entry.get("query", "(multi-turn)"),
                    "latency_s": 0,
                    "error": f"FATAL: {type(e).__name__}: {e}\n{traceback.format_exc()}",
                    "tool_calls": [],
                    "final_response": "",
                    "metrics": {},
                    "judge": None,
                    "pass_summary": {"agent_completed": False},
                }],
            }
        results.append(r)

        try:
            (out_dir / "transcripts" / f"{r['id']}.md").write_text(
                render_transcript_md(r), encoding="utf-8"
            )
        except Exception as e:
            print(f"{prefix}WARN: transcript write failed: {e}", flush=True)

    duration = time.time() - t0
    ended_at = datetime.now(timezone.utc)

    meta = {
        "timestamp": timestamp,
        "started_at": started_at.isoformat(),
        "ended_at": ended_at.isoformat(),
        "duration_s": duration,
        "model": os.environ.get("BC_WINE_MODEL", "gemini-3.5-flash"),
        "judge_model": "gemini-3.1-pro-preview (temp=0)",
        "n_selected": len(selected),
        "n_completed": len(results),
        "n_total_in_suite": len(GOLDEN_QUERIES),
        "interrupted": interrupted,
        "filters": {
            "only": args.only,
            "id": args.id,
            "dry_run": args.dry_run,
            "limit": args.limit,
            "skip_judge": args.skip_judge,
        },
    }
    agg = aggregate(results)

    (out_dir / "results.json").write_text(
        json.dumps({
            "run_metadata": meta,
            "aggregate": agg,
            "queries": results,
        }, indent=2, default=str),
        encoding="utf-8",
    )
    (out_dir / "summary.md").write_text(
        render_summary_md(meta, agg, results),
        encoding="utf-8",
    )

    print("", flush=True)
    print("=" * 78, flush=True)
    status = "Interrupted — partial results written" if interrupted else "Done"
    print(f"{status} in {duration:.1f}s ({duration/60:.1f} min). "
          f"Completed {len(results)}/{len(selected)} queries.", flush=True)
    print(f"Results: {out_dir / 'results.json'}", flush=True)
    print(f"Summary: {out_dir / 'summary.md'}", flush=True)
    print("=" * 78, flush=True)
    return 130 if interrupted else 0


def main() -> int:
    parser = argparse.ArgumentParser(
        description="BC Wine AI quality eval runner",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Examples:\n"
            "  python -m tests.quality_eval --list                  # see all queries\n"
            "  python -m tests.quality_eval --id INV-001            # one query\n"
            "  python -m tests.quality_eval --only INV,CRI          # category filter\n"
            "  python -m tests.quality_eval --dry-run --skip-judge  # quickest sanity\n"
            "  python -m tests.quality_eval --limit 5               # first 5 queries\n"
            "  python -m tests.quality_eval                         # full suite (~25 min)\n"
        ),
    )
    parser.add_argument("--only", help="Comma-separated category codes (e.g. INV,CRI)", default=None)
    parser.add_argument("--id", help="Run a single golden-query id (e.g. INV-001)", default=None)
    parser.add_argument("--dry-run", action="store_true", help="Run only the first 2 queries")
    parser.add_argument("--limit", type=int, default=None, help="Run only the first N queries after other filters")
    parser.add_argument("--list", action="store_true", help="Print all available queries (grouped by category) and exit")
    parser.add_argument("--skip-judge", action="store_true", help="Skip LLM-as-judge calls (deterministic metrics only — much faster)")
    parser.add_argument("--skip-preflight", action="store_true", help="Skip the env/credential pre-flight check")
    args = parser.parse_args()
    try:
        return asyncio.run(amain(args))
    except KeyboardInterrupt:
        # Shouldn't reach here normally — amain catches per-query interrupts
        # and writes partial results. This is a last-resort fallback.
        print("\n⚠  Interrupted before any results were written.", flush=True)
        return 130


if __name__ == "__main__":
    sys.exit(main())
