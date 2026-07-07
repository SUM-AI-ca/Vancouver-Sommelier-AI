"""Production Cloud SQL checkpointer — end-to-end smoke test.

Exercises the DB-backed conversation persistence of the LIVE service by driving
the same public path a browser uses (Cloudflare Pages worker → Cloud Run). No
secrets needed: the worker injects X-Proxy-Secret, and Turnstile is off in prod.

What it checks (each prints PASS/FAIL):
  1. health        GET  /api/health                      → service is up
  2. session       POST /api/session                     → fresh thread_id
  3. continuity    two /api/chat turns on one thread      → turn-2 recalls a
                   distinctive budget set in turn-1  ⇒ checkpoint PERSISTED &
                   READ BACK from Postgres (the heart of the DB feature)
  4. forget        POST /api/session/{id}/end, then a 3rd turn on the same
                   thread → the budget is GONE  ⇒ adelete_thread worked
  5. cleanup-guard POST {run.app}/internal/cleanup with no secret → 403
                   (verifies the abandoned-session sweeper's auth gate)

Run:
    python -m scripts.db_e2e_smoke
    DB_E2E_BASE=http://localhost:8080 python -m scripts.db_e2e_smoke   # local app

Exit code 0 = all critical checks passed, 1 = a critical check failed.
"""

import asyncio
import json
import os
import sys

import httpx

# Korean answers + ✓/✗ marks must survive the Windows console (cp1252 default).
for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8", errors="replace")  # type: ignore[attr-defined]
    except Exception:
        pass

BASE = os.getenv("DB_E2E_BASE", "https://wineaiagent.com").rstrip("/")
# Direct Cloud Run URL for the /internal/* path (NOT proxied by the worker, which
# only forwards /api/ and /mcp). Used solely for the no-auth 403 guard check.
RUNAPP = os.getenv(
    "DB_E2E_RUNAPP",
    "https://bc-wine-agent-135257828500.us-west1.run.app",
).rstrip("/")

# A deliberately odd budget so a correct turn-2 recall can't be a lucky guess.
BUDGET = "37"

TIMEOUT = httpx.Timeout(connect=15.0, read=240.0, write=30.0, pool=30.0)

_results: list[tuple[str, bool, str]] = []


def record(name: str, ok: bool, detail: str = "") -> None:
    _results.append((name, ok, detail))
    mark = "PASS" if ok else "FAIL"
    print(f"  [{mark}] {name}" + (f" — {detail}" if detail else ""))


async def chat_turn(client: httpx.AsyncClient, thread_id: str, message: str) -> dict:
    """Send one /api/chat turn, consume the SSE stream, and return a summary.

    Mirrors the frontend: tokens carry a run_id and the UI clears prior partial
    text whenever the run_id changes, so the user-facing answer is the LAST
    run_id's accumulated text. Also captures any clarification question and the
    list of tools the agent invoked.
    """
    by_run: dict[str, list[str]] = {}
    run_order: list[str] = []
    tools: list[str] = []
    clarification = None
    error = None

    async with client.stream(
        "POST", f"{BASE}/api/chat",
        json={"thread_id": thread_id, "message": message},
    ) as resp:
        if resp.status_code != 200:
            body = (await resp.aread()).decode("utf-8", "replace")[:200]
            return {"status": resp.status_code, "answer": "", "tools": [],
                    "clarification": None, "error": f"HTTP {resp.status_code}: {body}"}
        async for line in resp.aiter_lines():
            if not line.startswith("data:"):
                continue
            try:
                ev = json.loads(line[5:].strip())
            except json.JSONDecodeError:
                continue
            t = ev.get("type")
            if t == "token":
                rid = str(ev.get("run_id"))
                if rid not in by_run:
                    by_run[rid] = []
                    run_order.append(rid)
                by_run[rid].append(ev.get("text", ""))
            elif t == "tool_start":
                tools.append(ev.get("tool", "?"))
            elif t == "clarification_request":
                clarification = ev.get("question", "")
            elif t == "error":
                error = ev.get("message", "unknown")
            elif t == "done":
                break

    answer = "".join(by_run[run_order[-1]]) if run_order else ""
    return {"status": 200, "answer": answer, "tools": tools,
            "clarification": clarification, "error": error}


async def main() -> int:
    print(f"Target: {BASE}\n")
    async with httpx.AsyncClient(timeout=TIMEOUT, follow_redirects=True) as client:
        # 1. health ------------------------------------------------------------
        try:
            r = await client.get(f"{BASE}/api/health")
            record("health", r.status_code == 200 and r.json().get("ok") is True,
                   f"status={r.status_code}")
        except Exception as e:
            record("health", False, repr(e))

        # 2. session create ----------------------------------------------------
        thread_id = None
        try:
            r = await client.post(f"{BASE}/api/session")
            thread_id = r.json().get("thread_id")
            record("session-create", bool(thread_id), f"thread_id={thread_id}")
        except Exception as e:
            record("session-create", False, repr(e))
        if not thread_id:
            print("\nCannot continue without a thread_id.")
            return 1

        # 3. continuity: turn-1 sets a budget, turn-2 must recall it ------------
        print("\n  turn-1 (set budget): sending…")
        t1 = await chat_turn(
            client, thread_id,
            f"드라이한 BC 레드 와인을 찾고 있어. 예산은 정확히 {BUDGET}달러야. 한 병 추천해줘.",
        )
        print(f"    tools={t1['tools']} answer[:120]={t1['answer'][:120]!r}"
              + (f" ERROR={t1['error']}" if t1["error"] else ""))
        record("turn-1", t1["status"] == 200 and bool(t1["answer"] or t1["clarification"]),
               t1["error"] or f"{len(t1['answer'])} chars")

        print("\n  turn-2 (recall budget): sending…")
        t2 = await chat_turn(
            client, thread_id,
            "방금 내가 말한 예산이 정확히 얼마였는지 숫자만 다시 알려줘. 그 예산 안에서 이어가자.",
        )
        recalled = BUDGET in (t2["answer"] or "")
        print(f"    answer[:200]={t2['answer'][:200]!r}")
        record("continuity (turn-2 recalls budget)", recalled,
               f"'{BUDGET}' {'found' if recalled else 'NOT found'} in recall answer")

        # 4. forget: end the session, then a 3rd turn must NOT recall ----------
        try:
            r = await client.post(f"{BASE}/api/session/{thread_id}/end")
            record("session-end", r.status_code == 200, f"status={r.status_code}")
        except Exception as e:
            record("session-end", False, repr(e))

        print("\n  turn-3 (after /end — should NOT recall): sending…")
        t3 = await chat_turn(
            client, thread_id,
            "방금 내가 말한 예산이 정확히 얼마였는지 숫자만 다시 알려줘.",
        )
        print(f"    answer[:200]={t3['answer'][:200]!r}")
        forgot = BUDGET not in (t3["answer"] or "")
        record("forget (turn-3 lost budget after /end)", forgot,
               f"'{BUDGET}' {'absent (forgotten)' if forgot else 'STILL present — delete failed?'}")

        # 5. cleanup auth guard (direct run.app; not proxied) ------------------
        try:
            r = await client.post(f"{RUNAPP}/internal/cleanup")
            record("cleanup-guard (no secret → 403)", r.status_code == 403,
                   f"status={r.status_code}")
        except Exception as e:
            record("cleanup-guard (no secret → 403)", False, repr(e))

    # summary -----------------------------------------------------------------
    print("\n" + "=" * 60)
    passed = sum(1 for _, ok, _ in _results if ok)
    print(f"SUMMARY: {passed}/{len(_results)} checks passed")
    for name, ok, detail in _results:
        print(f"  {'✓' if ok else '✗'} {name}")

    # Critical checks whose failure means the DB feature is broken.
    critical = {"health", "session-create", "turn-1",
                "continuity (turn-2 recalls budget)",
                "forget (turn-3 lost budget after /end)"}
    failed_critical = [n for n, ok, _ in _results if n in critical and not ok]
    if failed_critical:
        print(f"\nCRITICAL FAILURES: {failed_critical}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(asyncio.run(main()))
