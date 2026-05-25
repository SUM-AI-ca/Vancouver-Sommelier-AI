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


@app.post("/api/session")
async def create_session() -> SessionResponse:
    return SessionResponse(thread_id=str(uuid.uuid4()))


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

        try:
            async for event in graph.astream_events(inputs, config=config, version="v2"):
                kind = event["event"]
                name = event.get("name", "")

                if kind == "on_tool_start":
                    data = event.get("data", {})
                    yield sse({
                        "type": "tool_start",
                        "tool": name,
                        "args": data.get("input"),
                    })
                elif kind == "on_tool_end":
                    yield sse({"type": "tool_end", "tool": name})
                elif kind == "on_chat_model_stream":
                    chunk = event["data"]["chunk"]
                    content = chunk.content if hasattr(chunk, "content") else ""
                    if content and isinstance(content, str):
                        yield sse({"type": "token", "text": content})
                    elif content and isinstance(content, list):
                        for part in content:
                            text = part.get("text", "") if isinstance(part, dict) else str(part)
                            if text:
                                yield sse({"type": "token", "text": text})

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
