# BC Wine AI Agents

BC 와인을 검색하고 추천해주는 AI 에이전트. LangGraph 기반으로 여러 와인 사이트의 데이터를 통합해서 사용자 질문에 답변하는 게 최종 목표.

현재 단계: **LangGraph 에이전트 코어 구현 완료. FastAPI + SSE 스트리밍 + 와인 컬러 풀스크린 채팅 UI 동작 중. Pre-agent query validation gate 추가 (off-topic 쿼리는 그래프 우회). Tool result compaction node 추가 (라운드 사이 context bloat 해결). Golden-query + LLM-as-judge 품질 평가 파이프라인 가동 중 (8회 iteration, 현재 Tool orchestration 100% / Hallucination 8.9% / Judge overall 3.4–3.9).**

### Tool Result Compaction Node (신규)

ReAct loop이 `tools → orchestrator`로 돌아갈 때, 각 라운드의 raw tool JSON (store당 24+ rows × 20+ fields)이 그대로 `state["messages"]`에 쌓이면서 다음 라운드 오케스트레이터가 그걸 전부 다시 attend함. 이걸 해결하려고 `tools`와 `orchestrator` 사이에 결정론적(LLM 없음) compaction 노드를 끼움.

각 batch에 대해:
1. Raw 결과를 **즉시** `wine_context`에 incremental merge — synthesis가 쓸 facts를 loop 내부에서 미리 채움.
2. 각 compactable ToolMessage를 **같은 id로** 작은 projection (`top_results`: top-5, key field만)으로 교체 → langgraph `add_messages` reducer가 in-place replace. 다음 라운드 orchestrator context가 ~10× 감소.
3. `results: []`을 compact payload에 박아둬서 최종 `merge_results_node`의 재호출은 자동 no-op.
4. Tavily / reasoning_pair_wine / update_preferences는 pass-through (synthesis aux collector, prefs harvest에서 raw가 필요).

구현: [`compaction.py`](compaction.py) (`compact_tool_results_node` + projection 헬퍼), [`agent.py`](agent.py)에 노드 + 엣지 추가. 그래프 흐름은 이제 `orchestrator → tools → compact_tool_results → orchestrator (loop)`.

### Query Validation Gate (신규)

`/api/chat`이 그래프를 호출하기 **전에** 한 번의 Gemini Flash 분류 호출로 쿼리가 에이전트 범위(와인 / 페어링 / 인사) 안에 있는지 판정한다. Off-topic이면 (날씨, 스포츠, 코딩 질문 등) 그래프를 건너뛰고 **사용자 입력 언어 그대로** 짧은 거절 메시지를 SSE 토큰으로 흘려보낸다. 한국어 질문엔 한국어, 영어 질문엔 영어로 자동 응답. 검증 LLM이 실패하면 fail-open으로 기존 에이전트 경로로 그대로 진입 — 오케스트레이터의 Rule 13이 백스톱 역할. 실측 오프토픽 응답 시간 ~2.6s (기존 ~10s+).

구현: [`validation.py`](validation.py) (Pydantic `ValidationResult` + `validate_query()`), [`prompts.py`](prompts.py)의 `VALIDATION_SYSTEM_PROMPT`, [`app.py:154`](app.py) 게이트 삽입.

### 최근 UI/UX 개편

- **랜딩 + 풀스크린 채팅 오버레이** — 간단한 capability 설명이 있는 랜딩 페이지에서 "Start chatting" 버튼을 누르면 화면을 가득 채우는 채팅 오버레이가 뜬다.
- **연한 와인 컬러 팔레트** — 기존 SUM AI 파란색에서 데사추레이트된 burgundy(`#7A3D4F`) 톤으로 교체. 이모지/장식용 유니코드 심볼은 모두 제거.
- **상태 인디케이터** — 채팅 헤더가 `Ready` → `Processing` → `Running <tool>` → `Writing response` → `Task finished` 순으로 실시간 상태를 보여준다. 작동 중 점 세 개 애니메이션은 제거.
- **툴 배지** — 각 tool 호출이 expandable 배지로 렌더링됨. 완료되면 결과 개수 표시 + 클릭으로 결과 미리보기 드롭다운. Sommelier reasoning / Tavily 처럼 긴 본문은 마크다운으로 렌더링.
- **세션은 채팅 오픈 단위** — `thread_id`를 `localStorage`에 저장하지 않음. 채팅을 열 때마다 새 thread_id 발급 → 같은 오버레이 안에서는 follow-up이 메모리를 공유하지만, 닫고 다시 열면 깨끗한 상태로 시작한다. (이전: 영구 persisted thread → `wine_context`가 무한 누적되며 무관한 와인이 새 대화에 누출됨)
- **중복 출력 제거** — 오케스트레이터 draft tokens은 서버에서 버퍼링되고 `format_response`의 synthesis만 클라이언트로 스트리밍됨. Off-topic 쿼리(synthesis 스킵)에서는 마지막 orchestrator 응답이 fallback으로 release.
- **링크는 새 탭** — `marked.parse` 결과 모든 `<a>` 태그에 `target="_blank" rel="noopener noreferrer"` 자동 주입.

상세 아키텍처 설계는 [`docs/AGENT_DESIGN.md`](docs/AGENT_DESIGN.md)에 다 정리해놨다.

---

## 전체 구조

```
사용자 질문
    ↓
HTML/CSS/JS 프론트엔드 (static/ — SUMAI 디자인 채팅 모달)
    ↓
FastAPI 백엔드 (app.py — SSE 스트리밍)
    ↓
Validation Gate (validation.py — Gemini Flash 분류)
    │
    ├─ INVALID → 사용자 언어로 거절 → 그래프 우회 → 종료
    │
    └─ VALID ↓
LangGraph Agent (agent.py — Gemini 3.5 Flash, 10개 tool)
    │
    │   orchestrator → tools → compact_tool_results → orchestrator (loop)
    │                                                       ↓ (no tool_calls)
    │   merge_results → format_response → END
    ↓
┌─────────────────────────────────────────────────────┐
│  Tools (데이터 수집 — 모두 완성)                       │
│                                                       │
│  winealign_tool.py ──── 전문가 리뷰 & 점수            │
│  bcliquor_tool.py ───── 가격 & 재고 (공식 주류 판매)   │
│  okanagan_cellars_tool.py ── 밴쿠버 와인샵 재고       │
│  marquis_tool.py ────── 밴쿠버 큐레이션 와인샵        │
│  everythingwine_tool.py ── 밴쿠버 와인샵 재고         │
│  gismondi_tool.py ───── BC/캐나다 와인 평론 (로컬 DB)  │
│  robert_parker_tool.py ── Robert Parker 평점/리뷰     │
│  tavily_tool.py ─────── 웹 검색 fallback              │
└───────────────────────────────────────────────────────┘
```

---

## 데이터 소스 & 수집 방식

| Source | 파일 | 방식 | 로그인 |
|-------|------|------|--------|
| **Gismondi on Wine** | `gismondi_tool.py` + `data/wines.db` | 별도 submodule CSV → SQLite (FTS5) | ❌ |
| **WineAlign** | `winealign_tool.py` | HTML scraping + login session | ✅ 필요 |
| **Robert Parker** | `robert_parker_tool.py` | Algolia REST API + auto-login | ✅ 필요 (구독) |
| **BC Liquor Store** | `bcliquor_tool.py` | JSON API (`/ajax/browse`) | ❌ |
| **Okanagan Cellars** | `okanagan_cellars_tool.py` | JSON API (`/api/shop/.../products`) | ❌ |
| **Everything Wine** | `everythingwine_tool.py` | HTML scraping (`catalogsearch`) | ❌ |
| **Marquis Wine Cellars** | `marquis_tool.py` | JSON API (BigCommerce Discovery) | ❌ |
| **Tavily 웹 검색** | `tavily_tool.py` | REST API (paid) | ✅ 필요 |

---

## 각 Tool 상세

### 1. WineAlign (`winealign_tool.py`)

캐나다 최대 와인 리뷰 플랫폼. **월 구독료를 내야** 전문가 리뷰를 볼 수 있다. JSON API를 따로 못 찾아서, 구독하고 내 계정으로 로그인한 뒤 웹페이지를 파싱하는 방식으로 만들었다.

- **인증**: `authenticity_token` + `person_credentials` 쿠키 기반 세션
- **자동 재로그인**: 세션 만료되면 `/login` 리다이렉트 감지해서 자동으로 다시 로그인
- **데이터**: 와인 이름, appellation, 점수, 가격, 전문가별 리뷰 (점수, 테이스팅 노트, value rating, drink window)
- **주의**: 요청 사이에 0.5초 딜레이 넣어서 polite하게 동작

```python
results = await search_winealign("pinot noir", max_pages=3, include_reviews=True)
```

### 2. BC Liquor Store (`bcliquor_tool.py`)

BC주 공식 주류 판매점. 다행히 Elasticsearch 기반 JSON API가 있어서 깔끔하게 데이터를 가져올 수 있었다.

- **API**: `GET /ajax/browse?search=...&sort=_score:desc&size=24&page=1`
- **데이터**: 이름, 가격 (세일 여부), 품종, 국가, 도수, 테이스팅 노트, 소비자 평점/투표수, 재고 매장 수, BC VQA 여부
- **특징**: 카테고리 필터 가능 (`wine`, `beer`, `spirits`)

```python
results = await search_bcliquor("tantalus", max_pages=2, category="wine")
```

### 3. Okanagan Cellars (`okanagan_cellars_tool.py`)

밴쿠버에 2개 매장 (West 1st Ave, West 4th Ave) 있는 와인샵. JSON API가 열려 있어서 바로 사용.

- **API**: `GET /api/shop/131-41/products?q=...&show_on_web=true`
- **데이터**: 이름, 카테고리, 가격, 세일 여부, 재고 수량, 용량 (750ml, 1.5L 등)
- **특징**: `_dc` 타임스탬프 파라미터로 캐시 우회, OOS 상품도 포함 가능

```python
results = await search_okanagan_cellars("checkmate")
```

### 4. Marquis Wine Cellars (`marquis_tool.py`)

밴쿠버의 큐레이션 와인 전문점. BigCommerce 기반이라 Discovery API가 public으로 열려 있다.

- **API**: `GET https://discovery.marquis-wines.com/apis/ecommerce-service/public/discovery/v2/search`
- **데이터**: 이름, SKU, 가격 (정가/세일가), 재고 수준, 카테고리 계층 (예: White Wine > Chardonnay > BC > Okanagan)
- **특징**: 이미지 URL이 JSON string으로 들어오는데 한 번 더 파싱해야 함. 페이지네이션 지원 (limit/skip)

```python
results, total = await search_marquis("martins lane", limit=30)
```

### 5. Everything Wine (`everythingwine_tool.py`)

밴쿠버 와인샵. API가 없어서 HTML scraping으로 만들었다. Magento 계열 프론트엔드라 서버사이드 렌더링.

- **방식**: `GET /catalogsearch/result/?q=...` → BeautifulSoup으로 파싱
- **데이터**: 이름, 가격, 세일 여부, 국가, 재고 상태 (창고배송/매장픽업/타매장)
- **특징**: 재고 상태가 3단계로 나뉨 — ✅ available, ❌ unavailable, ⚠️ other-store
- **디버그**: `debug_everythingwine.py`로 HTML 구조 확인용 스크립트도 있음

```python
results = await search_everything_wine("synchromesh")
```

### 6. Gismondi on Wine (`gismondi_tool.py` + `data/wines.db`)

캐나다 와인 평론가 Anthony Gismondi의 리뷰 데이터. 원본 CSV는 별도 submodule (`gismondi-canada-wines/`)에서 관리되고, 거기 GitHub Actions이 주 3회 자동 스크래핑한다. 그런데 매번 CSV를 파싱하는 건 비효율적이라 SQLite로 빌드해서 쓰기로 했다. 어차피 데이터가 1400건 수준이라 SQLite로 충분하고, FTS5 가상 테이블 붙이면 풀텍스트 검색도 깔끔하게 된다.

처음엔 FTS5 쿼리에 아포스트로피("quails' gate" 같은) 넣으면 syntax error가 났는데, `re.sub(r'[^\w\s]', ' ', query)`로 special char 다 날리고 토큰만 남기는 식으로 해결했다. FTS5는 디폴트가 implicit AND라서 토큰 두 개 들어가면 둘 다 매칭되는 문서만 반환한다.

- **데이터**: 와인 이름, /100 점수, /20 점수, region, tasting notes, taster, 가격, producer, grape, distributor, url 등 — 현재 1391건
- **FTS5 인덱스 필드**: title, region, tasting_notes, grape, producer
- **필터**: `score_min`, `price_max`, `bc_only` (기본 True)
- **빌드**: `python build_db.py` (CSV → `data/wines.db`)
- **자동 업데이트**: `.github/workflows/update_db.yml`이 Tue/Thu/Sat 02:00 UTC에 submodule pull → DB 재빌드 → 변경분 커밋. 원본 스크래퍼가 Mon/Wed/Fri에 돌아서 2시간 뒤 따라가게 맞췄다.
- **async 처리**: SQLite는 blocking이라 `asyncio.to_thread()`로 감싸서 이벤트 루프 안 막게 함

```python
results = await search_gismondi(
    "pinot noir",
    score_min=90,
    price_max=50,
    bc_only=True,
)
```

### 7. Robert Parker (`robert_parker_tool.py`)

세계에서 가장 영향력 있는 와인 평가 시스템. Robert Parker Wine Advocate의 100점 만점 평점, 전문 테이스팅 노트, 음용 기간(drink window) 등을 Algolia 기반 REST API로 검색한다. 월간 구독($9.99 USD/month)이 필요하다.

- **인증**: CSRF 토큰 + 이메일/비밀번호 자동 로그인. `GET /users/csrf-token`으로 CSRF 쿠키를 받고, `POST /users/login`에 `xsrf-token` 헤더로 전달. JWT `accessToken` (~30일 유효)을 발급받아 이후 API 호출에 사용. 401 에러 시 자동 재로그인.
- **검색**: Algolia `filters` 문법으로 rating, country, region, color, variety 필터링 가능. `facetFilters` 배열은 이 API에서 무시됨 — 반드시 `filters` 문자열 사용.
- **데이터**: 와인 이름, producer, vintage, RP 점수 (100점), varieties, region/sub_region/appellation, 가격 범위, drink window, certified (Organic 등), 리뷰어별 테이스팅 노트 + 기사 제목 + producer note
- **용도**: 국제적으로 인정받는 점수 체계가 필요할 때. WineAlign/Gismondi가 캐나다 중심이라면, RP는 전 세계 와인과의 비교가 가능.

```python
results = await search_robert_parker(
    "pinot noir",
    country="Canada",
    region="British Columbia",
    rating_min=90,
    hits_per_page=5,
)
```

### 8. Tavily 웹 검색 (`tavily_tool.py`)

기존 와인 매장/리뷰 툴로 답이 안 나오는 질문 — 예를 들면 "Thai green curry랑 어울리는 BC 와인", "Naramata Bench는 어떤 지역인가", 또는 매장에 없는 와인 이름 disambiguate — 처리용 폴백. Tavily API를 그대로 호출하고, `include_answer=True`로 AI 요약(`answer` 필드)까지 같이 받아서 LLM이 바로 활용할 수 있게 했다.

기존 툴들이 다 `httpx.AsyncClient` 쓰고 있어서 SDK(`tavily-python`) 안 깔고 REST API 직접 호출. 의존성 하나 늘리지 않고 패턴도 일관됨.

- **인증**: `.env`의 `TAVILY_API_KEY` 필요
- **데이터**: title, url, content snippet, relevance score, published_date, AI-generated summary
- **주의**: 호출당 과금. agent 시스템 프롬프트에서 호출 빈도 제한할 예정 (turn당 1회 권장)

```python
results, answer = await search_tavily("best food pairings for BC Pinot Noir")
```

---

## 프로젝트 파일 구조

```
BC-wine-ai-agents/
├── agent.py                    # LangGraph 그래프 빌더 (ReAct + 10 tools)
├── app.py                      # FastAPI 백엔드 (SSE 스트리밍, 세션 관리, validation 게이트)
├── validation.py               # Pre-agent query 검증 (off-topic 쿼리 그래프 우회)
├── compaction.py               # Tool result compaction 노드 (라운드 사이 context 축소 + incremental wine_context merge)
├── state.py                    # AgentState TypedDict + 관련 스키마
├── models.py                   # Gemini 3.5 Flash LLM 팩토리
├── prompts.py                  # 오케스트레이터/페어링/합성/검증 시스템 프롬프트
├── safety.py                   # safe_tool 데코레이터 (에러 래핑)
├── merge.py                    # 와인 이름 정규화 + 매장 간 중복 제거
├── winealign_tool.py           # WineAlign 검색
├── bcliquor_tool.py            # BC Liquor Store 검색
├── okanagan_cellars_tool.py    # Okanagan Cellars 검색
├── marquis_tool.py             # Marquis Wine Cellars 검색
├── everythingwine_tool.py      # Everything Wine 검색
├── robert_parker_tool.py       # Robert Parker 평점/리뷰 (Algolia API)
├── gismondi_tool.py            # Gismondi DB 검색 (SQLite + FTS5)
├── tavily_tool.py              # Tavily 웹 검색 fallback
├── build_db.py                 # CSV → SQLite 빌드 스크립트
├── requirements.txt            # Python 패키지 의존성
├── static/
│   ├── index.html              # 랜딩 페이지 + 풀스크린 채팅 오버레이
│   ├── styles.css              # 와인 컬러 팔레트, 채팅 + 툴 배지 스타일
│   └── app.js                  # SSE 클라이언트, run_id 기반 툴 배지 매칭, 마크다운 렌더링
├── data/
│   ├── wines.db                # Gismondi 리뷰 SQLite (1391 rows, FTS5)
│   └── checkpoints.db          # LangGraph 체크포인터 (gitignored)
├── gismondi-canada-wines/      # 원본 CSV (git submodule)
├── tests/                      # Golden-query quality evaluation
│   ├── golden_queries.py       # 38 queries across 13 categories (INV/CRI/PAIR/MT/...)
│   ├── metrics.py              # Deterministic metrics (orch, hallucination, coverage, structure)
│   ├── judge.py                # LLM-as-judge (Gemini Flash temp=0)
│   ├── quality_eval.py         # Runner — produces results.json + summary.md + transcripts
│   └── results/<timestamp>/    # Per-run outputs (gitignored)
├── docs/
│   └── AGENT_DESIGN.md         # 전체 아키텍처 설계 문서 + iteration history
├── .github/workflows/
│   └── update_db.yml           # DB 자동 업데이트 (Tue/Thu/Sat)
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
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Mac/Linux

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
ROBERT_PARKER_API_KEY=7ZPWPBFIRE2JLR6JBV5SCZPW54ZZSGGY

# LangSmith (optional — tracing)
LANGCHAIN_TRACING_V2=true
LANGCHAIN_API_KEY=ls__...
LANGCHAIN_PROJECT=bc-wine-ai-agent
```

### Gismondi DB 빌드 (최초 1회)

GitHub Actions이 자동으로 업데이트해주지만, 처음 clone하면 직접 빌드해야 한다:

```bash
python build_db.py
```

### 각 tool 독립 테스트

```bash
python winealign_tool.py        # "storm haven" 검색
python bcliquor_tool.py         # "tantalus", "checkmate" 검색
python okanagan_cellars_tool.py # "checkmate", "tantalus", "cedar creek" 검색
python marquis_tool.py          # "checkmate", "martins lane", "pinot noir" 검색
python everythingwine_tool.py   # "martins", "synchromesh" 검색
python tavily_tool.py           # 페어링/지역 지식 쿼리 3종
python robert_parker_tool.py    # martin's lane, BC pinot noir, riesling 검색
python gismondi_tool.py         # pinot/riesling/chardonnay 등 6종 쿼리
```

---

## Tech Stack

- **httpx** — async HTTP 클라이언트 (세션/쿠키 관리 포함)
- **BeautifulSoup4** — HTML 파싱 (WineAlign, Everything Wine)
- **Pydantic** — 데이터 모델 & 유효성 검사
- **python-dotenv** — 환경변수 로딩
- **SQLite + FTS5** — Gismondi 리뷰 로컬 DB (Python 표준 라이브러리, 별도 설치 없음)
- **LangGraph** — ReAct 에이전트 오케스트레이션 (10개 tool, 병렬 실행)
- **Gemini 3.5 Flash (Vertex AI)** — 모든 노드에서 사용하는 LLM
- **FastAPI** — SSE 스트리밍 백엔드
- **HTML/CSS/JS** — SUM AI 디자인 계승 채팅 UI (vanilla, 빌드 스텝 없음)
- **rapidfuzz** — 와인 이름 퍼지 매칭 (매장 간 중복 제거)
- **LangSmith** — 트레이스/관측 (환경변수 설정 시 자동 활성화)

---

## 공통 패턴

모든 tool은 같은 구조를 따름:

1. **`search_*(query)` 함수** — async, 구조화된 Pydantic 모델 리스트 반환
2. **`format_results()` 함수** — LLM이 읽기 좋은 텍스트 포맷으로 변환
3. **`main()` 함수** — `python tool.py`로 독립 실행 가능한 테스트
4. **Pydantic 모델** — 각 사이트에 맞는 데이터 구조 정의

---

## 서버 실행

```bash
python -m uvicorn app:app --port 8000
```

브라우저에서 `http://localhost:8000` 열면 채팅 UI가 뜬다.

---

## 다음 단계

상세 설계는 [`docs/AGENT_DESIGN.md`](docs/AGENT_DESIGN.md)에 다 정리해놨다 — 8회 iteration 의 결과 분석과 다음 architectural 개선 후보까지 같이 들어 있다. 남은 항목:

- [x] `state.py` — `AgentState` TypedDict
- [x] `models.py` — Gemini 3.5 Flash 팩토리 (Vertex AI)
- [x] `prompts.py` — orchestrator + synthesis 프롬프트 (15개 behavioral rules, table-skeleton output contract)
- [x] `safety.py` — `safe_tool` 데코레이터 (graceful degradation)
- [x] `merge.py` — 와인 이름 정규화 + 매장 간 중복 제거 (rapidfuzz). Gismondi 의 `price_channel` → synthetic StorePrice 변환 포함.
- [x] `agent.py` — LangGraph 그래프 빌드, ReAct + InMemorySaver. `MAX_TOOL_ROUNDS=3` safety net + `format_response_node` 합성 단계 구현.
- [x] `app.py` — FastAPI + SSE 스트리밍 + 세션 관리
- [x] `static/` — SUMAI 디자인 베이스 채팅 UI
- [x] `tests/` — 38개 golden query + 결정론적 metric + LLM-as-judge (`python -m tests.quality_eval`)
- [ ] Architectural 다음 단계: query-type routing, deterministic Where-to-buy 렌더링, merge fuzzy matching 강화 (`docs/AGENT_DESIGN.md` §18.2 참조)
- [ ] Dockerfile + 배포

### 품질 평가 파이프라인 실행

```bash
python -m tests.quality_eval                    # 전체 38 query (~40-50 min)
python -m tests.quality_eval --only INV,CRI     # 카테고리 필터
python -m tests.quality_eval --id INV-001       # 단일 query
python -m tests.quality_eval --dry-run          # 빠른 sanity check (2 query)
python -m tests.quality_eval --skip-judge       # 결정론적 metric 만
```

결과는 `tests/results/<YYYYMMDD-HHMMSS>/` 에 `results.json`, `summary.md`, `transcripts/<id>.md` 형식으로 저장됨.
