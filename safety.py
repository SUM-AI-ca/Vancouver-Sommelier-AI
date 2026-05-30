"""tool_error_to_json — turns a tool exception into a tool result instead of a crash.

Wired into the graph as `ToolNode(TOOLS, handle_tool_errors=tool_error_to_json)`.
LangGraph's *default* handler only swallows argument-validation errors and re-raises
everything else (network, auth, parsing), which propagates out of the graph and kills
the whole turn. This handler catches ALL exceptions per tool call and returns a JSON
error string, so a single tool's failure becomes a visible `status="error"` result —
the orchestrator still receives every other tool's output and answers from those.

The `e: Exception` annotation is load-bearing: ToolNode reads it (`_infer_handled_types`)
to decide which exceptions to route here. `GraphInterrupt` (the human-in-the-loop
clarification mechanism) is a `GraphBubbleUp` and is re-raised by ToolNode *before* this
handler runs, so clarifications are unaffected.
"""

import json

import httpx


def tool_error_to_json(e: Exception) -> str:
    if isinstance(e, httpx.TimeoutException):
        return json.dumps({
            "status": "timeout",
            "message": "The source timed out.",
            "results": [],
        })
    if isinstance(e, httpx.HTTPStatusError):
        return json.dumps({
            "status": "http_error",
            "code": e.response.status_code,
            "message": f"HTTP {e.response.status_code} from the source.",
            "results": [],
        })
    return json.dumps({
        "status": "error",
        "message": f"{type(e).__name__}: {e}",
        "results": [],
    })
