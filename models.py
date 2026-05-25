"""LLM factory for the BC Wine AI Agent — Gemini 3.5 Flash via Vertex AI."""

from langchain_google_genai import ChatGoogleGenerativeAI

PROJECT = "wine-agent-jh-2026"
LOCATION = "global"
MODEL = "gemini-3.5-flash"


def get_llm(temperature: float = 0.3) -> ChatGoogleGenerativeAI:
    return ChatGoogleGenerativeAI(
        model=MODEL,
        project=PROJECT,
        location=LOCATION,
        temperature=temperature,
    )
