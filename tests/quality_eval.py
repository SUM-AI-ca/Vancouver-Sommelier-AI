"""Main runner for Vancouver Drinks AI quality eval (LLM-as-Judge only).

Run from the project root:

    python -m tests.quality_eval                          # full suite (~25 min)
    python -m tests.quality_eval --only INV,CRI           # category filter
    python -m tests.quality_eval --id INV-001             # single query
    python -m tests.quality_eval --dry-run                # first 2 queries only
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
  golden query → graph.ainvoke → capture state → LLM-as-Judge scoring
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
    extract_final_response,
    extract_tool_call_records,
    extract_tool_messages,
    summarize_tool_results,
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
# Per-turn evaluation (LLM-as-Judge only)
# =====================================================================

async def evaluate_turn(
    turn_expected: dict,
    full_state: dict,
    new_msgs: list,
    latency_s: float,
    error_str: str,
) -> dict:
    """Score one turn via LLM-as-Judge. Returns a turn-result dict."""
    if error_str:
        return {
            "query": turn_expected.get("query", ""),
            "latency_s": round(latency_s, 2),
            "error": error_str,
            "tool_calls": [],
            "final_response": "",
            "judge": None,
        }

    scoped_state = {**full_state, "messages": new_msgs}

    tool_call_records = extract_tool_call_records(scoped_state)
    tool_messages = extract_tool_messages(scoped_state)
    final_response = extract_final_response(scoped_state)

    tr_summary = summarize_tool_results(tool_messages)
    judge_scores = await judge_response(
        user_query=turn_expected.get("query", ""),
        tool_results_summary=tr_summary,
        final_response=final_response,
        judge_focus=turn_expected.get("judge_focus"),
    )

    return {
        "query": turn_expected.get("query", ""),
        "latency_s": round(latency_s, 2),
        "error": "",
        "tool_calls": tool_call_records,
        "tool_messages_count": len(tool_messages),
        "final_response": final_response,
        "judge": judge_scores,
    }


# =====================================================================
# Per-query runner (single + multi-turn)
# =====================================================================

async def run_query(graph, entry: dict, console_prefix: str = "") -> dict:
    is_multi = "turns" in entry
    eval_id = entry["id"]
    thread_id = f"eval-{eval_id}-{uuid4().hex[:8]}"

    print(f"{console_prefix}▶ {eval_id} ({entry['category']})  thread={thread_id[:18]}…", flush=True)

    turn_results: list[dict] = []
    prev_msg_count = 0

    if is_multi:
        for i, turn_expected in enumerate(entry["turns"]):
            full_state, new_msgs, latency, err = await invoke_turn(
                graph, thread_id, turn_expected["query"], eval_id, prev_msg_count
            )
            r = await evaluate_turn(turn_expected, full_state, new_msgs, latency, err)
            r["turn_index"] = i
            turn_results.append(r)
            _print_turn_summary(console_prefix + "    ", i, r)

            if isinstance(full_state, dict) and full_state.get("messages"):
                prev_msg_count = len(full_state["messages"])
    else:
        full_state, new_msgs, latency, err = await invoke_turn(
            graph, thread_id, entry["query"], eval_id, 0
        )
        r = await evaluate_turn(entry, full_state, new_msgs, latency, err)
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
    judge = r.get("judge") or {}
    j_overall = judge.get("overall", "-")
    tools = [tc["name"] for tc in r.get("tool_calls", [])]
    print(
        f"{prefix}T{idx}  {r['latency_s']:>5.1f}s  judge={j_overall}/5  tools={tools[:6]}",
        flush=True,
    )
    low_dims = [
        f"{k}={judge[k]}" for k in ("relevance", "correctness", "helpfulness", "coherence", "harmlessness")
        if isinstance(judge.get(k), int) and judge[k] < 3
    ]
    if low_dims:
        print(f"{prefix}      low: {', '.join(low_dims)}", flush=True)


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

    # Per-category breakdown
    by_cat: dict[str, dict] = {}
    for t in turns:
        cat = t["category"]
        bc = by_cat.setdefault(cat, {"n_turns": 0, "n_completed": 0, "judge_overall": []})
        bc["n_turns"] += 1
        if t.get("error"):
            continue
        bc["n_completed"] += 1
        j = t.get("judge") or {}
        if isinstance(j.get("overall"), int) and j["overall"] > 0:
            bc["judge_overall"].append(j["overall"])
    for cat, bc in by_cat.items():
        bc["judge_overall_avg"] = round(mean(bc["judge_overall"]), 2) if bc["judge_overall"] else None
        del bc["judge_overall"]

    # Collect judge issues across all turns
    all_issues: list[dict] = []
    for t in completed:
        j = t.get("judge") or {}
        issues = j.get("issues", [])
        if issues:
            all_issues.append({
                "id": t["id"],
                "category": t["category"],
                "turn_index": t.get("turn_index", 0),
                "query": t["query"],
                "overall": j.get("overall", 0),
                "issues": issues,
            })

    # Top issues — automated TL;DR for the next-session Claude
    top_issues: list[str] = []
    for dim in ("relevance", "correctness", "helpfulness", "coherence", "harmlessness"):
        avg = judge_avg.get(dim)
        if avg is not None and avg < 3.5:
            guidance = {
                "relevance": "응답이 질문과 관련 없는 내용을 포함하거나 핵심을 벗어남. orchestrator 프롬프트에서 질문 재확인 단계 강화 필요.",
                "correctness": "사실 정확도가 낮음. `prompts.py` 'Never invent' 규칙 강화 및 tool 결과 외 주장 금지 검토.",
                "helpfulness": "응답의 실행 가능성(actionability) 부족. 구체적인 제품, 가격, 구매처 포함 유도 필요.",
                "coherence": "응답 내 논리적 일관성 부족. 응답 구조화 또는 synthesis 단계 개선 필요.",
                "harmlessness": "부적절한 음주 권장 또는 비전문적 톤 감지. 프롬프트 안전 규칙 강화 필요.",
            }
            top_issues.append(f"**Judge '{dim}' 평균 {avg}/5** — {guidance[dim]}")

    n_low = sum(1 for t in completed if (t.get("judge") or {}).get("overall", 5) < 3)
    if n_low:
        top_issues.append(
            f"**Overall < 3 응답 {n_low}/{len(completed)}건** — 아래 Per-Query Detail에서 개별 이슈 확인 필요."
        )

    return {
        "n_queries": len(results),
        "n_turns": n_turns,
        "n_completed": len(completed),
        "n_errored": n_turns - len(completed),
        "judge_avg": judge_avg,
        "judge_n": judge_n,
        "latency": latency_stats,
        "by_category": by_cat,
        "judge_issues": all_issues,
        "top_issues_for_next_session": top_issues,
    }


# =====================================================================
# Output rendering
# =====================================================================

def render_summary_md(meta: dict, agg: dict, results: list[dict]) -> str:
    lines: list[str] = []
    add = lines.append
    add(f"# Vancouver Drinks AI Quality Eval — {meta['timestamp']}")
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

    add("## Judge Scores (LLM-as-Judge)")
    add("")
    add("| Dimension | Average | N |")
    add("|---|---|---|")
    j = agg["judge_avg"]
    jn = agg["judge_n"]
    for dim in ("relevance", "correctness", "helpfulness", "coherence", "harmlessness", "overall"):
        add(f"| {dim} | {j[dim]} | {jn[dim]} |")
    add("")

    add("## Latency")
    add("")
    add(f"| Stat | Value |")
    add(f"|---|---|")
    lat = agg["latency"]
    add(f"| avg | {lat['avg']}s |")
    add(f"| median | {lat['median']}s |")
    add(f"| p95 | {lat['p95']}s |")
    add(f"| max | {lat['max']}s |")
    add("")

    add("## Per-Category Breakdown")
    add("")
    add("| Category | Turns | Completed | Judge overall avg |")
    add("|---|---|---|---|")
    for cat in sorted(agg["by_category"].keys()):
        bc = agg["by_category"][cat]
        add(f"| {cat} | {bc['n_turns']} | {bc['n_completed']} | {bc.get('judge_overall_avg')} |")
    add("")

    add("## Per-Query Detail")
    add("")
    add("| ID | Cat | Turn | Latency | Rel | Corr | Help | Coh | Harm | Ovr | Issues |")
    add("|---|---|---|---|---|---|---|---|---|---|---|")
    for q in results:
        for t in q["turns"]:
            if t.get("error"):
                add(f"| {q['id']} | {q['category']} | {t['turn_index']} | — | — | — | — | — | — | — | ERROR |")
                continue
            j = t.get("judge") or {}
            issues_list = j.get("issues", [])
            short = "; ".join(issues_list)[:80] if issues_list else ""
            add(
                f"| {q['id']} | {q['category']} | {t['turn_index']} "
                f"| {t['latency_s']}s "
                f"| {j.get('relevance', '—')} "
                f"| {j.get('correctness', '—')} "
                f"| {j.get('helpfulness', '—')} "
                f"| {j.get('coherence', '—')} "
                f"| {j.get('harmlessness', '—')} "
                f"| {j.get('overall', '—')} "
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
    add("- `transcripts/<ID>.md` — per-query transcripts with tool I/O + final response + judge scores")
    return "\n".join(lines)


def _suggest_code_targets(agg: dict) -> list[str]:
    targets = []
    judge = agg["judge_avg"]
    if judge.get("correctness") is not None and judge["correctness"] < 3.5:
        targets.append("`prompts.py` — correctness 낮음. 'Never invent' 규칙 강화 및 tool 결과 외 주장 금지 검토.")
    if judge.get("relevance") is not None and judge["relevance"] < 3.5:
        targets.append("`prompts.py` — relevance 낮음. orchestrator 프롬프트에서 질문 재확인 단계 강화 필요.")
    if judge.get("helpfulness") is not None and judge["helpfulness"] < 3.5:
        targets.append("`prompts.py` — helpfulness 낮음. 응답의 실행 가능성(actionability) 개선 필요.")
    if judge.get("coherence") is not None and judge["coherence"] < 3.5:
        targets.append("`prompts.py` — coherence 낮음. 응답 구조화 또는 synthesis 단계 개선 필요.")
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
        lines.append(f"### Judge Scores")
        lines.append("")
        if t.get("judge"):
            lines.append("```json")
            j = dict(t["judge"])
            j.pop("raw", None)
            lines.append(json.dumps(j, indent=2, default=str))
            lines.append("```")
        else:
            lines.append("_(judge error)_")
        lines.append("")
        lines.append(f"### Latency")
        lines.append("")
        lines.append(f"- {t['latency_s']}s")
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
    """Soft check for credentials / common setup issues."""
    warnings: list[str] = []

    env_path = _PROJECT_ROOT / ".env"
    if not env_path.exists():
        warnings.append(f".env file not found at {env_path}.")

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
    eta_per = 50.0
    est_total = n_invocations * eta_per

    print("=" * 78, flush=True)
    print(f"Vancouver Drinks AI Quality Eval (LLM-as-Judge)", flush=True)
    print(f"Output dir:    {out_dir}", flush=True)
    print(f"Selected:      {len(selected)} queries ({n_invocations} invocations)", flush=True)
    print(f"Estimated:     ~{_format_eta(est_total)} "
          f"(at ~{eta_per:.0f}s/invocation; varies by tool latency)", flush=True)
    print("=" * 78, flush=True)

    graph = get_graph()

    started_at = datetime.now(timezone.utc)
    t0 = time.time()

    results: list[dict] = []
    interrupted = False
    for i, entry in enumerate(selected, 1):
        elapsed = time.time() - t0
        if i > 1 and results:
            avg = elapsed / (i - 1)
            remaining = avg * (len(selected) - i + 1)
            eta_str = f"  ETA ~{_format_eta(remaining)}"
        else:
            eta_str = ""
        prefix = f"[{i:>2}/{len(selected)}{eta_str}] "
        try:
            r = await run_query(graph, entry, console_prefix=prefix)
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
                    "judge": None,
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
        description="Vancouver Drinks AI quality eval (LLM-as-Judge)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Examples:\n"
            "  python -m tests.quality_eval --list                  # see all queries\n"
            "  python -m tests.quality_eval --id INV-001            # one query\n"
            "  python -m tests.quality_eval --only INV,CRI          # category filter\n"
            "  python -m tests.quality_eval --dry-run               # quickest sanity (2 queries)\n"
            "  python -m tests.quality_eval --limit 5               # first 5 queries\n"
            "  python -m tests.quality_eval                         # full suite (~25 min)\n"
        ),
    )
    parser.add_argument("--only", help="Comma-separated category codes (e.g. INV,CRI)", default=None)
    parser.add_argument("--id", help="Run a single golden-query id (e.g. INV-001)", default=None)
    parser.add_argument("--dry-run", action="store_true", help="Run only the first 2 queries")
    parser.add_argument("--limit", type=int, default=None, help="Run only the first N queries after other filters")
    parser.add_argument("--list", action="store_true", help="Print all available queries (grouped by category) and exit")
    parser.add_argument("--skip-preflight", action="store_true", help="Skip the env/credential pre-flight check")
    args = parser.parse_args()
    try:
        return asyncio.run(amain(args))
    except KeyboardInterrupt:
        print("\n⚠  Interrupted before any results were written.", flush=True)
        return 130


if __name__ == "__main__":
    sys.exit(main())
