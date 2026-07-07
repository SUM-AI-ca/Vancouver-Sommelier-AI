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

import asyncio
import re

import httpx
from langchain_core.messages import HumanMessage, SystemMessage
from pydantic import BaseModel

from models import get_grounded_llm

# Gemini 2.0+ uses {"google_search": {}}; older models use {"google_search_retrieval": {}}.
# Try the modern spec first and fall back so this works across model/SDK versions.
_GROUNDING_TOOL_SPECS = ({"google_search": {}}, {"google_search_retrieval": {}})

# Gemini grounding returns each source as an opaque redirect token, not the real page URL:
#   https://vertexaisearch.cloud.google.com/grounding-api-redirect/<~200 chars>
# These are ~200-char tokens whose only human-readable part is the bare domain (shown as the
# link text). When the Supervisor LLM re-composes the final answer it cannot reproduce the
# token, so it shortens the href to the domain (homepage) or drops the link. We resolve each
# token to its real destination deep URL server-side so the model sees a short, meaningful,
# non-expiring link it can copy verbatim — the same kind store tools already return.
_REDIRECT_PREFIX = "https://vertexaisearch.cloud.google.com/grounding-api-redirect/"
_REDIRECT_RE = re.compile(
    r"https://vertexaisearch\.cloud\.google\.com/grounding-api-redirect/[^\s)\]\"'<>]+"
)
_RESOLVE_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/124.0 Safari/537.36"
    )
}

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


async def _resolve_one(client: httpx.AsyncClient, url: str) -> tuple[str, str]:
    """Resolve a single grounding-redirect token to its real destination URL.

    Reads the first redirect's `Location` (the precise grounded page) rather than following
    into the destination site's own canonical/consent redirects. Loops only while the target
    is itself another grounding redirect. Returns (original, resolved); on any failure returns
    (original, original) so a transient network error never breaks the turn.
    """
    if not url.startswith(_REDIRECT_PREFIX):
        return url, url
    current = url
    try:
        for _ in range(3):
            resp = await client.get(current)
            if not resp.is_redirect:
                break
            location = resp.headers.get("location")
            if not location:
                break
            current = location
            if not current.startswith(_REDIRECT_PREFIX):
                break
    except Exception:  # noqa: BLE001 — keep the original token on any resolution failure
        return url, url
    return url, current


async def _resolve_redirect_urls(urls: list[str]) -> dict[str, str]:
    """Map each unique grounding-redirect token to its resolved real URL (concurrently)."""
    uniq = {u for u in urls if u.startswith(_REDIRECT_PREFIX)}
    if not uniq:
        return {}
    async with httpx.AsyncClient(
        follow_redirects=False, timeout=8.0, headers=_RESOLVE_HEADERS
    ) as client:
        pairs = await asyncio.gather(*(_resolve_one(client, u) for u in uniq))
    return {orig: real for orig, real in pairs if real != orig}


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
            sources = _extract_sources(resp)
            # Resolve grounding-redirect tokens (in both the source list and inline in the
            # answer, where Gemini embeds them too) to real destination deep URLs so the
            # downstream LLM sees links it can reproduce verbatim instead of homepages.
            redirect_urls = [s.url for s in sources]
            if answer:
                redirect_urls += _REDIRECT_RE.findall(answer)
            mapping = await _resolve_redirect_urls(redirect_urls)
            if mapping:
                for s in sources:
                    s.url = mapping.get(s.url, s.url)
                if answer:
                    for orig, real in mapping.items():
                        answer = answer.replace(orig, real)
            return sources, answer
        except Exception as e:  # noqa: BLE001 — try the next grounding spec
            last_err = e
    raise last_err if last_err else RuntimeError("grounding failed")


if __name__ == "__main__":

    async def _smoke() -> None:
        results, answer = await search_web_grounded(
            "What do reviewers say about Painted Rock Syrah 2021?"
        )
        print("ANSWER:\n", answer)
        print("\nSOURCES (should be real deep URLs, not grounding-api-redirect):")
        for r in results:
            print(f"- {r.title} — {r.url}")
        leaked = [r.url for r in results if r.url.startswith(_REDIRECT_PREFIX)]
        if answer:
            leaked += _REDIRECT_RE.findall(answer)
        print(
            f"\nUnresolved redirect tokens remaining: {len(leaked)}"
            + ("" if not leaked else f"\n  {leaked}")
        )

    asyncio.run(_smoke())
