"""LLM factory for Vancouver Drinks AI — Gemini via Gemini Enterprise Agent Platform (formerly Vertex AI)."""

from langchain_google_genai import ChatGoogleGenerativeAI

PROJECT = "wine-agent-jh-2026"
LOCATION = "global"
MODEL = "gemini-3.5-flash"
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
