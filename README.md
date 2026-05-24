# BC Wine AI Agents

BC 와인을 검색하고 추천해주는 AI 에이전트. LangGraph 기반으로 여러 와인 사이트의 데이터를 통합해서 사용자 질문에 답변하는 게 최종 목표.

현재 단계: **LangGraph 에이전트 구축 전, 데이터 수집용 tool 개발 완료.**

---

## 전체 구조

```
사용자 질문
    ↓
LangGraph Agent (TODO)
    ↓
┌─────────────────────────────────────────────────────┐
│  Tools (데이터 수집 — 각 사이트별 search 함수)       │
│                                                     │
│  winealign_tool.py ──── 전문가 리뷰 & 점수          │
│  bcliquor_tool.py ───── 가격 & 재고 (공식 주류 판매) │
│  okanagan_cellars_tool.py ── 밴쿠버 와인샵 재고     │
│  marquis_tool.py ────── 밴쿠버 큐레이션 와인샵      │
│  everythingwine_tool.py ── 밴쿠버 와인샵 재고       │
│  gismondi-canada-wines/ ── 캐나다 와인 평론 데이터   │
└─────────────────────────────────────────────────────┘
```

---

## 데이터 소스 & 수집 방식

| Store | 파일 | 방식 | 로그인 |
|-------|------|------|--------|
| **Gismondi on Wine** | `gismondi-canada-wines/` (submodule) | 별도 repo에서 스크래핑한 데이터 | ❌ |
| **WineAlign** | `winealign_tool.py` | HTML scraping + login session | ✅ 필요 |
| **BC Liquor Store** | `bcliquor_tool.py` | JSON API (`/ajax/browse`) | ❌ |
| **Okanagan Cellars** | `okanagan_cellars_tool.py` | JSON API (`/api/shop/.../products`) | ❌ |
| **Everything Wine** | `everythingwine_tool.py` | HTML scraping (`catalogsearch`) | ❌ |
| **Marquis Wine Cellars** | `marquis_tool.py` | JSON API (BigCommerce Discovery) | ❌ |

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

### 6. Gismondi on Wine (`gismondi-canada-wines/`)

캐나다 와인 평론가 Anthony Gismondi의 리뷰 데이터. 별도 GitHub repo에서 스크래핑하고, 이 프로젝트에서는 **git submodule**로 참조만 한다. 원본 repo에서 GitHub Actions가 주간 스케줄로 자동 업데이트 중.

```bash
# 최신 데이터 가져오기
git submodule update --remote
```

---

## 프로젝트 파일 구조

```
BC-wine-ai-agents/
├── winealign_tool.py           # WineAlign 검색 (HTML scraping + 로그인)
├── bcliquor_tool.py            # BC Liquor Store 검색 (JSON API)
├── okanagan_cellars_tool.py    # Okanagan Cellars 검색 (JSON API)
├── marquis_tool.py             # Marquis Wine Cellars 검색 (BigCommerce API)
├── everythingwine_tool.py      # Everything Wine 검색 (HTML scraping)
├── debug_everythingwine.py     # Everything Wine HTML 구조 디버깅용
├── gismondi-canada-wines/      # Gismondi 리뷰 데이터 (git submodule)
├── .env                        # 환경변수 (WineAlign 계정 — git 추적 안됨)
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

pip install httpx beautifulsoup4 pydantic python-dotenv
```

### 환경변수

`.env` 파일 생성 (WineAlign 계정 필요):

```
WINEALIGN_EMAIL=your_email@example.com
WINEALIGN_PASSWORD=your_password
```

### 각 tool 독립 테스트

```bash
python winealign_tool.py        # "storm haven" 검색
python bcliquor_tool.py         # "tantalus", "checkmate" 검색
python okanagan_cellars_tool.py # "checkmate", "tantalus", "cedar creek" 검색
python marquis_tool.py          # "checkmate", "martins lane", "pinot noir" 검색
python everythingwine_tool.py   # "martins", "synchromesh" 검색
```

---

## Tech Stack

- **httpx** — async HTTP 클라이언트 (세션/쿠키 관리 포함)
- **BeautifulSoup4** — HTML 파싱 (WineAlign, Everything Wine)
- **Pydantic** — 데이터 모델 & 유효성 검사
- **python-dotenv** — 환경변수 로딩
- **LangGraph** — 에이전트 오케스트레이션 (구축 예정)

---

## 공통 패턴

모든 tool은 같은 구조를 따름:

1. **`search_*(query)` 함수** — async, 구조화된 Pydantic 모델 리스트 반환
2. **`format_results()` 함수** — LLM이 읽기 좋은 텍스트 포맷으로 변환
3. **`main()` 함수** — `python tool.py`로 독립 실행 가능한 테스트
4. **Pydantic 모델** — 각 사이트에 맞는 데이터 구조 정의

---

## 다음 단계

- [ ] LangGraph 에이전트 구축 — 사용자 질문을 받아서 적절한 tool 호출
- [ ] tool 간 데이터 통합 — 같은 와인을 여러 소스에서 찾아 비교
- [ ] Gismondi 데이터 연동 — submodule의 리뷰 데이터를 agent가 참조
