"""FastAPI backend — SSE chat endpoint, session management, static file serving."""

import json
import logging
import os
import uuid

import httpx
from dotenv import load_dotenv
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
from langchain_core.messages import HumanMessage
from langgraph.types import Command
from pydantic import BaseModel
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from slowapi.util import get_remote_address

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

PROXY_SECRET = os.getenv("PROXY_SECRET", "")

limiter = Limiter(key_func=get_remote_address)
app = FastAPI(title="Vancouver Drinks AI")
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)


@app.middleware("http")
async def verify_proxy_secret(request: Request, call_next):
    """Block direct Cloud Run access. Only requests from the Cloudflare
    Pages Function proxy (which injects X-Proxy-Secret) are accepted.
    Skipped when PROXY_SECRET is not set (local development)."""
    if PROXY_SECRET and request.url.path.startswith("/api/"):
        if request.headers.get("X-Proxy-Secret") != PROXY_SECRET:
            return JSONResponse(status_code=403, content={"error": "Direct access not allowed"})
    return await call_next(request)


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://wineaiagent.com",
        "https://www.wineaiagent.com",
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
    cf_turnstile_token: str | None = None


class SessionResponse(BaseModel):
    thread_id: str


TURNSTILE_SECRET = os.getenv("CF_TURNSTILE_SECRET", "")


async def _verify_turnstile(token: str | None, request: Request) -> bool:
    """Verify a Cloudflare Turnstile token. Returns True if valid or if
    Turnstile is not configured (secret not set)."""
    if not TURNSTILE_SECRET:
        return True
    if not token:
        return False
    async with httpx.AsyncClient() as client:
        resp = await client.post(
            "https://challenges.cloudflare.com/turnstile/v0/siteverify",
            data={"secret": TURNSTILE_SECRET, "response": token,
                  "remoteip": request.client.host if request.client else ""},
        )
        return resp.json().get("success", False)


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
            # Some store APIs return the price already prefixed with "$".
            # Normalize so we never end up with "$$".
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

    # Grounded web search and reasoning_pair_wine don't have "results" — surface their
    # answer. These return long markdown prose; the frontend renders the body as
    # markdown (markdown=True) instead of clipping it as a plain subtitle.
    if not rows:
        answer_titles = {
            "search_web_grounded": "Web answer",
            "sourcing_agent": "Sourcing agent",
            "sommelier_agent": "Sommelier agent",
            "menu_architect": "Menu architect",
        }
        if tool in answer_titles and data.get("answer"):
            rows.append({
                "title": answer_titles[tool],
                "body": str(data["answer"])[:8000],
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


AGENT_TOOLS = {"sourcing_agent_tool", "sommelier_agent_tool", "menu_architect_tool"}

INNER_TOOL_LABELS = {
    "search_bcliquor_tool": "BC Liquor Store",
    "search_everything_wine_tool": "Everything Wine",
    "search_okanagan_cellars_tool": "Okanagan Cellars",
    "search_suttonplace_tool": "Sutton Place Wine Merchant",
    "search_marquis_tool": "Marquis Wine Cellars",
    "search_legacy_liquor_store_tool": "Legacy Liquor Store",
    "search_web_grounded_tool": "Web Search",
    "reasoning_pair_wine_tool": "Wine Pairing",
    "sourcing_agent_tool": "Sourcing Agent",
    "ask_user_clarification_tool": "Clarification",
}


def _summarize_agent_output(output) -> dict:
    """Summarize an agent tool's output including per-inner-tool breakdowns.

    Returns {"summary": [...], "count": N, "inner_tools": [...]}.
    """
    if hasattr(output, "content"):
        output = output.content
    if not isinstance(output, str):
        return {"summary": [], "count": 0, "inner_tools": []}
    try:
        data = json.loads(output)
    except (json.JSONDecodeError, TypeError):
        return {"summary": [], "count": 0, "inner_tools": []}
    if not isinstance(data, dict):
        return {"summary": [], "count": 0, "inner_tools": []}

    inner_tools_raw = data.get("inner_tools") if isinstance(data.get("inner_tools"), list) else []
    inner_tools = []
    for it in inner_tools_raw:
        if not isinstance(it, dict):
            continue
        tool_name = it.get("tool", "")
        content = it.get("content", "")
        rows = _summarize_tool_output(content)
        inner_tools.append({
            "tool": tool_name,
            "label": INNER_TOOL_LABELS.get(tool_name, tool_name),
            "summary": rows,
            "count": len(rows),
        })

    summary = _summarize_tool_output(output)
    return {
        "summary": summary,
        "count": len(summary),
        "inner_tools": inner_tools,
    }


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
                str(x) for x in (lab.get("producer"), lab.get("product_name")) if x
            ) or "Drink label"
            bits = [lab.get("category"), lab.get("style"), lab.get("vintage"), lab.get("region"), lab.get("abv")]
            rows.append({
                "title": title[:160],
                "subtitle": " · ".join(str(b) for b in bits if b)[:200],
                "url": None,
            })
        elif dtype == "drink_list" and isinstance(ex.get("drink_list"), dict):
            for it in ex["drink_list"].get("items", []):
                if not isinstance(it, dict):
                    continue
                title = it.get("product_name") or it.get("raw_text") or "Drink"
                bits = [it.get("category"), it.get("producer"), it.get("style"), it.get("price")]
                rows.append({
                    "title": str(title)[:160],
                    "subtitle": " · ".join(str(b) for b in bits if b)[:200],
                    "url": None,
                })
        elif dtype == "food_menu" and isinstance(ex.get("food_menu"), dict):
            fm = ex["food_menu"]
            cuisine = fm.get("cuisine")
            for it in fm.get("items", []):
                if not isinstance(it, dict):
                    continue
                title = it.get("dish_name") or it.get("raw_text") or "Dish"
                bits = [it.get("description"), it.get("price"), it.get("section")]
                if cuisine:
                    bits.append(cuisine)
                rows.append({
                    "title": str(title)[:160],
                    "subtitle": " · ".join(str(b) for b in bits if b)[:200],
                    "url": None,
                })
        elif dtype == "other":
            rows.append({
                "title": "Not a recognized image",
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
@limiter.limit("20/hour")
async def chat(req: ChatRequest, request: Request):
    if not await _verify_turnstile(req.cf_turnstile_token, request):
        return JSONResponse(status_code=403, content={"error": "Bot verification failed"})

    async def event_stream():
        graph = _get_graph()
        config = {
            "recursion_limit": 30,
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

        # Stream orchestrator tokens in real-time so the user sees text
        # immediately — especially on follow-up turns where no tools run.
        # Each orchestrator round has a unique run_id; the frontend already
        # handles run_id changes by clearing the previous partial answer, so
        # intermediate tool-calling rounds are naturally replaced by the final
        # answer round. For clarification interrupts the frontend cleans up
        # any partial text when the clarification_request event arrives.

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
                    if name in AGENT_TOOLS:
                        agent_result = _summarize_agent_output(output)
                        yield sse({
                            "type": "tool_end",
                            "tool": name,
                            "run_id": event.get("run_id"),
                            "is_agent": True,
                            "inner_tools": agent_result["inner_tools"],
                            "summary": agent_result["summary"],
                            "count": agent_result["count"],
                        })
                    else:
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
                    for t in texts:
                        yield sse({"type": "token", "text": t, "run_id": run_id})

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
        except Exception as e:
            yield sse({"type": "error", "message": str(e)})
            yield sse({"type": "done"})

    return StreamingResponse(event_stream(), media_type="text/event-stream")


@app.get("/api/health")
async def health():
    return {"ok": True}


app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")
