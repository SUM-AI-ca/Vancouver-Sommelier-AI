"""FastAPI backend — SSE chat endpoint, session management, static file serving."""

import json
import uuid

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.responses import FileResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from agent import get_graph

load_dotenv()

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

    Returns a list of up to 5 result rows, each shaped like:
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
    for r in results[:5]:
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
            "tags": ["bc-wine-agent"],
            "metadata": {"thread_id": req.thread_id},
        }
        inputs = {"messages": [("user", req.message)]}

        # The graph streams two LLM responses per turn for on-topic queries:
        # the orchestrator's draft and format_response's synthesis. We only
        # want the user to see ONE — the synthesis. So we stream
        # format_response tokens through directly, and buffer any other node's
        # tokens (orchestrator). The buffer is only released at the end if
        # format_response never emitted (off-topic queries where the early
        # return in format_response_node skips the synthesis LLM call). When
        # a new orchestrator round starts we drop the previous round's
        # buffer — only the LATEST orchestrator response is the fallback.
        fallback_buffer: list[str] = []
        fallback_run_id = None
        format_response_started = False

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
                    metadata = event.get("metadata") or {}
                    node = metadata.get("langgraph_node", "")
                    run_id = event.get("run_id")
                    texts = _extract_token_texts(event["data"]["chunk"])
                    if not texts:
                        continue

                    if node == "format_response":
                        format_response_started = True
                        for t in texts:
                            yield sse({"type": "token", "text": t, "run_id": run_id})
                    else:
                        # Orchestrator (any round). Reset buffer when a new
                        # LLM call starts so only the latest round is kept.
                        if run_id != fallback_run_id:
                            fallback_buffer = []
                            fallback_run_id = run_id
                        fallback_buffer.extend(texts)

            # If the synthesis never ran (off-topic query → format_response
            # early-returned), flush the last orchestrator response so the
            # user isn't left with an empty reply.
            if not format_response_started and fallback_buffer:
                for t in fallback_buffer:
                    yield sse({"type": "token", "text": t, "run_id": fallback_run_id})

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
