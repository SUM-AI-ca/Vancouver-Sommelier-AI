"""
Tavily Web Search Tool for BC Wine AI Agent (LangGraph)

General-purpose web search fallback for wine knowledge queries that cannot be
answered by the wine-store-specific tools (e.g., food pairings, grape info,
wine regions, vinification techniques).

Uses the Tavily Search API (REST). Requires TAVILY_API_KEY in .env.
"""

import asyncio
import os

import httpx
from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()


# ── Config ──────────────────────────────────────────────────────────

TAVILY_API_KEY = os.getenv("TAVILY_API_KEY", "")
TAVILY_SEARCH_URL = "https://api.tavily.com/search"


# ── Data Model ──────────────────────────────────────────────────────

class TavilyResult(BaseModel):
    title: str
    url: str
    content: str
    score: float | None = None
    published_date: str | None = None


# ── Core Search ─────────────────────────────────────────────────────

async def search_tavily(
    query: str,
    max_results: int = 5,
    search_depth: str = "basic",
    include_answer: bool = True,
) -> tuple[list[TavilyResult], str | None]:
    """
    Search the web via Tavily for general wine knowledge.

    Args:
        query:          Search query (e.g., "best food pairings for Pinot Noir")
        max_results:    Number of results to return (1-10, default 5)
        search_depth:   "basic" (faster, cheaper) or "advanced" (more thorough)
        include_answer: If True, returns an AI-generated summary answer

    Returns:
        (results, answer) — list of TavilyResult and optional answer string
    """
    if not TAVILY_API_KEY:
        raise ValueError("TAVILY_API_KEY not set in .env")

    payload = {
        "api_key": TAVILY_API_KEY,
        "query": query,
        "max_results": max_results,
        "search_depth": search_depth,
        "include_answer": include_answer,
        "include_raw_content": False,
        "include_images": False,
    }

    async with httpx.AsyncClient(timeout=15.0) as client:
        resp = await client.post(TAVILY_SEARCH_URL, json=payload)
        resp.raise_for_status()
        data = resp.json()

    answer = data.get("answer") if include_answer else None

    results: list[TavilyResult] = []
    for item in data.get("results", []):
        results.append(
            TavilyResult(
                title=item.get("title", ""),
                url=item.get("url", ""),
                content=item.get("content", ""),
                score=item.get("score"),
                published_date=item.get("published_date"),
            )
        )

    return results, answer


# ── Formatting ──────────────────────────────────────────────────────

def format_results(
    results: list[TavilyResult], query: str, answer: str | None = None
) -> str:
    if not results and not answer:
        return f"No web results found for '{query}'."

    lines = [f"Web Search: {len(results)} results for '{query}'\n"]

    if answer:
        lines.append(f"Summary: {answer}\n")

    for i, r in enumerate(results, 1):
        parts = [f"{i}. {r.title}"]
        if r.content:
            parts.append(f"   {r.content}")
        if r.score is not None:
            parts.append(f"   Relevance: {r.score:.2f}")
        if r.published_date:
            parts.append(f"   Published: {r.published_date}")
        parts.append(f"   URL: {r.url}")
        lines.append("\n".join(parts))

    return "\n\n".join(lines)


# ── Standalone Test ─────────────────────────────────────────────────

async def main():
    for query in [
        "best food pairings for BC Pinot Noir",
        "Okanagan Valley wine region climate terroir",
        "difference between old world and new world Chardonnay",
    ]:
        print(f"Searching '{query}'...\n")
        results, answer = await search_tavily(query)
        print(format_results(results, query, answer))
        print("\n" + "=" * 60 + "\n")


if __name__ == "__main__":
    asyncio.run(main())
