"""FastAPI backend — SSE chat endpoint, session management, static file serving."""

import json
import logging
import os
import uuid

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from fastapi.staticfiles import StaticFiles
from langchain_core.messages import HumanMessage
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

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://wineaiagent.com",
        "https://www.wineaiagent.com",
        "https://bcwineaiagents.juhyun5328-b18.workers.dev",
        "http://localhost:8000",
    ],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Cap attached images per turn (matches the frontend limit).
MAX_IMAGES = 2

_graph = None


def _get_graph():
    global _graph
    if _graph is None:
        _graph = get_graph()
    return _graph


class ChatRequest(BaseModel):
    thread_id: str
    message: str
    # Base64 data-URLs (data:image/...;base64,...). The frontend downscales and
    # re-encodes to JPEG before sending. None/empty ⇒ a normal text turn.
    images: list[str] | None = None


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

    # Surface tool failures so the dropdown shows the error instead of a silent
    # "no results". The orchestrator still answers from the other tools (errors are
    # contained by tool_error_to_json); this only makes the failure visible.
    if not rows:
        status = data.get("status")
        if status and status != "ok":
            rows.append({
                "title": "⚠️ Tool error",
                "subtitle": str(data.get("message") or f"status: {status}")[:300],
                "url": None,
            })
    return rows


def _summarize_vision(extractions) -> list[dict]:
    """Compact rows describing what the vision_node read from the attached image(s),
    for the frontend's expandable badge. Reuses the {title, subtitle, url} row shape
    that renderToolRow already knows how to draw.

    `extractions` is the list of VisionExtraction.model_dump() dicts the node wrote
    to state under "vision_extractions".
    """
    rows: list[dict] = []
    if not isinstance(extractions, list):
        return rows
    for ex in extractions:
        if not isinstance(ex, dict):
            continue
        dtype = ex.get("document_type")
        if dtype == "label" and isinstance(ex.get("label"), dict):
            lab = ex["label"]
            title = " ".join(
                str(x) for x in (lab.get("producer"), lab.get("wine_name")) if x
            ) or "Wine label"
            bits = [lab.get("varietal"), lab.get("vintage"), lab.get("region"), lab.get("abv")]
            rows.append({
                "title": title[:160],
                "subtitle": " · ".join(str(b) for b in bits if b)[:200],
                "url": None,
            })
        elif dtype == "wine_list" and isinstance(ex.get("wine_list"), dict):
            for it in ex["wine_list"].get("items", []):
                if not isinstance(it, dict):
                    continue
                title = it.get("wine_name") or it.get("raw_text") or "Wine"
                bits = [it.get("producer"), it.get("vintage"), it.get("region"), it.get("price")]
                rows.append({
                    "title": str(title)[:160],
                    "subtitle": " · ".join(str(b) for b in bits if b)[:200],
                    "url": None,
                })
        elif dtype == "other":
            rows.append({
                "title": "Not a wine image",
                "subtitle": str(ex.get("notes") or "")[:200],
                "url": None,
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

        if not is_resume and not req.images:
            # Pre-agent validation gate. Off-topic queries (weather, sports, code, etc.)
            # short-circuit here with an in-language rejection so we don't pay for an
            # orchestrator round + tools. Failures fall through to the agent — the
            # orchestrator's Guideline G5 (off-topic redirect) is the backstop.
            #
            # Skipped when an image is attached: validate_query only sees text, and an
            # image with little/no text would trip it. Scope is enforced downstream
            # instead — vision_node tags non-wine photos document_type="other" and the
            # orchestrator (G7) declines them politely.
            try:
                verdict = await validate_query(req.message)
            except Exception:
                verdict = None
            if verdict is not None and not verdict.is_valid:
                yield sse({"type": "token", "text": verdict.rejection_message, "run_id": None})
                yield sse({"type": "done"})
                return

        if is_resume:
            inputs = Command(resume=req.message)
        elif req.images:
            # Multimodal turn: text + image parts in one HumanMessage. The id is set
            # explicitly so vision_node can swap this message in place (same id) after
            # it folds the extraction in and strips the image. See agent.vision_node.
            parts = [{"type": "text", "text": req.message or "이 와인 이미지를 분석해줘"}]
            for url in req.images[:MAX_IMAGES]:
                parts.append({"type": "image_url", "image_url": {"url": url}})
            inputs = {"messages": [HumanMessage(content=parts, id=str(uuid.uuid4()))]}
        else:
            inputs = {"messages": [("user", req.message)]}

        # The orchestrator is the only LLM that streams (synthesis was removed).
        # It may run several rounds per turn; the tool-calling rounds are
        # intermediate and must not reach the user — only the FINAL round (the
        # one with no tool_calls) is the answer. We can't tell mid-stream which
        # round is final, so we buffer each round's tokens keyed by run_id
        # (resetting on each new round, so only the latest survives) and flush
        # that buffer once the graph ends with no pending clarification.
        answer_buffer: list[str] = []
        answer_run_id = None

        # vision_node is a graph node (not a tool), so on_tool_* never fires for it.
        # Surface its progress to the UI via metadata.langgraph_node (robust across
        # langgraph naming): the first event inside the node opens the badge, and the
        # node's on_chain_end carries the extraction. A post-loop state read is the
        # fallback so the badge always resolves even if that exact event is missed.
        vision_started = False
        vision_result_sent = False

        try:
            async for event in graph.astream_events(inputs, config=config, version="v2"):
                kind = event["event"]
                name = event.get("name", "")
                node = (event.get("metadata") or {}).get("langgraph_node", "")

                if node == "vision" and not vision_started:
                    vision_started = True
                    yield sse({"type": "vision_start"})

                if kind == "on_chain_end" and name == "vision" and not vision_result_sent:
                    out = event.get("data", {}).get("output")
                    extractions = out.get("vision_extractions") if isinstance(out, dict) else None
                    if extractions is not None:
                        vision_result_sent = True
                        summary = _summarize_vision(extractions)
                        yield sse({
                            "type": "vision_result",
                            "summary": summary,
                            "count": len(summary),
                        })

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

            # Fallback: if the image was analyzed but the in-loop vision_result was
            # missed, read the extraction off final state so the badge still resolves.
            if vision_started and not vision_result_sent:
                state_vals = getattr(post_snapshot, "values", None) or {} if post_snapshot else {}
                summary = _summarize_vision(state_vals.get("vision_extractions"))
                yield sse({"type": "vision_result", "summary": summary, "count": len(summary)})
                vision_result_sent = True

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


app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")
