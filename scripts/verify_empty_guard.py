"""Verify the empty-response guards.

A/B/C are deterministic stub tests (no network): they force Gemini's "empty
response" by feeding blank AIMessages and assert the retry recovers a real answer.
D is a live regression turn (needs WSL service-account creds) confirming a normal
sommelier+sourcing turn still streams a non-empty answer.

Run via WSL:  PYTHONPATH=. python3 scripts/verify_empty_guard.py
"""
import asyncio

from dotenv import load_dotenv
load_dotenv()

from langchain_core.messages import AIMessage, HumanMessage  # noqa: E402

import agent  # noqa: E402
import agents.react_subagent as react_subagent  # noqa: E402


class StubLLM:
    """Returns the scripted responses in order (repeats the last one)."""
    def __init__(self, responses):
        self._responses = responses
        self.calls = 0

    def bind_tools(self, tools):
        return self

    async def ainvoke(self, messages):
        r = self._responses[min(self.calls, len(self._responses) - 1)]
        self.calls += 1
        return r


def _txt(msg):
    c = msg.content
    if isinstance(c, list):
        return "".join(p.get("text", "") for p in c if isinstance(p, dict))
    return c or ""


PASS, FAIL = "✅ PASS", "❌ FAIL"


def test_is_blank():
    f = agent._is_blank_response
    cases = [
        (AIMessage(content=""), True),
        (AIMessage(content="   "), True),
        (AIMessage(content=[]), True),
        (AIMessage(content=[{"type": "text", "text": ""}]), True),
        (AIMessage(content="hi"), False),
        (AIMessage(content=[{"type": "text", "text": "hi"}]), False),
        (AIMessage(content="", tool_calls=[
            {"name": "x", "args": {}, "id": "1", "type": "tool_call"}]), False),
    ]
    ok = all(f(m) is exp for m, exp in cases)
    print(f"A. _is_blank_response truth table: {PASS if ok else FAIL}")
    return ok


async def test_orchestrator_retry():
    # empty, empty, then real → guard should retry twice and recover.
    stub = StubLLM([
        AIMessage(content=""),
        AIMessage(content=""),
        AIMessage(content="최종 답변입니다."),
    ])
    orig = agent.get_llm
    agent.get_llm = lambda *a, **k: stub
    try:
        out = await agent.orchestrator_node({"messages": [HumanMessage("스테이크 와인 추천")]})
    finally:
        agent.get_llm = orig
    msg = out["messages"][0]
    ok = _txt(msg) == "최종 답변입니다." and stub.calls == 3
    print(f"B. orchestrator_node retries empty→real: {PASS if ok else FAIL} "
          f"(invokes={stub.calls}, answer={_txt(msg)!r})")

    # All-empty → bounded (no infinite loop), gives up after 1+retries.
    stub2 = StubLLM([AIMessage(content="")])
    agent.get_llm = lambda *a, **k: stub2
    try:
        await agent.orchestrator_node({"messages": [HumanMessage("hi")]})
    finally:
        agent.get_llm = orig
    bounded = stub2.calls == 1 + agent.EMPTY_RESPONSE_RETRIES
    print(f"   bounded when always empty: {PASS if bounded else FAIL} "
          f"(invokes={stub2.calls}, expected={1 + agent.EMPTY_RESPONSE_RETRIES})")
    return ok and bounded


async def test_subagent_retry():
    stub = StubLLM([
        AIMessage(content=""),
        AIMessage(content="소믈리에 답변입니다."),
    ])
    orig = react_subagent.get_llm
    react_subagent.get_llm = lambda *a, **k: stub
    try:
        graph = react_subagent.build_react_subagent("sys prompt", [], max_rounds=3)
        final = await graph.ainvoke({"messages": [HumanMessage("hi")]})
    finally:
        react_subagent.get_llm = orig
    last = final["messages"][-1]
    ok = _txt(last) == "소믈리에 답변입니다." and stub.calls == 2
    print(f"C. sub-agent agent_node retries empty→real: {PASS if ok else FAIL} "
          f"(invokes={stub.calls}, answer={_txt(last)!r})")
    return ok


def _texts_from_chunk(chunk):
    content = getattr(chunk, "content", "")
    if isinstance(content, str):
        return [content] if content else []
    if isinstance(content, list):
        return [p.get("text", "") if isinstance(p, dict) else str(p) for p in content
                if (p.get("text") if isinstance(p, dict) else p)]
    return []


async def test_live_regression():
    from langgraph.checkpoint.memory import InMemorySaver
    graph = agent.build_graph(checkpointer=InMemorySaver())
    config = {"recursion_limit": 30, "configurable": {"thread_id": "verify-live"}}
    streamed = ""
    async for event in graph.astream_events(
        {"messages": [HumanMessage("스테이크에 어울리는 와인 추천해줘")]},
        config=config, version="v2",
    ):
        if event["event"] == "on_chat_model_stream" and \
           (event.get("metadata") or {}).get("langgraph_node") == "orchestrator":
            for t in _texts_from_chunk(event["data"]["chunk"]):
                streamed += t
    snap = await graph.aget_state(config)
    final = snap.values["messages"][-1]
    final_txt = _txt(final)
    ok = len(streamed) > 0 and len(final_txt) > 0
    print(f"D. live turn streams non-empty answer: {PASS if ok else FAIL} "
          f"(streamed={len(streamed)} chars, state_final={len(final_txt)} chars)")
    print(f"   preview: {streamed[:120]!r}")
    return ok


async def main():
    results = []
    results.append(test_is_blank())
    results.append(await test_orchestrator_retry())
    results.append(await test_subagent_retry())
    try:
        results.append(await test_live_regression())
    except Exception as e:
        print(f"D. live turn: ⚠️ SKIPPED/ERROR ({type(e).__name__}: {e})")
    print(f"\n{'='*50}\nRESULT: {sum(results)}/{len(results)} passed")


if __name__ == "__main__":
    asyncio.run(main())
