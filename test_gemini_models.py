"""
Gemini Model Comparison Test for BC Wine AI Agent

Tests 7 Gemini models across 3 roles with 10 queries total.
Saves full results to test_results.txt for evaluation.

Usage:
    python test_gemini_models.py
"""

import time
import json
import sys
import os
from datetime import datetime
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage

PROJECT = "wine-agent-jh-2026"
LOCATION = "global"
OUTPUT_FILE = "test_results_v2.txt"


MODELS = [
    # --- Gemini 3 Generation ---
    "gemini-3.5-flash",  # 최신 정식 버전 (2026.05.19 릴리스)
    "gemini-3.1-pro-preview",  # 3.1 Pro (Preview)
    "gemini-3.1-flash-lite",  # 정식 버전 (2026.05.07 GA 승격, 이전 preview 태그 제거됨)
    "gemini-3-flash-preview",  # 3.0 Flash (Preview)
    # --- Gemini 2.5 Generation ---
    "gemini-2.5-pro",  # 2.5 Pro (Stable)
    "gemini-2.5-flash",  # 2.5 Flash (Stable)
    "gemini-2.5-flash-lite",  # 2.5 Flash Lite (Stable)
]

# output helpers
_out_file = None


def to_text(content):
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        parts = []
        for item in content:
            if isinstance(item, str):
                parts.append(item)
            elif isinstance(item, dict):
                parts.append(item.get("text", ""))
            else:
                parts.append(getattr(item, "text", str(item)))
        return "".join(parts)
    return str(content)


def p(text=""):
    print(text, flush=True)
    if _out_file:
        _out_file.write(text + "\n")
        _out_file.flush()


def get_llm(model: str, temperature: float = 0.3):
    return ChatGoogleGenerativeAI(
        model=model,
        project=PROJECT,
        location=LOCATION,
        temperature=temperature,
    )


def timed_invoke(llm, messages):
    start = time.time()
    response = llm.invoke(messages)
    elapsed = time.time() - start
    content = response.content
    meta = response.response_metadata or {}
    usage = meta.get("usage_metadata", {})
    input_tokens = usage.get("prompt_token_count", 0)
    output_tokens = usage.get("candidates_token_count", 0)
    return content, elapsed, input_tokens, output_tokens


# =====================================================================
# TEST 1: ORCHESTRATOR -- Intent Classification & Tool Selection
# =====================================================================

ORCHESTRATOR_SYSTEM = """You are a BC Wine AI Agent orchestrator. Your job is to classify user intent and decide which tools to call.

Available tools:
1. search_reviews -- Search WineAlign and Gismondi for expert critic reviews and scores
2. search_bcliquor -- Search BC Liquor Store for prices, availability, and product details
3. search_stores -- Search 3 Vancouver wine shops (Okanagan Cellars, Marquis Wine, Everything Wine) for inventory and pricing
4. wine_pairing -- Use wine knowledge to recommend pairings for food

For each user query, respond in this exact JSON format:
{
  "intent": "pairing|review|price_search|inventory|complex",
  "tools_to_call": ["tool_name1", "tool_name2"],
  "search_queries": ["query1", "query2"],
  "reasoning": "brief explanation of your decision"
}

Respond ONLY with the JSON. No markdown, no extra text."""

ORCHESTRATOR_QUERIES = [
    # Q1: simple pairing
    "What's the best wine to pair with grilled salmon?",
    # Q2: price + inventory
    "Where can I buy Tantalus Riesling in Vancouver and how much does it cost?",
    # Q3: complex multi-step
    "Find me a BC Pinot Noir under $50 that scores above 90 points and is currently in stock",
    # Q4: review only
    "What do critics think about Painted Rock Syrah 2021?",
]


# =====================================================================
# TEST 2: REASONING -- Wine Pairing & Sommelier Knowledge
# =====================================================================

PAIRING_SYSTEM = """You are an expert sommelier specializing in British Columbia wines.
You have deep knowledge of BC wine regions (Okanagan Valley, Similkameen Valley, Fraser Valley, Vancouver Island) and their characteristics.

When recommending wine pairings:
1. Explain WHY the pairing works (flavor bridges, contrast, texture)
2. Suggest specific BC grape varietals and sub-regions
3. Name 2-3 specific BC wineries known for that style
4. Consider price range if mentioned
5. Be specific -- don't just say "a light red", say "a cool-climate Pinot Noir from the Naramata Bench"

Keep your response under 300 words."""

PAIRING_QUERIES = [
    # Q5: delicate white fish
    "I'm making pan-seared halibut with lemon butter sauce and roasted asparagus. What BC wine would you recommend?",
    # Q6: heavy meat + budget
    "We're having a BBQ with smoked brisket, coleslaw, and cornbread. What BC wines work here? Budget is $30-50 per bottle.",
    # Q7: tricky pairing (spicy food)
    "I'm cooking Thai green curry with prawns. Most people say don't pair wine with spicy food, but I want to try. Any BC wine suggestions?",
]


# =====================================================================
# TEST 3: SYNTHESIS -- Formatting Raw Search Results
# =====================================================================

SYNTHESIS_SYSTEM = """You are a helpful wine assistant. Given raw search results from multiple sources, synthesize them into a clear, actionable response for the user.

Guidelines:
- Lead with the direct answer to the user's question
- Combine data from multiple sources (don't just list each source separately)
- Highlight price differences between stores
- Note availability/stock status clearly
- Keep it concise but complete
- If a wine appears in multiple stores, compare them side by side"""

MOCK_RESULTS_1 = """User asked: "Where can I buy Tantalus Riesling and how much is it?"

## search_bcliquor results:
1. Tantalus Vineyards Old Vines Riesling 2022
   Price: $28.99
   Grape: RIESLING | Country: Canada | Volume: 0.750L | ABV: 12.5%
   Consumer Rating: 4.6/5 (23 votes) | BC VQA: Yes
   Available at: 12 stores (47 units)
   Tasting Notes: Aromatic with notes of lime, green apple, and petrol. Crisp acidity with a long mineral finish.

2. Tantalus Vineyards Riesling 2023
   Price: $24.99
   Consumer Rating: 4.3/5 (8 votes) | BC VQA: Yes
   Available at: 8 stores (31 units)

## search_stores results:
Okanagan Cellars:
1. Tantalus Old Vines Riesling 2022 -- $27.99 -- In Stock (6)
2. Tantalus Riesling 2023 -- $23.99 -- In Stock (4)

Marquis Wine Cellars:
1. Tantalus Old Vines Riesling 2022 -- $29.50 -- In Stock (3)

Everything Wine:
1. Tantalus Old Vines Riesling 2022 -- $28.99 -- Available for delivery and pick up

## search_reviews results:
Tantalus Old Vines Riesling 2022:
- [John Szabo MS] Score: 93 points
  "Stunning purity and precision. Lime blossom, wet stone, and a hint of petrol. Drink 2024-2034."
  Value: 4/5 stars
- [Sara d'Amato] Score: 92 points
  "Classic BC Riesling at its finest. Green apple, white flowers, slate minerality."
  Value: 5/5 stars"""

MOCK_RESULTS_2 = """User asked: "Find a BC Pinot Noir under $40 with good reviews"

## search_bcliquor results:
1. Quails' Gate Stewart Family Reserve Pinot Noir 2021
   Price: $44.99
   Consumer Rating: 4.5/5 (15 votes) | BC VQA: Yes
   Available at: 6 stores (18 units)

2. CedarCreek Platinum Block 2 Pinot Noir 2021
   Price: $39.99
   Consumer Rating: 4.2/5 (5 votes) | BC VQA: Yes
   Available at: 4 stores (9 units)

3. Meyer Family Vineyards Pinot Noir 2022
   Price: $29.99
   Consumer Rating: 4.0/5 (3 votes) | BC VQA: Yes
   Available at: 10 stores (42 units)

4. Haywire Pinot Noir 2022
   Price: $24.99
   Consumer Rating: 3.8/5 (7 votes) | BC VQA: Yes
   Available at: 15 stores (67 units)

## search_stores results:
Okanagan Cellars:
1. Meyer Family Pinot Noir 2022 -- $28.99 -- In Stock (3)
2. Haywire Pinot Noir 2022 -- $23.99 -- In Stock (5)

Marquis Wine Cellars:
1. CedarCreek Platinum Block 2 Pinot Noir 2021 -- $38.50 -- In Stock (2)

Everything Wine:
1. Meyer Family Pinot Noir 2022 -- $29.99 -- Available for delivery
2. Haywire Pinot Noir 2022 -- $24.99 -- Pick up only (no delivery)

## search_reviews results:
CedarCreek Platinum Block 2 Pinot Noir 2021:
- [Anthony Gismondi] Score: 91 points
  "Elegant and refined. Cherry, raspberry, forest floor. Beautiful texture and length."
- [John Szabo MS] Score: 90 points
  "Well-made, classic Okanagan Pinot. Needs a year or two."
  Drink 2024-2030

Meyer Family Vineyards Pinot Noir 2022:
- [Sara d'Amato] Score: 89 points
  "Bright cherry, cranberry, and a touch of spice. Easy drinking but not simple."
  Value: 4/5 stars

Haywire Pinot Noir 2022:
- [Anthony Gismondi] Score: 87 points
  "Honest, straightforward Pinot. Good value at this price point."
  Value: 5/5 stars"""

SYNTHESIS_QUERIES = [
    f"Synthesize these results into a helpful response:\n\n{MOCK_RESULTS_1}",
    f"Synthesize these results into a helpful response:\n\n{MOCK_RESULTS_2}",
    # Q10: ambiguous -- tests how model handles incomplete data
    """Synthesize these results into a helpful response:

User asked: "Is Checkmate Chardonnay worth the price?"

## search_bcliquor results:
1. Checkmate Artisan Winery Attack Chardonnay 2019
   Price: $54.99
   Consumer Rating: 4.8/5 (4 votes) | BC VQA: Yes
   Available at: 2 stores (5 units)

## search_stores results:
Okanagan Cellars: No results found
Marquis Wine Cellars: No results found
Everything Wine: No results found

## search_reviews results:
Checkmate Attack Chardonnay 2019:
- [John Szabo MS] Score: 95 points
  "One of BC's greatest Chardonnays. Layered, complex, with stunning balance between richness and freshness. Toasted hazelnut, citrus curd, wet stone. A wine of real ambition and achievement. Drink 2023-2033."
  Value: 4/5 stars
- [Anthony Gismondi] Score: 94 points
  "Superb. This rivals top-shelf Burgundy at a fraction of the price. Worth every penny."
  Value: 5/5 stars
- [Sara d'Amato] Score: 93 points
  "Impeccable winemaking. Precise and powerful without being heavy."
  Value: 4/5 stars""",
]


# =====================================================================
# RUNNER
# =====================================================================

# Track stats for summary table
stats = []


def run_test(test_name: str, system_prompt: str, queries: list[str], models: list[str]):
    p(f"\n{'='*80}")
    p(f"  TEST: {test_name}")
    p(f"{'='*80}")

    for q_idx, query in enumerate(queries, 1):
        short_query = query.split("\n")[0][:100]
        p(
            f"\n--- Query {q_idx}: {short_query}{'...' if len(short_query) >= 100 else ''} ---\n"
        )

        for model in models:
            try:
                llm = get_llm(model)
                messages = [
                    SystemMessage(content=system_prompt),
                    HumanMessage(content=query),
                ]
                content, elapsed, in_tok, out_tok = timed_invoke(llm, messages)

                # Gemini 3.x compatibility
                if isinstance(content, list):
                    normalized = []

                    for item in content:
                        if isinstance(item, str):
                            normalized.append(item)

                        elif isinstance(item, dict):
                            normalized.append(item.get("text", str(item)))

                        elif hasattr(item, "text"):
                            normalized.append(item.text)

                        else:
                            normalized.append(str(item))

                    content = "".join(normalized)

                else:
                    content = str(content)

                stats.append(
                    {
                        "test": test_name,
                        "query": q_idx,
                        "model": model,
                        "time_s": round(elapsed, 2),
                        "input_tokens": in_tok,
                        "output_tokens": out_tok,
                        "response_len": len(content),
                        "error": None,
                    }
                )

                p(f"  [{model}]  time={elapsed:.2f}s  in={in_tok} out={out_tok}")
                p(f"  {'-'*70}")
                for line in content.split("\n"):
                    p(f"    {line}")
                p()

            except Exception as e:
                stats.append(
                    {
                        "test": test_name,
                        "query": q_idx,
                        "model": model,
                        "time_s": 0,
                        "input_tokens": 0,
                        "output_tokens": 0,
                        "response_len": 0,
                        "error": str(e),
                    }
                )
                p(f"  [{model}]  ERROR: {e}\n")


def print_summary():
    p(f"\n\n{'='*80}")
    p("  SUMMARY TABLE")
    p(f"{'='*80}\n")

    # group by model
    model_stats = {}
    for s in stats:
        m = s["model"]
        if m not in model_stats:
            model_stats[m] = {
                "times": [],
                "in_tokens": [],
                "out_tokens": [],
                "errors": 0,
                "calls": 0,
            }
        model_stats[m]["calls"] += 1
        if s["error"]:
            model_stats[m]["errors"] += 1
        else:
            model_stats[m]["times"].append(s["time_s"])
            model_stats[m]["in_tokens"].append(s["input_tokens"])
            model_stats[m]["out_tokens"].append(s["output_tokens"])

    header = f"  {'Model':<28} {'Avg Time':>9} {'Min':>6} {'Max':>6} {'Avg In':>8} {'Avg Out':>8} {'Errors':>7}"
    p(header)
    p(f"  {'-'*78}")

    for model in MODELS:
        ms = model_stats.get(model)
        if not ms or not ms["times"]:
            p(
                f"  {model:<28} {'N/A':>9} {'':>6} {'':>6} {'':>8} {'':>8} {ms['errors'] if ms else 0:>7}"
            )
            continue
        avg_t = sum(ms["times"]) / len(ms["times"])
        min_t = min(ms["times"])
        max_t = max(ms["times"])
        avg_in = sum(ms["in_tokens"]) / len(ms["in_tokens"])
        avg_out = sum(ms["out_tokens"]) / len(ms["out_tokens"])
        p(
            f"  {model:<28} {avg_t:>8.2f}s {min_t:>5.1f}s {max_t:>5.1f}s {avg_in:>7.0f} {avg_out:>7.0f} {ms['errors']:>7}"
        )

    p()

    # per-test breakdown
    p(f"\n  Per-Test Breakdown:")
    p(f"  {'-'*78}")
    tests = sorted(set(s["test"] for s in stats))
    for test in tests:
        p(f"\n  {test}:")
        test_stats = [s for s in stats if s["test"] == test and not s["error"]]
        for model in MODELS:
            ms = [s for s in test_stats if s["model"] == model]
            if not ms:
                continue
            avg_t = sum(s["time_s"] for s in ms) / len(ms)
            avg_out = sum(s["output_tokens"] for s in ms) / len(ms)
            p(f"    {model:<28} avg={avg_t:.2f}s  avg_out_tokens={avg_out:.0f}")

    # raw stats as JSON
    p(f"\n\n{'='*80}")
    p("  RAW STATS (JSON)")
    p(f"{'='*80}\n")
    p(json.dumps(stats, indent=2))


def main():
    global _out_file
    _out_file = open(OUTPUT_FILE, "w", encoding="utf-8")

    p("=" * 80)
    p(f"  GEMINI MODEL COMPARISON -- BC Wine AI Agent")
    p(f"  Models: {', '.join(MODELS)}")
    p(f"  Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    p(f"  Total API calls: {len(MODELS)} models x 10 queries = {len(MODELS) * 10}")
    p("=" * 80)

    run_test(
        "ORCHESTRATOR",
        ORCHESTRATOR_SYSTEM,
        ORCHESTRATOR_QUERIES,
        MODELS,
    )

    run_test(
        "REASONING (Wine Pairing)",
        PAIRING_SYSTEM,
        PAIRING_QUERIES,
        MODELS,
    )

    run_test(
        "SYNTHESIS",
        SYNTHESIS_SYSTEM,
        SYNTHESIS_QUERIES,
        MODELS,
    )

    print_summary()

    p(f"\n  Finished: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    p("=" * 80)

    _out_file.close()
    print(f"\nResults saved to {os.path.abspath(OUTPUT_FILE)}", flush=True)


if __name__ == "__main__":
    main()
