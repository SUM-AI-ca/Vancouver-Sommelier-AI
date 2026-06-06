# Vancouver Drinks AI

A multi-agent AI drinks concierge for the Vancouver market. Built on a LangGraph Supervisor + 3 specialist agent architecture, it searches real-time inventory and pricing across 6 Vancouver-area retail chains (including BC Liquor Stores' 200+ locations and Everything Wine's 4 Lower Mainland stores), provides expert knowledge via Google Search grounding, and offers food pairing guidance. Supports both B2C (consumer recommendations) and B2B (beverage menu design for F&B businesses).

**Live: [wineaiagent.com](https://wineaiagent.com)**

Status: **Production.** Cloudflare Pages (frontend) + Google Cloud Run (backend API). Multi-agent Supervisor + 3 specialists (Sourcing / Sommelier / Menu Architect), FastAPI SSE streaming, multimodal vision node (wine label / wine list / food menu photo scanning), human-in-the-loop clarification, pre-agent query validation gate, golden-query + LLM-as-judge quality eval pipeline.

---

## Architecture

```
User query (+ optional wine label / wine list / food menu photo)
    ↓
Cloudflare Pages (frontend/ — vanilla HTML/CSS/JS, no build step)
    ↓  CORS (cross-origin fetch)
Google Cloud Run — FastAPI backend (app.py — SSE streaming)
    ↓
Validation Gate (validation.py — Gemini Flash classifier)   ※ bypassed when image attached
    │
    ├─ INVALID → reject in user's language → skip graph → end
    │
    └─ VALID ↓
LangGraph Supervisor (agent.py — Gemini 3.5 Flash)
    │
    │   entry_router ─(image)──→ vision_node ─┐
    │                └─(text)────────────────┴→ supervisor
    │
    │   supervisor → specialist routing (+ owns clarification / preferences)
    │       ↓ (ask_user_clarification_tool)
    │    interrupt() → SSE clarification_request → user reply
    │       ↓ Command(resume=...) → next supervisor round
    │
    │   ┌──────────────────────────────────────────────────────────────────┐
    │   │  Specialist Agents (independent ReAct sub-graphs)                │
    │   │                                                                  │
    │   │  Sourcing Agent ──── parallel search across 6 retail chains      │
    │   │    └─ bcliquor, everythingwine, okanagan_cellars,               │
    │   │       suttonplace, marquis, legacy                              │
    │   │                                                                  │
    │   │  Sommelier Agent ── pairing recs + Google Search grounding       │
    │   │    └─ reasoning_pair_wine, search_web_grounded                  │
    │   │                                                                  │
    │   │  Menu Architect ─── (B2B) food menu → beverage menu design      │
    │   │    └─ sourcing_agent (A2A), search_web_grounded                 │
    │   └──────────────────────────────────────────────────────────────────┘
    │
    │   supervisor final answer → END
    ↓
SSE streaming → frontend (agent-box UI + tool badges + markdown rendering)
```

---

## Agent Architecture

Supervisor + 3 specialist pattern. Each specialist runs as an independent ReAct sub-graph, exposed to the Supervisor as a single `@tool`.

| Agent | Role | Tools | Model |
|-------|------|-------|-------|
| **Supervisor** | Query routing, specialist coordination, final answer synthesis, owns clarification/preferences | ask_user_clarification, update_preferences + 3 specialist tools | Gemini 3.5 Flash |
| **Sourcing Agent** | Inventory, pricing, where-to-buy — parallel calls to all 6 retail chains every time | 6 retailer tools | Gemini 3.5 Flash |
| **Sommelier Agent** | Pairing recs, drinks knowledge, reviews/scores (Google grounding, with citations) | reasoning_pair_wine, search_web_grounded | Gemini 3.1 Pro Preview |
| **Menu Architect** | (B2B) Design beverage menu from food menu → source real products/prices (A2A delegation) | sourcing_agent (A2A), search_web_grounded | Gemini 3.1 Pro Preview |

**Agent-to-Agent (A2A)**: Menu Architect calls `sourcing_agent_tool` directly to source real Vancouver retail products and prices after designing the menu. Direct delegation without Supervisor mediation.

---

## Deployment

Frontend and backend are deployed separately.

| Layer | Service | URL |
|-------|---------|-----|
| **Frontend** | Cloudflare Pages | `wineaiagent.com` / `www.wineaiagent.com` |
| **Backend API** | Google Cloud Run | `bc-wine-agent-135257828500.us-west1.run.app` |

- Frontend (`frontend/`) is deployed directly to Cloudflare Pages. No build command, output directory `frontend/`.
- Backend is built as a Docker image and deployed to Cloud Run. Gemini API is called via GCP service account authentication.
- Frontend JS (`frontend/app.js`) calls the Cloud Run URL directly via `API_BASE`, and `app.py`'s `CORSMiddleware` allows `wineaiagent.com` / `www.wineaiagent.com` origins.
- For local development, `API_BASE` is empty, so requests go to the same server's `/api/*` endpoints.

### Cloud Run Deployment

```bash
gcloud run deploy bc-wine-agent --source . --region us-west1 --project wine-agent-jh-2026 --allow-unauthenticated
```

Required IAM roles for the Cloud Run service account:
- `roles/aiplatform.user` — Gemini API calls
- `roles/run.invoker` (allUsers) — public access

### Cloudflare Pages Deployment

Cloudflare Pages project settings:
- **Production branch**: `main`
- **Build command**: (none)
- **Build output directory**: `frontend`
- **Custom domains**: `wineaiagent.com`, `www.wineaiagent.com`

---

## Core Features

### Query Validation Gate

Before the graph is invoked, `/api/chat` runs a single Gemini Flash classification call to determine whether the query falls within the agent's scope (drinks / pairing / greetings). Off-topic queries (weather, sports, coding, etc.) bypass the graph entirely and return a short rejection message via SSE tokens **in the user's language**. If the validation LLM fails, it fails open and enters the normal agent path. Measured off-topic response time: ~2.6s (previously ~10s+).

Implementation: [`validation.py`](validation.py), `VALIDATION_SYSTEM_PROMPT` in [`prompts.py`](prompts.py), gate in [`app.py`](app.py).

### Human-in-the-Loop Clarification

The Supervisor can **explicitly** ask the user follow-up questions using LangGraph's `interrupt()` primitive.

Flow: Supervisor calls `ask_user_clarification_tool(question, options?)` → `interrupt({...})` fires inside the tool → graph pauses at the thread's checkpoint → `app.py` sends an SSE `clarification_request` event with question + options → frontend renders option chips + hint UI → user clicks an option or types free text → next `/api/chat` call detects pending interrupt via `aget_state(config)` → `Command(resume=req.message)` resumes the graph → tool receives the user's reply as a string and returns normally → next supervisor round proceeds.

Rules (`prompts.py` Guideline G6):
- **Ask**: genuinely ambiguous queries with 2+ interpretations, closely-matched results requiring preference tie-breaking, missing essential info.
- **Don't ask**: when user_preferences resolve it, when a default answer is natural, for informational/educational questions.
- **Limit**: max 3 per turn (`MAX_CLARIFICATIONS_PER_TURN`). At cap, forced to give best-effort answer.
- **Round counting**: clarification-only rounds are excluded from `MAX_TOOL_ROUNDS` count.
- **Validation skip on resume**: resume branch skips the validation gate so short clarification replies don't trip the off-topic filter.

Implementation: `ask_user_clarification_tool` in [`agent_tools.py`](agent_tools.py), `_count_clarifications_this_turn` in [`agent.py`](agent.py), interrupt detection + `Command(resume=...)` in [`app.py`](app.py), `renderClarification()` in [`frontend/app.js`](frontend/app.js).

### Vision — Multimodal Label / Wine List / Food Menu Scanning

When the user attaches a **wine label**, **restaurant wine list**, or **food menu photo**, a dedicated `vision_node` runs before the Supervisor to extract structured text from the image, then passes it into the normal search/recommendation flow.

Flow: frontend downscales the photo to longest edge ≤2048px JPEG and sends as base64 → `app.py` constructs a multimodal `HumanMessage` (validation gate bypassed when image attached) → `entry_router` branches on image presence → `vision_node` uses `with_structured_output(VisionExtraction)` to extract **only visible text** → replaces the `HumanMessage` in place (same id) to drop the image and fold to text (token savings) → supervisor operates text-only.

- **Wine label**: extracts producer/cuvee/varietal/vintage/region for a single wine → store tools look up price/stock.
- **Wine list**: extracts verbatim `raw_text` per line + parsed fields for N wines → queries/compares all wines on the list.
- **Food menu**: extracts menu text → Menu Architect agent designs a beverage menu.
- **Lossless**: text that doesn't fit named fields is preserved in catch-all fields (`other_text`/`raw_text`). Non-wine images get `document_type="other"` with a polite decline.
- **UI**: attach button + drag-and-drop + clipboard paste, thumbnail preview (max 2 images), `vision_start`/`vision_result` SSE events show "Image analysis" badge.

Implementation: [`vision.py`](vision.py), `VISION_EXTRACTION_PROMPT` in [`prompts.py`](prompts.py), `vision_node` + `entry_router` in [`agent.py`](agent.py), multimodal input + vision SSE in [`app.py`](app.py), image attachment UI in [`frontend/`](frontend/). Design doc: [`docs/VISION_NODE_DESIGN.md`](docs/VISION_NODE_DESIGN.md).

### Tool Robustness — Error Isolation + Query Fallback

**Tool error isolation.** `ToolNode(TOOLS, handle_tool_errors=tool_error_to_json)` catches **all exceptions as `status:"error"` JSON results** — a failing tool is marked as errored while the remaining tools' results are used to answer. Clarification `interrupt` (GraphInterrupt) is re-raised before the handler, so it's unaffected.

**Query fallback.** Some store backends (Okanagan Cellars, Everything Wine, Legacy) **AND-match all query tokens** against product names. The shared helper [`tools/query_fallback.py`](tools/query_fallback.py) retries on zero results by **stripping varietal/vintage, then progressively trimming trailing tokens** (minimum 3 tokens) until a non-empty result set is found.

Implementation: `tool_error_to_json` in [`safety.py`](safety.py) + ToolNode wiring in [`agent.py`](agent.py), `search_with_fallback` in [`tools/query_fallback.py`](tools/query_fallback.py).

---

## UI/UX

- **Landing + fullscreen chat overlay** — a landing page with capability descriptions; clicking "Start chatting" opens a fullscreen chat overlay.
- **Soft wine color palette** — desaturated burgundy (`#7A3D4F`) tone.
- **Status indicator** — top-left of chat header shows **symbol only** (no text). A fixed dot when idle, a spinning ring when active. `aria-live` delivers status text to screen readers.
- **Agent box** — specialist agent results (Sourcing, Sommelier, Menu Architect) render in collapsible agent-box components showing inner tool call details and the answer in markdown.
- **Tool badges** — each tool call renders as an expandable badge. Shows result count on completion + click for result preview dropdown.
- **Session per chat open** — a new `thread_id` is issued each time the chat overlay opens. Follow-ups within the same overlay share memory, but closing and reopening starts fresh.
- **Duplicate output suppression** — the server buffers tokens per `run_id` and discards previous round buffers so only the **last round without tool_calls** is flushed to the client.
- **Links open in new tab** — all `<a>` tags from `marked.parse` get `target="_blank" rel="noopener noreferrer"` injected automatically.

Detailed architecture design is documented in [`docs/AGENT_DESIGN.md`](docs/AGENT_DESIGN.md).

---

## Data Sources

| Source | File | Method | Auth |
|--------|------|--------|------|
| **BC Liquor Store** | `tools/bcliquor_tool.py` | JSON API | — |
| **Everything Wine** | `tools/everythingwine_tool.py` | HTML scraping + In-Store Pickup REST API | — |
| **Okanagan Cellars** | `tools/okanagan_cellars_tool.py` | JSON API | — |
| **Sutton Place Wine Merchant** | `tools/suttonplace_tool.py` | JSON API | — |
| **Marquis Wine Cellars** | `tools/marquis_tool.py` | JSON API | — |
| **Legacy Liquor Store** | `tools/legacy_tool.py` | GraphQL API | — |
| **Google Search grounding** | `tools/google_search_tool.py` | Gemini native grounding (Vertex AI) | — (ADC) |

---

## Tool Details

### 1. BC Liquor Store (`tools/bcliquor_tool.py`)

BC's government liquor retailer (200+ locations). Carries wine, beer, spirits, and cider.

- **Data**: name, price (sale status), varietal, country, ABV, tasting notes, consumer rating/votes, number of stores in stock, BC VQA status
- **Features**: category filter (`wine`, `beer`, `spirits`)

```python
results = await search_bcliquor("tantalus", max_pages=2, category="wine")
```

### 2. Okanagan Cellars (`tools/okanagan_cellars_tool.py`)

Wine shop with 2 Vancouver locations (West 1st Ave, West 4th Ave).

- **Data**: name, category, price, sale status, stock quantity, volume
- **Query fallback**: AND-matching backend → retries via [`tools/query_fallback.py`](tools/query_fallback.py)

```python
results = await search_okanagan_cellars("checkmate")
```

### 3. Sutton Place Wine Merchant (`tools/suttonplace_tool.py`)

Vancouver Yaletown wine shop (1168 Hamilton St). Same Barnet Network platform as Okanagan Cellars.

- **Data**: name, category, price, sale status, stock quantity, volume, country, varietal, vintage, ABV, staff pick, featured
- **Query fallback**: Barnet AND-matching → retries via [`tools/query_fallback.py`](tools/query_fallback.py)

```python
results = await search_suttonplace("pinot noir")
```

### 4. Marquis Wine Cellars (`tools/marquis_tool.py`)

Vancouver's curated boutique wine shop. BigCommerce-based.

- **Data**: name, SKU, price (regular/sale), stock level, category hierarchy
- **Features**: pagination support (limit/skip)

```python
results, total = await search_marquis("martins lane", limit=20)
```

### 5. Legacy Liquor Store (`tools/legacy_tool.py`)

Vancouver's premium independent wine shop. GraphQL API-based.

- **Data**: name, brand, price (regular/sale), sale status, staff pick, new arrival, country, region, tags, stock quantity
- **Features**: price range filter (`price_min`/`price_max`), staff pick filter, sale filter
- **Query fallback**: AND-matching → retries via [`tools/query_fallback.py`](tools/query_fallback.py)

```python
results, total = await search_legacy("pinot noir", limit=30, price_min=20, price_max=50, staff_pick=True)
```

### 6. Everything Wine (`tools/everythingwine_tool.py`)

Vancouver wine shop (Magento 2 + Elasticsuite). Search results via HTML scraping, **per-store pickup stock via public REST API**.

- **Data**: name, SKU, price, sale status, country, warehouse/store stock status
- **Per-store stock**: In-Store Pickup REST API provides exact quantities at 4 Lower Mainland locations (Vancouver / North Vancouver / South Surrey / Langley)
- **Query fallback**: Elasticsuite AND-matching → retries via [`tools/query_fallback.py`](tools/query_fallback.py)

```python
results = await search_everything_wine("synchromesh")
```

### 7. Google Search Grounding (`tools/google_search_tool.py`)

Knowledge and review search using Gemini's native Google Search grounding. Runs on Vertex AI credentials (ADC) with no extra API key required.

- **Data**: grounded answer + source URL list
- **Use cases**: drinks education, region/producer info, reviews/scores (citation + summary only, no full-text reproduction), supplementing gaps in store tool results
- **Copyright guardrail**: caller prompts enforce source attribution + summary only, prohibiting verbatim reproduction of reviews

```python
results, answer = await search_web_grounded("best food pairings for BC Pinot Noir")
```

---

## Project Structure

```
BC-wine-ai-agents/
├── agent.py                    # LangGraph Supervisor graph (entry_router + vision + supervisor ↔ tools)
├── agent_tools.py              # @tool wrappers + specialist groups (SOURCING / SOMMELIER / SUPERVISOR_DIRECT)
├── app.py                      # FastAPI backend (SSE streaming, CORS, multimodal input, validation gate)
├── validation.py               # Pre-agent query validation (off-topic bypass)
├── vision.py                   # Multimodal label/wine-list/food-menu extraction (VisionExtraction schema)
├── state.py                    # AgentState TypedDict (messages + tool_call_log + vision_extractions)
├── models.py                   # Gemini LLM factory (3.5 Flash + 3.1 Pro Preview)
├── prompts.py                  # Supervisor/specialist/pairing/relevance-filter/validation/vision prompts
├── safety.py                   # tool_error_to_json (tool exceptions → status:error JSON, ToolNode isolation)
├── HYPERPARAMETERS.md          # All tuning constants (temperatures, timeouts, limits)
├── requirements.txt            # Python dependencies
├── Dockerfile                  # Container build (python:3.12-slim, uvicorn, port 8080)
├── .dockerignore               # Docker build exclusions
├── agents/                     # Specialist agents (independent ReAct sub-graphs)
│   ├── __init__.py             # Architecture docs
│   ├── react_subagent.py       # Shared ReAct sub-graph builder + run_subagent_json wrapper
│   ├── sourcing_agent.py       # Sourcing Agent — parallel search across 6 retail chains
│   ├── sommelier_agent.py      # Sommelier Agent — pairing + grounding
│   └── menu_architect.py       # Menu Architect — B2B beverage menu design (A2A)
├── tools/                      # Data collection tools
│   ├── __init__.py
│   ├── bcliquor_tool.py        # BC Liquor Store search
│   ├── okanagan_cellars_tool.py # Okanagan Cellars search
│   ├── suttonplace_tool.py     # Sutton Place Wine Merchant search
│   ├── marquis_tool.py         # Marquis Wine Cellars search
│   ├── legacy_tool.py          # Legacy Liquor Store search (GraphQL)
│   ├── everythingwine_tool.py  # Everything Wine search
│   ├── google_search_tool.py   # Google Search grounding
│   └── query_fallback.py       # Shared query fallback (okanagan/everythingwine/legacy)
├── frontend/                   # Frontend (vanilla HTML/CSS/JS, no build step)
│   ├── index.html              # Landing page + fullscreen chat overlay
│   ├── styles.css              # Wine color palette, chat + tool badge + agent-box styles
│   ├── app.js                  # SSE client, CORS API_BASE, image attachment, tool badges, markdown
│   └── _worker.js              # Cloudflare Workers proxy (API routing + security filtering)
├── scripts/                    # Utility scripts
│   ├── debug_everythingwine.py # Everything Wine HTML structure debugging
│   └── test_gemini_models.py   # Gemini model comparison test
├── draw_graph.py               # Architecture Mermaid diagram generator
├── tests/                      # Golden-query quality evaluation
│   ├── golden_queries.py       # Golden queries (multiple categories)
│   ├── metrics.py              # Deterministic metrics (orchestration, hallucination, coverage, structure)
│   ├── judge.py                # LLM-as-judge (Gemini 3.1 Pro Preview temp=0)
│   ├── quality_eval.py         # Runner — produces results.json + summary.md + transcripts
│   └── results/<timestamp>/    # Per-run outputs (gitignored)
├── docs/
│   ├── AGENT_DESIGN.md         # Full architecture design doc + iteration history
│   └── VISION_NODE_DESIGN.md   # Vision node design (as-built)
├── .env                        # API keys (gitignored)
├── .gitignore
└── README.md
```

---

## Setup

### Installation

```bash
git clone https://github.com/SUM-AI-ca/BC-wine-ai-agents.git
cd BC-wine-ai-agents

python -m venv venv
source venv/bin/activate  # Mac/Linux
# venv\Scripts\activate   # Windows

pip install -r requirements.txt
```

### Google Cloud Authentication (Gemini API)

```bash
gcloud auth application-default login
```

### Environment Variables

Create a `.env` file:

```
# LangSmith (optional — tracing & observability)
LANGSMITH_TRACING=true
LANGSMITH_API_KEY=lsv2_sk_...
LANGSMITH_PROJECT=bc-wine-agent
LANGSMITH_ENDPOINT=https://api.smith.langchain.com
```

### Individual Tool Testing

```bash
python -m tools.bcliquor_tool
python -m tools.okanagan_cellars_tool
python -m tools.suttonplace_tool
python -m tools.marquis_tool
python -m tools.legacy_tool
python -m tools.everythingwine_tool
```

---

## Running the Server

### Local Development

```bash
python -m uvicorn app:app --port 8000
```

Open `http://localhost:8000` in a browser to access the chat UI.

### Docker (Local)

```bash
docker build -t bc-wine-agent .
docker run -p 8080:8080 --env-file .env bc-wine-agent
```

### Production Deployment

```bash
# Cloud Run (backend)
gcloud run deploy bc-wine-agent --source . --region us-west1 --project wine-agent-jh-2026 --allow-unauthenticated

# Cloudflare Pages (frontend)
# Cloudflare Dashboard → Workers & Pages → bcwineaiagents project
# Auto-deploys on push to main via GitHub integration
```

---

## Tech Stack

- **LangGraph** — multi-agent Supervisor + 3 specialist sub-graph orchestration
- **Gemini 3.5 Flash** — Supervisor, Sourcing Agent, validation, vision node
- **Gemini 3.1 Pro Preview** — Sommelier Agent, Menu Architect (advanced reasoning)
- **Google Search grounding** — reviews/scores/factual knowledge (Vertex AI native)
- **FastAPI** — SSE streaming backend
- **HTML/CSS/JS** — wine-colored chat UI (vanilla, no build step)
- **Google Cloud Run** — backend container hosting
- **Cloudflare Pages** — frontend static hosting + custom domains
- **httpx** — async HTTP client (session/cookie management)
- **BeautifulSoup4** — HTML parsing (Everything Wine)
- **Pydantic** — data models & validation
- **LangSmith** — tracing/observability (auto-enabled when env vars set)
- **python-dotenv** — env var loading
- **Docker** — container build (python:3.12-slim)

---

## Common Patterns

All tools follow the same structure:

1. **`search_*(query)` function** — async, returns a list of structured Pydantic models
2. **`format_results()` function** — human-readable text format. **For standalone test (`main()`) only** — in the agent path, the `@tool` wrapper serializes via `json.dumps(model_dump())` and this function is never called.
3. **`main()` function** — standalone test via `python -m tools.<name>`
4. **Pydantic model** — site-specific data structure definition

---

## Quality Eval Pipeline

```bash
python -m tests.quality_eval                    # full suite
python -m tests.quality_eval --only INV,CRI     # category filter
python -m tests.quality_eval --id INV-001       # single query
python -m tests.quality_eval --dry-run          # quick sanity check (2 queries)
python -m tests.quality_eval --skip-judge       # deterministic metrics only
```

Results are saved to `tests/results/<YYYYMMDD-HHMMSS>/` as `results.json`, `summary.md`, and `transcripts/<id>.md`.
