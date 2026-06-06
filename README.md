# Vancouver Drinks AI

밴쿠버 주류 시장을 위한 멀티 에이전트 AI 음료 컨시어지. LangGraph Supervisor + 3 specialist 에이전트 아키텍처로, 6개 밴쿠버 주류 매장의 실시간 재고/가격을 통합 검색하고, Google Search grounding 기반 전문가 지식과 푸드 페어링을 제공한다. B2C (소비자 추천) + B2B (식음업체 음료 메뉴 설계) 모두 지원.

**Live: [wineaiagent.com](https://wineaiagent.com)**

현재 단계: **프로덕션 배포 완료.** Cloudflare Pages (프론트엔드) + Google Cloud Run (백엔드 API) 분리 호스팅. 멀티 에이전트 Supervisor + 3 specialist (Sourcing / Sommelier / Menu Architect), FastAPI SSE 스트리밍, 멀티모달 vision 노드 (와인 라벨 / 와인리스트 / 음식 메뉴 사진 스캔), human-in-the-loop clarification, pre-agent query validation gate, golden-query + LLM-as-judge 품질 평가 파이프라인 가동 중.

---

## 전체 구조

```
사용자 질문 (+ 와인 라벨/리스트/음식 메뉴 사진 첨부 가능)
    ↓
Cloudflare Pages (frontend/ — vanilla HTML/CSS/JS, 빌드 스텝 없음)
    ↓  CORS (cross-origin fetch)
Google Cloud Run — FastAPI 백엔드 (app.py — SSE 스트리밍)
    ↓
Validation Gate (validation.py — Gemini Flash 분류)   ※ 이미지 첨부 시 우회
    │
    ├─ INVALID → 사용자 언어로 거절 → 그래프 우회 → 종료
    │
    └─ VALID ↓
LangGraph Supervisor (agent.py — Gemini 3.5 Flash)
    │
    │   entry_router ─(이미지)─→ vision_node ─┐
    │                └─(텍스트)──────────────┴→ supervisor
    │
    │   supervisor → specialist 라우팅 (+ clarification / preferences 직접 소유)
    │       ↓ (ask_user_clarification_tool)
    │    interrupt() → SSE clarification_request → 유저 응답
    │       ↓ Command(resume=...) → 다음 supervisor round
    │
    │   ┌─────────────────────────────────────────────────────────────┐
    │   │  Specialist Agents (독립 ReAct sub-graph)                    │
    │   │                                                             │
    │   │  Sourcing Agent ──── 6개 매장 병렬 검색 (가격/재고/구매처)     │
    │   │    └─ bcliquor, everythingwine, okanagan_cellars,           │
    │   │       suttonplace, marquis, legacy                          │
    │   │                                                             │
    │   │  Sommelier Agent ── 페어링 추천 + Google Search grounding    │
    │   │    └─ reasoning_pair_wine, search_web_grounded              │
    │   │                                                             │
    │   │  Menu Architect ─── (B2B) 음식 메뉴 → 음료 메뉴 설계         │
    │   │    └─ sourcing_agent (A2A), search_web_grounded             │
    │   └─────────────────────────────────────────────────────────────┘
    │
    │   supervisor 최종 답변 → END
    ↓
SSE 스트리밍 → 프론트엔드 (agent-box UI + 툴 배지 + 마크다운 렌더링)
```

---

## 에이전트 아키텍처

Supervisor + 3 specialist 패턴. 각 specialist는 독립 ReAct sub-graph로, Supervisor에게 단일 `@tool`로 노출된다.

| Agent | 역할 | 사용 Tool | 모델 |
|-------|------|-----------|------|
| **Supervisor** | 쿼리 라우팅, specialist 조율, 최종 답변 합성, clarification/preferences 직접 소유 | ask_user_clarification, update_preferences + 3 specialist tools | Gemini 3.5 Flash |
| **Sourcing Agent** | 재고, 가격, 구매처 검색 — 매번 6개 매장 병렬 호출 | 6개 store tools | Gemini 3.5 Flash |
| **Sommelier Agent** | 페어링 추천, 음료 지식, 리뷰/점수 (Google grounding 기반, 인용 포함) | reasoning_pair_wine, search_web_grounded | Gemini 3.1 Pro Preview |
| **Menu Architect** | (B2B) 음식 메뉴에서 음료 메뉴 설계 → 실제 상품/가격 소싱 (A2A 위임) | sourcing_agent (A2A), search_web_grounded | Gemini 3.1 Pro Preview |

**Agent-to-Agent (A2A)**: Menu Architect는 음료 메뉴 설계 후 `sourcing_agent_tool`을 호출해 실제 밴쿠버 매장의 상품/가격을 가져온다. Supervisor가 중개하지 않는 직접 위임.

---

## 배포 아키텍처

프론트엔드와 백엔드를 분리 배포한다.

| 계층 | 서비스 | URL |
|------|--------|-----|
| **프론트엔드** | Cloudflare Pages | `wineaiagent.com` / `www.wineaiagent.com` |
| **백엔드 API** | Google Cloud Run | `bc-wine-agent-135257828500.us-west1.run.app` |

- 프론트엔드(`frontend/`)는 Cloudflare Pages에 직접 배포. 빌드 커맨드 없음, 출력 디렉토리 `frontend/`.
- 백엔드는 Docker 이미지로 빌드해 Cloud Run에 배포. Gemini API는 GCP 서비스 계정 인증으로 호출.
- 프론트엔드 JS(`frontend/app.js`)가 `API_BASE`로 Cloud Run URL을 직접 호출하고, `app.py`의 `CORSMiddleware`가 `wineaiagent.com` / `www.wineaiagent.com` origin을 허용한다.
- 로컬 개발 시에는 `API_BASE`가 빈 문자열이 되어 같은 서버의 `/api/*` 엔드포인트를 호출.

### Cloud Run 배포

```bash
gcloud run deploy bc-wine-agent --source . --region us-west1 --project wine-agent-jh-2026 --allow-unauthenticated
```

Cloud Run 서비스 계정에 필요한 IAM 역할:
- `roles/aiplatform.user` — Gemini API 호출
- `roles/run.invoker` (allUsers) — 퍼블릭 접근

### Cloudflare Pages 배포

Cloudflare Pages 프로젝트 설정:
- **Production branch**: `main`
- **Build command**: (없음)
- **Build output directory**: `frontend`
- **Custom domains**: `wineaiagent.com`, `www.wineaiagent.com`

---

## 핵심 기능

### Query Validation Gate

`/api/chat`이 그래프를 호출하기 **전에** 한 번의 Gemini Flash 분류 호출로 쿼리가 에이전트 범위(음료 / 페어링 / 인사) 안에 있는지 판정한다. Off-topic이면 (날씨, 스포츠, 코딩 질문 등) 그래프를 건너뛰고 **사용자 입력 언어 그대로** 짧은 거절 메시지를 SSE 토큰으로 흘려보낸다. 한국어 질문엔 한국어, 영어 질문엔 영어로 자동 응답. 검증 LLM이 실패하면 fail-open으로 기존 에이전트 경로로 그대로 진입. 실측 오프토픽 응답 시간 ~2.6s (기존 ~10s+).

구현: [`validation.py`](validation.py), [`prompts.py`](prompts.py)의 `VALIDATION_SYSTEM_PROMPT`, [`app.py`](app.py) 게이트 삽입.

### Human-in-the-Loop Clarification

LangGraph의 `interrupt()` primitive를 이용해 Supervisor가 **명시적으로** 유저에게 되묻을 수 있다.

흐름: Supervisor가 `ask_user_clarification_tool(question, options?)`을 호출 → tool 내부에서 `interrupt({...})` 발생 → 그래프가 같은 thread의 checkpoint에 멈춤 → `app.py`가 SSE `clarification_request` 이벤트로 question + options를 프론트에 전송 → 프론트가 옵션 chip + hint UI 렌더링 → 유저가 옵션 클릭 or 자유 입력 → 다음 `/api/chat` 호출 진입 시 `aget_state(config)`로 pending interrupt 감지 → `Command(resume=req.message)`로 그래프 재개 → tool은 유저 응답을 string으로 받고 정상 종료 → 다음 supervisor round 진행.

규칙(`prompts.py` Guideline G6):
- **묻는다**: 2+ 해석 가능한 모호 쿼리, 비슷한 점수의 매칭이 다수일 때, 필수 정보 누락.
- **묻지 않는다**: user_preferences로 답이 나오는 경우, default가 자연스러운 경우, 정보성/교육성 질문.
- **횟수 제한**: 한 turn에 최대 3회 (`MAX_CLARIFICATIONS_PER_TURN`). cap 도달 시 강제로 best-effort 답변.
- **Round counting**: clarification-only round는 `MAX_TOOL_ROUNDS` 카운트에서 제외.
- **Validation skip on resume**: clarification 응답이 validator를 트립하지 않도록 resume 분기에선 validation 게이트를 건너뜀.

구현: [`agent_tools.py`](agent_tools.py)의 `ask_user_clarification_tool`, [`agent.py`](agent.py)의 `_count_clarifications_this_turn`, [`app.py`](app.py)의 interrupt 감지 + `Command(resume=...)` 분기, [`frontend/app.js`](frontend/app.js)의 `renderClarification()`.

### Vision — 멀티모달 라벨/와인리스트/음식 메뉴 스캔

사용자가 **와인 라벨**, **레스토랑 와인 리스트**, 또는 **음식 메뉴 사진**을 첨부하면, Supervisor 앞단의 전용 `vision_node`가 먼저 돌아 사진 속 텍스트를 구조화 추출한 뒤 기존 검색/추천 흐름으로 넘긴다.

흐름: 프론트가 사진을 긴 변 ≤2048px JPEG로 다운스케일/재인코딩해 base64로 전송 → `app.py`가 텍스트+이미지 멀티모달 `HumanMessage` 구성 (이미지 첨부 시 validation 게이트 우회) → `entry_router`가 이미지 유무로 분기 → `vision_node`가 `with_structured_output(VisionExtraction)`으로 **보이는 텍스트만** 추출 → 추출 결과를 **같은 id로 `HumanMessage` 교체**해 이미지를 버리고 텍스트로 fold (토큰 절약) → supervisor는 text-only로 동작.

- **와인 라벨**: producer/cuvee/품종/vintage/region 등 1종 추출 → store 툴로 가격/재고 조회.
- **와인 리스트**: 줄별 verbatim `raw_text` + 파싱 필드로 N종 추출 → 리스트의 와인을 전부 조회/비교.
- **음식 메뉴**: 메뉴 텍스트 추출 → Menu Architect 에이전트가 음료 메뉴 설계.
- **무손실**: named field에 안 맞는 텍스트는 catch-all(`other_text`/`raw_text`)에 보존. 비와인 사진은 `document_type="other"`로 정중히 거절.
- **UI**: 첨부 버튼 + 드래그드롭 + 클립보드 붙여넣기, 썸네일 미리보기(최대 2장), `vision_start`/`vision_result` SSE로 "Image analysis" 배지 표시.

구현: [`vision.py`](vision.py), [`prompts.py`](prompts.py)의 `VISION_EXTRACTION_PROMPT`, [`agent.py`](agent.py)의 `vision_node` + `entry_router`, [`app.py`](app.py)의 멀티모달 입력 + vision SSE, [`frontend/`](frontend/)의 이미지 첨부 UI. 설계 문서는 [`docs/VISION_NODE_DESIGN.md`](docs/VISION_NODE_DESIGN.md).

### Tool 견고성 — 에러 격리 + 쿼리 폴백

**툴 에러 격리.** `ToolNode(TOOLS, handle_tool_errors=tool_error_to_json)`로 **모든 예외를 `status:"error"` JSON 결과로 격리** — 실패한 툴은 에러로 표시되고 나머지 툴 결과로 답변을 이어간다. clarification의 `interrupt`(GraphInterrupt)는 핸들러보다 먼저 re-raise되어 영향 없음.

**쿼리 폴백.** 일부 store 백엔드(Okanagan Cellars, Everything Wine, Legacy)는 쿼리의 **모든 토큰을 AND 매칭**한다. 공통 헬퍼 [`tools/query_fallback.py`](tools/query_fallback.py)가 0건이면 **품종/연도를 떼고 → 뒤 토큰을 점진적으로 줄여** 재시도해 첫 비어있지 않은 결과를 반환한다.

구현: [`safety.py`](safety.py)의 `tool_error_to_json` + [`agent.py`](agent.py) ToolNode 연결, [`tools/query_fallback.py`](tools/query_fallback.py)의 `search_with_fallback`.

---

## UI/UX

- **랜딩 + 풀스크린 채팅 오버레이** — 간단한 capability 설명이 있는 랜딩 페이지에서 "Start chatting" 버튼을 누르면 화면을 가득 채우는 채팅 오버레이가 뜬다.
- **연한 와인 컬러 팔레트** — 데사추레이트된 burgundy(`#7A3D4F`) 톤.
- **상태 인디케이터** — 채팅 헤더 좌상단에 텍스트 없이 **심볼만** 표시한다. 대기 중에는 고정된 점, 작동 중에는 회전 링 스피너로 전환. `aria-live`로 스크린리더에 상태 텍스트 전달.
- **Agent box** — specialist agent(Sourcing, Sommelier, Menu Architect) 호출 결과가 접을 수 있는 agent-box 컴포넌트로 렌더링됨. inner tool 호출 상세와 답변을 마크다운으로 표시.
- **툴 배지** — 각 tool 호출이 expandable 배지로 렌더링됨. 완료되면 결과 개수 표시 + 클릭으로 결과 미리보기 드롭다운.
- **세션은 채팅 오픈 단위** — 채팅을 열 때마다 새 thread_id 발급 → 같은 오버레이 안에서는 follow-up이 메모리를 공유하지만, 닫고 다시 열면 깨끗한 상태로 시작한다.
- **중복 출력 제거** — 서버는 각 라운드 토큰을 `run_id`별로 버퍼링하고 새 라운드마다 이전 버퍼를 폐기해 **tool_calls가 없는 마지막 라운드**만 클라이언트로 flush한다.
- **링크는 새 탭** — `marked.parse` 결과 모든 `<a>` 태그에 `target="_blank" rel="noopener noreferrer"` 자동 주입.

상세 아키텍처 설계는 [`docs/AGENT_DESIGN.md`](docs/AGENT_DESIGN.md)에 정리돼 있다.

---

## 데이터 소스

| Source | 파일 | 방식 | 로그인 |
|-------|------|------|--------|
| **BC Liquor Store** | `tools/bcliquor_tool.py` | JSON API | - |
| **Everything Wine** | `tools/everythingwine_tool.py` | HTML scraping + In-Store Pickup REST API | - |
| **Okanagan Cellars** | `tools/okanagan_cellars_tool.py` | JSON API | - |
| **Sutton Place Wine Merchant** | `tools/suttonplace_tool.py` | JSON API | - |
| **Marquis Wine Cellars** | `tools/marquis_tool.py` | JSON API | - |
| **Legacy Liquor Store** | `tools/legacy_tool.py` | GraphQL API | - |
| **Google Search grounding** | `tools/google_search_tool.py` | Gemini native grounding (Vertex AI) | - (ADC) |

---

## 각 Tool 상세

### 1. BC Liquor Store (`tools/bcliquor_tool.py`)

BC주 공식 주류 판매점. 와인, 맥주, 스피릿, 사이더 모두 취급.

- **데이터**: 이름, 가격 (세일 여부), 품종, 국가, 도수, 테이스팅 노트, 소비자 평점/투표수, 재고 매장 수, BC VQA 여부
- **특징**: 카테고리 필터 가능 (`wine`, `beer`, `spirits`)

```python
results = await search_bcliquor("tantalus", max_pages=2, category="wine")
```

### 2. Okanagan Cellars (`tools/okanagan_cellars_tool.py`)

밴쿠버에 2개 매장 (West 1st Ave, West 4th Ave) 있는 와인샵.

- **데이터**: 이름, 카테고리, 가격, 세일 여부, 재고 수량, 용량
- **쿼리 폴백**: AND 매칭 백엔드 → [`tools/query_fallback.py`](tools/query_fallback.py)로 재시도

```python
results = await search_okanagan_cellars("checkmate")
```

### 3. Sutton Place Wine Merchant (`tools/suttonplace_tool.py`)

밴쿠버 Yaletown (1168 Hamilton St)의 와인샵. Okanagan Cellars와 동일한 Barnet Network 플랫폼.

- **데이터**: 이름, 카테고리, 가격, 세일 여부, 재고 수량, 용량, 국가, 품종, 빈티지, 알코올 도수, 스태프 픽, 피처드
- **쿼리 폴백**: Barnet AND 매칭 → [`tools/query_fallback.py`](tools/query_fallback.py)로 재시도

```python
results = await search_suttonplace("pinot noir")
```

### 4. Marquis Wine Cellars (`tools/marquis_tool.py`)

밴쿠버의 큐레이션 와인 전문점. BigCommerce 기반.

- **데이터**: 이름, SKU, 가격 (정가/세일가), 재고 수준, 카테고리 계층
- **특징**: 페이지네이션 지원 (limit/skip)

```python
results, total = await search_marquis("martins lane", limit=20)
```

### 5. Legacy Liquor Store (`tools/legacy_tool.py`)

밴쿠버의 프리미엄 독립 와인샵. GraphQL API 기반.

- **데이터**: 이름, 브랜드, 가격 (정가/세일가), 세일 여부, 스태프 픽, 신상품, 국가, 지역, 태그, 재고 수량
- **특징**: 가격 범위 필터 (`price_min`/`price_max`), 스태프 픽 필터, 세일 필터
- **쿼리 폴백**: AND 매칭 → [`tools/query_fallback.py`](tools/query_fallback.py)로 재시도

```python
results, total = await search_legacy("pinot noir", limit=30, price_min=20, price_max=50, staff_pick=True)
```

### 6. Everything Wine (`tools/everythingwine_tool.py`)

밴쿠버 와인샵 (Magento 2 + Elasticsuite). 검색 결과는 HTML scraping, **매장별 픽업 재고는 공개 REST API**로 보강.

- **데이터**: 이름, SKU, 가격, 세일 여부, 국가, 창고/매장 재고 상태
- **매장별 재고**: In-Store Pickup REST API로 Lower Mainland 4개 매장 (Vancouver / North Vancouver / South Surrey / Langley) 매장별 정확 수량
- **쿼리 폴백**: Elasticsuite AND 매칭 → [`tools/query_fallback.py`](tools/query_fallback.py)로 재시도

```python
results = await search_everything_wine("synchromesh")
```

### 7. Google Search grounding (`tools/google_search_tool.py`)

Gemini의 native Google Search grounding을 이용한 지식/리뷰 검색. Vertex AI 인증 (ADC)만으로 동작하며 별도 API 키 불필요.

- **데이터**: grounded 답변 + source URL 리스트
- **용도**: 음료 교육, 산지/생산자 정보, 리뷰/점수 (인용 + 요약만, 전문 복제 금지), store tool로 안 나오는 정보 보충
- **저작권 가드레일**: caller prompt에서 리뷰/점수는 출처 귀속 + 요약만 허용, 전문 복제 금지

```python
results, answer = await search_web_grounded("best food pairings for BC Pinot Noir")
```

---

## 프로젝트 파일 구조

```
BC-wine-ai-agents/
├── agent.py                    # LangGraph Supervisor 그래프 (entry_router + vision + supervisor ↔ tools)
├── agent_tools.py              # @tool 래퍼 + specialist 그룹 (SOURCING / SOMMELIER / SUPERVISOR_DIRECT)
├── app.py                      # FastAPI 백엔드 (SSE 스트리밍, CORS, 멀티모달 입력, validation 게이트)
├── validation.py               # Pre-agent query 검증 (off-topic 쿼리 그래프 우회)
├── vision.py                   # 멀티모달 라벨/와인리스트/음식메뉴 추출 (VisionExtraction 스키마)
├── state.py                    # AgentState TypedDict (messages + tool_call_log + vision_extractions)
├── models.py                   # Gemini LLM 팩토리 (3.5 Flash + 3.1 Pro Preview)
├── prompts.py                  # Supervisor/specialist/페어링/relevance-filter/검증/vision 프롬프트
├── safety.py                   # tool_error_to_json (툴 예외 → status:error JSON, ToolNode 격리)
├── HYPERPARAMETERS.md          # 모든 튜닝 상수 (온도, 타임아웃, 한도)
├── requirements.txt            # Python 패키지 의존성
├── Dockerfile                  # 컨테이너 빌드 (python:3.12-slim, uvicorn, port 8080)
├── .dockerignore               # Docker 빌드 제외 목록
├── agents/                     # Specialist 에이전트 (독립 ReAct sub-graph)
│   ├── __init__.py             # 아키텍처 문서
│   ├── react_subagent.py       # 공유 ReAct sub-graph 빌더 + run_subagent_json 래퍼
│   ├── sourcing_agent.py       # Sourcing Agent — 6개 매장 병렬 검색
│   ├── sommelier_agent.py      # Sommelier Agent — 페어링 + grounding
│   └── menu_architect.py       # Menu Architect — B2B 음료 메뉴 설계 (A2A)
├── tools/                      # 데이터 수집 도구 모음
│   ├── __init__.py
│   ├── bcliquor_tool.py        # BC Liquor Store 검색
│   ├── okanagan_cellars_tool.py # Okanagan Cellars 검색
│   ├── suttonplace_tool.py     # Sutton Place Wine Merchant 검색
│   ├── marquis_tool.py         # Marquis Wine Cellars 검색
│   ├── legacy_tool.py          # Legacy Liquor Store 검색 (GraphQL)
│   ├── everythingwine_tool.py  # Everything Wine 검색
│   ├── google_search_tool.py   # Google Search grounding
│   └── query_fallback.py       # 공통 쿼리 폴백 (okanagan/everythingwine/legacy 공유)
├── frontend/                   # 프론트엔드 (vanilla HTML/CSS/JS, 빌드 스텝 없음)
│   ├── index.html              # 랜딩 페이지 + 풀스크린 채팅 오버레이
│   ├── styles.css              # 와인 컬러 팔레트, 채팅 + 툴 배지 + agent-box 스타일
│   ├── app.js                  # SSE 클라이언트, CORS API_BASE, 이미지 첨부, 툴 배지, 마크다운
│   └── _worker.js              # Cloudflare Workers 프록시 (API 라우팅 + 보안 필터)
├── scripts/                    # 유틸리티 스크립트
│   ├── debug_everythingwine.py # Everything Wine HTML 구조 확인용
│   └── test_gemini_models.py   # Gemini 모델 비교 테스트
├── draw_graph.py               # 아키텍처 Mermaid 다이어그램 생성기
├── tests/                      # Golden-query quality evaluation
│   ├── golden_queries.py       # 골든 쿼리 (여러 카테고리)
│   ├── metrics.py              # Deterministic metrics (orch, hallucination, coverage, structure)
│   ├── judge.py                # LLM-as-judge (Gemini 3.1 Pro Preview temp=0)
│   ├── quality_eval.py         # Runner — produces results.json + summary.md + transcripts
│   └── results/<timestamp>/    # Per-run outputs (gitignored)
├── docs/
│   ├── AGENT_DESIGN.md         # 전체 아키텍처 설계 문서 + iteration history
│   └── VISION_NODE_DESIGN.md   # vision 노드 설계 (as-built)
├── .env                        # API 키 (gitignored)
├── .gitignore
└── README.md
```

---

## Setup

### 설치

```bash
git clone https://github.com/SUM-AI-ca/BC-wine-ai-agents.git
cd BC-wine-ai-agents

python -m venv venv
source venv/bin/activate  # Mac/Linux
# venv\Scripts\activate   # Windows

pip install -r requirements.txt
```

### Google Cloud 인증 (Gemini API)

```bash
gcloud auth application-default login
```

### 환경변수

`.env` 파일 생성:

```
# LangSmith (optional — tracing & observability)
LANGSMITH_TRACING=true
LANGSMITH_API_KEY=lsv2_sk_...
LANGSMITH_PROJECT=bc-wine-agent
LANGSMITH_ENDPOINT=https://api.smith.langchain.com
```

### 각 tool 독립 테스트

```bash
python -m tools.bcliquor_tool
python -m tools.okanagan_cellars_tool
python -m tools.suttonplace_tool
python -m tools.marquis_tool
python -m tools.legacy_tool
python -m tools.everythingwine_tool
```

---

## 서버 실행

### 로컬 개발

```bash
python -m uvicorn app:app --port 8000
```

브라우저에서 `http://localhost:8000` 열면 채팅 UI가 뜬다.

### Docker (로컬)

```bash
docker build -t bc-wine-agent .
docker run -p 8080:8080 --env-file .env bc-wine-agent
```

### 프로덕션 배포

```bash
# Cloud Run 배포 (백엔드)
gcloud run deploy bc-wine-agent --source . --region us-west1 --project wine-agent-jh-2026 --allow-unauthenticated

# Cloudflare Pages 배포 (프론트엔드)
# Cloudflare Dashboard → Workers & Pages → bcwineaiagents 프로젝트
# GitHub 연동으로 main 브랜치 push 시 자동 배포
```

---

## Tech Stack

- **LangGraph** — 멀티 에이전트 Supervisor + 3 specialist sub-graph 오케스트레이션
- **Gemini 3.5 Flash** — Supervisor, Sourcing Agent, validation, vision 노드
- **Gemini 3.1 Pro Preview** — Sommelier Agent, Menu Architect (고급 추론)
- **Google Search grounding** — 리뷰/점수/사실 기반 지식 (Vertex AI native)
- **FastAPI** — SSE 스트리밍 백엔드
- **HTML/CSS/JS** — 와인 컬러 채팅 UI (vanilla, 빌드 스텝 없음)
- **Google Cloud Run** — 백엔드 컨테이너 호스팅
- **Cloudflare Pages** — 프론트엔드 정적 호스팅 + 커스텀 도메인
- **httpx** — async HTTP 클라이언트 (세션/쿠키 관리 포함)
- **BeautifulSoup4** — HTML 파싱 (Everything Wine)
- **Pydantic** — 데이터 모델 & 유효성 검사
- **LangSmith** — 트레이스/관측 (환경변수 설정 시 자동 활성화)
- **python-dotenv** — 환경변수 로딩
- **Docker** — 컨테이너 빌드 (python:3.12-slim)

---

## 공통 패턴

모든 tool은 같은 구조를 따름:

1. **`search_*(query)` 함수** — async, 구조화된 Pydantic 모델 리스트 반환
2. **`format_results()` 함수** — 사람이 읽기 좋은 텍스트 포맷. **독립 실행 테스트(`main()`) 전용** — 에이전트 경로에서는 `@tool` 래퍼가 `json.dumps(model_dump())`로 전체 필드를 직렬화해 반환하므로 호출되지 않는다.
3. **`main()` 함수** — `python -m tools.<name>`으로 독립 실행 가능한 테스트
4. **Pydantic 모델** — 각 사이트에 맞는 데이터 구조 정의

---

## 품질 평가 파이프라인

```bash
python -m tests.quality_eval                    # 전체 suite
python -m tests.quality_eval --only INV,CRI     # 카테고리 필터
python -m tests.quality_eval --id INV-001       # 단일 query
python -m tests.quality_eval --dry-run          # 빠른 sanity check (2 query)
python -m tests.quality_eval --skip-judge       # 결정론적 metric 만
```

결과는 `tests/results/<YYYYMMDD-HHMMSS>/` 에 `results.json`, `summary.md`, `transcripts/<id>.md` 형식으로 저장됨.
