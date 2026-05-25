"""safe_tool decorator — wraps tool functions so failures degrade gracefully."""

import functools

import httpx


def safe_tool(tool_fn):
    @functools.wraps(tool_fn)
    async def wrapped(*args, **kwargs):
        try:
            return await tool_fn(*args, **kwargs)
        except httpx.TimeoutException:
            return {"status": "timeout", "results": [], "tool": tool_fn.__name__}
        except httpx.HTTPStatusError as e:
            return {
                "status": "http_error",
                "code": e.response.status_code,
                "results": [],
                "tool": tool_fn.__name__,
            }
        except ValueError as e:
            return {
                "status": "unavailable",
                "message": str(e),
                "results": [],
                "tool": tool_fn.__name__,
            }
        except Exception as e:
            return {
                "status": "error",
                "message": f"{type(e).__name__}: {e}",
                "results": [],
                "tool": tool_fn.__name__,
            }

    return wrapped
