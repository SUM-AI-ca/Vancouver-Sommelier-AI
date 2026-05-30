# BC Wine AI Agent

BC 와인을 검색하고 추천해주는 AI 에이전트. LangGraph 기반으로 여러 와인 사이트의 데이터를 통합해서 사용자 질문에 답변한다.

현재 단계: **LangGraph 에이전트 코어 구현 완료. FastAPI + SSE 스트리밍 + 와인 컬러 풀스크린 채팅 UI 동작 중. Pre-agent query validation gate 추가 (off-topic 쿼리는 그래프 우회). 멀티모달 vision 노드 추가 — 와인 라벨/레스토랑 와인리스트 사진을 스캔해 검색/추천으로 연결. Docker 컨테이너 배포 준비 완료. Golden-query + LLM-as-judge 품질 평가 파이프라인 가동 중.**

### Query Validation Gate

`/api/chat`이 그래프를 호출하기 **전에** 한 번의 Gemini Flash 분류 호출로 쿼리가 에이전트 범위(와인 / 페어링 / 인사) 안에 있는지 판정한다. Off-topic이면 (날씨, 스포츠, 코딩 질문 등) 그래프를 건너뛰고 **사용자 입력 언어 그대로** 짧은 거절 메시지를 SSE 토큰으로 흘려보낸다. 한국어 질문엔 한국어, 영어 질문엔 영어로 자동 응답. 검증 LLM이 실패하면 fail-open으로 기존 에이전트 경로로 그대로 진입 — 오케스트레이터의 Guideline G5 (off-topic 처리)가 백스톱 역할. 실측 오프토픽 응답 시간 ~2.6s (기존 ~10s+).

구현: [`validation.py`](validation.py) (Pydantic `ValidationResult` + `validate_query()`), [`prompts.py`](prompts.py)의 `VALIDATION_SYSTEM_PROMPT`, [`app.py`](app.py) 게이트 삽입.

### Human-in-the-Loop Clarification

기존엔 쿼리/툴 결과가 모호해도 오케스트레이터가 **암묵적으로** best-match를 잡고 진행했다. 이제 LangGraph의 `interrupt()` primitive를 이용해 오케스트레이터가 **명시적으로** 유저에게 되묻을 수 있다.

흐름: 오케스트레이터가 `ask_user_clarification_tool(question, options?)`을 호출 → tool 내부에서 `interrupt({...})` 발생 → 그래프가 같은 thread의 checkpoint에 멈춤 → `app.py`가 SSE `clarification_request` 이벤트로 question + options를 프론트에 전송 → 프론트가 옵션 chip + hint UI 렌더링 → 유저가 옵션 클릭 or 자유 입력 → 다음 `/api/chat` 호출 진입 시 `aget_state(config)`로 pending interrupt 감지 → `Command(resume=req.message)`로 그래프 재개 → tool은 유저 응답을 string으로 받고 정상 종료 → 다음 orchestrator round 진행.

규칙(`prompts.py` Guideline G6):
- **묻는다**: 2+ 해석 가능한 모호 쿼리("좋은 와인 추천해줘"), 비슷한 점수의 매칭이 다수일 때 (preference로 tie-break), 필수 정보 누락 (페어링인데 음식 없음, "the second one"인데 prior context 없음).
- **묻지 않는다**: user_preferences로 답이 나오는 경우, "약 5개 와인 추천" 같은 default가 자연스러운 경우, 정보성/교육성 질문.
- **횟수 제한**: 한 turn에 최대 3회 (`MAX_CLARIFICATIONS_PER_TURN`). cap 도달 시 system prompt에 안내가 append되어 강제로 best-effort 답변.
- **Round counting**: clarification-only round는 `MAX_TOOL_ROUNDS` 카운트에서 제외 — 데이터 수집 round와 분리.
- **Validation skip on resume**: clarification 응답("$50 under" 같은 짧은 텍스트)이 validator를 트립하지 않도록 resume 분기에선 validation 게이트를 건너뜀.

구현: [`agent.py`](agent.py)의 `ask_user_clarification_tool` + `_count_clarifications_this_turn`, [`prompts.py`](prompts.py) Guideline G6, [`app.py`](app.py)의 interrupt 감지 + `Command(resume=...)` 분기, [`frontend/app.js`](frontend/app.js)의 `renderClarification()`, [`frontend/styles.css`](frontend/styles.css)의 `.clarification*` 클래스.

### Vision — 멀티모달 라벨/와인리스트 스캔

사용자가 **와인 라벨 사진**이나 **레스토랑 와인 리스트 사진**을 첨부하면, 오케스트레이터 앞단의 전용 `vision_node`가 먼저 돌아 사진 속 텍스트를 구조화 추출한 뒤 기존 검색/추천 흐름으로 넘긴다. 모델은 그대로 Gemini 3.5 Flash (이미 멀티모달이라 모델 교체 없음).

흐름: 프론트가 사진을 긴 변 ≤2048px JPEG로 다운스케일/재인코딩해 base64로 전송 → `app.py`가 텍스트+이미지 멀티모달 `HumanMessage` 구성 (이미지 첨부 시 validation 게이트 우회) → `entry_router`가 이미지 유무로 분기 → `vision_node`가 `with_structured_output(VisionExtraction)`으로 **보이는 텍스트만** 추출 (환각 방지: 안 보이면 null, 정규화/번역 금지) → 추출 결과를 **같은 id로 `HumanMessage` 교체**해 이미지를 버리고 텍스트로 fold (현재/미래 턴 토큰 절약) → orchestrator는 text-only로 동작.

- **라벨**: producer/cuvee/품종/vintage/region 등 1종 추출 → 기존 store/critic 툴로 가격/재고/평점 조회.
- **와인 리스트**: 줄별 verbatim `raw_text` + 파싱 필드로 N종 추출 → 리스트의 와인을 전부 조회/비교 (가성비/평점/페어링), tool budget 한도 내.
- **무손실**: named field에 안 맞는 텍스트는 catch-all(`other_text`/`raw_text`)에 보존. 비와인 사진은 `document_type="other"`로 정중히 거절.
- **UI**: 첨부 버튼 + 드래그드롭 + 클립보드 붙여넣기, 썸네일 미리보기(최대 2장), `vision_start`/`vision_result` SSE로 "Image analysis" 배지 표시.

구현: [`vision.py`](vision.py) (스키마 + `extract_vision` + `format_extraction`), [`prompts.py`](prompts.py)의 `VISION_EXTRACTION_PROMPT` + 오케스트레이터 Guideline G7, [`agent.py`](agent.py)의 `vision_node` + `entry_router`, [`app.py`](app.py)의 멀티모달 입력 + vision SSE, [`frontend/`](frontend/)의 이미지 첨부 UI. 설계 문서는 [`docs/VISION_NODE_DESIGN.md`](docs/VISION_NODE_DESIGN.md).

### Tool 견고성 — 에러 격리 + 쿼리 폴백

**툴 에러 격리.** 예전엔 한 툴이 런타임 에러(네트워크/인증/파싱)를 던지면 그래프 밖으로 전파돼 **턴 전체가 멈췄다** (LangGraph 기본 핸들러는 인자 검증 오류만 잡고 나머지는 re-raise). 이제 `ToolNode(TOOLS, handle_tool_errors=tool_error_to_json)`로 **모든 예외를 `status:"error"` JSON 결과로 격리** — 실패한 툴은 에러로 표시되고 나머지 툴 결과로 답변을 이어간다 (orchestrator Guideline G8). clarification의 `interrupt`(GraphInterrupt)는 핸들러보다 먼저 re-raise되어 영향 없음. 프론트 드롭다운에도 "Tool error"로 노출.

**쿼리 폴백.** 일부 store 백엔드(Okanagan Cellars, Everything Wine, Legacy, Liberty)는 쿼리의 **모든 토큰을 상품명에 AND 매칭**한다. 그래서 라벨/vision에서 뽑은 풀 문자열("Mission Hill Perpetua 2022 Chardonnay")은 상품명(`MISSION HILL - PERPETUA 2022`)에 "Chardonnay"가 없어 **0건**이 났다. 공통 헬퍼 [`tools/query_fallback.py`](tools/query_fallback.py)가 0건이면 **품종/연도를 떼고 → 뒤 토큰을 점진적으로(최소 3토큰) 줄여** 재시도해 첫 비어있지 않은 결과를 반환한다. (bcliquor는 검색이 관대해 불필요, marquis는 반대로 over-match라 별개 과제.)

구현: [`safety.py`](safety.py)의 `tool_error_to_json` + [`agent.py`](agent.py) ToolNode 연결 + [`prompts.py`](prompts.py) G8, [`tools/query_fallback.py`](tools/query_fallback.py)의 `search_with_fallback` (okanagan/everythingwine/legacy/liberty 공유).

### UI/UX

- **랜딩 + 풀스크린 채팅 오버레이** — 간단한 capability 설명이 있는 랜딩 페이지에서 "Start chatting" 버튼을 누르면 화면을 가득 채우는 채팅 오버레이가 뜬다.
- **연한 와인 컬러 팔레트** — 기존 SUM AI 파란색에서 데사추레이트된 burgundy(`#7A3D4F`) 톤으로 교체.
- **상태 인디케이터** — 채팅 헤더 좌상단에 텍스트 없이 **심볼만** 표시한다. 대기 중에는 고정된 점, 작동 중에는 회전 링 스피너로 전환된다 (내부적으로 `Ready`/`Processing`/`Running <tool>`/`Writing response`/`Task finished` 상태의 working 플래그로 토글). 상태 텍스트는 `font-size:0`으로 시각적으로만 숨기고 DOM에는 남겨 `aria-live`로 스크린리더에 그대로 전달된다.
- **툴 배지** — 각 tool 호출이 expandable 배지로 렌더링됨. 완료되면 결과 개수 표시 + 클릭으로 결과 미리보기 드롭다운. Sommelier reasoning / Tavily 처럼 긴 본문은 마크다운으로 렌더링.
- **세션은 채팅 오픈 단위** — `thread_id`를 `localStorage`에 저장하지 않음. 채팅을 열 때마다 새 thread_id 발급 → 같은 오버레이 안에서는 follow-up이 메모리를 공유하지만, 닫고 다시 열면 깨끗한 상태로 시작한다.
- **중복 출력 제거** — synthesis 패스는 제거됨 (오케스트레이터 출력이 곧 최종 답변). 한 turn에 오케스트레이터가 여러 라운드를 돌 수 있어, 서버는 각 라운드 토큰을 `run_id`별로 버퍼링하고 새 라운드마다 이전 버퍼를 폐기해 **tool_calls가 없는 마지막 라운드**만 클라이언트로 flush한다.
- **링크는 새 탭** — `marked.parse` 결과 모든 `<a>` 태그에 `target="_blank" rel="noopener noreferrer"` 자동 주입.

상세 아키텍처 설계는 [`docs/AGENT_DESIGN.md`](docs/AGENT_DESIGN.md)에 다 정리해놨다.

---

## 전체 구조

```
사용자 질문 (+ 와인 라벨/리스트 사진 첨부 가능)
    ↓
HTML/CSS/JS 프론트엔드 (frontend/ — 와인 컬러 채팅 모달, 이미지 첨부)
    ↓
FastAPI 백엔드 (app.py — SSE 스트리밍)
    ↓
Validation Gate (validation.py — Gemini Flash 분류)   ※ 이미지 첨부 시 우회
    │
    ├─ INVALID → 사용자 언어로 거절 → 그래프 우회 → 종료
    │
    └─ VALID ↓
LangGraph Agent (agent.py — Gemini 3.5 Flash, 13개 tool)
    │
    │   entry_router ─(이미지)─→ vision_node ─┐
    │                └─(텍스트)──────────────┴→ orchestrator
    │   orchestrator → tools → orchestrator (loop)   ※ 툴 에러는 격리되어 계속 진행
    │                     ↓ (ask_user_clarification_tool)
    │                  interrupt() → SSE clarification_request → 유저 응답
    │                     ↓ Command(resume=...) → 다음 orchestrator round
    │                                                       ↓ (no tool_calls)
    │   orchestrator 최종 답변 → END  (별도 synthesis 노드 없음)
    ↓
┌──────────────────────────────────────────────────────────┐
│  Tools (데이터 수집 — 모두 완성)                           │
│                                                          │
│  winealign_tool.py ──── 전문가 리뷰 & 점수                │
│  bcliquor_tool.py ───── 가격 & 재고 (공식 주류 판매)       │
│  okanagan_cellars_tool.py ── 밴쿠버 와인샵 재고            │
│  marquis_tool.py ────── 밴쿠버 큐레이션 와인샵             │
│  legacy_tool.py ─────── 밴쿠버 프리미엄 와인샵             │
│  liberty_tool.py ────── 밴쿠버 대형 독립 와인샵            │
│  everythingwine_tool.py ── 밴쿠버 와인샵 재고 + 매장별 수량 │
│  gismondi_tool.py ───── BC/캐나다 와인 평론 (로컬 DB)      │
│  robert_parker_tool.py ── Robert Parker 평점/리뷰          │
│  tavily_tool.py ─────── 웹 검색 fallback                  │
└──────────────────────────────────────────────────────────┘
```

---

## 데이터 소스 & 수집 방식

| Source | 파일 | 방식 | 로그인 |
|-------|------|------|--------|
| **Gismondi on Wine** | `tools/gismondi_tool.py` + `data/wines.db` | 별도 submodule CSV → SQLite (FTS5) | - |
| **WineAlign** | `tools/winealign_tool.py` | HTML scraping + login session | 필요 |
| **Robert Parker** | `tools/robert_parker_tool.py` | Algolia REST API + auto-login | 필요 (구독) |
| **BC Liquor Store** | `tools/bcliquor_tool.py` | JSON API (`/ajax/browse`) | - |
| **Okanagan Cellars** | `tools/okanagan_cellars_tool.py` | JSON API (`/api/shop/.../products`) | - |
| **Everything Wine** | `tools/everythingwine_tool.py` | HTML scraping + In-Store Pickup REST API (매장별 재고) | - |
| **Marquis Wine Cellars** | `tools/marquis_tool.py` | JSON API (BigCommerce Discovery) | - |
| **Legacy Liquor Store** | `tools/legacy_tool.py` | GraphQL API (Apollo Server) | - |
| **Liberty Wine Merchants** | `tools/liberty_tool.py` | WooCommerce Store REST API | - |
| **Tavily 웹 검색** | `tools/tavily_tool.py` | REST API (paid) | 필요 |

---

## 각 Tool 상세

### 1. WineAlign (`tools/winealign_tool.py`)

캐나다 최대 와인 리뷰 플랫폼. **월 구독료를 내야** 전문가 리뷰를 볼 수 있다. 검색 가능한 JSON API를 따로 못 찾아서, 구독하고 내 계정으로 로그인한 뒤 웹페이지를 파싱하는 방식으로 만들었다.

- **인증**: `authenticity_token` + `person_credentials` 쿠키 기반 세션
- **자동 재로그인**: 세션 만료되면 `/login` 리다이렉트 감지해서 자동으로 다시 로그인
- **데이터**: 와인 이름, appellation, 점수, 가격, 전문가별 리뷰 (점수, 테이스팅 노트, value rating, drink window)
- **속도**: 와인별 리뷰 detail 페이지를 동시(병렬, 최대 `REVIEW_CONCURRENCY`=10개)로 가져온다

```python
results = await search_winealign("pinot noir", max_pages=3, include_reviews=True)
```

### 2. BC Liquor Store (`tools/bcliquor_tool.py`)

BC주 공식 주류 판매점. Elasticsearch 기반 JSON API가 있어서 깔끔하게 데이터를 가져올 수 있었다.

- **API**: `GET /ajax/browse?search=...&sort=_score:desc&size=24&page=1`
- **데이터**: 이름, 가격 (세일 여부), 품종, 국가, 도수, 테이스팅 노트, 소비자 평점/투표수, 재고 매장 수, BC VQA 여부
- **특징**: 카테고리 필터 가능 (`wine`, `beer`, `spirits`)

```python
results = await search_bcliquor("tantalus", max_pages=2, category="wine")
```

### 3. Okanagan Cellars (`tools/okanagan_cellars_tool.py`)

밴쿠버에 2개 매장 (West 1st Ave, West 4th Ave) 있는 와인샵. JSON API가 열려 있어서 바로 사용.

- **API**: `GET /api/shop/131-41/products?q=...&show_on_web=true`
- **데이터**: 이름, 카테고리, 가격, 세일 여부, 재고 수량, 용량 (750ml, 1.5L 등)
- **쿼리 폴백**: 백엔드가 모든 토큰을 AND 매칭 → 라벨 풀 쿼리가 0건 나면 [`tools/query_fallback.py`](tools/query_fallback.py)가 품종/연도를 떼고 재시도

```python
results = await search_okanagan_cellars("checkmate")
```

### 4. Marquis Wine Cellars (`tools/marquis_tool.py`)

밴쿠버의 큐레이션 와인 전문점. BigCommerce 기반이라 Discovery API가 public으로 열려 있다.

- **API**: `GET https://discovery.marquis-wines.com/apis/ecommerce-service/public/discovery/v2/search`
- **데이터**: 이름, SKU, 가격 (정가/세일가), 재고 수준, 카테고리 계층 (예: White Wine > Chardonnay > BC > Okanagan)
- **특징**: 이미지 URL이 JSON string으로 들어오는데 한 번 더 파싱해야 함. 페이지네이션 지원 (limit/skip)

```python
results, total = await search_marquis("martins lane", limit=20)
```

### 5. Legacy Liquor Store (`tools/legacy_tool.py`)

밴쿠버의 프리미엄 독립 와인샵. GraphQL API (Apollo Server on Google Cloud Run)가 열려 있어서 바로 사용.

- **API**: `POST https://production-retail-store-api-hagnfhf3sq-uc.a.run.app/graphql` (storeId: `"LL"`)
- **데이터**: 이름, 브랜드, 가격 (정가/세일가), 세일 여부, 스태프 픽, 신상품, 국가, 지역, 태그, 재고 수량
- **특징**: 가격 범위 필터 (`price_min`/`price_max`), 스태프 픽 필터, 세일 필터
- **쿼리 폴백**: AND 매칭이라 라벨 풀 쿼리가 0건이면 [`tools/query_fallback.py`](tools/query_fallback.py)로 재시도. Legacy는 아포스트로피를 보존해야 해서("Martin's Lane") 자체 cleaner를 폴백에 주입

```python
results, total = await search_legacy("pinot noir", limit=30, price_min=20, price_max=50, staff_pick=True)
```

### 6. Liberty Wine Merchants (`tools/liberty_tool.py`)

밴쿠버의 대형 독립 와인 소매점. WooCommerce Store REST API가 public으로 열려 있어서 인증 없이 바로 사용.

- **API**: `GET https://www.libertywinemerchants.com/wp-json/wc/store/products?search=...`
- **데이터**: 이름, SKU, 가격 (정가/세일가), 세일 여부, 재고 여부/수량, 카테고리, 태그 (Liberty Exclusive, Value Picks, Best of BC, Staff Picks), producer, country, region, grape, vintage
- **특징**: 와인별 상세 attribute (producer, grape, region, vintage)를 API가 바로 반환. 태그 기반 큐레이션 정보가 풍부함
- **쿼리 폴백**: AND 매칭이라 [`tools/query_fallback.py`](tools/query_fallback.py)로 재시도. 아포스트로피 보존 필요 ("Martin's Lane")

```python
results, total = await search_liberty("pinot noir", limit=20)
```

### 7. Everything Wine (`tools/everythingwine_tool.py`)

밴쿠버 와인샵 (Magento 2 + Elasticsuite). 검색 결과는 HTML scraping, **매장별 픽업 재고는 공개 REST API**로 보강한다.

- **방식**: `GET /catalogsearch/result/?q=...` → BeautifulSoup으로 파싱
- **데이터**: 이름, SKU, 가격, 세일 여부, 국가, 창고/매장 재고 상태
- **매장별 재고**: Magento **In-Store Pickup REST API** (`GET /rest/V1/inventory/in-store-pickup/pickup-locations`)는 무인증 공개라 SKU로 **매장별 정확 수량**을 준다. SKU는 검색결과 이미지 파일명에서 추출. Lower Mainland 4개 매장(Vancouver / North Vancouver / South Surrey / Langley)만 필터링
- **쿼리 폴백**: Elasticsuite AND 매칭 → 라벨 풀 쿼리가 0건이면 [`tools/query_fallback.py`](tools/query_fallback.py)로 재시도

```python
results = await search_everything_wine("synchromesh")
results = await search_everything_wine("synchromesh", with_store_stock=False)
```

### 8. Gismondi on Wine (`tools/gismondi_tool.py` + `data/wines.db`)

캐나다 와인 평론가 Anthony Gismondi의 리뷰 데이터. 원본 CSV는 별도 submodule (`gismondi-canada-wines/`)에서 관리되고, 거기 GitHub Actions이 자동 스크래핑한다. SQLite + FTS5로 풀텍스트 검색.

- **데이터**: 와인 이름, /100 점수, /20 점수, region, tasting notes, taster, 가격, producer, grape, distributor, url 등 — 현재 13,539건
- **FTS5 인덱스 필드**: title, region, tasting_notes, grape, producer
- **필터**: `score_min`, `price_max`, `bc_only` (기본 True)
- **빌드**: `python scripts/build_db.py` (CSV → `data/wines.db`)
- **자동 업데이트**: `.github/workflows/update_db.yml`이 Wed/Sat 02:00 UTC에 submodule pull → DB 재빌드 → 변경분 커밋
- **async 처리**: SQLite는 blocking이라 `asyncio.to_thread()`로 감싸서 이벤트 루프 안 막게 함

```python
results = await search_gismondi("pinot noir", score_min=90, price_max=50, bc_only=True)
```

### 9. Robert Parker (`tools/robert_parker_tool.py`)

세계에서 가장 영향력 있는 와인 평가 시스템. Robert Parker Wine Advocate의 100점 만점 평점, 전문 테이스팅 노트, 음용 기간(drink window) 등을 Algolia 기반 REST API로 검색한다.

- **인증**: CSRF 토큰 + 이메일/비밀번호 자동 로그인. 401 에러 시 자동 재로그인.
- **검색**: Algolia `filters` 문법으로 rating, country, region, color, variety 필터링 가능. `hits_per_page`는 호출당 **최대 20**으로 하드캡.
- **데이터**: 와인 이름, producer, vintage, RP 점수 (100점), varieties, region/sub_region/appellation, 가격 범위, drink window, 리뷰어별 테이스팅 노트

```python
results = await search_robert_parker("pinot noir", country="Canada", region="British Columbia", rating_min=90, hits_per_page=5)
```

### 10. Tavily 웹 검색 (`tools/tavily_tool.py`)

기존 와인 매장/리뷰 툴로 답이 안 나오는 질문 처리용 폴백. Tavily API를 그대로 호출하고, `include_answer=True`로 AI 요약까지 같이 받는다. SDK 안 깔고 REST API 직접 호출.

- **인증**: `.env`의 `TAVILY_API_KEY` 필요
- **데이터**: title, url, content snippet, relevance score, published_date, AI-generated summary
- **주의**: 호출당 과금

```python
results, answer = await search_tavily("best food pairings for BC Pinot Noir")
```

---

## 프로젝트 파일 구조

```
BC-wine-ai-agents/
├── agent.py                    # LangGraph 그래프 빌더 (entry_router + vision + ReAct 13 tools)
├── app.py                      # FastAPI 백엔드 (SSE 스트리밍, 멀티모달 입력, validation 게이트)
├── validation.py               # Pre-agent query 검증 (off-topic 쿼리 그래프 우회)
├── vision.py                   # 멀티모달 라벨/와인리스트 추출 (VisionExtraction 스키마)
├── state.py                    # AgentState TypedDict (messages + tool_call_log + vision_extractions)
├── models.py                   # Gemini 3.5 Flash LLM 팩토리
├── prompts.py                  # 오케스트레이터/페어링/relevance-filter/검증/vision 시스템 프롬프트
├── safety.py                   # tool_error_to_json (툴 예외 → status:error JSON, ToolNode 격리)
├── requirements.txt            # Python 패키지 의존성
├── Dockerfile                  # 컨테이너 빌드 (python:3.12-slim, uvicorn)
├── .dockerignore               # Docker 빌드 제외 목록
├── tools/                      # 데이터 수집 도구 모음
│   ├── winealign_tool.py       # WineAlign 검색
│   ├── bcliquor_tool.py        # BC Liquor Store 검색
│   ├── okanagan_cellars_tool.py # Okanagan Cellars 검색
│   ├── marquis_tool.py         # Marquis Wine Cellars 검색
│   ├── legacy_tool.py          # Legacy Liquor Store 검색 (GraphQL)
│   ├── liberty_tool.py         # Liberty Wine Merchants 검색 (WooCommerce)
│   ├── everythingwine_tool.py  # Everything Wine 검색
│   ├── robert_parker_tool.py   # Robert Parker 평점/리뷰 (Algolia API)
│   ├── gismondi_tool.py        # Gismondi DB 검색 (SQLite + FTS5)
│   ├── tavily_tool.py          # Tavily 웹 검색 fallback
│   └── query_fallback.py       # 공통 쿼리 폴백 (okanagan/everythingwine/legacy/liberty 공유)
├── frontend/                   # 프론트엔드 (vanilla HTML/CSS/JS, 빌드 스텝 없음)
│   ├── index.html              # 랜딩 페이지 + 풀스크린 채팅 오버레이
│   ├── styles.css              # 와인 컬러 팔레트, 채팅 + 툴 배지 스타일
│   ├── app.js                  # SSE 클라이언트, 이미지 첨부/다운스케일, 툴 배지, 마크다운 렌더링
│   └── _redirects              # Netlify 리버스 프록시 (API → Cloud Run)
├── scripts/                    # 유틸리티 스크립트
│   ├── build_db.py             # CSV → SQLite 빌드 스크립트
│   ├── debug_everythingwine.py # Everything Wine HTML 구조 확인용
│   └── test_gemini_models.py   # Gemini 모델 비교 테스트
├── data/
│   ├── wines.db                # Gismondi 리뷰 SQLite (~13,539 rows, FTS5)
│   └── checkpoints.db          # LangGraph 체크포인터 (gitignored)
├── gismondi-canada-wines/      # 원본 CSV (git submodule)
├── tests/                      # Golden-query quality evaluation
│   ├── golden_queries.py       # 38 queries across 13 categories
│   ├── metrics.py              # Deterministic metrics (orch, hallucination, coverage, structure)
│   ├── judge.py                # LLM-as-judge (Gemini Flash temp=0)
│   ├── quality_eval.py         # Runner — produces results.json + summary.md + transcripts
│   └── results/<timestamp>/    # Per-run outputs (gitignored)
├── docs/
│   ├── AGENT_DESIGN.md         # 전체 아키텍처 설계 문서 + iteration history
│   └── VISION_NODE_DESIGN.md   # vision 노드 설계 (as-built)
├── .github/workflows/
│   └── update_db.yml           # DB 자동 업데이트 (Wed/Sat)
├── .env                        # API 키 (gitignored)
├── .gitignore
├── .gitmodules
└── README.md
```

---

## Setup

### 설치

```bash
git clone --recurse-submodules https://github.com/SUM-AI-ca/BC-wine-ai-agents.git
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
WINEALIGN_EMAIL=your_email@example.com
WINEALIGN_PASSWORD=your_password
TAVILY_API_KEY=tvly-...

# Robert Parker (subscription required — auto-login)
ROBERT_PARKER_EMAIL=your_email@example.com
ROBERT_PARKER_PASSWORD=your_password
ROBERT_PARKER_API_KEY=...

# LangSmith (optional — tracing & observability)
LANGSMITH_TRACING=true
LANGSMITH_API_KEY=lsv2_sk_...
LANGSMITH_PROJECT=bc-wine-agent
LANGSMITH_ENDPOINT=https://api.smith.langchain.com
```

### Gismondi DB 빌드 (최초 1회)

GitHub Actions이 자동으로 업데이트해주지만, 처음 clone하면 직접 빌드해야 한다:

```bash
python scripts/build_db.py
```

### 각 tool 독립 테스트

```bash
python -m tools.winealign_tool
python -m tools.bcliquor_tool
python -m tools.okanagan_cellars_tool
python -m tools.marquis_tool
python -m tools.legacy_tool
python -m tools.liberty_tool
python -m tools.everythingwine_tool
python -m tools.tavily_tool
python -m tools.robert_parker_tool
python -m tools.gismondi_tool
```

---

## 서버 실행

```bash
python -m uvicorn app:app --port 8000
```

브라우저에서 `http://localhost:8000` 열면 채팅 UI가 뜬다.

### Docker

```bash
docker build -t bc-wine-agent .
docker run -p 8080:8080 --env-file .env bc-wine-agent
```

---

## Tech Stack

- **LangGraph** — ReAct 에이전트 오케스트레이션 (13개 tool, 병렬 실행)
- **Gemini 3.5 Flash (langchain-google-genai)** — 모든 노드에서 사용하는 LLM (멀티모달 — vision 노드에서 라벨/와인리스트 이미지 분석)
- **FastAPI** — SSE 스트리밍 백엔드
- **HTML/CSS/JS** — SUM AI 디자인 계승 채팅 UI (vanilla, 빌드 스텝 없음)
- **httpx** — async HTTP 클라이언트 (세션/쿠키 관리 포함)
- **BeautifulSoup4** — HTML 파싱 (WineAlign, Everything Wine)
- **Pydantic** — 데이터 모델 & 유효성 검사
- **SQLite + FTS5** — Gismondi 리뷰 로컬 DB (Python 표준 라이브러리)
- **LangSmith** — 트레이스/관측 (환경변수 설정 시 자동 활성화)
- **python-dotenv** — 환경변수 로딩

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
python -m tests.quality_eval                    # 전체 38 query (~40-50 min)
python -m tests.quality_eval --only INV,CRI     # 카테고리 필터
python -m tests.quality_eval --id INV-001       # 단일 query
python -m tests.quality_eval --dry-run          # 빠른 sanity check (2 query)
python -m tests.quality_eval --skip-judge       # 결정론적 metric 만
```

결과는 `tests/results/<YYYYMMDD-HHMMSS>/` 에 `results.json`, `summary.md`, `transcripts/<id>.md` 형식으로 저장됨.
