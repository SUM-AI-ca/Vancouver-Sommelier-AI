# Vancouver Sommelier AI

> 2026 Google for Startups AI Agents Challenge — Track 1: Build

A multi-agent AI drinks concierge for the Vancouver market. Built on a LangGraph Supervisor + 3 specialist agent architecture, it searches real-time inventory and pricing across 6 Vancouver-area retail chains (including BC Liquor Stores' 200+ locations province-wide and Everything Wine's 4 Lower Mainland stores), provides expert knowledge via Google Search grounding, and offers food pairing guidance. Supports both B2C (consumer recommendations) and B2B (beverage menu design for F&B businesses).
Status: **Production.** Cloudflare Pages (frontend) + Google Cloud Run (backend API) + Cloud SQL Postgres (conversation state). Multi-agent Supervisor + 3 specialists (Sourcing / Sommelier / Menu Architect), retailer tools served over **MCP (Model Context Protocol)** on an externally reachable `/mcp` endpoint, FastAPI real-time SSE token streaming with heartbeat keepalive, durable cross-instance conversation persistence (Postgres checkpointer + session-end cleanup + scheduled abandoned-thread sweep), multimodal vision node (wine label / wine list / food menu photo scanning), human-in-the-loop clarification, pre-agent query validation gate, Gemini empty-response guard, transient API-failure retry (499/429/5xx backoff), grounding deep-link resolution, request timeout + error recovery, LLM-as-judge quality eval pipeline.

---

## Architecture

![Architecture Diagram](frontend/images/architecture-diagram.png)

```
User query (+ optional wine label / wine list / food menu photo)
    ↓
Cloudflare Pages (frontend/ — vanilla JS SSE client, 60min timeout)
    ↓  POST /api/chat { message, thread_id, images }
Google Cloud Run — FastAPI backend (app.py — SSE streaming)
    ↓
Proxy Secret check (Cloudflare) → Rate Limiter (slowapi)
    ↓
Pending interrupt? ──(yes — resume reply)──→ Command(resume=...) ─┐
    │(no — new turn)                                              │
    ↓                                                             │
Validation Gate (validation.py — Gemini Flash)   ※ bypassed when image attached
    │                                                             │
    ├─ INVALID → reject in user's language → SSE done → end       │
    │                                                             │
    └─ VALID ↓                                                    ↓
LangGraph Supervisor (agent.py — Gemini 3.6 Flash, max 7 tool rounds)
    │
    │   entry_router ─(image)──→ vision_node ─┐
    │                └─(text)────────────────┴→ supervisor
    │                                                ↕ AsyncPostgresSaver — Cloud SQL (thread_id)
    │                                                  (InMemorySaver fallback when DATABASE_URL unset)
    │   supervisor → specialist routing (+ owns clarification)
    │       ↓ (ask_user_clarification_tool)
    │    interrupt() → SSE clarification_request → user reply
    │       ↓ Command(resume=...) → next supervisor round
    │
    │   ┌──────────────────────────────────────────────────────────────────┐
    │   │  Specialist Agents (independent ReAct sub-graphs)                │
    │   │                                                                  │
    │   │  Sourcing Agent ──── 6 retailers in parallel (max 4 rounds)      │
    │   │    └─ MCP client → MCP Server "vancouver-retailers" (/mcp)       │
    │   │         └─ bcliquor, everythingwine, okanagan_cellars,          │
    │   │            suttonplace, marquis, legacy                         │
    │   │       (also served externally: <deployment-host>/mcp)           │
    │   │                                                                  │
    │   │  Sommelier Agent ── pairing + grounding (max 3 rounds,           │
    │   │                     single-round batched parallel lookups)       │
    │   │    └─ reasoning_pair_wine, search_web_grounded                  │
    │   │                                                                  │
    │   │  Menu Architect ─── B2B beverage menu design (max 5 rounds,      │
    │   │                     course-group sourcing batched in one round)  │
    │   │    └─ sourcing_agent (delegation), search_web_grounded          │
    │   └──────────────────────────────────────────────────────────────────┘
    │
    │   tool_error_to_json — exceptions → status:error (non-fatal)
    │   blank-response retry — Gemini empty-candidate guard (×3 supervisor, ×2 specialists)
    │   transient-failure retry — 499/429/5xx backoff on every specialist LLM call
    │   supervisor final answer → END
    ↓
Real-time SSE token streaming (15s heartbeat keepalive) → frontend (tool badges + markdown + PDF export)
    │   (nested wrapper tool runs suppressed — one event pair per real call)
    │   (final round streamed nothing? → recover answer from checkpoint state)
    ↓
LangSmith tracing (optional)
```

The diagram above is generated from [`draw_graph.py`](draw_graph.py) — that file is the single place to edit when the architecture changes, and it writes the copy the site serves, so the published diagram cannot drift from the repo's:

```bash
python draw_graph.py     # → graph_mermaid.md + graph.png + frontend/images/architecture-diagram.png
python draw_graph_v2.py  # collapsed variant (retailers folded into the MCP server) → graph_v2_mermaid.md + graph_v2.png
```

`draw_graph_v2.py` imports `build_mermaid()` from `draw_graph.py` rather than keeping its own copy of the source, so the two variants always describe the same system. Rendering goes through mermaid.ink's `pako:` (deflate) URL form — the plain-base64 form now exceeds that server's request-URI limit and returns HTTP 414.

---

## Agent Architecture

Supervisor + 3 specialist pattern. Each specialist runs as an independent ReAct sub-graph, exposed to the Supervisor as a single `@tool`.

| Agent | Role | Tools | Model |
|-------|------|-------|-------|
| **Supervisor** | Query routing, specialist coordination, final answer synthesis, owns clarification | ask_user_clarification + 3 specialist tools | Gemini 3.6 Flash |
| **Sourcing Agent** | Inventory, pricing, where-to-buy — parallel calls to all 6 retail chains every time | 6 retailer tools (via MCP) | Gemini 3.6 Flash |
| **Sommelier Agent** | Pairing recs, drinks knowledge, reviews/scores (Google grounding, with citations) | reasoning_pair_wine, search_web_grounded | Gemini 3.6 Flash |
| **Menu Architect** | (B2B) Design beverage menu from food menu → source real products/prices (direct delegation to Sourcing) | sourcing_agent, search_web_grounded | Gemini 3.6 Flash |

Every agent runs on Gemini 3.6 Flash. The Sommelier and Menu Architect previously ran on Gemini 3.1 Pro Preview; that model was the only source of runtime `499 CANCELLED` failures observed (the same symptom `tests/judge.py` had long carried a retry for), and on Google's published head-to-head 3.6 Flash leads it on every agentic and long-context benchmark — including GDM-MRCR v2 @1M (54.0% vs <27%), which is the metric that matters most here, since both agents must pull the right price and link out of very large tool payloads. `JUDGE_MODEL` stays on 3.1 Pro Preview so eval scores remain comparable across runs.

**Specialist-to-specialist delegation**: The Menu Architect calls `sourcing_agent_tool` directly to source real Vancouver retail products and prices after designing the menu — an in-process hand-off between specialists, without Supervisor mediation. (This is internal LangGraph delegation, not the A2A wire protocol.)

**Multi-turn enforcement**: The Supervisor prompt enforces specialist routing on every turn — when a follow-up asks for a new product category or new recommendations ("also recommend beer", "what about spirits"), it must route to the relevant specialist rather than answering from training knowledge. The "Never invent" rule applies equally on every turn.

**Single-round tool batching (Sommelier)**: A full recommendation typically needs several independent lookups (review searches for the wine, the beer, and the sake picks, plus possibly a pairing-reasoning call). Left to itself, the model issued them one per ReAct round, serializing what LangGraph would happily run in parallel — full-turn latency swung between ~47s and ~110s depending on how many rounds the model chose. The Sommelier prompt now mandates that every independent lookup be emitted **as one batch of tool calls in a single response** (holding a call back only when it genuinely needs a previous call's result), and `max_rounds` was trimmed 4 → 3. Measured effect: ~50s stable full-turn latency with unchanged answer quality.

**Single-round tool batching (Menu Architect)**: The same failure, one layer deeper. The Menu Architect is told to split its sourcing into 2-4 calls by course group, but nothing told it to emit them together — and with `max_rounds=5` the model comfortably spent one round per group. A traced izakaya menu ran its four `sourcing_agent_tool` calls strictly back-to-back (11.9→106s, 117→209s, 214→282s, 295→363s), so 323 of the turn's 443 seconds were sourcing waiting on sourcing. Course groups have no dependency on each other, so the prompt now requires them in one response. Measured effect: **443s → 139s (3.2×)**, 130 → 74 tool calls, with all seven dishes still covered and a longer menu (15.9k → 20.6k chars).

**Category preservation (Supervisor)**: The Sommelier deliberately answers a pairing request across wine, beer, spirit/cocktail, and sake, but the Supervisor's "Answer only what was asked" rule was pruning whole categories during synthesis — an omakase-sushi turn where the Sommelier returned a `Craft Beer` section produced a final answer with zero mentions of beer, and a spicy-Korean-fried-chicken turn dropped beer and sake despite both specialists supplying them. `prompts.py` now states that dropping a category the Sommelier judged relevant is a wrong answer rather than a tighter one, and scopes the older rule to topics the user never raised. Verified by A/B on the omakase prompt: 0/1 categories preserved before, 2/2 after, with no latency cost (89.5s baseline vs 93.6s).

**Pairing-tool guard**: `reasoning_pair_wine_tool` may only be called for a dish/cuisine **the user explicitly named** — never for a dish fabricated from a wine or product name. A product-only query ("synchromesh riesling") is treated as an information request: the Sommelier covers that product's style, profile, and cited reviews (noting suitable food *categories* in prose at most) instead of inventing a meal and branching into every beverage category. Enforced in both the Sommelier system prompt ([`agents/sommelier_agent.py`](agents/sommelier_agent.py)) and the tool docstring ([`agent_tools.py`](agent_tools.py)).

---

## MCP — Model Context Protocol

The six retailer search tools are not bound to the agent in-process — they are served by a dedicated **MCP server** and consumed over the protocol.

**Server — `vancouver-retailers`** ([`mcp_server.py`](mcp_server.py)). A FastMCP server (Streamable HTTP, stateless, JSON responses) exposing the 6 retailer tools with the exact same names, schemas, and JSON result envelopes as the legacy in-process wrappers. Mounted by `app.py` at `/mcp`, so one Cloud Run container serves both the chat API and the MCP endpoint.

**Client — the Sourcing Agent itself** ([`mcp_client.py`](mcp_client.py)). At first use, the Sourcing Agent loads its toolset from the MCP server via `langchain-mcp-adapters` (`MultiServerMCPClient`, `streamable_http` transport) — a self-connection to the mounted endpoint. Each tool invocation opens its own short-lived MCP session, so the agent's **all-6-retailers-in-parallel fan-out stays fully parallel** over the protocol. If the endpoint is unreachable (e.g. running the eval harness without the server), the loader logs an ERROR and falls back to the in-process tools — same tools, different transport.

**External endpoint — `https://<deployment-host>/mcp`.** The Cloudflare worker proxies `/mcp` to Cloud Run (injecting the proxy secret), so any external MCP client — MCP Inspector, Claude Desktop, ADK agents — can discover and call the same retailer tools the agent uses:

```bash
npx @modelcontextprotocol/inspector
# Transport: "Streamable HTTP" → URL: https://<deployment-host>/mcp
# → tools/list shows the 6 retailer tools → call any of them live
```

> The deployment is **unlisted** — see [Access & discoverability](#access--discoverability). Its host is shared privately rather than written down here, so substitute your own.

Security model: direct Cloud Run access to `/mcp` (like `/api/*`) is rejected without the `X-Proxy-Secret` header that only the Cloudflare worker injects. The tools are read-only searches over each retailer's public product-discovery endpoints.

| Env var | Default | Meaning |
|---------|---------|---------|
| `SOURCING_VIA_MCP` | `1` | `0` forces the legacy in-process tools (kill switch) |
| `MCP_SELF_URL` | `http://127.0.0.1:${PORT:-8080}/mcp/` | Where the Sourcing Agent's MCP client connects |

Standalone server (without the FastAPI app): `python mcp_server.py` → `http://127.0.0.1:3001/`. Smoke test: `python scripts/mcp_smoke.py` (asserts the 6 tools load over MCP and a live call returns the expected envelope).

---

## Deployment

Frontend and backend are deployed separately.

| Layer | Service | URL / Identifier |
|-------|---------|------------------|
| **Frontend** | Cloudflare Pages | project `bc-wine-ai-agents` — custom domain not published (see [Access & discoverability](#access--discoverability)) |
| **Backend API** | Google Cloud Run | `bc-wine-agent-135257828500.us-west1.run.app` |
| **Conversation state** | Cloud SQL for PostgreSQL 16 | instance `wine-agent-pg` (us-west1), DB `checkpoints`, unix-socket via `/cloudsql/wine-agent-jh-2026:us-west1:wine-agent-pg` |
| **Session sweep** | Cloud Scheduler | job `cleanup-abandoned-sessions` — daily 04:00 America/Vancouver → `POST /internal/cleanup` |

- Frontend (`frontend/`) is deployed directly to Cloudflare Pages. No build command, output directory `frontend/`.
- Backend is built as a Docker image and deployed to Cloud Run. Gemini API is called via GCP service account authentication.
- `API_BASE` in `frontend/app.js` is empty, so `/api/*` is always same-origin: in production the Cloudflare worker (`frontend/_worker.js`) proxies it to Cloud Run, and locally it hits the same uvicorn server. **No cross-origin request is ever made**, which is why `app.py`'s `CORSMiddleware` is only relevant to a cross-origin dev/test client — its allow-list comes from the `ALLOWED_ORIGINS` env var (comma-separated, default `http://localhost:8000`) rather than being hardcoded.
- Cloud Run serves the API only. `frontend/` is in `.dockerignore`, so the run.app URL returns 404 at `/` and `/api/*` + `/mcp` are rejected without the worker's `X-Proxy-Secret` — the site is not viewable through the backend URL.

### Cloud Run Deployment

```bash
gcloud run deploy bc-wine-agent --source . --region us-west1 --project wine-agent-jh-2026 \
  --allow-unauthenticated --timeout=3600 \
  --add-cloudsql-instances=wine-agent-jh-2026:us-west1:wine-agent-pg \
  --update-secrets=DATABASE_URL=DATABASE_URL:latest
```

> `--timeout=3600` sets Cloud Run's per-request timeout to 1 hour (Cloud Run's maximum). Without it the default is 300s (5 min), and long agent runs are cut off server-side regardless of the frontend timeout.

> `--add-cloudsql-instances` mounts the Cloud SQL unix socket into the container; `--update-secrets` maps the Secret Manager secret `DATABASE_URL` into the env var of the same name (socket-form conninfo: `postgresql://wineagent:…@/checkpoints?host=/cloudsql/wine-agent-jh-2026:us-west1:wine-agent-pg`). Both flags are **additive** and survive later `--source .` redeploys — never use `--set-secrets` / `--set-cloudsql-instances`, which overwrite the existing configuration.

Required IAM roles for the Cloud Run service account:
- `roles/aiplatform.user` — Gemini API calls
- `roles/run.invoker` (allUsers) — public access
- `roles/cloudsql.client` — Postgres checkpointer socket connection
- `roles/secretmanager.secretAccessor` — read the `DATABASE_URL` secret

### Cloudflare Pages Deployment

**The Pages project is connected to this Git repository, so a push to `main` builds and deploys the frontend automatically.** Editing anything under `frontend/` and pushing is the normal path — no CLI step.

A manual deploy is only for pushing frontend changes ahead of a commit:

```bash
npx wrangler pages deploy --project-name=bc-wine-ai-agents --branch=main
```

> A manual upload becomes the live production deployment immediately, but it does **not** update the Git connection — the next push to `main` rebuilds from the repo and supersedes it. Never leave the two out of sync: if you deploy manually, commit the same files.

> The Pages project on the Cloudflare dashboard is named **`bc-wine-ai-agents`**. The `name` field in `wrangler.toml` now matches it, but keep passing `--project-name` explicitly anyway. `--branch=main` targets the production branch (a direct-upload deploy without it can land as a preview).

Cloudflare Pages project settings:
- **Production branch**: `main`
- **Build command**: (none)
- **Build output directory**: `frontend` (from `pages_build_output_dir` in `wrangler.toml`)
- **Custom domain**: configured on the Cloudflare dashboard, not recorded here — see below

### Access & discoverability

The deployment is **unlisted**: anyone holding the link can use it, but nothing points at it and no search engine should carry it. The custom domain is therefore kept out of this repository — code and docs refer to `<deployment-host>` and read real values from the environment (`ALLOWED_ORIGINS`, `DB_E2E_BASE`).

Three layers keep it out of search results, because `robots.txt` alone is only a request that a crawler may ignore:

| Layer | Where | Covers |
|---|---|---|
| `robots.txt` — `Disallow: /` | [`frontend/robots.txt`](frontend/robots.txt) | Well-behaved crawlers, all paths |
| `<meta name="robots" content="noindex, nofollow, noarchive, nosnippet, noimageindex">` | `index.html`, `diagram.html`, `terms.html`, `privacy.html` | The HTML pages |
| `X-Robots-Tag` response header | [`frontend/_worker.js`](frontend/_worker.js) | **Everything**, including assets that cannot carry a meta tag — the architecture PNG, `favicon.svg`, `app.js`, `styles.css` |

Two caveats worth knowing:

- **Cloudflare Pages always also serves `<project>.pages.dev`**, plus a per-deployment preview hostname. Those are live and cannot be turned off from this repo — the noindex layers above cover them, but they remain reachable by anyone who guesses the project name. Blocking them outright needs a Host allow-list in `_worker.js` or a Cloudflare Access policy.
- **noindex removes an already-indexed page only on the next crawl.** For immediate removal, use the Google Search Console *Removals* tool on the property.

Unlisted is link-based, not authenticated. If the requirement becomes "only these specific people", put **Cloudflare Access** in front of the Pages project — that is a real identity check, not obscurity.

---

## Core Features

### Query Validation Gate

Before the graph is invoked, `/api/chat` runs a single Gemini Flash classification call to determine whether the query falls within the agent's scope (drinks / pairing / greetings). Off-topic queries (weather, sports, coding, etc.) bypass the graph entirely and return a short rejection message via SSE tokens **in the user's language**. If the validation LLM fails, it fails open and enters the normal agent path. Measured off-topic response time: ~2.6s (previously ~10s+).

**When the gate is bypassed.** It runs only on new text turns (`not is_resume and not req.images`). Two cases skip it by design:
- **Image turns** — the validator only reads text, so an image with little or no caption would false-trip it. Scope is enforced downstream instead: `vision_node` tags non-drink photos as `document_type="other"` and the Supervisor (Guideline G7) declines them politely.
- **Clarification replies (resume)** — a short in-context answer like "$50" or "the cheaper one" could be misread as off-topic, so the gate is skipped when resuming a pending interrupt.

Implementation: [`validation.py`](validation.py), `VALIDATION_SYSTEM_PROMPT` in [`prompts.py`](prompts.py), gate in [`app.py`](app.py).

### Human-in-the-Loop Clarification

The Supervisor can **explicitly** ask the user follow-up questions using LangGraph's `interrupt()` primitive.

Flow: Supervisor calls `ask_user_clarification_tool(question, options?)` → `interrupt({...})` fires inside the tool → graph pauses at the thread's checkpoint → `app.py` sends an SSE `clarification_request` event with question + options → frontend renders option chips + hint UI → user clicks an option or types free text → next `/api/chat` call detects pending interrupt via `aget_state(config)` → `Command(resume=req.message)` resumes the graph → tool receives the user's reply as a string and returns normally → next supervisor round proceeds.

Rules (`prompts.py` Guideline G6 — "when in doubt, ASK"):
- **Ask**: ambiguous requests (2+ interpretations), missing essential info (pairing with no dish, budget with no range), specialist results inconclusive (0 results, too many matches across categories), conflicting data between specialists, too many strong options that user preference would meaningfully filter.
- **Don't ask**: when a reasonable default exists, or you are stalling instead of making a judgment call.
- **Options**: 2-7 clickable options when natural; user can always type free text instead.
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

Implementation: [`vision.py`](vision.py), `VISION_EXTRACTION_PROMPT` in [`prompts.py`](prompts.py), `vision_node` + `entry_router` in [`agent.py`](agent.py), multimodal input + vision SSE in [`app.py`](app.py), image attachment UI in [`frontend/`](frontend/).

### Tool Robustness — Error Isolation + Query Fallback

**Tool error isolation.** `ToolNode(TOOLS, handle_tool_errors=tool_error_to_json)` catches **all exceptions as `status:"error"` JSON results** — a failing tool is marked as errored while the remaining tools' results are used to answer. Clarification `interrupt` (GraphInterrupt) is re-raised before the handler, so it's unaffected.

**Query fallback.** Some store backends (Okanagan Cellars, Everything Wine, Legacy) **AND-match all query tokens** against product names. The shared helper [`tools/query_fallback.py`](tools/query_fallback.py) retries on zero results by **stripping varietal/vintage, then progressively trimming trailing tokens** (minimum 3 tokens) until a non-empty result set is found.

Implementation: `tool_error_to_json` in [`safety.py`](safety.py) + ToolNode wiring in [`agent.py`](agent.py), `search_with_fallback` in [`tools/query_fallback.py`](tools/query_fallback.py).

### Durable Conversation State — Cloud SQL Postgres Checkpointer

Conversation state (message history, pending interrupts) is persisted in a **shared Cloud SQL Postgres checkpointer**, not in process memory. Cloud Run runs multiple instances: with the previous per-instance `InMemorySaver`, turns of one conversation that landed on different instances lost context and broke clarification resume, and every restart/deploy wiped all sessions. With the shared saver, any instance can serve any turn of any thread.

**Startup wiring.** The graph is built once in `app.py`'s `lifespan()` — not lazily — so the checkpointer's connection pool lives for the whole process lifetime. With `DATABASE_URL` set, a `psycopg` `AsyncConnectionPool` (autocommit, `prepare_threshold=0` for pooler compatibility, `max_size` = `DB_POOL_MAX_SIZE`, default 5) backs an `AsyncPostgresSaver`; `setup()` runs idempotent table migrations. Without `DATABASE_URL`, it falls back to `InMemorySaver` with a startup warning (local dev / tests only).

**Session lifecycle — three cleanup layers** (Postgres has no native TTL):
1. **Explicit close** — closing the chat overlay or the tab (`pagehide`, bfcache-aware) aborts any in-flight stream, then fires `navigator.sendBeacon` (keepalive-`fetch` fallback) to `POST /api/session/{thread_id}/end`, which deletes the thread's checkpoints (`adelete_thread`; best-effort, idempotent, behind the proxy guard but intentionally not rate-limited).
2. **Abandoned-thread sweep** — `POST /internal/cleanup` deletes every thread whose newest checkpoint is older than the cutoff (`CLEANUP_MAX_AGE_DAYS`, default 7). Called daily at 04:00 America/Vancouver by the Cloud Scheduler job `cleanup-abandoned-sessions` against the run.app URL directly (the path is outside `/api/`, so the proxy guard doesn't apply — it has its own `X-Cleanup-Secret` header auth instead). Supports `?dry_run=1` (count only) and `?days=N`; real deletions are floored at `CLEANUP_MIN_AGE_DAYS=1` so a leaked secret can't wipe everything with `days=0`.
3. **Fresh thread per open** — the frontend never reuses a `thread_id` across chat opens, so nothing accumulates per user.

**E2E verification.** `DB_E2E_BASE=https://<your-host> python -m scripts.db_e2e_smoke` drives the live public path (worker-proxied, no secrets needed): health → fresh session → **two-turn recall of a distinctive budget** (proves the checkpoint is written to and read back from Postgres) → **forget after `/end`** (proves `adelete_thread`) → 403 on unauthenticated `/internal/cleanup`.

Implementation: `lifespan()` + `end_session` + `cleanup_sessions` in [`app.py`](app.py), `build_graph(checkpointer)` in [`agent.py`](agent.py), `endSession()` + `pagehide` hook in [`frontend/app.js`](frontend/app.js), smoke test in [`scripts/db_e2e_smoke.py`](scripts/db_e2e_smoke.py).

### Streaming Reliability — SSE Heartbeat + Empty-Response Guard

**SSE heartbeat (proxy idle cut).** Long agent phases stream no bytes for minutes at a time — the sourcing fan-out, the silent relevance-filter pass, the final synthesis round. An intermediate proxy (Cloudflare edge in the Pages-worker → Cloud Run path) severs connections idle past ~100s, which the browser surfaced as a raw "Connection error" mid-turn. `app.py` therefore decouples graph output from the HTTP response with a producer/consumer queue: whenever the queue is idle past `HEARTBEAT_SECONDS` (15s), the stream emits a `: ping` SSE comment. The frontend parser only consumes `data:` lines, so pings are invisible client-side — but the connection never goes silent.

**Gemini empty-response guard.** Gemini intermittently returns an empty candidate ("Gemini produced an empty response. Continuing with empty message"). On a final-answer round, that blank `AIMessage` has no tool calls, so the graph routes to END and the turn finishes with tool badges showing "completed" but no answer text. Three layers prevent this:
1. **Supervisor retry** — `orchestrator_node` re-invokes the model up to `EMPTY_RESPONSE_RETRIES=3` times while the reply has neither tool calls nor text ([`agent.py`](agent.py)).
2. **Specialist retry** — the shared ReAct sub-graph applies the same blank-response check with up to 2 re-invokes, so a specialist never returns an empty answer to the Supervisor ([`agents/react_subagent.py`](agents/react_subagent.py)).
3. **Stream fallback** — `app.py` tracks whether any answer token actually reached the client; if the turn ends with nothing streamed and no pending clarification, it recovers the final AI message from checkpoint state and emits it as a single `final-fallback` token, so the UI never ends on a blank reply.

Verification: `scripts/verify_empty_guard.py` — deterministic stub tests forcing blank responses (asserts the retries recover a real answer) plus a live regression turn.

**Transient API-failure retry.** Gemini intermittently drops a request with `499 CANCELLED`, and less often 429/5xx or a deadline. Because 499 is a 4xx, the SDK classifies it as a client error and does **not** retry it — so a single blip silently deleted an entire specialist's contribution for the turn. `run_subagent_json` caught the exception and returned a `status="error"` envelope, which kept the turn alive but left the Supervisor to answer without that specialist and to apologise for a "technical hiccup" in the user's answer. `models.ainvoke_with_retry` now wraps every specialist LLM call with exponential backoff (`LLM_MAX_ATTEMPTS=3`, 1s doubling) over the same transient-hint list `tests/judge.py` has long used for the eval judge. Non-transient errors re-raise immediately, and `asyncio.CancelledError` — a `BaseException` — passes straight through, so a disconnected client is never retried against.

**One event pair per real tool call.** The Sourcing Agent's retailer tools are `StructuredTool` wrappers around the MCP adapter tools (`mcp_client._flat_tool`), so a single call produced two *nested* runs with the same name and args. Both fired `on_tool_start`/`on_tool_end`, so the SSE stream showed every retailer search twice — and the inner run returns raw content blocks that summarize to zero rows, so the pair even disagreed on the count. (No work was duplicated; only the instrumentation was.) `app.py` now tracks tool run ids and suppresses any tool run whose ancestor chain already contains a run of the same name, emitting only the outermost.

**Failed specialists read as failed.** A `status="error"` envelope carries no inner tools, so its result count was 0 — which fell through to the UI's "completed" label and hid the failure behind a finished-looking badge. `tool_end` now carries an explicit `error` field, and the frontend renders `failed` with the message in the badge tooltip and panel.

---

## UI/UX

- **19+ gate** — first visit shows a one-click age confirmation before the landing page is usable. The answer is stored in `localStorage`, and an inline script in `<head>` applies the `age-ok` class before first paint so returning visitors never see it flash.
- **Landing + fullscreen chat overlay** — a landing page with capability descriptions; clicking "Start chatting" opens a fullscreen chat overlay.
- **Persistent chat disclaimer** — a muted line under the chat input carries the non-commercial, non-affiliation, and responsible-drinking statements. It lives in the chat chrome rather than in the message stream: the overlay is `position: fixed; inset: 0`, so the page footer that normally carries those statements is hidden while the chat is open, and appending them to answers instead would both clutter the transcript and collide with the `run_id` bubble logic described below.
- **Page shell** — `body` is a flex column; `.landing` and `.page-main` claim `flex: 1` and the secondary background, and `.site-footer` uses `margin-top: auto`. A new page must use one of those two shells or it will render on the wrong background with the footer riding up under the content.
- **Soft wine color palette** — desaturated burgundy (`#7A3D4F`) tone.
- **Status indicator** — top-left of chat header shows **symbol only** (no text). A fixed dot when idle, a spinning ring when active. `aria-live` delivers status text to screen readers.
- **Agent box** — specialist agent results (Sourcing, Sommelier, Menu Architect) render in collapsible agent-box components showing inner tool call details and the answer in markdown.
- **Tool badges** — each tool call renders as an expandable badge. Shows result count on completion + click for result preview dropdown.
- **Session per chat open** — a new `thread_id` is issued each time the chat overlay opens. Follow-ups within the same overlay share memory, but closing and reopening starts fresh. Closing the chat — or the tab (`pagehide`, skipped when the page is bfcache-persisted) — also ends the session server-side: any in-flight stream is aborted first (so the running graph can't re-write a checkpoint just deleted), then `navigator.sendBeacon` (keepalive-`fetch` fallback) posts to `/api/session/{thread_id}/end` to delete the thread's checkpoints from Postgres.
- **Real-time token streaming** — orchestrator tokens stream to the client immediately via SSE. Each orchestrator round carries a unique `run_id`; the frontend detects `run_id` changes and clears the previous partial answer, so intermediate tool-calling rounds are naturally replaced by the final answer round. On clarification interrupts, any partial text is cleaned up before the clarification UI appears.
- **Request timeout + error recovery** — 60-minute `AbortController` timeout (matches Cloud Run's max `--timeout=3600`) prevents infinite spinner on backend hangs. Non-200 responses (429 rate limit, 5xx errors) are caught before SSE parsing with user-facing error messages. A `finally` safety net resets the spinner if the stream ends without a `done` event. The backend also emits `done` after `error` events for protocol completeness.
- **Links open in new tab** — all `<a>` tags from `marked.parse` get `target="_blank" rel="noopener noreferrer"` injected automatically.

---

## Legal & compliance

This is a **free, non-commercial demo** — nothing is sold, and no referral or affiliate
revenue is earned from any link in an answer. That is not just positioning: BC's Liquor
Control and Licensing Regulation s.169–170 restricts *any person* (not only licensees) who
publishes an advertisement in relation to liquor, and "advertisement" is a commercial notion.
Keeping the project non-commercial and saying so plainly is what keeps it outside that
reading. **Do not add affiliate or referral links** — that single change would undo it.

What the regulation asks for, and where each piece lives:

| Requirement | Implementation |
| --- | --- |
| s.169(1)(e) — carry a responsible-use statement | `.chat-disclaimer` under the chat input, plus the footer on every page |
| s.170(1)(a) — not a medium minors are expected to reach | one-click 19+ gate on first visit (`index.html` + `app.js`, `localStorage`) |
| Not affiliated with any retailer or producer | stated in the chat disclaimer, the footer, and `terms.html` |
| Reliance on stale scraped pricing | `terms.html` — pricing explicitly non-authoritative, no warranty, limitation of liability |
| BC PIPA — collection, retention, processors | `privacy.html`, backed by the 7-day sweep in [Durable Conversation State](#durable-conversation-state--cloud-sql-postgres-checkpointer) |

Notes for anyone editing this:

- **The disclaimer is UI, not a token.** It was briefly appended to each answer server-side.
  That fails twice: it clutters the transcript, and a token carrying a new `run_id` makes the
  frontend delete the bubble accumulated so far (see the streaming note in [UI/UX](#uiux)) —
  which erased the answer and left only the disclaimer on screen. Keep it in the chat chrome.
- **Retention has to match the policy.** `privacy.html` states conversation threads are
  deleted after 7 days; that number is `CLEANUP_MAX_AGE_DAYS` and the Cloud Scheduler job that
  calls `/internal/cleanup`. Change one, change the other.
- **The MCP endpoint is public and unauthenticated by design** — it is the interoperability
  demonstration. It is covered by `terms.html` and rate-limited, but it does serve product and
  pricing data to any caller, so treat widening it as a decision, not a detail.
- **Contact / takedown** is `info@sumai.ca`, listed in `terms.html`, `privacy.html`, and the
  footer. If a retailer asks to be excluded, dropping their tool from `mcp_server.py` and
  `agent_tools.py` is the intended response.

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
| **Google Search grounding** | `tools/google_search_tool.py` | Gemini native grounding (Gemini Enterprise Agent Platform) | — (ADC) |

---

## Tool Details

The six retailer tools below are exposed to the Sourcing Agent (and to external clients) through the `vancouver-retailers` MCP server — see [MCP](#mcp--model-context-protocol). The `tools/*.py` modules hold the underlying search implementations.

### 1. BC Liquor Store (`tools/bcliquor_tool.py`)

BC's government liquor retailer (200+ locations province-wide). Carries wine, beer, spirits, and cider.

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

Knowledge and review search using Gemini's native Google Search grounding. Runs on Gemini Enterprise Agent Platform credentials (ADC) with no extra API key required.

- **Data**: grounded answer + source URL list
- **Use cases**: drinks education, region/producer info, reviews/scores (citation + summary only, no full-text reproduction), supplementing gaps in store tool results
- **Copyright guardrail**: caller prompts enforce source attribution + summary only, prohibiting verbatim reproduction of reviews
- **Deep-link resolution**: Gemini grounding returns each source as an opaque redirect token (`vertexaisearch.cloud.google.com/grounding-api-redirect/…`), not the real page URL. These ~200-char tokens expire (~30 days), and because their only human-readable part is the bare domain, the Supervisor LLM tends to shorten them to the site homepage or drop them when composing the final answer. `search_web_grounded` resolves each token to its real destination deep URL server-side (concurrent `httpx`, first `Location` hop, graceful fallback to the token on failure) and rewrites both the source list and any inline links in the answer — so the model only ever sees short, stable, copy-able deep links. Caller prompts (`agents/sommelier_agent.py`, `prompts.py`) additionally require source URLs to be reproduced verbatim, never reduced to a homepage.

```python
results, answer = await search_web_grounded("best food pairings for BC Pinot Noir")
```

---

## Project Structure

```
Vancouver-Sommelier-AI/
├── agent.py                    # LangGraph Supervisor graph (entry_router + vision + supervisor ↔ tools, blank-response retry)
├── agent_tools.py              # @tool wrappers + specialist groups (SOURCING / SOMMELIER / SUPERVISOR_DIRECT)
├── app.py                      # FastAPI backend (SSE streaming + 15s heartbeat, validation gate, Postgres checkpointer lifecycle, session end/cleanup, /mcp mount)
├── mcp_server.py               # MCP server "vancouver-retailers" — 6 retailer tools over Streamable HTTP
├── mcp_client.py               # Sourcing Agent's MCP tool loader (self-connection + in-process fallback)
├── validation.py               # Pre-agent query validation (off-topic bypass)
├── vision.py                   # Multimodal label/wine-list/food-menu extraction (VisionExtraction schema)
├── state.py                    # AgentState TypedDict (messages + tool_call_log + vision_extractions)
├── models.py                   # Gemini LLM factory (3.6 Flash agents + 3.1 Pro Preview judge) + transient retry
├── prompts.py                  # Supervisor/specialist/pairing/relevance-filter/validation/vision prompts
├── safety.py                   # tool_error_to_json (tool exceptions → status:error JSON, ToolNode isolation)
├── HYPERPARAMETERS.md          # All tuning constants (temperatures, timeouts, limits)
├── requirements.txt            # Python dependencies
├── Dockerfile                  # Container build (python:3.12-slim, uvicorn, port 8080)
├── .dockerignore               # Docker build exclusions
├── agents/                     # Specialist agents (independent ReAct sub-graphs)
│   ├── __init__.py             # Architecture docs
│   ├── react_subagent.py       # Shared ReAct sub-graph builder (+ blank-response retry) + run_subagent_json wrapper
│   ├── sourcing_agent.py       # Sourcing Agent — parallel search across 6 retail chains
│   ├── sommelier_agent.py      # Sommelier Agent — pairing + grounding
│   └── menu_architect.py       # Menu Architect — B2B beverage menu design (delegates to Sourcing)
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
│   ├── index.html              # Landing + 19+ gate + fullscreen chat overlay
│   ├── diagram.html            # Architecture diagram viewer
│   ├── terms.html              # Terms of use (AI-output disclaimers, liability, BC law)
│   ├── privacy.html            # Privacy policy (BC PIPA)
│   ├── styles.css              # Wine color palette, chat + tool badge + agent-box styles
│   ├── app.js                  # Age gate, SSE client, image attachment, tool badges, markdown
│   ├── favicon.svg
│   ├── robots.txt              # Disallow: / — the deployment is unlisted
│   ├── images/                 # Architecture diagram asset (written by draw_graph.py)
│   └── _worker.js              # Cloudflare Workers proxy (API routing + security filtering + X-Robots-Tag)
├── scripts/                    # Utility scripts
│   ├── debug_everythingwine.py # Everything Wine HTML structure debugging
│   ├── mcp_smoke.py            # MCP smoke test (tools load + live call over the protocol)
│   ├── db_e2e_smoke.py         # Live E2E smoke of the Postgres checkpointer (recall / forget / cleanup auth)
│   └── verify_empty_guard.py   # Empty-response guard tests (stubbed retries + live regression)
├── draw_graph.py               # Architecture Mermaid diagram generator — single source of truth; also writes frontend/images/
├── draw_graph_v2.py            # Same diagram via build_mermaid(show_stores=False), retailers collapsed into the MCP server
├── tests/                      # Golden-query quality evaluation
│   ├── golden_queries.py       # Golden queries (multiple categories)
│   ├── metrics.py              # Deterministic metrics (orchestration, hallucination, coverage, structure)
│   ├── judge.py                # LLM-as-judge (Gemini 3.1 Pro Preview temp=0)
│   ├── quality_eval.py         # Runner — produces results.json + summary.md + transcripts
│   └── results/<timestamp>/    # Per-run outputs (gitignored; one reference run committed for judging)
├── .env                        # API keys (gitignored)
├── .gitignore
└── README.md
```

---

## Setup

### Installation

```bash
git clone https://github.com/SUM-AI-ca/Vancouver-Sommelier-AI.git
cd Vancouver-Sommelier-AI

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

Create a `.env` file (everything is optional for local runs):

```
# LangSmith (optional — tracing & observability)
LANGSMITH_TRACING=true
LANGSMITH_API_KEY=lsv2_sk_...
LANGSMITH_PROJECT=bc-wine-agent
LANGSMITH_ENDPOINT=https://api.smith.langchain.com

# Durable conversation state (optional locally — omit to use in-memory state)
# DATABASE_URL=postgresql://user:pass@localhost:5432/checkpoints
```

Full reference:

| Env var | Default | Meaning |
|---------|---------|---------|
| `DATABASE_URL` | (unset) | Postgres conninfo for the shared checkpointer. Unset ⇒ `InMemorySaver` (local dev only — state is per-instance and lost on restart). In production this is a Secret Manager secret in unix-socket form: `postgresql://wineagent:…@/checkpoints?host=/cloudsql/wine-agent-jh-2026:us-west1:wine-agent-pg` |
| `DB_POOL_MAX_SIZE` | `5` | Max connections in the checkpointer's async pool |
| `CLEANUP_SECRET` | (unset) | `X-Cleanup-Secret` header value for `/internal/cleanup` (unset ⇒ endpoint always 403s) |
| `CLEANUP_MAX_AGE_DAYS` | `7` | Default cutoff for the abandoned-thread sweep |
| `PROXY_SECRET` | (empty) | Shared secret the Cloudflare worker injects as `X-Proxy-Secret`; when set, direct Cloud Run access to `/api/*` and `/mcp` is rejected without it |
| `CF_TURNSTILE_SECRET` | (unset) | Cloudflare Turnstile server key; unset ⇒ bot verification disabled (current production setting) |
| `ALLOWED_ORIGINS` | `http://localhost:8000` | Comma-separated CORS allow-list. Production needs nothing here — `API_BASE` is empty, so the browser never goes cross-origin (see [Access & discoverability](#access--discoverability)) |
| `GOOGLE_CLOUD_PROJECT` | `wine-agent-jh-2026` | GCP project for Gemini calls |
| `GOOGLE_CLOUD_LOCATION` | `global` | Gemini location |
| `SOURCING_VIA_MCP` / `MCP_SELF_URL` | see [MCP](#mcp--model-context-protocol) | Sourcing-agent transport switches |
| `LANGSMITH_*` | (unset) | Tracing/observability (auto-enabled when set) |

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
python -m uvicorn app:app --port 8080
```

Open `http://localhost:8080` in a browser to access the chat UI.

Port 8080 matches the default `MCP_SELF_URL` (`http://127.0.0.1:8080/mcp/`), so the Sourcing Agent loads its tools over MCP locally too. On a different port, set `MCP_SELF_URL` accordingly — otherwise the loader logs an ERROR and falls back to direct in-process tools (everything still works; only the transport differs).

Without `DATABASE_URL`, startup logs a warning and uses `InMemorySaver` — fine for local development (state lives in the single process and vanishes on restart). Point `DATABASE_URL` at any local Postgres to exercise the durable checkpointer path; `AsyncPostgresSaver.setup()` creates its tables on first start.

### Docker (Local)

```bash
docker build -t bc-wine-agent .
docker run -p 8080:8080 --env-file .env bc-wine-agent
```

### Production Deployment

```bash
# Cloud Run (backend) — the Cloud SQL / secret flags are additive and persist across redeploys
gcloud run deploy bc-wine-agent --source . --region us-west1 --project wine-agent-jh-2026 \
  --allow-unauthenticated --timeout=3600 \
  --add-cloudsql-instances=wine-agent-jh-2026:us-west1:wine-agent-pg \
  --update-secrets=DATABASE_URL=DATABASE_URL:latest

# Cloudflare Pages (frontend) — direct upload via Wrangler (no git integration)
npx wrangler pages deploy --project-name=bc-wine-ai-agents --branch=main
```

---

## Tech Stack

- **LangGraph** — multi-agent Supervisor + 3 specialist sub-graph orchestration
- **MCP (Model Context Protocol)** — FastMCP server `vancouver-retailers` (mcp==1.27.2) serving the 6 retailer tools over Streamable HTTP; consumed by the Sourcing Agent via **langchain-mcp-adapters** (0.2.2); also reachable by external MCP clients at `<deployment-host>/mcp`
- **Gemini 3.6 Flash** — every agent (Supervisor, Sourcing, Sommelier, Menu Architect) plus validation and the vision node
- **Gemini 3.1 Pro Preview** — LLM-as-judge only (eval pipeline), kept distinct so the system never grades its own work
- **Google Search grounding** — reviews/scores/factual knowledge (Gemini Enterprise Agent Platform native)
- **FastAPI** — SSE streaming backend (15s heartbeat keepalive against proxy idle cuts)
- **Cloud SQL (PostgreSQL 16)** — durable cross-instance conversation checkpoints via **langgraph-checkpoint-postgres** (`AsyncPostgresSaver`) + **psycopg[binary,pool]**
- **Cloud Scheduler** — daily abandoned-session sweep (`POST /internal/cleanup`)
- **HTML/CSS/JS** — wine-colored chat UI (vanilla, no build step)
- **Google Cloud Run** — backend container hosting
- **Cloudflare Pages** — frontend static hosting + custom domains (deployed via Wrangler direct upload)
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
```

Results are saved to `tests/results/<YYYYMMDD-HHMMSS>/` as `results.json`, `summary.md`, and `transcripts/<id>.md`.

### How it works — LLM-as-Judge

Each turn's final response is scored by a **separate judge model** (Gemini 3.1 Pro Preview, temperature=0) — deliberately distinct from the agent's Gemini 3.6 Flash, so the system never grades its own work. The judge sees the user question, prior turns (for follow-ups), the **complete tool evidence** the agent received, and the final response. It scores five dimensions: **relevance, correctness, helpfulness, coherence, harmlessness** (plus an `overall`).

**Correctness is derived, not guessed** (RAGAS-style faithfulness). Instead of asking the judge for a holistic "how correct is this" number, `judge.py` has it extract every **atomic, checkable claim** (price, review score, stock level, vintage, purchase URL, region, ABV, producer fact) and label each one against the evidence:

| Label | Meaning | Counts as hallucination? |
|-------|---------|--------------------------|
| `SUPPORTED` | The specific value appears in the tool evidence (numbers must match) | No |
| `GENERAL_KNOWLEDGE` | Not in evidence, but standard sommelier/world knowledge ("Syrah shows black pepper") | No — **excluded from the denominator** |
| `NOT_IN_EVIDENCE` | A specific checkable value that is genuinely absent and not general knowledge | **Yes** |
| `CONTRADICTED` | The evidence states a different value (says $29.99, evidence says $34.99) | **Yes (2× weight)** |

The correctness score (1–5) is then computed deterministically from the label counts:

```
checkable T = #SUPPORTED + #NOT_IN_EVIDENCE + #CONTRADICTED          (GENERAL_KNOWLEDGE excluded)
penalty     = #NOT_IN_EVIDENCE + 2 × #CONTRADICTED                   (CONTRADICTION_WEIGHT = 2)
ratio       = penalty / T  →  bands (0.0→5, 0.15→4, 0.35→3, 0.6→2, else 1)
```

Excluding `GENERAL_KNOWLEDGE` from the denominator is the key anti-false-positive rule — it prevents a competent sommelier statement ("tannic reds clash with sweet sauces") from being scored as a hallucination. The tunables (`CONTRADICTION_WEIGHT`, `CORRECTNESS_RATIO_BANDS`, `EVIDENCE_BUDGET_CHARS`) live in [`tests/judge.py`](tests/judge.py) / [`tests/metrics.py`](tests/metrics.py) and are documented in [`HYPERPARAMETERS.md`](HYPERPARAMETERS.md). Transient judge API failures are retried with exponential backoff so one blip doesn't drop a turn's score.

### Golden query suite

28 queries across **15 categories** in [`tests/golden_queries.py`](tests/golden_queries.py); multi-turn entries expand to **34 graded turns**. Each entry declares what the agent *should* do, so the judge has explicit expectations.

| | | |
|---|---|---|
| `INV` inventory / buyability | `CRI` reviews / critic opinion | `DISC` discovery / filter |
| `PAIR-W` western common pairings | `PAIR-C` complex western pairings | `PAIR-N` non-western pairings |
| `EDU` educational | `SOM` sommelier-level | `BEG` beginner-level |
| `MT-REF` multi-turn reference resolution | `MT-PREF` multi-turn preference | `FB` fallback / disambiguation |
| `ML` multilingual (ZH / JA) | `B2B` menu architect | `OFF` off-topic / safety |

### Latest run — `20260608-093835`

28 queries → 34 turns, 0 errored.

| Dimension | Average (N=34) |
|-----------|----------------|
| relevance | 5.00 |
| helpfulness | 5.00 |
| harmlessness | 5.00 |
| coherence | 4.97 |
| correctness | 4.82 |
| **overall** | **4.88** |

**Claim & evidence health** — across **542** extracted claims: 523 `SUPPORTED`, 12 `GENERAL_KNOWLEDGE`, 5 `NOT_IN_EVIDENCE`, 2 `CONTRADICTED` → **~96.5% grounded** in retrieved evidence. 0 turns hit the evidence-truncation budget (so low-correctness turns are real signal, not a measurement artifact).

The 7 hallucination-flagged claims cluster on a single pattern: the agent embellishes **wine production details that no tool returned** — grape-blend composition, lees-aging duration, winemaker names, and tasting-note attribution — while its sourcing facts (price, stock, links, scores) stay fully grounded. This finding feeds the prompt "Never invent" guardrails in [`prompts.py`](prompts.py).

Per-run artifacts: `results.json` (full structured data), `summary.md` (human-readable rollup), and `transcripts/<id>.md` (per-query tool I/O + final response + judge verdicts).
