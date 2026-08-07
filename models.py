"""LLM factory for Vancouver Drinks AI — Gemini via Gemini Enterprise Agent Platform (formerly Vertex AI)."""

import asyncio
import logging
import os

from langchain_google_genai import ChatGoogleGenerativeAI

log = logging.getLogger("bc-wine-agent.models")

PROJECT = os.getenv("GOOGLE_CLOUD_PROJECT", "wine-agent-jh-2026")
LOCATION = os.getenv("GOOGLE_CLOUD_LOCATION", "global")
MODEL = "gemini-3.6-flash"
JUDGE_MODEL = "gemini-3.1-pro-preview"


def get_llm(temperature: float = 0.1, model: str | None = None) -> ChatGoogleGenerativeAI:
    return ChatGoogleGenerativeAI(
        model=model or MODEL,
        project=PROJECT,
        location=LOCATION,
        temperature=temperature,
    )


def get_grounded_llm(temperature: float = 0.1) -> ChatGoogleGenerativeAI:
    """Gemini configured for Google Search grounding.

    Returns the base LLM; callers enable grounding by binding the built-in Google
    Search tool (`tools/google_search_tool.py` does this and tolerates both the
    `google_search` and legacy `google_search_retrieval` specs). Grounding uses the
    same Gemini Enterprise Agent Platform credentials as get_llm — no extra API key.
    """
    return ChatGoogleGenerativeAI(
        model=MODEL,
        project=PROJECT,
        location=LOCATION,
        temperature=temperature,
    )


def get_judge_llm(temperature: float = 0.0) -> ChatGoogleGenerativeAI:
    return ChatGoogleGenerativeAI(
        model=JUDGE_MODEL,
        project=PROJECT,
        location=LOCATION,
        temperature=temperature,
    )


# ── Transient-failure retry ──────────────────────────────────────

# Gemini intermittently drops a request with "499 CANCELLED" (less often 429/5xx or a
# deadline). 499 is a 4xx, so the SDK classifies it as a client error and does NOT retry
# it — one blip otherwise wipes out a whole specialist's contribution for the turn. Same
# hint list tests/judge.py has long used for the eval judge.
LLM_MAX_ATTEMPTS = 3
LLM_RETRY_BASE_DELAY = 1.0  # seconds; doubled each retry

_TRANSIENT_HINTS = (
    "429", "499", "500", "502", "503", "504",
    "cancelled", "deadline", "timeout", "timed out", "unavailable",
    "resource exhausted", "resourceexhausted", "internal error",
    "connection", "temporarily",
)


def is_transient_llm_error(exc: Exception) -> bool:
    msg = f"{type(exc).__name__}: {exc}".lower()
    return any(h in msg for h in _TRANSIENT_HINTS)


async def ainvoke_with_retry(llm, messages, *, label: str = "llm"):
    """`llm.ainvoke(messages)` with exponential backoff on transient API failures.

    Anything that isn't transient is re-raised on the spot, and asyncio cancellation
    (a BaseException) passes straight through — a disconnected client must not be
    retried against.
    """
    for attempt in range(1, LLM_MAX_ATTEMPTS + 1):
        try:
            return await llm.ainvoke(messages)
        except Exception as e:  # noqa: BLE001 — re-raised below unless transient
            if attempt == LLM_MAX_ATTEMPTS or not is_transient_llm_error(e):
                raise
            delay = LLM_RETRY_BASE_DELAY * 2 ** (attempt - 1)
            log.warning(
                "%s: transient LLM failure (%s: %s) — retrying in %.1fs (attempt %d/%d)",
                label, type(e).__name__, e, delay, attempt, LLM_MAX_ATTEMPTS,
            )
            await asyncio.sleep(delay)
