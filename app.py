"""FastAPI backend — SSE chat endpoint, session management, static file serving."""

import json
import logging
import os
import uuid

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.responses import FileResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
from langgraph.types import Command
from pydantic import BaseModel

from agent import get_graph
from validation import validate_query

# .env must load BEFORE langchain/langgraph reads tracing env vars at import-time
# downstream. agent.py is already imported above, but its tracing decisions defer
# to env-var lookups at call-time (via langsmith.utils.tracing_is_enabled), so
# loading here is still effective.
load_dotenv()

log = logging.getLogger("bc-wine-agent")
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(name)s %(levelname)s %(message)s")


def _log_langsmith_status() -> None:
    """Log whether LangSmith tracing is wired up so misconfig is caught at boot."""
    tracing = (os.getenv("LANGSMITH_TRACING") or os.getenv("LANGCHAIN_TRACING_V2") or "").lower() == "true"
    api_key = os.getenv("LANGSMITH_API_KEY") or os.getenv("LANGCHAIN_API_KEY") or ""
    project = os.getenv("LANGSMITH_PROJECT") or os.getenv("LANGCHAIN_PROJECT") or "default"
    endpoint = os.getenv("LANGSMITH_ENDPOINT") or os.getenv("LANGCHAIN_ENDPOINT") or "https://api.smith.langchain.com"
    if tracing and api_key:
        log.info("LangSmith tracing ENABLED — project=%s endpoint=%s", project, endpoint)
    elif tracing and not api_key:
        log.warning("LangSmith tracing flag is set but no API key — traces will NOT be sent")
    else:
        log.info("LangSmith tracing disabled (set LANGSMITH_TRACING=true + LANGSMITH_API_KEY to enable)")


_log_langsmith_status()

app = FastAPI(title="BC Wine AI Agent")

_graph = None


def _get_graph():
    global _graph
    if _graph is None:
        _graph = get_graph()
    return _graph


class ChatRequest(BaseModel):
    thread_id: str
    message: str


class SessionResponse(BaseModel):
    thread_id: str


def sse(payload: dict) -> str:
    return f"data: {json.dumps(payload)}\n\n"


def _summarize_tool_output(output) -> list[dict]:
    """Extract a compact preview from a tool's JSON output so the frontend can
    render an expandable dropdown showing what the tool actually found.

    Returns a list of result rows, each shaped like:
        {"title": "...", "subtitle": "...", "url": "..." | None}

    Tool outputs are JSON strings produced by the @tool wrappers — they look
    like {"status": "ok", "tool": "search_X", "results": [...]} where each
    result item's fields depend on the source.
    """
    if output is None:
        return []
    if hasattr(output, "content"):  # ToolMessage from LangGraph
        output = output.content
    if not isinstance(output, str):
        return []
    try:
        data = json.loads(output)
    except (json.JSONDecodeError, TypeError):
        return []
    if not isinstance(data, dict):
        return []

    tool = data.get("tool", "")
    results = data.get("results") if isinstance(data.get("results"), list) else []

    rows: list[dict] = []
    for r in results:
        if not isinstance(r, dict):
            continue
        # Each store / critic returns slightly different fields — coalesce.
        title = (
            r.get("name") or r.get("title") or r.get("display_name")
            or r.get("wine_name") or "Untitled"
        )
        price = r.get("current_price") or r.get("price") or r.get("sale_price")
        score = r.get("score_100") or r.get("rating") or r.get("rating_display")
        subtitle_bits = []
        if r.get("producer"):
            subtitle_bits.append(str(r["producer"]))
        if r.get("region"):
            subtitle_bits.append(str(r["region"]))
        if price is not None:
            # WineAlign scrapes the price already prefixed with "$", BC Liquor
            # returns a bare number. Normalize so we never end up with "$$".
            p_str = str(price).strip()
            for prefix in ("CA$", "C$", "CAD", "USD"):
                if p_str.upper().startswith(prefix):
                    p_str = p_str[len(prefix):].strip()
                    break
            p_str = p_str.lstrip("$").strip()
            if p_str:
                subtitle_bits.append(f"${p_str}")
        if score is not None:
            subtitle_bits.append(f"{score} pts")
        url = (
            r.get("product_url") or r.get("url") or r.get("wine_url")
            or r.get("review_url")
        )
        rows.append({
            "title": str(title)[:160],
            "subtitle": " · ".join(subtitle_bits)[:200],
            "url": url if isinstance(url, str) else None,
        })

    # Tavily and reasoning_pair_wine don't have "results" — surface their answer.
    # These return long markdown prose; the frontend renders the body as
    # markdown (markdown=True) instead of clipping it as a plain subtitle.
    if not rows:
        if tool == "search_tavily" and data.get("answer"):
            rows.append({
                "title": "Web answer",
                "body": str(data["answer"])[:4000],
                "url": None,
                "markdown": True,
            })
        elif tool == "reasoning_pair_wine" and data.get("recommendation"):
            rows.append({
                "title": "Sommelier reasoning",
                "body": str(data["recommendation"])[:4000],
                "url": None,
                "markdown": True,
            })
    return rows


@app.post("/api/session")
async def create_session() -> SessionResponse:
    return SessionResponse(thread_id=str(uuid.uuid4()))


def _extract_token_texts(chunk) -> list[str]:
    """Pull a list of text fragments out of a chat-model stream chunk.

    Gemini sometimes emits a list of typed parts ({type, text, ...}); other
    providers emit a plain string. Empty/non-text parts are skipped.
    """
    content = chunk.content if hasattr(chunk, "content") else ""
    if isinstance(content, str):
        return [content] if content else []
    if isinstance(content, list):
        out: list[str] = []
        for part in content:
            text = part.get("text", "") if isinstance(part, dict) else str(part)
            if text:
                out.append(text)
        return out
    return []


@app.post("/api/chat")
async def chat(req: ChatRequest):
    async def event_stream():
        graph = _get_graph()
        config = {
            "configurable": {"thread_id": req.thread_id},
            "tags": ["bc-wine-agent", "chat"],
            "metadata": {
                "thread_id": req.thread_id,
                # Truncated user message so the LangSmith trace list is scannable
                # without leaking long inputs into metadata indexing.
                "user_message_preview": req.message[:120],
                "message_length": len(req.message),
            },
            "run_name": f"chat: {req.message[:60]}",
        }

        # If a previous turn paused on ask_user_clarification_tool, this thread
        # has a pending interrupt. The user's message is the clarification reply,
        # so resume the graph with Command(resume=...) instead of starting a new
        # turn. Validation is skipped on resume — short replies like "$50" or
        # "the cheaper one" could trip the validator but are valid in-context.
        is_resume = False
        try:
            snapshot = await graph.aget_state(config)
            if snapshot and getattr(snapshot, "interrupts", None):
                is_resume = True
        except Exception:
            snapshot = None

        if not is_resume:
            # Pre-agent validation gate. Off-topic queries (weather, sports, code, etc.)
            # short-circuit here with an in-language rejection so we don't pay for an
            # orchestrator round + tools. Failures fall through to the agent — the
            # orchestrator's Guideline G5 (off-topic redirect) is the backstop.
            try:
                verdict = await validate_query(req.message)
            except Exception:
                verdict = None
            if verdict is not None and not verdict.is_valid:
                yield sse({"type": "token", "text": verdict.rejection_message, "run_id": None})
                yield sse({"type": "done"})
                return

        inputs = Command(resume=req.message) if is_resume else {"messages": [("user", req.message)]}

        # The orchestrator is the only LLM that streams (synthesis was removed).
        # It may run several rounds per turn; the tool-calling rounds are
        # intermediate and must not reach the user — only the FINAL round (the
        # one with no tool_calls) is the answer. We can't tell mid-stream which
        # round is final, so we buffer each round's tokens keyed by run_id
        # (resetting on each new round, so only the latest survives) and flush
        # that buffer once the graph ends with no pending clarification.
        answer_buffer: list[str] = []
        answer_run_id = None

        try:
            async for event in graph.astream_events(inputs, config=config, version="v2"):
                kind = event["event"]
                name = event.get("name", "")

                if kind == "on_tool_start":
                    data = event.get("data", {})
                    yield sse({
                        "type": "tool_start",
                        "tool": name,
                        "run_id": event.get("run_id"),
                        "args": data.get("input"),
                    })
                elif kind == "on_tool_end":
                    output = event.get("data", {}).get("output")
                    summary = _summarize_tool_output(output)
                    yield sse({
                        "type": "tool_end",
                        "tool": name,
                        "run_id": event.get("run_id"),
                        "summary": summary,
                        "count": len(summary),
                    })
                elif kind == "on_chat_model_stream":
                    # Only the orchestrator's output is user-facing. Other LLM
                    # calls in the graph also stream tokens — the relevance filter
                    # in compact_tool_results (emits JSON like {"drop_indices":[…]})
                    # and the pairing sub-LLM inside a tool — and must NEVER reach
                    # the user. Filter by node.
                    node = (event.get("metadata") or {}).get("langgraph_node", "")
                    if node != "orchestrator":
                        continue
                    run_id = event.get("run_id")
                    texts = _extract_token_texts(event["data"]["chunk"])
                    if not texts:
                        continue
                    # New run_id = new orchestrator round; drop the prior round's
                    # buffer so only the latest (final) round is flushed below.
                    if run_id != answer_run_id:
                        answer_buffer = []
                        answer_run_id = run_id
                    answer_buffer.extend(texts)

            # If the orchestrator paused on ask_user_clarification_tool, the
            # graph stops at an interrupt. Surface the question to the frontend
            # so the user can reply (the next /api/chat hit will resume).
            try:
                post_snapshot = await graph.aget_state(config)
            except Exception:
                post_snapshot = None
            pending = getattr(post_snapshot, "interrupts", None) if post_snapshot else None
            if pending:
                payload = pending[0].value if hasattr(pending[0], "value") else pending[0]
                if not isinstance(payload, dict):
                    payload = {"question": str(payload), "options": []}
                yield sse({
                    "type": "clarification_request",
                    "question": payload.get("question", ""),
                    "options": payload.get("options") or [],
                })
                yield sse({"type": "done"})
                return

            # Flush the final orchestrator round — its answer. Reached only when
            # there's no pending clarification interrupt (that path returns above).
            if answer_buffer:
                for t in answer_buffer:
                    yield sse({"type": "token", "text": t, "run_id": answer_run_id})

            yield sse({"type": "done"})
        except Exception as e:
            yield sse({"type": "error", "message": str(e)})

    return StreamingResponse(event_stream(), media_type="text/event-stream")


@app.get("/api/health")
async def health():
    return {"ok": True}


app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def index():
    return FileResponse("static/index.html")
