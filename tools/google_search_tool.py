"""Google Search grounding tool — replaces the prior web-search fallback.

Uses Gemini's native Google Search grounding (Gemini Enterprise Agent Platform) to answer knowledge / review
questions with up-to-date, cited information, and returns the source URLs Gemini
grounded on so the agent can attribute and link every claim.

Copyright guardrail: this tool surfaces SOURCE LINKS + brief grounded summaries only.
Callers (prompts) must attribute any published review/score to its publication and
summarize — never reproduce full proprietary review or tasting-note text verbatim.

Grounding uses the same Gemini Enterprise Agent Platform credentials as the rest of the app (no extra key).
"""
from __future__ import annotations

from langchain_core.messages import HumanMessage, SystemMessage
from pydantic import BaseModel

from models import get_grounded_llm

# Gemini 2.0+ uses {"google_search": {}}; older models use {"google_search_retrieval": {}}.
# Try the modern spec first and fall back so this works across model/SDK versions.
_GROUNDING_TOOL_SPECS = ({"google_search": {}}, {"google_search_retrieval": {}})

_GROUNDING_SYSTEM = (
    "You answer drinks questions (wine, beer, spirits, cider, sake, cocktails) using "
    "Google Search grounding. Be concise and factual, and ground every claim in a "
    "specific source. When relaying a published review or score, attribute it to the "
    "publication or critic and SUMMARIZE briefly — never reproduce the full review or "
    "tasting-note text verbatim. Prefer sources relevant to the Vancouver, BC market."
)


class WebResult(BaseModel):
    title: str | None = None
    url: str
    content: str | None = None


def _flatten_text(content) -> str:
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        return "".join(
            part.get("text", "") for part in content if isinstance(part, dict)
        )
    return str(content) if content is not None else ""


def _extract_sources(message) -> list[WebResult]:
    """Best-effort pull of grounding source URLs from response metadata.

    The grounding-metadata shape varies by langchain-google-genai version, so we look
    in both response_metadata and additional_kwargs and tolerate camelCase/snake_case.
    Degrades to [] rather than raising — the answer text still carries inline citations.
    """
    meta: dict = {}
    for container in (
        getattr(message, "response_metadata", None),
        getattr(message, "additional_kwargs", None),
    ):
        if isinstance(container, dict):
            gm = container.get("grounding_metadata") or container.get("groundingMetadata")
            if isinstance(gm, dict):
                meta = gm
                break

    chunks = meta.get("grounding_chunks") or meta.get("groundingChunks") or []
    out: list[WebResult] = []
    seen: set[str] = set()
    for ch in chunks:
        web = ch.get("web") if isinstance(ch, dict) else None
        if isinstance(web, dict):
            uri = web.get("uri")
            if isinstance(uri, str) and uri not in seen:
                seen.add(uri)
                out.append(WebResult(title=web.get("title"), url=uri))
    return out


async def search_web_grounded(query: str) -> tuple[list[WebResult], str | None]:
    """Answer `query` with Google Search grounding; return (source_results, answer)."""
    llm = get_grounded_llm()
    messages = [
        SystemMessage(content=_GROUNDING_SYSTEM),
        HumanMessage(content=query),
    ]
    last_err: Exception | None = None
    for spec in _GROUNDING_TOOL_SPECS:
        try:
            resp = await llm.bind_tools([spec]).ainvoke(messages)
            answer = _flatten_text(resp.content).strip() or None
            return _extract_sources(resp), answer
        except Exception as e:  # noqa: BLE001 — try the next grounding spec
            last_err = e
    raise last_err if last_err else RuntimeError("grounding failed")


if __name__ == "__main__":
    import asyncio

    async def _smoke() -> None:
        results, answer = await search_web_grounded(
            "What is the Naramata Bench known for in BC wine?"
        )
        print("ANSWER:\n", answer)
        print("\nSOURCES:")
        for r in results:
            print(f"- {r.title} — {r.url}")

    asyncio.run(_smoke())
