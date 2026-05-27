# BC Wine AI Agent — Architectural Design

**Status:** Core implementation complete (11 / 12 files done — tests remaining)
**Last Updated:** 2026-05-25
**Stack:** LangGraph · Gemini 3.5 Flash (Vertex AI) · Python 3.12 · FastAPI · HTML/CSS/JavaScript · SQLite (FTS5) · LangSmith

---

## Table of Contents

1. [Overview](#1-overview)
2. [Architecture Diagram](#2-architecture-diagram)
3. [Tool Inventory](#3-tool-inventory)
4. [LangGraph Design](#4-langgraph-design)
5. [Model Selection](#5-model-selection)
6. [System Prompt Blueprint](#6-system-prompt-blueprint)
7. [Tool Orchestration Patterns](#7-tool-orchestration-patterns)
8. [Data Merging & Deduplication](#8-data-merging--deduplication)
9. [Conversation Memory (Multi-Turn)](#9-conversation-memory-multi-turn)
10. [Error Handling & Graceful Degradation](#10-error-handling--graceful-degradation)
11. [Language Convention](#11-language-convention)
12. [Backend API (FastAPI)](#12-backend-api-fastapi)
13. [Frontend & UI Design](#13-frontend--ui-design)
14. [Observability (LangSmith)](#14-observability-langsmith)
15. [Implementation Roadmap](#15-implementation-roadmap)
16. [Verification & Testing Strategy](#16-verification--testing-strategy)
17. [Deployment](#17-deployment)
18. [Open Questions & Future Improvements](#18-open-questions--future-improvements)

---

## 1. Overview

### Purpose

The BC Wine AI Agent is a domain-specific conversational assistant that answers questions about British Columbia (BC) wines by unifying data across **professional critic reviews**, **retail inventory**, **pricing**, and **general wine education**. It is built on LangGraph and acts as a single ReAct agent that orchestrates eight specialized tools.

### Target Users

Anyone who needs information about BC wines:

- Casual drinkers exploring BC wine for the first time.
- Wine enthusiasts looking for tasting notes and critic opinions.
- Sommeliers and retail buyers cross-referencing inventory and prices.
- Importers evaluating wines for export.
- Cooks looking for food-pairing suggestions.
- Students of wine using the system as an interactive learning tool.

The interface meets all of them at their level — the same chat surface answers a beginner's "what's a Riesling" and an importer's "find me a BC Pinot Noir under $50 in stock at multiple retailers" without mode switching.

### Success Criteria

| Criterion | Target |
|---|---|
| End-to-end latency on a typical query | ≤ 8 seconds |
| Store cross-referencing when a wine is buyable | ≥ 3 distinct sources |
| Hallucination rate (fabricated scores / vintages / wineries) | 0 in the golden-query test set |
| Multi-turn reference resolution ("the second one", "cheaper one") | Works on ≥ 90% of test cases |
| Graceful degradation when one tool fails | Turn completes; failure is noted |

### Scope

**In scope:**
- Inventory lookup across 4 BC retailers + the government store.
- Aggregated professional reviews (WineAlign + Gismondi).
- Food pairing recommendations.
- Wine education questions (regions, varietals, techniques).
- Multi-turn conversation with persistent memory.
- Streaming UX showing intermediate tool calls.
- Web UI (FastAPI backend + vanilla HTML/CSS/JS frontend) styled to match the [SUM AI](https://sumai.ca) brand.

**Out of scope (for now):**
- Korean-language output (English-only system; deferred).
- User accounts / per-user authentication.
- Order placement or payment.
- Mobile-native UI.

---

## 2. Architecture Diagram

```
                       ┌─────────────────────────┐
                       │   User (browser)        │
                       │   HTML / CSS / JS UI    │
                       │   (SUM AI design lang.) │
                       └──────────────┬──────────┘
                                      │ HTTPS
                                      │ POST /api/chat (SSE stream)
                                      ▼
                       ┌─────────────────────────┐
                       │  FastAPI Backend        │
                       │  app.py                  │
                       │  - /api/chat (stream)   │
                       │  - /api/session         │
                       │  - static/* (assets)    │
                       └──────────────┬──────────┘
                                      │
                                      ▼
                       ┌─────────────────────────┐
                       │  Validation Gate         │
                       │  validation.py           │
                       │  (Gemini Flash, temp=0)  │
                       │  Pydantic-structured     │
                       │  ──────────────────────  │
                       │  INVALID → in-language   │
                       │  rejection → SSE → END   │
                       └──────────────┬──────────┘
                                      │ VALID
                                      │ astream_events()
                                      ▼
                       ┌─────────────────────────┐
                       │   LangGraph Application  │
                       │   build_graph()          │
                       │   (agent.py)             │
                       └──────────────┬──────────┘
                                      ▼
                  ┌──────────────────────────────────┐
                  │  ReAct Orchestrator (Node)        │
                  │  Model: Gemini 3.5 Flash          │
                  │  Role: intent → tool selection    │
                  │        → response shaping         │
                  └─┬──┬──┬──┬──┬──┬──┬──┬──────────┘
                    │  │  │  │  │  │  │  │
        ┌───────────┘  │  │  │  │  │  │  └──────────────┐
        ▼              ▼  ▼  ▼  ▼  ▼  ▼                  ▼
   ┌─────────┐ ┌────────┐ ┌────────┐ ┌──────────┐ ... ┌─────────────┐
   │bcliquor │ │marquis │ │okanagan│ │everything│     │ reasoning_  │
   │         │ │        │ │cellars │ │_wine     │     │ pair_wine   │
   └─────────┘ └────────┘ └────────┘ └──────────┘     │ (Flash)     │
   ┌─────────┐ ┌─────────────┐ ┌──────────────┐       └─────────────┘
   │winealign│ │gismondi (DB)│ │tavily (web)  │
   │  AUTH   │ │ SQLite FTS5 │ │   AUTH       │
   └─────────┘ └─────────────┘ └──────────────┘
   ┌──────────────┐
   │robert_parker │
   │  AUTH (JWT)  │
   └──────────────┘
                                      │
                                      │ (tool results in messages)
                                      ▼
                       ┌─────────────────────────┐
                       │  compact_tool_results    │
                       │  Pure Python, no LLM     │
                       │  - incremental merge     │
                       │    into wine_context     │
                       │  - replace ToolMessages  │
                       │    with top-5 projection │
                       │    (same id → reducer    │
                       │     replaces in place)   │
                       │  - pass-through Tavily / │
                       │    pair_wine / prefs     │
                       └──────────────┬──────────┘
                                      │ (loop back to orchestrator
                                      │  for next ReAct round)
                                      ▼
                       ┌─────────────────────────┐
                       │  merge_results (Node)    │
                       │  Pure Python, no LLM     │
                       │  - final pass (mostly    │
                       │    no-op on compact msgs)│
                       │  - update last_recs from │
                       │    wine_context tail     │
                       └──────────────┬──────────┘
                                      ▼
                       ┌─────────────────────────┐
                       │  format_response (Node)  │
                       │  Model: Gemini 3.5 Flash │
                       │  Role: final formatting  │
                       └──────────────┬──────────┘
                                      ▼
                       ┌─────────────────────────┐
                       │  END                    │
                       └──────────────┬──────────┘
                                      │
            ┌─────────────────────────┼─────────────────────────┐
            ▼                         ▼                         ▼
   ┌─────────────────┐     ┌─────────────────┐       ┌─────────────────┐
   │  SqliteSaver    │     │  LangSmith      │       │ Streamed tokens │
   │ Checkpoint      │     │ Trace export    │       │ → SSE → browser │
   │ data/           │     │ (every span)    │       │                 │
   │ checkpoints.db  │     │                 │       │                 │
   └─────────────────┘     └─────────────────┘       └─────────────────┘
```

### Edge Legend

- The ReAct orchestrator self-loops via standard LangGraph ReAct semantics: each turn it may emit zero or more `tool_calls`. Those calls are dispatched in parallel by the `ToolNode`, results are appended to `messages`, and control returns to the orchestrator. The loop exits when the orchestrator produces an AIMessage with no `tool_calls`.
- `merge_results` and `format_response` run **once** per turn, after the ReAct loop terminates.
- Checkpoints persist after every super-step.
- LangSmith receives spans for every LLM call and tool call automatically when `LANGCHAIN_TRACING_V2=true`.

---

## 3. Tool Inventory

Eight tools total — all implemented. Specifications below match the shipping code.

### Summary Table

| # | Tool (file) | Source | Auth | Returns | Typical Latency | Primary Use |
|---|---|---|---|---|---|---|
| 1 | `bcliquor_tool.py` | BC Liquor Stores (gov't) | none | `list[BCLiquorResult]` | ~1 s | Inventory + consumer ratings + BC VQA flag |
| 2 | `winealign_tool.py` | WineAlign critic reviews | required | `list[WineAlignResult]` | 3–10 s | Multi-critic professional reviews + drink windows |
| 3 | `everythingwine_tool.py` | Everything Wine (Vancouver) | none | `list[EverythingWineResult]` | ~2 s | Pickup/delivery availability |
| 4 | `okanagan_cellars_tool.py` | Okanagan Cellars (Vancouver, 2 locations) | none | `list[OkanaganCellarsResult]` | ~1 s | Exact stock counts, large-format bottles |
| 5 | `marquis_tool.py` | Marquis Wine Cellars (Vancouver, curated) | none | `tuple[list[MarquisResult], int]` | ~1 s | Curated picks, MSRP, hierarchical categories |
| 6 | `tavily_tool.py` | Tavily web search API | required (paid) | `tuple[list[TavilyResult], str \| None]` | ~2 s | Pairings (niche cuisines), education, regions |
| 7 | `gismondi_tool.py` | Anthony Gismondi reviews via local SQLite (FTS5) | none | `list[GismondiResult]` | < 100 ms | Canadian wine authority, deep tasting notes |
| 8 | `robert_parker_tool.py` | Robert Parker Wine Advocate (Algolia API) | required (subscription) | `list[RobertParkerResult]` | ~1 s | World-class ratings, tasting notes, drink windows |

### Per-Tool Detail

#### 3.1 `search_bcliquor` — BC Liquor Stores

```python
async def search_bcliquor(
    query: str,
    max_pages: int = 2,
    category: str | None = None,   # "wine" | "beer" | "spirits"
) -> list[BCLiquorResult]
```

**Unique value:** Only source providing **consumer ratings** (user votes), **store_count** (how many BC stores carry it), **available_units** (total inventory across all stores), and the **BC VQA** certification flag.

**When the orchestrator should call it:**
- User asks about price, availability, or "where can I buy".
- User wants consumer (non-expert) sentiment.
- User specifies a budget filter.
- User explicitly mentions BC VQA or wants certified BC wines.

**Notes:** Pagination via `max_pages`; default returns up to 48 results. `tasting_notes` may be the literal value `False` from the API (handled in the tool).

---

#### 3.2 `search_winealign` — Professional Critic Reviews

```python
async def search_winealign(
    query: str,
    max_pages: int = 3,
    include_reviews: bool = True,
) -> list[WineAlignResult]
```

**Unique value:** **Multi-critic reviews** (John Szabo MS, Sara d'Amato, Anthony Gismondi, et al.) with individual scores, full tasting notes, value ratings (0–5 stars), and **drink windows** (e.g., "Drink 2025–2032").

**When the orchestrator should call it:**
- User asks "what do critics think" or "is this worth buying".
- User wants aging guidance.
- User wants value-for-money analysis.

**Notes:** Slow (3–10 s). Requires `WINEALIGN_EMAIL` / `WINEALIGN_PASSWORD` in `.env`. Auto-relogin on session expiry. Politeness delay: 0.5 s between requests. **Limit:** the orchestrator must not call this more than twice per turn.

---

#### 3.3 `search_everything_wine` — Everything Wine (Vancouver)

```python
async def search_everything_wine(query: str) -> list[EverythingWineResult]
```

**Unique value:** **3-level stock status** per result: (1) warehouse delivery, (2) in-store pickup, (3) "check other stores". Other store tools collapse availability to a single boolean.

**When the orchestrator should call it:**
- User explicitly wants Vancouver-area pickup or home delivery.
- User asks about logistics ("can I get it today?").

**Notes:** HTML scraping; fragile to layout changes. No pagination — single page response.

---

#### 3.4 `search_okanagan_cellars` — Okanagan Cellars (Vancouver, 2 locations)

```python
async def search_okanagan_cellars(query: str) -> list[OkanaganCellarsResult]
```

**Unique value:** **Exact integer stock_qty** per SKU; **unit_size** (750ml, 1.5L, etc.) — useful for users seeking magnums or half-bottles.

**When the orchestrator should call it:**
- User wants precise bottle count availability.
- User asks about non-standard sizes.

**Notes:** Returns all matches in one request — no pagination. `_dc` cache-bypass timestamp baked in. Returns out-of-stock items too (filter on `in_stock` when needed).

---

#### 3.5 `search_marquis` — Marquis Wine Cellars (Vancouver, curated)

```python
async def search_marquis(
    query: str,
    limit: int = 30,
    skip: int = 0,
) -> tuple[list[MarquisResult], int]   # (results, total_count)
```

**Unique value:** **Hierarchical category strings** (e.g., `["White Wine", "Chardonnay", "British Columbia", "Okanagan"]`) — only source that provides type → grape → region → subregion. Also has **retail_price (MSRP)** alongside the sale price.

**When the orchestrator should call it:**
- User wants curated/boutique selections.
- User wants to know MSRP vs sale price discount.
- Query is varietal-based and benefits from hierarchical categorization.

**Notes:** Returns a `tuple` (not a bare list). Image URLs are stored as a JSON-encoded string in the API response — the tool already parses these.

---

#### 3.6 `search_tavily` — Web Search Fallback

```python
async def search_tavily(
    query: str,
    max_results: int = 5,
    search_depth: str = "basic",   # "basic" | "advanced"
    include_answer: bool = True,
) -> tuple[list[TavilyResult], str | None]   # (results, answer_summary)
```

**Unique value:** General web knowledge with an **AI-generated answer summary** included in the response.

**When the orchestrator should call it:**
- User asks about food pairings for **non-Western cuisines** (Korean, Sichuan, Thai, Indian, etc.) where built-in pairing principles need cultural specificity.
- User asks about a wine region, winemaking technique, or piece of wine history not covered by store tools.
- All store tools return zero results for a queried wine name (disambiguation fallback).

**Notes:** Requires `TAVILY_API_KEY`. Paid per request — the orchestrator should **call at most once per turn** and never as a first-line tool for inventory/pricing.

---

#### 3.7 `search_gismondi` — Gismondi Reviews (SQLite + FTS5)

```python
async def search_gismondi(
    query: str,
    limit: int = 10,
    score_min: int = 0,            # filter score_100 >= N
    price_max: float | None = None, # CAD ceiling; None = no cap
    bc_only: bool = True,           # bias to BC-region wines
) -> list[GismondiResult]
```

```python
class GismondiResult(BaseModel):
    note_id: int
    title: str
    score_100: int
    score_20: str                   # e.g., "16¼/20"
    region: str
    tasting_notes: str
    tasting_date: str
    taster: str                     # usually "Anthony Gismondi"
    price: float | None
    price_format: str               # e.g., "750ml"
    price_channel: str | None
    producer: str
    grape: list[str]                # split from " - " delimited string
    distributor: str | None
    cspc: str | None
    upc: str | None
    url: str
```

**Implementation (shipped in `gismondi_tool.py`):**
- Backing store: `data/wines.db` (built by `build_db.py` from the `gismondi-canada-wines` git submodule, refreshed Tue/Thu/Sat by `.github/workflows/update_db.yml`).
- Query: `wines_fts MATCH ?` joined to `wines` via `note_id == rowid`.
- Query sanitization: `re.sub(r'[^\w\s]', ' ', query)` strips FTS5-significant chars (apostrophes, parens, colons) before binding. Multiple tokens are implicitly AND-ed by FTS5.
- `bc_only=True`: append `AND region LIKE '%British Columbia%'`.
- `score_min` / `price_max` applied as additional `WHERE` clauses. When `price_max` is set, NULL-priced rows are excluded; when unset, all rows pass the price filter.
- `grape` field: split the source string on ` - ` into a list.
- Returns at most `limit` rows, ordered by `score_100 DESC, tasting_date DESC`.
- `_search_sync()` (blocking) wrapped via `asyncio.to_thread()` so the async signature is honored without blocking the event loop.

**Unique value:** Deep, single-expert (Anthony Gismondi) tasting notes for **Canadian-only** wines, with a far longer historical archive than what WineAlign returns for any single critic. Excellent for BC wine discovery.

**When the orchestrator should call it:**
- User asks about a specific Canadian/BC wine and wants a deep tasting note.
- User wants Gismondi's specific opinion (he's a recognized name within Canadian wine media).
- Discovery queries ("best BC Riesling under $40") benefit from `bc_only=True` + `score_min=90`.

**Speed:** Local SQLite FTS5 — sub-100 ms.

---

#### 3.8 `search_robert_parker` — Robert Parker Wine Advocate

```python
async def search_robert_parker(
    query: str,
    rating_min: int = 50,
    hits_per_page: int = 10,
    page: int = 0,
    sort: str = "relevancy",       # "relevancy" | "rating" | "vintage" | "price"
    country: str | None = None,    # e.g. "Canada"
    region: str | None = None,     # e.g. "British Columbia"
    color: str | None = None,      # "Red" | "White" | "Rosé"
    variety: str | None = None,    # e.g. "Pinot Noir"
) -> list[RobertParkerResult]
```

```python
class RobertParkerTastingNote(BaseModel):
    reviewer: str
    rating: str
    content: str
    published_at: str | None
    article_title: str | None
    producer_note: str | None

class RobertParkerResult(BaseModel):
    wine_id: str
    display_name: str              # e.g. "2017 Martin's Lane Winery Pinot Noir Naramata Ranch"
    producer: str
    name: str
    vintage: int | None
    color_class: str               # "Red", "White", etc.
    country: str
    region: str
    sub_region: str | None         # e.g. "Okanagan Valley"
    appellation: str | None
    sub_appellation: str | None
    varieties: list[str]           # e.g. ["Pinot Noir"]
    rating_display: str            # e.g. "94", "89+", "91+?"
    rating_computed: float         # sortable numeric rating
    price_low: float | None
    price_high: float | None
    drink_date_low: int | None
    drink_date_high: int | None
    dryness: str | None
    wine_type: str | None          # "Table", "Sparkling", etc.
    certified: list[str]           # e.g. ["Organic"]
    last_reviewer: str | None
    tasting_notes: list[RobertParkerTastingNote]
    slug: str | None
```

**Implementation:**
- Algolia-backed REST API at `api.robertparker.com/v2/v2/algolia`.
- Auth: automated login — `GET /users/csrf-token` (obtains CSRF token + cookie), then `POST /users/login` with header `xsrf-token` and body `{"username", "password", "device"}`. Returns JWT `accessToken` (~30-day expiry). On 401, auto-relogins.
- Filtering via Algolia `filters` string syntax (e.g. `"rating_computed:90 TO 100 AND country:Canada AND region:'British Columbia'"`). `facetFilters` array is ignored by this API.
- `.env` keys: `ROBERT_PARKER_EMAIL`, `ROBERT_PARKER_PASSWORD`, `ROBERT_PARKER_API_KEY` (public key `7ZPW...`).

**Unique value:** **Robert Parker / Wine Advocate ratings** — the single most influential wine scoring system globally. Provides authoritative **100-point ratings**, detailed tasting notes from expert reviewers (e.g., Mark Squires for Canada), **drink windows** (e.g., 2024–2035), **producer notes** (winemaker context per vintage), and **article references**. Coverage spans all major wine regions worldwide.

**When the orchestrator should call it:**
- User asks "what does Robert Parker rate this wine" or wants RP scores specifically.
- User wants internationally recognized ratings (vs. Canadian-focused WineAlign/Gismondi).
- User wants global comparison — e.g., "how does this BC Pinot compare to Burgundy?"
- Discovery queries for high-rated wines across any region.

**Notes:** Requires an active subscription (~$99 USD/year). Auto-login handles token refresh transparently. **Limit:** the orchestrator should call at most once per turn.

---

## 4. LangGraph Design

### 4.1 `AgentState` (TypedDict)

```python
# state.py
from typing import TypedDict, Annotated, NotRequired
from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages


class StorePrice(TypedDict):
    store: str               # "bcliquor" | "marquis" | "okanagan" | "everythingwine"
    price: float
    on_sale: bool
    in_stock: bool


class MergedWineRecord(TypedDict):
    normalized_key: str      # producer_slug + wine_slug + vintage
    display_name: str
    producer: str
    vintage: int | None
    prices: list[StorePrice]
    best_price: StorePrice | None
    critic_reviews: list[dict]   # combined winealign + gismondi + robert_parker
    consumer_rating: float | None
    is_bc_vqa: bool


class UserPreferences(TypedDict, total=False):
    budget_max: float
    preferred_varietals: list[str]    # e.g., ["Riesling", "Pinot Noir"]
    sweetness: str                    # "dry" | "off-dry" | "sweet"
    style: str                        # "elegant" | "powerful" | "fresh"


class AgentState(TypedDict):
    # Required — managed by add_messages reducer
    messages: Annotated[list[BaseMessage], add_messages]

    # Optional — populated as the conversation evolves
    wine_context: NotRequired[dict[str, MergedWineRecord]]   # keyed by normalized_key
    user_preferences: NotRequired[UserPreferences]
    last_recommendations: NotRequired[list[str]]             # normalized_keys from previous turn
    tool_call_log: NotRequired[list[dict]]                   # for tracing & dedup
```

**Why these fields:**
- `messages` — standard. `add_messages` reducer auto-appends and de-duplicates by id.
- `wine_context` — the cross-tool merge cache, keyed for O(1) lookup in subsequent turns.
- `user_preferences` — accumulates as the user reveals stable preferences; updated via the `update_preferences` tool (§9).
- `last_recommendations` — enables reference resolution like "the second one".
- `tool_call_log` — diagnostic; also used to suppress redundant tool calls within a turn.

### 4.2 Nodes

| Node | Type | Function | LLM call? |
|---|---|---|---|
| `orchestrator` | Custom Python wrapping `ChatGoogleGenerativeAI.bind_tools(TOOLS)` | Intent classification, tool selection, post-tool reasoning. Temperature 0.2. Receives user prefs + cached wine_context as system context. | Yes — Gemini 3.5 Flash |
| `tools` | `tool_node_with_logging` wrapping `ToolNode` | Dispatches `tool_calls` to wrapped tool functions, then appends each call to `tool_call_log` for downstream auditing | No |
| `compact_tool_results` | Custom Python (`compaction.py`) | Runs after every `tools` round. (1) Identifies this batch of ToolMessages (since last AIMessage). (2) Incrementally merges raw results into `wine_context` via `merge_tool_results` + `_merge_into_context`. (3) Harvests `update_preferences` payloads. (4) Replaces each compactable ToolMessage with a same-id projection (top-5 rows, key fields only, `results: []`). The `add_messages` reducer replaces in place, so the **next orchestrator round sees ~10× less raw JSON**. Pass-through: `search_tavily`, `reasoning_pair_wine`, `update_preferences`. See §8.9. | No |
| `merge_results` | Custom Python | Walks `state["messages"]`, parses `ToolMessage` JSON, normalizes wine names, dedups across stores, aggregates into `wine_context`. Also harvests `update_preferences` calls. With compaction active, this becomes a defensive final pass: most ToolMessages now carry `results: []` and are no-op'd; `wine_context` is already populated by `compact_tool_results`. Sets `last_recommendations` from `wine_context` tail (insertion order). | No |
| `format_response` | Custom (single LLM call) | Synthesis pass. Takes user query + orchestrator draft + compact `wine_context` + supplementary tool outputs (pairing reasoning, Tavily answers) and emits the canonical markdown skeleton (§6.5). Replaces the orchestrator's last `AIMessage` in-place by reusing its `id` so streaming consumers see only the synthesized text. Temperature 0.0. Skipped for off-topic turns (empty `wine_context` AND empty aux outputs). | Yes — Gemini 3.5 Flash |

#### Tool-rounds safety net

`should_continue` enforces a hard cap of `MAX_TOOL_ROUNDS = 3` rounds of tool calls per user turn (counted as AIMessages-with-tool_calls since the most recent HumanMessage). When the cap is hit, the graph short-circuits straight to `merge_results` even if the orchestrator wanted another round. This protects against runaway retry loops that previously hit `recursion_limit` and crashed the run. `format_response_node` includes a fallback path for this case: if the most recent AIMessage still has `tool_calls`, it is reused as the intent signal and synthesis writes the final response from data alone.

### 4.3 Edges

```
START
  └→ orchestrator
       ├→ tools  (if tool_calls present AND tool rounds < MAX_TOOL_ROUNDS)
       │    └→ compact_tool_results
       │         └→ orchestrator  (ReAct self-loop — now over compact messages)
       └→ merge_results  (when orchestrator emits AIMessage with no tool_calls,
                          OR when MAX_TOOL_ROUNDS is reached)
             └→ format_response
                  └→ END
```

### 4.4 Checkpointer

```python
from langgraph.checkpoint.sqlite import SqliteSaver

checkpointer = SqliteSaver.from_conn_string("data/checkpoints.db")
graph = builder.compile(checkpointer=checkpointer)
```

- Thread ID = chat session ID (UUID generated by the frontend on first message; persisted in a browser cookie).
- Survives server restarts. `data/checkpoints.db` is added to `.gitignore`.

### 4.5 Tool Registration

Tools are wrapped with `@tool` (from `langchain_core.tools`) **and** the `safe_tool` decorator (§10) before being passed to `create_react_agent`. Each tool's docstring is what the orchestrator sees as the tool description — these docstrings must mirror the "When the orchestrator should call it" guidance in §3.

```python
# Pseudocode
from langgraph.prebuilt import create_react_agent

TOOLS = [
    safe_tool(search_bcliquor_tool),
    safe_tool(search_winealign_tool),
    safe_tool(search_everything_wine_tool),
    safe_tool(search_okanagan_cellars_tool),
    safe_tool(search_marquis_tool),
    safe_tool(search_tavily_tool),
    safe_tool(search_gismondi_tool),
    safe_tool(reasoning_pair_wine_tool),
    safe_tool(update_preferences_tool),   # §9
]

orchestrator = create_react_agent(
    model=get_llm(),
    tools=TOOLS,
    state_modifier=SYSTEM_PROMPT,  # §6
)
```

### 4.6 Human-in-the-Loop Clarification

When the user's query or the available data is genuinely ambiguous, the orchestrator can pause the graph and ask the user a clarifying question instead of guessing. This is implemented as a tool that triggers a LangGraph `interrupt()` rather than as a dedicated node — the orchestrator decides when to ask, the same way it decides which store to query.

**Mechanism.** `ask_user_clarification_tool(question, options=None)` calls `langgraph.types.interrupt({"type": "clarification_request", "question": ..., "options": [...]})`. The checkpointer freezes the graph state at that point. `app.py` polls `graph.aget_state(config)` after the stream ends; if `snapshot.interrupts` is non-empty, it emits an SSE `clarification_request` event carrying the question and options. The frontend renders option chips + a hint. The user either clicks a chip (which fills the input box and submits) or types free text. On the next `/api/chat` call, `app.py` detects the pending interrupt again and resumes with `Command(resume=req.message)` instead of `{"messages": [...]}` — the tool's `interrupt()` returns the user's reply, the tool finishes normally, and the next orchestrator round proceeds with that reply in scope.

**Why a tool, not a node.** The orchestrator already controls tool selection. Wiring clarification as a node would require a separate routing decision and structured "I want to ask" output. A tool fits the existing ReAct pattern, gives the orchestrator natural fan-out (`ask_user_clarification_tool` can be one of several tool_calls in a round), and lets the prompt's behavioral rules drive when to use it.

**Triggers (`prompts.py` Rule 9).**
- User request has 2+ plausible interpretations with materially different answers (e.g. "좋은 와인 추천해줘" with no budget/style/occasion hint).
- Top tool results tie and a user preference would break the tie (e.g. 5 Chardonnays at similar scores from different producers).
- Essential info is missing (food pairing with no dish; "the second one" with no prior context in `wine_context`).

**Anti-triggers.** Don't ask when a reasonable default exists from `user_preferences` or `wine_context`, when "here are 2-3 picks across styles" is a fine answer, or for informational/educational queries. Don't stall by clarifying instead of answering.

**Round counting.** A round whose `tool_calls` are **all** `ask_user_clarification_tool` is excluded from `_count_tool_rounds_this_turn`, so clarifications don't push the orchestrator toward the `MAX_TOOL_ROUNDS = 3` data-tool safety stop. A separate counter `_count_clarifications_this_turn` enforces `MAX_CLARIFICATIONS_PER_TURN = 3`. When the cap is reached, `orchestrator_node` appends a "clarification cap reached — proceed with best-effort answer" line to the system prompt so the model stops asking and synthesizes a response.

**Validation skip on resume.** Short clarification replies like "$50 under" or "the cheaper one" could trip the off-topic validator. `app.py` detects resume turns via `aget_state(config).interrupts` and skips the validation gate in that branch — the message is already in-context as a clarification reply.

**Frontend treatment.** The `ask_user_clarification_tool` tool badge is intentionally **skipped** by `static/app.js` (no `addToolBadge` on `tool_start`). Because the tool blocks on `interrupt()`, its `tool_end` doesn't fire until the user replies, which would leave the spinner stuck and force the global "done" event to mark it completed prematurely. The dedicated clarification UI is the only visible signal; on resume, the tool's `tool_end` is also ignored so no orphan badge appears.

**Files involved.**
- `agent.py` — `ask_user_clarification_tool`, `MAX_CLARIFICATIONS_PER_TURN`, `_count_clarifications_this_turn`, round-counter exclusion, system-prompt cap notice.
- `prompts.py` — Tool Catalog entry + Behavioral Rule 9.
- `app.py` — interrupt detection on entry → `Command(resume=...)`; post-stream interrupt detection → SSE `clarification_request`; validation skip on resume.
- `static/app.js` — `clarification_request` handler, `renderClarification()`, badge skip for the clarification tool.
- `static/styles.css` — `.clarification`, `.clarification-question`, `.clarification-options`, `.clarification-option-btn`, `.clarification-hint`.

---

## 5. Model Selection

### 5.1 One Model Everywhere: Gemini 3.5 Flash

Every node and sub-LLM in the agent uses **`gemini-3.5-flash`** for now. This includes:

- The ReAct orchestrator (tool selection + reasoning).
- The `reasoning_pair_wine` sub-tool.
- The terminal `format_response` synthesis node.

Cost-tier optimization (cheaper models for synthesis, more expensive for reasoning) is **deferred**. Picking a single model keeps the graph simple to build, test, and reason about. If a follow-up engineer wants to swap models per node later, the only file that changes is the model factory (`models.py`).

### 5.2 Model Factory

Lift the pattern that already exists in `test_gemini_models.py`:

```python
# models.py
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
```

**Why Gemini 3.5 Flash:**
- Native parallel tool calling (essential for the multi-store fan-out pattern in §7).
- Strong tool-selection accuracy at the 7-tool scale this agent uses.
- Stable GA release (2026-05-19).
- Fast enough for the ≤ 8 s end-to-end target.

### 5.3 Auth

Vertex AI authentication uses Google Cloud Application Default Credentials. Locally:

```bash
gcloud auth application-default login
```

In production, set `GOOGLE_APPLICATION_CREDENTIALS` to a service account key file (see §17).

---

## 6. System Prompt Blueprint

The full text lives in `prompts.py`. This section specifies the **structure and key directives**. The orchestrator system prompt has five sections:

### 6.1 Identity & Domain (paragraph)

> *"You are the BC Wine Expert AI Agent — a domain assistant that helps anyone, from curious beginners to professional sommeliers, find, evaluate, and learn about wines from British Columbia, Canada. You source data exclusively through the provided tools; you never invent wineries, vintages, scores, or prices. When tool data is missing, you say so explicitly."*

### 6.2 BC Regional Knowledge Anchor

A bounded list the orchestrator must know without tool calls, so it can interpret user queries that name regions:

- **Okanagan Valley** (largest BC region) → sub-appellations: Naramata Bench, Black Sage Bench, Golden Mile, Oliver, Osoyoos, Kelowna, Lake Country, Summerland.
- **Similkameen Valley**
- **Fraser Valley**
- **Vancouver Island**
- **Gulf Islands**
- **Cowichan Valley** (within Vancouver Island GI)

Plus a short list of flagship wineries the orchestrator should recognize without searching: Mission Hill, Quails' Gate, CheckMate, Tantalus, Blue Mountain, Burrowing Owl, Osoyoos Larose, Martin's Lane, Synchromesh, Poplar Grove, Blue Grouse, Stag's Hollow.

Signature varietals: Riesling, Pinot Noir, Chardonnay, Pinot Gris, Syrah, Gamay, sparkling (traditional method).

### 6.3 Tool Catalog (with selection criteria)

Each tool gets one paragraph. Example (full version for `search_winealign`):

> *`search_winealign(query, max_pages=3, include_reviews=True)` — Professional critic reviews from WineAlign, Canada's largest wine review platform. Returns multiple critic opinions per wine with individual scores, full tasting notes, value ratings (0–5 stars), and drink windows (e.g., "Drink 2025-2032"). Use when the user asks "what do critics think", "is X worth it", or wants aging guidance. **Slow (3–10s) and authenticated** — do not call more than twice per turn. Always attribute citations by critic name (e.g., "John Szabo MS scored it 93").*

The other six follow the same template. Each tool's description **must** include: signature, returns, latency, auth requirements, call limits per turn, and the "when to call" trigger phrases.

### 6.4 Behavioral Rules

The orchestrator's system prompt encodes 15 rules. The first 10 are the original behavior; rules 11–15 were added across quality-eval iterations (see §16.5) to fix specific failure modes (tool storms, fabricated retailers, Tavily abuse, link omission).

1. **Parallelize inventory checks.** When the user asks "where can I buy X" or wants pricing, emit `tool_calls` for `search_bcliquor_tool`, `search_marquis_tool`, `search_okanagan_cellars_tool`, and `search_everything_wine_tool` in a single response.
2. **Never invent.** If no tool returned a score, vintage, or price, do not state one.
3. **Attribute critics by name.** Quote the critic and source when citing a review.
4. **Cite stores by name** when reporting prices and inventory.
5. **Prefer in-stock results** when ranking recommendations.
6. **Use Tavily sparingly.** It is paid. Only call it for non-Western pairing questions, regional/educational queries, or to disambiguate a wine name when all store tools return empty.
7. **Use `reasoning_pair_wine_tool` for non-trivial pairings.** Common pairings (steak + Cabernet, salmon + Pinot) — answer from built-in knowledge. Non-trivial — invoke the sub-LLM.
8. **Respect the multi-turn state.** Before recommending a wine, scan `wine_context` — if the user already saw it last turn, reference it as such ("the Tantalus Riesling I mentioned earlier").
9. **Resolve references.** "The second one" / "the cheaper one" / "tell me more" → resolve against `last_recommendations` and `wine_context`.
10. **Calibrate depth to audience.** A beginner question gets a friendly, jargon-light answer; a sommelier question gets the full critic detail. Read the user's vocabulary as a cue.
11. **Always include links.** Wrap each cited store / critic review in a markdown link using the URL from the tool result.
12. **Hard cap on tool calls per turn.** At most 2 rounds: round 1 is a parallel fan-out; round 2 is an optional targeted follow-up. Total ≤ 8 calls. Backed by `MAX_TOOL_ROUNDS` in `agent.py` (§4.2) — exceeding the prompt cap still triggers the code-level short-circuit.
13. **Off-topic queries: respond directly, no tools.** Weather / sports / jokes get a 1–2 sentence answer + gentle redirect to wine. Calling Tavily for these is forbidden.
14. **Tavily is FORBIDDEN for "where can I buy / pricing / inventory" questions.** Tavily routinely fabricates retailer URLs (Legacy Liquor, ZYN.ca, BSW Liquor) that then propagate into the response. When store tools come back empty, tell the user so — do not paper over with web search.
15. **Never invent retailers.** Only mention stores that appear in tool results: BC Liquor, Marquis Wine Cellars, Everything Wine, Okanagan Cellars. No out-of-province retailers unless they appear verbatim in a tool response.

### 6.5 Output Contract

The synthesis pass (`format_response_node`, §4.2) reads `SYNTHESIS_SYSTEM_PROMPT` and emits the canonical skeleton:

```
[Lead — one sentence naming the specific wine, producer, and vintage if known]

**Why this wine**
- Critic scores (attributed: "John Szabo (WineAlign) — 92 pts")
- Style / tasting notes (1–2 lines from tool data)
- Drink window if available

**Where to buy**

| Store | Price (CAD) | Availability |
|-------|-------------|--------------|
| [BC Liquor](https://www.bcliquorstores.com/product/...) | $34.99 | In stock (612 units across 73 stores) |
| [Marquis Wine Cellars](https://www.marquis-wines.com/...) | $39.99 | 13 bottles in stock |
| [Everything Wine](https://www.everythingwine.ca/...) | $36.50 | Warehouse delivery |

**Pairing note** (only when the user mentioned a food or dish)
[1–2 sentences explaining the pairing logic]
```

The synthesizer follows these structural rules:

- **Treat the orchestrator's draft as the intent signal** — which wines to feature, which `wine_context` entries are fuzzy-search noise. The synthesizer reformats, it does not re-select.
- **One row per store, all stores that carry each wine.** Do not collapse to `best_price` only — users compare across retailers.
- **OMIT the "Where to buy" section entirely** for a featured wine if it has zero store rows in the data. Do not invent placeholders like "Retail Database / - / No current local retail listings" — empty placeholder tables are worse than no table.
- **Specific-wine query, no exact match in data** → say "We could not find this exact wine at the BC retailers we checked", then recommend 1–2 close alternatives from the **same varietal and region**. Never silently swap in unrelated wines (e.g., a French Bordeaux when the user asked about a BC Syrah).
- **Recommendation query** (pairing, "under $X", "best for Y") → the wine data IS the answer pool. Pick 2–3 wines from it; never end such a query with "we could not find anything" if any matching wine exists.
- **Critic scores require an exact bottling match.** A review of "Painted Rock Syrah Cabernet Sauvignon 2021" does not back a claim about "Painted Rock Syrah 2021" — they are different wines. Say "no critic reviews available for this specific bottling" rather than borrow scores from the adjacent bottling.

The frontend renders this markdown into HTML before showing it to the user (see §13).

---

## 7. Tool Orchestration Patterns

Three patterns the orchestrator uses, encoded by behavioral rules in the system prompt rather than by graph nodes (so that Gemini's native parallel tool calling does the work).

### 7.1 Parallel Fan-Out (Inventory Queries)

Trigger: user asks about price, availability, or "where can I buy X".

```
t=0   User: "Where can I buy CheckMate Chardonnay 2019 in BC?"
t=0   orchestrator emits 4 tool_calls in one AIMessage:
          ├── search_bcliquor("CheckMate Chardonnay 2019")
          ├── search_marquis("CheckMate Chardonnay 2019")
          ├── search_okanagan_cellars("CheckMate Chardonnay 2019")
          └── search_everything_wine("CheckMate Chardonnay 2019")
t=~1  All 4 ToolMessages return in parallel (~1–2s wall time)
t=~1  orchestrator emits AIMessage with no tool_calls → exit ReAct
t=~1  merge_results → format_response → END
```

### 7.2 Sequential Reasoning + Verification (Pairing)

Trigger: non-trivial pairing question.

```
t=0   User: "What BC wine pairs with miso-glazed black cod?"
t=0   orchestrator calls: reasoning_pair_wine(dish="miso-glazed black cod")
t=~3  Tool returns: "Off-dry BC Riesling or aged Chardonnay; specifically
                    Tantalus Old Vines Riesling or Mission Hill Perpetua."
t=~3  orchestrator then emits 2 tool_calls:
          ├── search_bcliquor("Tantalus Old Vines Riesling")
          └── search_bcliquor("Mission Hill Perpetua Chardonnay")
t=~4  ToolMessages return → orchestrator exits ReAct
t=~4  merge_results → format_response → END
```

### 7.3 Fallback Chain (No Matches → Disambiguation)

Trigger: all store tools return empty.

```
t=0   User: "Do you carry Niche 2021 Pinot Blanc?"
t=0   orchestrator fans out to 4 store tools in parallel
t=~1  All 4 return empty
t=~1  orchestrator calls: search_tavily("Niche 2021 Pinot Blanc BC wine")
t=~3  Tavily returns AI summary: "Niche Wine Company, Lake Country BC — Pinot Blanc 2021"
t=~3  orchestrator retries with corrected name:
          ├── search_bcliquor("Niche Wine Company Pinot Blanc")
          ├── search_marquis("Niche Wine Company Pinot Blanc")
          ├── ...
t=~4  Results arrive → orchestrator exits ReAct
```

---

## 8. Data Merging & Deduplication

### 8.1 Why Merging Is Necessary

The same wine commonly appears in BC Liquor + Marquis + Okanagan Cellars + Everything Wine. Without deduplication, a single recommendation would be repeated four times with slightly different names and prices.

### 8.2 Normalization Algorithm

```python
import re
from rapidfuzz import fuzz

VINTAGE_RE = re.compile(r"\b(19|20)\d{2}\b")
NOISE_WORDS = {"vineyards", "winery", "estate", "cellars", "wines", "vineyard"}

def normalize(name: str, producer: str | None = None) -> tuple[str, str, int | None]:
    """Returns (producer_slug, wine_slug, vintage)."""
    vintage_match = VINTAGE_RE.search(name)
    vintage = int(vintage_match.group()) if vintage_match else None
    cleaned = VINTAGE_RE.sub("", name)
    cleaned = re.sub(r"[^\w\s]", " ", cleaned).lower()
    tokens = [t for t in cleaned.split() if t and t not in NOISE_WORDS]
    wine_slug = " ".join(tokens)
    prod_slug = (producer or "").lower().strip() if producer else ""
    prod_slug = " ".join(t for t in prod_slug.split() if t not in NOISE_WORDS)
    return prod_slug, wine_slug, vintage
```

**Deterministic match:** Two records match iff `(producer_slug, wine_slug, vintage)` are equal.

**Fuzzy fallback:** When two candidate `wine_slug` strings have the **same vintage and same producer_slug** but differ slightly (e.g., one source lists "Old Vines Riesling" and another lists "Riesling Old Vines"), use `rapidfuzz.fuzz.token_set_ratio(a, b) >= 88` to merge.

### 8.3 `MergedWine` Schema

```python
from pydantic import BaseModel

class StorePrice(BaseModel):
    store: str               # "bcliquor" | "marquis" | "okanagan" | "everythingwine"
    price: float
    on_sale: bool = False
    in_stock: bool = True
    url: str | None = None
    stock_qty: int | None = None  # if store provides it (okanagan)

class CriticReviewMerged(BaseModel):
    source: str              # "winealign" | "gismondi"
    critic_name: str
    score: str               # raw display, e.g. "93/100" or "16¼/20"
    tasting_notes: str
    value_rating: int | None = None
    drink_window: str | None = None

class MergedWine(BaseModel):
    normalized_key: str
    display_name: str
    producer: str
    vintage: int | None
    grape: list[str] = []

    prices: list[StorePrice] = []
    best_price: StorePrice | None = None

    critic_reviews: list[CriticReviewMerged] = []
    avg_critic_score: float | None = None   # /100 scale; computed from numeric scores only

    consumer_rating: float | None = None    # from BC Liquor
    consumer_votes: int | None = None

    is_bc_vqa: bool = False
    tasting_notes_consolidated: str | None = None  # longest non-empty
```

### 8.4 Best-Price Selection

1. Filter to in-stock entries.
2. Within in-stock: pick the lowest `price`. Tiebreak by `on_sale=True` first, then alphabetical store name.
3. If no entries are in-stock: pick the lowest `price` overall (and flag "currently out of stock").

### 8.5 Critic Score Aggregation

- **Never average across critics.** Different humans use different rubrics — averaging "John Szabo 93/100" with "Anthony Gismondi 91/100" is misleading.
- The `avg_critic_score` field, if computed, uses **only** scores from the same source family (e.g., all WineAlign critics), normalized to /100, and is presented with the count: "Avg WineAlign: 92.5 (n=3)".
- Display the individual critic reviews alongside any aggregate.

### 8.6 Critic-derived StorePrice (Gismondi)

`GismondiResult` carries `price`, `price_format`, and `price_channel` fields that describe the retail price the critic observed at review time. These are the only retail-price hints available for many BC wines whose names do not exact-match what the store-search tools return. The merge step therefore promotes them into the wine record as synthetic `StorePrice` entries.

```python
# inside _extract_gismondi
if r.get("price") is not None:
    channel = (r.get("price_channel") or "").lower()
    store = next(
        (mapped for hint, mapped in _GISMONDI_CHANNEL_MAP.items() if hint in channel),
        "winery",
    )
    prices.append({
        "store": store,
        "price": float(r["price"]),
        "on_sale": False,
        "in_stock": True,            # Gismondi does not track inventory
        "url": r.get("url"),         # points at the review, not a cart
        "stock_qty": None,
    })
```

Channel mapping: `"BC Liquor" → bcliquor`, `"Marquis" → marquis`, `"Everything Wine" → everythingwine`, `"Okanagan Cellars" → okanagan`. Anything else (e.g., direct-from-winery) falls through to `store="winery"`. The URL points at the Gismondi review so the user can see the context for the price quote.

For symmetry, `_extract_winealign` and `_extract_robert_parker` also return the 5-tuple `(prod_slug, wine_slug, vintage, reviews, prices)` with an empty `prices` list. The merge loop unpacks uniformly and extends each matched record's `prices` array, so `best_price` selection (§8.4) automatically picks up Gismondi-derived prices alongside store-tool prices.

### 8.7 Tool-name resolution in `merge_tool_results`

The JSON payload our `@tool` wrappers emit carries a canonical bare name in its `"tool"` field (`"search_bcliquor"`), but the LangChain `ToolMessage.name` arrives with the binding suffix (`"search_bcliquor_tool"`). Merge prefers the payload's canonical name and falls back to `msg.name` with the `_tool` suffix stripped:

```python
parsed_tool, results = _parse_tool_content(content)
effective_tool = parsed_tool or tool_name
if effective_tool and effective_tool.endswith("_tool"):
    effective_tool = effective_tool[:-5]
```

This was a silent bug for a long time — without the strip, every `ToolMessage` failed the `effective_tool in TOOL_TO_EXTRACTOR` check and `wine_context` stayed empty. Responses still cited stores because the orchestrator's raw draft was visible to it through `state["messages"]`, but the synthesis pass was operating on an empty data blob and could not enforce the skeleton properly. Fixing this was the single biggest quality jump in the eval history (see §16.5, R4 → R5).

### 8.8 Implementation Location

`merge.py` exposes:

```python
def merge_tool_results(messages: list[BaseMessage]) -> dict[str, MergedWine]:
    """
    Scan ToolMessages in the conversation, parse tool results, normalize, and merge.
    Returns a dict keyed by normalized_key, suitable for storing in state["wine_context"].
    """
```

Called from the `merge_results` node — and **also from `compact_tool_results_node`** (§8.9) on each individual tool batch, so `wine_context` is built incrementally during the ReAct loop rather than only at the end.

### 8.9 In-Loop Compaction (`compaction.py`)

A separate node, `compact_tool_results_node`, sits between `tools` and the loop-back to `orchestrator`. Two responsibilities:

**(a) Incremental wine_context merge.** Calls `merge_tool_results` on just this round's `ToolMessage` batch and folds the result into `state["wine_context"]` via `_merge_into_context` — which extends `prices` / `critic_reviews` on duplicate `normalized_key` entries (instead of overwriting) and recomputes `best_price` after the extension. Synthesis facts are therefore ready the moment the loop exits; the final `merge_results_node` becomes a defensive no-op pass.

**(b) ToolMessage compaction.** For each compactable ToolMessage, emits a replacement with the **same `id`** so the LangGraph `add_messages` reducer overwrites in place. The replacement content is a small projection:

```json
{
  "status": "ok",
  "tool": "search_bcliquor",
  "compacted": true,
  "result_count": 24,
  "top_results": [
    {"name": "...", "price": 34.99, "in_stock": true, "vintage": 2021}
  ],
  "results": []
}
```

Two invariants baked into the payload:

1. `results: []` — so any future call to `merge_tool_results` over the message list (e.g. the final `merge_results_node`) iterates an empty array and produces no records, leaving the already-populated `wine_context` untouched.
2. Top-N (default 5, constant `MAX_COMPACT_TOP_N`) carries only the fields the orchestrator needs to decide round-2 actions: name + price + in_stock + vintage for store tools; name + score + critic + vintage for critic tools. Tasting notes, URLs, descriptions, store counts are dropped from the orchestrator's view but remain in `wine_context` for synthesis.

**Pass-through tools.** Three tools are NOT compacted because their raw payload is small *and* has downstream consumers that need it intact:

| Tool | Why pass-through |
|---|---|
| `search_tavily` | `_collect_aux_tool_outputs` (agent.py) reads the `answer` field for synthesis context. |
| `reasoning_pair_wine` | Same aux-collector path — synthesis surfaces the sommelier reasoning. |
| `update_preferences` | `merge_results_node` parses these to populate `user_preferences`. (`compact_tool_results_node` also harvests them, so the final pass is idempotent.) |

**Tool projections** (per `_project_store_row` / `_project_critic_row` in `compaction.py`):

| Tool | Projection fields |
|---|---|
| `search_bcliquor`, `search_marquis`, `search_okanagan_cellars`, `search_everything_wine` | `name`, `price`, `in_stock`, `vintage` |
| `search_winealign` | `wine_name`, top critic score, critic name, vintage |
| `search_gismondi` | `title`, `score_100`/100, taster, vintage |
| `search_robert_parker` | `display_name`, top reviewer rating, reviewer, vintage |

**Why deterministic (no LLM) compaction.** Adding an LLM call between every tool round would (a) add ~1–2 s latency per round, (b) introduce a new failure surface inside the ReAct loop, and (c) risk lossy summaries that prevent the orchestrator from making accurate round-2 decisions. A fixed-shape Python projection avoids all three.

**Stability invariants.** Verified end-to-end:

- SSE `on_tool_end` event in `app.py` fires from the LangGraph tool node, **before** compaction runs. Frontend tool-badge dropdowns still show real tool output.
- `_count_tool_rounds_this_turn` / `should_continue` count AIMessages, not ToolMessages — unaffected by content replacement.
- `MAX_TOOL_ROUNDS=3` safety net — unaffected.
- Off-topic / no-tool-call paths never enter the compaction node.
- Multi-turn reference resolution: `merge_results_node` now derives `last_recommendations` from `list(wine_context.keys())[-10:]` (insertion order — newest at tail).

---

## 9. Conversation Memory (Multi-Turn)

### 9.1 Checkpoint Strategy

- `InMemorySaver` (LangGraph) — process-local; survives across HTTP requests but cleared on server restart. The `SqliteSaver` upgrade for durable persistence is still on the roadmap.
- Thread ID = UUID generated server-side by `POST /api/session`. The frontend mints a **new** thread_id every time the chat overlay is opened and does *not* persist it in `localStorage` — this scopes the agent's `wine_context` cache to one open/close cycle of the chat. (See §13 for the rationale: prior builds persisted the thread_id across reloads, and `wine_context` accumulated indefinitely, causing wines from earlier unrelated queries to leak into new conversations.)
- Within a single open chat the thread_id is stable, so follow-up turns ("what about the 2022 vintage?") still share memory.
- Persistence covers `messages`, `wine_context`, `user_preferences`, `last_recommendations`, `tool_call_log`.

### 9.2 What Survives Turns

| State Key | Survives? | Use |
|---|---|---|
| `messages` | Yes | Full chat history; LangGraph compaction may trim per its policy |
| `wine_context` | Yes | Cross-turn cache of merged wine records |
| `user_preferences` | Yes | Budget, varietals, dryness preference |
| `last_recommendations` | Yes (overwritten each turn) | List of `normalized_key` strings ordered as they appeared in the last response |
| `tool_call_log` | Yes (capped at last N=50) | Diagnostic + suppression of redundant calls within a turn |

### 9.3 Reference Resolution

When the user says **"the second one"**, **"the cheaper one"**, or **"tell me more"**:

1. The orchestrator inspects `state["last_recommendations"]` (passed in as part of the system message).
2. It resolves the referenced wine's `normalized_key`.
3. It looks up the full record in `state["wine_context"][key]`.
4. It can serve the answer immediately if the cached data suffices, or selectively re-query specific tools for missing details (e.g., re-fetch WineAlign reviews if they weren't included originally).

The orchestrator's system prompt includes an instruction:

> *"Before searching, check `wine_context` for the wine the user is referencing. If it's already in memory, use it. Only re-query tools when the user explicitly asks for fresh data or when the cached entry lacks the requested field."*

### 9.4 Preference Inference

Stable preferences are committed via an LLM-callable tool:

```python
@tool
async def update_preferences(
    budget_max: float | None = None,
    add_varietals: list[str] | None = None,
    sweetness: str | None = None,
    style: str | None = None,
) -> str:
    """Record a stable user preference for use in future turns.

    Call this when the user expresses a preference that should persist
    (e.g., "I always want to stay under $50", "I prefer dry whites").
    Do NOT call for one-off filters within a single query.
    """
```

The orchestrator's system prompt instructs it to call this only on **stable** preferences — not on ad-hoc filters within a single turn.

### 9.5 Why Not Just Raw History?

LangGraph may compact the message history under context pressure. Critical state (preferences, wine cache) should be in **structured state**, not in the message log, to survive compaction.

---

## 10. Error Handling & Graceful Degradation

### 10.1 `safe_tool` Decorator

```python
# safety.py
import functools
import httpx

class ToolError(Exception):
    pass

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
            # raised by tools for missing API keys
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
```

Tool functions exposed to LangGraph (e.g., `search_bcliquor_tool`) are thin wrappers around the underlying search functions that:
1. Convert Pydantic results to JSON-serializable dicts.
2. Return `{"status": "ok", "results": [...]}` on success.
3. Are wrapped with `safe_tool` so failures degrade to the structured error envelope.

The orchestrator's system prompt instructs it to:

> *"When a tool returns `status != 'ok'`, do not retry it within the same turn. Continue with the other tools' results. If the failure is material to the user's request, note it briefly in the final response (e.g., 'WineAlign reviews are temporarily unavailable')."*

### 10.2 Failure Mode Table

| Failure | Tool affected | Strategy |
|---|---|---|
| Session expired | `winealign` | Auto-relogin (built into `WineAlignSession`). Second failure → return `{"status": "auth_failed"}` |
| Credentials missing in `.env` | `winealign`, `tavily` | Return `{"status": "unavailable"}`; orchestrator silently omits |
| Rate limit (HTTP 429) | `tavily` | Return `{"status": "rate_limited"}`; never retried in the same turn |
| Server error (HTTP 5xx) | Store APIs | Single retry with 1 s backoff inside the tool; second failure → empty results + error note |
| Network timeout | All HTTP tools | `httpx.TimeoutException` → empty results + error note; turn continues |
| DB missing | `gismondi` | Return `{"status": "unavailable", "message": "Knowledge base not built. Run python build_db.py"}` |
| Empty results | All tools | Not an error; orchestrator decides whether to fall back to Tavily |

### 10.3 Critical UX Rule

**A single tool failure must never abort the turn.** If three of four store tools fail, the agent must still answer using the one that succeeded, while noting reduced coverage in its final response.

### 10.4 Query Sanitization (`_clean_query`)

Each store / critic tool runs its incoming `query` through a tiny `_clean_query` helper that strips ASCII and smart apostrophes before passing it to the backend:

```python
def _clean_query(q: str) -> str:
    return q.replace("'", "").replace("’", "").replace("‘", "")
```

The motivation is a confirmed backend pathology on Okanagan Cellars' search: `"Quails' Gate"` returns **0 results**, `"Quails Gate"` returns **15 results**. The behaviour is silent — no error, just a zero-row response — so the agent would naturally conclude "this winery isn't in stock here" and move on. Stripping the apostrophe before sending the query unblocks 10–15+ wines per affected query. The other store backends (BC Liquor, Marquis, Everything Wine) tolerate apostrophes fine, but applying the same `_clean_query` uniformly is harmless and protects against future drift.

`gismondi_tool.py` already runs its FTS5 input through a stricter sanitizer (`_sanitize_fts_query`) that strips all non-`\w\s` characters, since apostrophes have query-language meaning in FTS5 and would otherwise raise a syntax error. `tavily_tool.py` is unaffected — apostrophes pass through full-text web search cleanly.

### 10.5 Logging

Each tool call (success or failure) appends an entry to `state["tool_call_log"]`:

```python
{
    "tool": "search_bcliquor",
    "query": "tantalus riesling",
    "status": "ok",          # or "timeout", "auth_failed", etc.
    "n_results": 4,
    "ts": "2026-05-25T10:33:12Z",
}
```

This log is used for (a) diagnostics, (b) the LLM-as-judge evaluation (§16), and (c) suppression of duplicate calls within a turn. All these calls are also captured automatically by LangSmith (§14).

---

## 11. Language Convention

**English-only** for the agent path. **Auto-detect** for the validation rejection path.

- All prompts (orchestrator, sub-LLM, synthesis) are written in English; agent responses are English.
- All tool inputs and outputs are English.
- The frontend UI strings are English.
- **Exception:** the validation gate (§12.6) generates its rejection in the **same language as the user's input**, handled inside the validator's LLM call (the `VALIDATION_SYSTEM_PROMPT` carries both Korean and English example rejections). This is the only place where non-English output is produced today.

Wine-specific tokens (winery names, varietals, region names) are kept in their original Latin/French/German spelling regardless — this is universal practice and not language-dependent.

Korean language support inside the agent path itself is **deferred** as a future improvement. See §18 for the design sketch.

---

## 12. Backend API (FastAPI)

The backend is a thin FastAPI app that:

1. Serves static frontend assets (HTML/CSS/JS).
2. Exposes a streaming chat endpoint that wraps the LangGraph application.
3. Manages session IDs (thread IDs for LangGraph's checkpointer).

### 12.1 File Layout

```
app.py                  # FastAPI entry point
agent.py                # build_graph() — LangGraph application
static/
  index.html
  styles.css
  app.js
  assets/
    logo.svg
```

FastAPI serves `static/` directly. No Node build step. No JavaScript bundler. No framework. Pure HTML/CSS/vanilla JS.

### 12.2 Endpoints

| Endpoint | Method | Purpose | Response |
|---|---|---|---|
| `/` | GET | Serves `static/index.html` | HTML |
| `/static/*` | GET | Static assets (CSS, JS, images) | files |
| `/api/session` | POST | Create a new session (returns thread_id) | `{"thread_id": "<uuid>"}` |
| `/api/chat` | POST | Send a message; streams agent response via SSE | `text/event-stream` |
| `/api/history/{thread_id}` | GET | Get full message history for a thread | `{"messages": [...]}` |
| `/api/health` | GET | Liveness probe | `{"ok": true}` |

### 12.3 Streaming via Server-Sent Events (SSE)

`/api/chat` returns an SSE stream that surfaces every LangGraph event so the frontend can render incremental progress.

```python
# app.py (sketch)
from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import json

from agent import build_graph

app = FastAPI()
graph = build_graph()


class ChatRequest(BaseModel):
    thread_id: str
    message: str


@app.post("/api/chat")
async def chat(req: ChatRequest):
    async def event_stream():
        config = {"configurable": {"thread_id": req.thread_id}}
        inputs = {"messages": [("user", req.message)]}

        async for event in graph.astream_events(inputs, config=config, version="v2"):
            kind = event["event"]
            name = event.get("name", "")

            if kind == "on_tool_start":
                yield sse({"type": "tool_start", "tool": name, "args": event["data"].get("input")})
            elif kind == "on_tool_end":
                yield sse({"type": "tool_end", "tool": name})
            elif kind == "on_chat_model_stream":
                chunk = event["data"]["chunk"].content
                if chunk:
                    yield sse({"type": "token", "text": chunk})

        yield sse({"type": "done"})

    return StreamingResponse(event_stream(), media_type="text/event-stream")


def sse(payload: dict) -> str:
    return f"data: {json.dumps(payload)}\n\n"


app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def index():
    return StaticFiles(directory="static").lookup_path("index.html")
```

### 12.4 Event Types (SSE Contract)

The frontend listens for these event types:

| Event type | Payload | Frontend behavior |
|---|---|---|
| `tool_start` | `{tool, args}` | Show "Searching <friendly-label>…" badge (skipped for `ask_user_clarification_tool`) |
| `tool_end` | `{tool}` | Mark the badge as complete (skipped for `ask_user_clarification_tool`) |
| `token` | `{text}` | Append to the current assistant message bubble |
| `clarification_request` | `{question, options}` | Render dashed-border bubble with option chips + free-text hint (§4.6) |
| `done` | none | Re-enable the input field |
| `error` | `{message}` | Show an error banner |

A friendly-label map lives in the frontend (`app.js`):

```javascript
const TOOL_LABELS = {
  search_bcliquor: "BC Liquor inventory",
  search_winealign: "WineAlign critic reviews",
  search_everything_wine: "Everything Wine availability",
  search_okanagan_cellars: "Okanagan Cellars stock",
  search_marquis: "Marquis curated selection",
  search_tavily: "Web reference",
  search_gismondi: "Gismondi tasting notes",
  reasoning_pair_wine: "Sommelier reasoning",
};
```

### 12.5 Session Management

The frontend, on first load, calls `POST /api/session` to receive a `thread_id` and persists it in `localStorage` under the key `bc_wine_thread_id`. Every subsequent `/api/chat` POST includes that ID. This is the LangGraph checkpointer key — multi-turn memory works automatically.

### 12.6 Pre-Agent Validation Gate

Before the FastAPI handler invokes `graph.astream_events`, it runs the user message through a one-shot LLM classifier that decides whether the query is in scope for the agent. Off-topic queries (weather, sports, code, generic trivia) short-circuit at the API boundary — they never enter the graph, never spend an orchestrator round, never trigger tool calls. In-scope queries fall through to the existing pipeline unchanged.

**File:** `validation.py`. One async function, one Pydantic model:

```python
from langchain_core.messages import HumanMessage, SystemMessage
from pydantic import BaseModel, Field

from models import get_llm
from prompts import VALIDATION_SYSTEM_PROMPT


class ValidationResult(BaseModel):
    is_valid: bool = Field(description="True if the query is in scope for the BC Wine agent.")
    rejection_message: str = Field(default="", description="Polite redirect in the user's language; empty when is_valid=True.")


async def validate_query(message: str) -> ValidationResult:
    llm = get_llm(temperature=0.0).with_structured_output(ValidationResult)
    return await llm.ainvoke([
        SystemMessage(content=VALIDATION_SYSTEM_PROMPT),
        HumanMessage(content=message),
    ])
```

**Integration in `app.py`** — at the very top of `event_stream()` inside the `/api/chat` handler:

```python
try:
    verdict = await validate_query(req.message)
except Exception:
    verdict = None   # fail-open

if verdict is not None and not verdict.is_valid:
    yield sse({"type": "token", "text": verdict.rejection_message, "run_id": None})
    yield sse({"type": "done"})
    return
# else: fall through to graph.astream_events()
```

**Scope** (encoded in `VALIDATION_SYSTEM_PROMPT`):

| Verdict | Examples |
|---|---|
| **VALID** | Wine questions (any region/varietal/producer), food–wine pairings, wine education, prices/availability, greetings ("hi", "안녕하세요"), system-help ("what can you do"), **short follow-ups** ("the second one", "cheaper one") |
| **INVALID** | Weather, sports, news, jokes, coding/math/politics, non-wine alcoholic beverages on their own, general trivia |

**Leniency rule:** the prompt biases the classifier toward VALID on ambiguous follow-ups so multi-turn reference resolution (§9.3) isn't broken by a stale current-message-only view.

**Output language:** the same call also generates the rejection message in the **same language as the user's input**, with explicit Korean / English / coding-question examples in the prompt. There is no separate language-detection step.

**Fail-open behavior:** if the validator LLM raises (timeout, quota, transient Vertex AI error), the handler proceeds to the graph as if validation never ran. Behavioral Rule 13 in `ORCHESTRATOR_SYSTEM_PROMPT` (§6.4) remains a defense-in-depth backstop for off-topic queries that slip through.

**Observed latency:**

| Path | End-to-end wall time |
|---|---|
| INVALID (gate short-circuit) | ~2.6 s |
| VALID, greeting only (no tools) | ~10 s |
| VALID, full inventory fan-out | ~50 s |

Validation adds roughly 500–1000 ms upfront on the valid path; the saving on the invalid path is the entire orchestrator + synthesis cost (~8–15 s).

**No frontend change.** The rejection rides the existing SSE `token` + `done` channel as a single chunk — `app.js` renders it identically to a streamed agent response.

---

## 13. Frontend & UI Design

### 13.1 Tech Stack

- **Vanilla HTML / CSS / JavaScript.** No framework. No build step.
- One HTML page (`index.html`), one stylesheet (`styles.css`), one script (`app.js`).
- Google Fonts: **DM Sans**, weights 400/500/700.

### 13.2 SUM AI Design Inheritance

The frontend inherits the existing [SUM AI website](https://sumai.ca) design language verbatim. The source code lives at `C:\Users\PJ\Desktop\000\t\works\sum_ai\dist\styles.css`. Lift the design tokens into this project's `static/styles.css` so they stay in sync.

#### Color tokens

```css
:root {
    --primary-color: #010050;       /* deep navy — buttons, accents, logo */
    --primary-hover: #0a0080;
    --text-primary: #000000;
    --text-secondary: #666666;
    --text-tertiary: #888888;
    --background: #FFFFFF;
    --background-secondary: #F8F9FA;
    --border-color: #E5E7EB;
    --border-subtle: #d1d5db;
    --chat-surface: #1a1a1a;        /* dark message bubble text */
}
```

#### Typography

```css
body {
    font-family: 'DM Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    line-height: 1.6;
}
```

| Element | Size | Weight | Notes |
|---|---|---|---|
| Hero title | 3.5rem | 700 | letter-spacing -0.5px |
| Section title | 2.5rem | 700 | |
| Body | 1rem | 400 | |
| Button | 0.95rem | 600 | |

#### Layout

- Container max-width: **1200px**, centered, horizontal padding 2rem.
- Section vertical padding: **5rem**.
- Border radius: 6px (small), 8px (medium), 12px (cards), 16px (chat modal).

#### Components to reuse

- `.navbar` — sticky top, backdrop-blur, white background.
- `.btn-primary` — filled navy.
- `.btn-secondary` — outlined navy.
- `.service-card` — white card, 1px border, 12px radius, lifts on hover.
- **`.demo-chat-*` family** — already a working chat modal in `sum_ai/dist/styles.css`. Lift `.demo-chat-modal`, `.demo-chat-header`, `.demo-chat-messages`, `.demo-chat-message.ai`, `.demo-chat-message.user`, `.demo-chat-typing`, `.demo-chat-input-area` directly. This saves roughly all of the chat UI styling work.

### 13.3 Page Structure

```
<header class="navbar">
  <div class="container nav-wrapper">
    <div class="logo"><a href="/">BC Wine AI</a></div>
    <nav class="nav-menu">
      <a href="#about" class="nav-link">About</a>
      <a href="#chat" class="nav-link">Chat</a>
    </nav>
  </div>
</header>

<section class="hero">
  <div class="container hero-content">
    <h1 class="hero-title">Ask anything about BC wine.</h1>
    <p class="hero-subtitle">
      Inventory, prices, critic scores, and pairings — across every major
      BC retailer and Canada's top wine reviewers — in one chat.
    </p>
    <button class="btn-primary btn-large" id="open-chat">Start chatting</button>
  </div>
</section>

<section class="about-section">
  <!-- short feature grid: 3 cards — Inventory, Reviews, Pairings -->
</section>

<!-- Chat modal (overlay) -->
<div class="demo-chat-overlay" id="chat-overlay">
  <div class="demo-chat-modal">
    <header class="demo-chat-header">
      <div>
        <div class="demo-chat-header-title">BC Wine AI</div>
        <div class="demo-chat-header-subtitle">Ask about any BC wine</div>
      </div>
      <button class="demo-chat-close" id="chat-close">×</button>
    </header>

    <div class="demo-chat-messages" id="chat-messages"></div>

    <div class="demo-chat-typing" id="chat-typing">
      <span></span><span></span><span></span>
    </div>

    <div class="demo-chat-input-area">
      <textarea class="demo-chat-input" id="chat-input"
                placeholder="e.g., Find me a BC Pinot Noir under $50…"></textarea>
      <button class="demo-chat-send" id="chat-send">→</button>
    </div>
  </div>
</div>
```

### 13.4 Frontend Behavior (`app.js`)

Responsibilities:

1. On load: ensure `localStorage.bc_wine_thread_id` exists; call `POST /api/session` if not.
2. On send: append the user message bubble; open SSE via `POST /api/chat`; route events to the renderer.
3. Render `tool_start` events as small inline badges between message bubbles ("◷ Searching BC Liquor inventory…").
4. Render `token` events by appending to the active assistant bubble (markdown → HTML via a tiny inline renderer, e.g., `marked.min.js` from a CDN, or hand-rolled).
5. On `done`: re-enable the input and clear the typing indicator.

### 13.5 Markdown Rendering

The agent's final response is markdown (per §6.5). The frontend renders it client-side. Use [`marked`](https://marked.js.org) from a CDN (~25 KB minified) — pulled in via a single `<script>` tag, no build step:

```html
<script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
```

Apply it on `tool_end` of the last message, or buffer tokens and rerender on each chunk.

---

## 14. Observability (LangSmith)

### 14.1 Why LangSmith

LangSmith automatically captures a span for every LLM call and every tool call in the LangGraph application. With one environment variable, the user gets:

- Per-turn timelines (which tools fired, in what order, with what latency).
- Token usage and cost per call.
- Full prompt and response payloads (for debugging hallucinations or prompt regressions).
- Project-level dashboards (success rate, average latency).

### 14.2 Environment Variables

```bash
# .env
LANGCHAIN_TRACING_V2=true
LANGCHAIN_API_KEY=ls__...
LANGCHAIN_PROJECT=bc-wine-ai-agent
```

That's the entire integration. `langchain_google_genai`, `langgraph.prebuilt`, and the rest of the stack are LangSmith-aware out of the box.

### 14.3 What to Trace

Everything, by default. No selective tracing is needed at this stage. Specifically the user will see, per turn:

- An overall trace named after the user's input (the first user message of the turn).
- A child span per ReAct iteration (model invocation).
- A child span per tool call (including the `safe_tool`-wrapped wrappers).
- The `merge_results` node as a span.
- The `format_response` LLM call as a final span.

### 14.4 Custom Metadata

Tag each trace with the thread_id so the user can filter LangSmith by conversation:

```python
config = {
    "configurable": {"thread_id": req.thread_id},
    "tags": ["bc-wine-agent"],
    "metadata": {"thread_id": req.thread_id, "user_query_len": len(req.message)},
}
async for event in graph.astream_events(inputs, config=config, version="v2"):
    ...
```

### 14.5 Local-Only Mode

If `LANGCHAIN_TRACING_V2` is unset, tracing silently no-ops. There is no runtime dependency on LangSmith being reachable — the agent works offline.

---

## 15. Implementation Roadmap

Build order (each item assumes the prior items are done):

| # | File | Status | Purpose | Est. effort |
|---|---|---|---|---|
| 1 | `gismondi_tool.py` | ✅ Done | Wrap `data/wines.db` (FTS5) into the standard tool pattern | 1 day |
| 2 | `state.py` | ✅ Done | `AgentState` TypedDict and related schemas | 0.25 day |
| 3 | `models.py` | ✅ Done | LLM factory (Gemini 3.5 Flash via Vertex AI) | 0.25 day |
| 4 | `prompts.py` | ✅ Done | Orchestrator system prompt, sub-LLM prompts, synthesis prompt | 0.5 day |
| 5 | `safety.py` | ✅ Done | `safe_tool` decorator + tool wrapping helpers | 0.25 day |
| 6 | `merge.py` | ✅ Done | `normalize()`, `MergedWine` model, `merge_tool_results()` | 1 day |
| 7 | `agent.py` | ✅ Done | `build_graph()` — wires nodes, tools, checkpointer | 1.5 days |
| 8 | `app.py` | ✅ Done | FastAPI: SSE chat endpoint, session management, static mount | 0.75 day |
| 9 | `static/index.html` + `static/styles.css` + `static/app.js` | ✅ Done | Frontend chat UI in SUM AI design language | 1.5 days |
| 10 | `tests/golden_queries.py` + `tests/test_agent.py` | ☐ | 12+ golden queries, assertions, LLM-as-judge | 1 day |
| 11 | `validation.py` | ✅ Done | Pre-agent query validation gate (off-topic → SSE rejection, skip graph). See §12.6. | 0.25 day |
| 12 | `compaction.py` | ✅ Done | In-loop tool-result compaction node: incremental `wine_context` merge + same-id ToolMessage replacement. See §8.9. | 0.25 day |
| 13 | `docs/DEPLOYMENT.md` | ☐ | Deploy notes (Docker, env vars, hosting target) | 0.5 day |

### 15.1 Critical Path

~~`gismondi_tool.py`~~ → ~~`merge.py`~~ → ~~`agent.py`~~ → ~~`app.py`~~ → ~~frontend~~. All done.

`prompts.py`, `state.py`, `models.py`, and `safety.py` are small and can be slotted in alongside `agent.py` work.

### 15.2 What's Already Done (out of plan)

These pieces already exist in the repo and are not counted in the table above because they are infrastructure rather than agent code:

- All six original store/web tools (`bcliquor_tool.py`, `winealign_tool.py`, `everythingwine_tool.py`, `okanagan_cellars_tool.py`, `marquis_tool.py`, `tavily_tool.py`).
- `build_db.py` — CSV → SQLite + FTS5 builder.
- `data/wines.db` — populated (1391 BC/Canadian wine reviews).
- `.github/workflows/update_db.yml` — refreshes `data/wines.db` on Tue/Thu/Sat (2 h after the upstream submodule scrape).

### 15.3 Recommended Order Inside Each File

For each implementation file:

1. Write the data model (Pydantic / TypedDict).
2. Write the function signatures with docstrings.
3. Run a standalone `python <file>.py` smoke test before integrating.
4. Integrate into the graph or app.

---

## 16. Verification & Testing Strategy

### 16.1 Layer 1 — Standalone Tool Tests

Each `*_tool.py` already contains an executable `main()` that runs representative queries and prints results. These are smoke tests, not assertions.

Action item: add a one-line `pytest.mark.smoke` test that simply imports each tool and runs `main()` with a trivial query, asserting no exceptions.

### 16.2 Layer 2 — Golden Queries

`tests/golden_queries.py` holds 38 hand-written queries across 13 categories. Each entry carries expected-tool / forbidden-tool / coverage / multi-turn fields:

```python
{
    "id": "INV-001",
    "category": "INV",
    "query": "Where can I buy Mission Hill Reserve Pinot Noir 2021 in BC?",
    "expected_tools_all_of": [
        "search_bcliquor", "search_marquis",
        "search_okanagan_cellars", "search_everything_wine",
    ],
    "expected_tools_any_of": [],
    "forbidden_tools": ["search_tavily"],
    "must_mention": ["Mission Hill", "Pinot Noir"],
    "min_distinct_stores": 3,
}
```

Categories: `INV` (inventory/parallel fan-out), `CRI` (critic queries), `PAIR-W` / `PAIR-C` / `PAIR-N` (Western / complex / non-Western pairing), `EDU` (regional knowledge), `MT-REF` / `MT-PREF` (multi-turn reference resolution / preference inference), `DISC` (open-ended discovery), `BEG` (beginner-tier), `SOM` (sommelier-tier), `FB` (fallback — wine not in stock), `OFF` (off-topic redirect).

`tests/quality_eval.py` runs each query (or category subset) through the compiled graph and writes:
- `tests/results/<YYYYMMDD-HHMMSS>/results.json` — full structured data
- `tests/results/<YYYYMMDD-HHMMSS>/summary.md` — Claude-readable summary
- `tests/results/<YYYYMMDD-HHMMSS>/transcripts/<ID>.md` — per-query tool I/O + final response

CLI:
```bash
python -m tests.quality_eval                          # full suite
python -m tests.quality_eval --only INV,CRI           # category filter
python -m tests.quality_eval --id INV-001             # single query
python -m tests.quality_eval --dry-run                # first 2 queries
python -m tests.quality_eval --skip-judge             # deterministic metrics only
```

### 16.3 Layer 3 — Deterministic Metrics (`tests/metrics.py`)

For each turn, the eval computes:

- **Tool orchestration** — precision / recall / F1 against `expected_tools_*`, plus `forbidden_called` and per-turn-limit checks (`search_winealign ≤ 2`, `search_robert_parker ≤ 1`, `search_tavily ≤ 1`). Tool names are normalized via `_strip_tool_suffix` so the binding's `_tool` suffix doesn't trip the comparison.
- **Hallucination** — for each declared field family (winery / score / vintage / price), check whether the response's mention appears verbatim in at least one tool result.
- **Coverage** — distinct stores cited (for buyability queries), distinct critics cited (for review queries).
- **Output contract** — regex-checked presence of Lead / "Why this wine" / "Where to buy" table / "Pairing note". Bullet-list fallback for the table is accepted when the section names ≥ 2 known stores with prices.
- **Mention / forbidden mention** — golden-query-defined required and prohibited substrings.
- **Latency** — wall time per turn.
- **Reference resolution** (multi-turn) — does turn N's response reference the wine from turn N-1?

### 16.4 Layer 4 — LLM-as-Judge (`tests/judge.py`)

```python
JUDGE_RUBRIC = """
Score 1–5 on:
- Accuracy: every claim supported by tool results
- Citation: critics named, stores named
- Completeness: addresses all parts of the user's question
- Style: clear, no rambling
- Helpfulness: actionable next step
- Structure: follows the synthesis skeleton
Return JSON: {accuracy, citation, completeness, style, helpfulness, structure,
              overall, issues[], strengths[]}
"""
```

Judge model: `gemini-3.5-flash` with `temperature=0` (separate from the system-under-test). Aggregate scores across the suite power a simple regression dashboard. The Judge receives the user query, the tool-results blob, and the final response — it does NOT see the orchestrator's draft or internal state.

### 16.5 Iteration History

The eval has been the primary driver of architectural decisions. Each run produces a timestamped folder under `tests/results/`. Headline trajectory across the first eight runs:

| Run | Headline change(s) | Judge overall | Tool orch pass | Hallucination | Output structure | Errors |
|---|---|---|---|---|---|---|
| R1 | baseline | 3.57 | 34% | 18.2% | 1.50 / 4 | 1 |
| R2 | synthesis LLM call activated; temperatures lowered (orch 0.3 → 0.2, synthesis 0.2 → 0.0) | 3.82 | 29% | 15.6% | 1.38 | 0 |
| R3 | tighter synthesis prompt; `output_contract_score` accepts narrative bullets | 3.59 | 41% | 13.6% | 2.02 | 1 |
| R4 | content-list extraction fix (Gemini's `[{type:text,...}]` no longer leaks into responses) | 3.55 | 11% | 13.6% | 1.98 | 1 |
| R5 | **`merge.py` tool-name resolution fix** — `wine_context` actually populated for the first time. Metric normalization for `_tool` suffix. | 3.38 | 89% | 8.9% | 2.76 | 0 |
| R6 | synthesis prompt rebalanced (follow orchestrator's selection, multi-store rows) | **3.91** | 86% | 13.6% | 3.05 | 1 |
| R7 | `MAX_TOOL_ROUNDS=3` safety net; Rule 12/14 tightened; query-classification rule | 3.51 | 96% | 17.8% | 2.67 | 0 |
| R8 | partial rollback of R7 synthesis prompt + Gismondi-price extraction in merge | 3.44 | **100%** | 8.9% | 2.49 | 0 |

Patterns visible in the trajectory:

- **Pure prompt iteration hit diminishing returns around R3–R4**. The single biggest jump in deterministic metrics (R4 → R5, tool orch 11% → 89%) was an unblocking code fix, not a prompt tweak.
- **Synthesis rule pressure is multi-objective and unstable.** Tightening anti-hallucination simultaneously suppresses helpful alternatives; loosening it brings back fabricated wineries. The yo-yo on Judge overall between R5 and R8 is the visible signature of that trade-off.
- **Code-level safety nets compound cleanly.** `MAX_TOOL_ROUNDS`, the metric's `_strip_tool_suffix`, and Gismondi's synthetic StorePrice are independent improvements that each lifted a specific failure mode without regressing another.

The next category of wins is **architectural rather than prompt-level** — see §18.2 for candidates (query-type routing, stricter merge fuzzy matching, deterministic table rendering).

### 16.6 Layer 5 — Trace Review via LangSmith

After running the suite, open the LangSmith project (§14) and spot-check failing or borderline cases. The trace tells you exactly which tool was called with what arguments and what it returned — much faster than re-running the agent locally.

---

## 17. Deployment

### 17.1 Container

Package the whole thing as a single Docker image:

```dockerfile
# Dockerfile
FROM python:3.12-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
RUN python build_db.py   # build SQLite from CSV at image build time

EXPOSE 8000
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
```

The container ships the static frontend in the same image. One artifact, one process.

### 17.2 Hosting Options

| Host | Why it fits | Notes |
|---|---|---|
| **Fly.io** | Free tier, single-region, easy SSE | Persistent volume for `data/checkpoints.db` |
| **Railway** | One-click Docker deploy, easy env vars | Volume mount required for SQLite persistence |
| **Render** | Free web service tier, good docs | Disk persistence on paid tier only |
| **Google Cloud Run** | Already in the Gemini ecosystem; pay-per-request | Add a Cloud SQL or persistent FUSE mount for checkpoints |
| **Local + Ngrok** | Fastest iteration during development | Not for long-term hosting |

For the first deploy, **Fly.io** is the lowest-friction path: `fly launch`, point to the Dockerfile, attach a 1 GB persistent volume for `data/`, set env vars in the Fly dashboard.

### 17.3 Environment Variables Checklist

Required:

```
# Gemini / Vertex AI
GOOGLE_APPLICATION_CREDENTIALS=/app/secrets/sa.json
# (or paste JSON content into the host's secret manager)

# WineAlign
WINEALIGN_EMAIL=...
WINEALIGN_PASSWORD=...

# Tavily
TAVILY_API_KEY=...

# LangSmith (recommended — see §14)
LANGCHAIN_TRACING_V2=true
LANGCHAIN_API_KEY=ls__...
LANGCHAIN_PROJECT=bc-wine-ai-agent
```

### 17.4 Persistent Volumes

The container needs persistence for:
- `data/wines.db` — built once at image build, read-only at runtime (no volume needed).
- `data/checkpoints.db` — read/write at runtime. **Requires a persistent volume** (Fly volume, Render disk, etc.). Without one, multi-turn memory resets on container restart.

### 17.5 CORS

Not needed if the frontend is served from the same origin as the API. The deploy plan above bundles both — no CORS configuration required.

---

## 18. Open Questions & Future Improvements

### 18.1 Open Questions for the Team

1. **Vintage default policy.** When a user asks about "Tantalus Riesling" without a year, default to the latest in-stock vintage, or list all vintages? **Current default:** latest in-stock, mention other vintages exist.

2. **Tax-inclusive pricing.** BC Liquor prices include PST/GST (10% + 5%). Some private retailers may quote pre-tax. The best-price comparison may be unfair across stores. **Current default:** treat all prices as quoted; do not normalize. Document the limitation in the response.

3. **Tavily budget cap.** Per-turn limit is 1 call (enforced by prompt). Per-day cap: not enforced. Should a daily-usage tracker be added?

4. **WineAlign session reuse.** Each call to `search_winealign` instantiates a new `WineAlignSession`. For latency, pre-login at app startup and reuse the session across all turns. Risk: cookie expiry during long uptime.

5. **Gismondi DB rebuild schedule.** The `gismondi-canada-wines` git submodule auto-updates on a schedule. The `update_db.yml` workflow already rebuilds `data/wines.db` on Tue/Thu/Sat. Confirm the deploy pipeline picks up the updated DB on each redeploy.

### 18.2 Future Improvements

**Architectural (surfaced by quality-eval iteration — see §16.5):**

- **Query-type routing.** _Partially shipped (off-topic split):_ the pre-agent validation gate (§12.6) now intercepts off-topic queries at the API boundary and returns an in-language rejection in ~2.6 s without entering the graph. Still open: routing **specific-wine** queries to a narrower tool fan-out and **recommendation** queries to the full path. Both still go through the same orchestrator path today.
- **Deterministic Where-to-buy rendering.** The synthesizer occasionally invents store rows ("Retail Database", placeholder URLs) or omits valid prices. Render the Where-to-buy table from `wine_context["prices"]` in Python; let the LLM only write the narrative sections (Lead / Why / Pairing). Hallucination in the most user-visible piece of data drops to zero.
- **Stricter merge fuzzy matching.** `_find_match` currently requires `prod_slug` to be equal — when one source has `producer = "Tantalus Vineyards"` and another has the producer embedded in the wine title (`"Tantalus Riesling"`, producer slug empty), the two records do not merge and the user sees critic-only and store-only rows for the same wine. Treat empty `prod_slug` as a wildcard, or fuzzy-match producer slugs. **Note:** the in-loop incremental merge (§8.9) makes this misalignment slightly more visible because Gismondi-derived prices (`prod_slug = "tantalus"`) and BC Liquor store rows (`prod_slug = ""`) for the same wine end up under separate keys in `wine_context` mid-loop.
- **BC Liquor `is_bc_vqa` parsing.** Certain BC Liquor results (observed on `"Quails Gate"`) return a value for `is_bc_vqa` that fails Pydantic boolean validation, dropping the entire result set. Coerce to `bool` with a tolerant parser inside `bcliquor_tool.py`.
- **WineAlign `value_rating` + `price` fields.** The merge currently keeps `value_rating` (0–5 stars) on `CriticReviewMerged` but the synthesis prompt never surfaces it. Either render it ("4 stars — great value") or drop it from the schema. WineAlign's listing prices, similarly, could feed `wine_context["prices"]` the same way Gismondi's now does (§8.6).
- **Consumer rating / votes display.** `MergedWineRecord` carries `consumer_rating` and `consumer_votes` from BC Liquor but the synthesis prompt doesn't reference them. Adding a one-line "consumer score (n votes)" to the Why section provides cheap social proof.

**Product / UX:**

- **Korean-language output.** Detect Hangul in the user's first message → set `state["user_language"] = "ko"` → pass to the synthesis prompt with an instruction to render in Korean using 존댓말 and natural sommelier register. Wine names stay in original spelling.
- **Per-node model tiering.** Once cost matters, downgrade `format_response` to a smaller/cheaper Gemini variant and reserve full Flash power for the orchestrator.
- **Vector search over Gismondi tasting notes.** SQLite FTS5 is keyword-based. Adding `sqlite-vec` and embedding the tasting notes would unlock semantic queries ("rich, buttery wines under $40").
- **Image generation of bottle shots.** Some store APIs return image URLs; consolidate and display them in the chat bubbles.
- **Order placement integration.** Stretch — partner with one of the four retailers' carts.
- **User accounts + saved preferences.** Today preferences are per-thread. Persisting per-user across threads requires an auth layer.
- **Mobile-native UI.** A Next.js or React Native frontend hitting the same FastAPI endpoints would unlock app-store distribution.

---

## Appendix A — File Layout (Post-Implementation)

Legend: ✅ = exists · ☐ = to build

```
BC-wine-ai-agents/
├── ✅ agent.py                    # build_graph()
├── ✅ state.py                    # AgentState TypedDict
├── ✅ models.py                   # LLM factory (Gemini 3.5 Flash)
├── ✅ prompts.py                  # All prompts (orch + pairing + synthesis + validation)
├── ✅ merge.py                    # Normalize + dedup logic
├── ✅ safety.py                   # safe_tool decorator
├── ✅ validation.py               # Pre-agent query validation gate (§12.6)
├── ✅ compaction.py               # In-loop tool-result compaction node (§8.9)
├── ✅ app.py                      # FastAPI entry point
├── ✅ bcliquor_tool.py
├── ✅ winealign_tool.py
├── ✅ everythingwine_tool.py
├── ✅ okanagan_cellars_tool.py
├── ✅ marquis_tool.py
├── ✅ tavily_tool.py
├── ✅ gismondi_tool.py            # §3.7
├── ✅ build_db.py
├── data/
│   ├── ✅ wines.db                # built from CSV (1391 reviews)
│   └── ☐ checkpoints.db          # LangGraph SqliteSaver (gitignored)
├── ✅ static/
│   ├── index.html                # chat UI
│   ├── styles.css                # SUM AI design tokens
│   ├── app.js                    # SSE client + chat logic
│   └── assets/
├── ☐ tests/
│   ├── golden_queries.py
│   └── test_agent.py
├── ✅ gismondi-canada-wines/      # git submodule (CSV source)
├── docs/
│   ├── ✅ AGENT_DESIGN.md         # this file
│   └── ☐ DEPLOYMENT.md
├── .github/workflows/
│   └── ✅ update_db.yml           # Tue/Thu/Sat DB refresh
├── ☐ Dockerfile
├── ✅ .env                        # gitignored
├── ✅ README.md
└── ✅ requirements.txt
```

## Appendix B — Minimum `requirements.txt`

```
fastapi
uvicorn[standard]
httpx
pydantic
python-dotenv
beautifulsoup4
langgraph
langchain-core
langchain-google-genai
langsmith
rapidfuzz
```
