# Google for Startups AI Agents Challenge — Build Plan (v2)

## Context

제출 마감: 2026-06-11 5PM PT. **Track 1 (Build, Net-New Agents)** 트랙.
기존 단일 ReAct 에이전트(LangGraph, Gemini 3.5 Flash, Cloud Run, wineaiagent.com 라이브)를
**전 주류 대응 멀티에이전트 시스템**으로 리빌드.

### 제품 피벗 (기존 BC 와인 전용 → 전 주류 컨시어지)
- **범위**: 와인뿐 아니라 맥주·증류주·칵테일까지. 지역 포커스 **밴쿠버 전용**.
- **B2C**: "뭘 살까 / 이 음식엔 뭘 / 근처 어디서" — 다국어(EN default, KO/ZH/JA).
- **B2B (F&B)**: 식당이 음식 메뉴(사진/텍스트) 입력 → 에이전트가 어울리는 **주류 메뉴를 설계**하고 실제 매장·가격까지 소싱. (소믈리에 고용 대체)
- **Gismondi 제거**: 저작권 정리. 리뷰/점수는 Google Search grounding으로 보강하되 **출처 링크 + 요약만**.

### 필수 기술 요건 (Track 1) — 충족 현황
| 요건 | 현황 |
|------|------|
| Intelligence: Gemini | Gemini 3.5 Flash ✓ |
| Orchestration: ADK 또는 지원 OSS(LangChain/CrewAI) | LangGraph/LangChain ✓ (지원 프레임워크) |
| Infrastructure: Cloud Run/GKE | Cloud Run ✓ |
| MCP(권장) | LangChain @tool로 동등 기능; 다이어그램에 "MCP-compatible tools" 표기 |
| A2A / Agent Engine | Track 3 전용 → SKIP |

### 심사 기준
Technical Implementation 30% / Business Case 30% / Innovation & Creativity 20% / Demo & Presentation 20%

---

## 타깃 아키텍처 — Supervisor + 3 Specialist

```
User → [Entry Router] ──(이미지)──> [Vision Node]  (라벨 / 와인리스트 / 음식메뉴 추출)
                       └─(텍스트)──┐        │
                                  ▼        ▼
                          [Supervisor Agent]  (Gemini 3.5 Flash)
                          역할: 라우팅 · 종합 · 명확화 · 선호도
                          tools: ask_user_clarification, update_preferences
                                  │
              ┌───────────────────┼───────────────────────┐
              ▼                   ▼                         ▼
     [Sourcing Agent]     [Sommelier Agent]        [Menu Architect Agent]  (B2B)
     6 store tools         pairing 추론              음식메뉴 → 주류메뉴 설계
     + Google Maps         + 전 주류 지식            + Sourcing 호출(실제 제품/가격)
     역할: 가격/재고/        + Google Search          역할: 코스별 와인/맥주/칵테일
       매장위치 비교          grounding(사실·리뷰)        페어링 메뉴 + 소싱
```

- 각 specialist는 독립 mini ReAct StateGraph. Supervisor가 `@tool` 래퍼로 호출(기존 `reasoning_pair_wine_tool` 패턴 재사용).
- Vision node / entry_router는 유지(음식메뉴 타입만 추가).
- `app.py` SSE 스트리밍은 supervisor 노드만 스트리밍 → 변경 최소.

---

## 변경 사항 (우선순위순)

### P0-1. Gismondi 완전 제거 (0.5일)
- 삭제: `tools/gismondi_tool.py`, `data/wines.db`, `scripts/build_db.py`, `.github/workflows/update_db.yml`
- 서브모듈 제거: `gismondi-canada-wines` (deinit + `.gitmodules` 정리)
- 코드 정리: `agent.py`(import/래퍼/TOOLS), `prompts.py:80-81`, `tests/metrics.py`(KNOWN_CRITICS), `tests/golden_queries.py`(CRI 카테고리 → 리뷰는 grounding 기반으로 재정의), README

### P0-2. 전 주류로 범위 확장 (0.5일) — 대부분 프롬프트 레벨
- `prompts.py` **G5 뒤집기**: "BC 와인 전용 + 맥주/증류주 거부" → "와인·맥주·증류주·칵테일 모두 지원, 지역 포커스 밴쿠버 전용"
- `validation.py` `VALIDATION_SYSTEM_PROMPT`: 맥주/증류주/칵테일을 valid로 허용 (현재 거부 → 수정)
- store tool은 변경 불필요 (BC Liquor·Legacy가 전 주류 반환). 와인 전용 매장은 자연스럽게 빈 결과.
- 브랜딩: 도메인은 wineaiagent.com 유지하되 카피는 "drinks/beverage concierge"로 리프레이밍 (프론트 문구만)

### P0-3. 멀티에이전트 리팩토링 — Supervisor + 3 Specialist (2일)
- 신규 `agents/` 디렉토리:
  - `agents/supervisor.py` — supervisor 그래프 + 라우팅 프롬프트 + specialist 호출
  - `agents/sourcing_agent.py` — 6 store tool + Google Maps, 독립 StateGraph
  - `agents/sommelier_agent.py` — pairing 추론 + 전 주류 지식 + Google Search grounding
  - `agents/menu_architect.py` — (B2B) 음식메뉴 → 주류메뉴 설계, Sourcing 결과 활용
- `agent.py` 리팩토링: 11개 tool 래퍼를 각 specialist로 이동, `build_graph()`를 supervisor 중심으로 재구성
- `prompts.py`: supervisor 프롬프트 + 3개 specialist 프롬프트 추가 (기존 ORCHESTRATOR 분리)
- `state.py`: `specialist_results`, `drink_menu`(B2B 산출물) 필드 추가

### P0-4. Google Search Grounding — Tavily 교체 (0.5일)
- `models.py`에 `get_grounded_llm()` 추가 — Gemini 네이티브 Google Search grounding 활성화
- Sommelier / Menu Architect가 사실·리뷰 보강에 사용
- `tools/tavily_tool.py` 제거(또는 미사용), `prompts.py` C2 규칙 → Google Search 규칙으로 교체
- **리뷰 저작권 가드레일**(프롬프트 명시): grounding으로 얻은 리뷰/점수는 **출처 매체명 + 링크 + 짧은 요약만** 인용. 전문 평론 텍스트(verbatim tasting note) 재현 금지. 점수는 출처와 함께만.

### P0-5. Google Maps Places API (0.5일)
- 신규 `tools/google_maps_tool.py` — Places API (New) `searchText` (매장명/주소/영업시간/평점/위치)
- Sourcing Agent에 연결 → "근처 BC Liquor", "밴쿠버에서 영업 중인 매장"
- GCP: Places API (New) enable + `GOOGLE_MAPS_API_KEY` (`.env`)

### P0-6. B2B Menu Architect + 음식메뉴 비전 (1일)
- `vision.py`: `document_type`에 **`food_menu`** 추가 → 음식 항목(요리명/설명/코스/가격) 구조화 추출. `prompts.py` VISION 프롬프트 확장.
- `agents/menu_architect.py`: 음식메뉴(비전 추출 or 텍스트) → 코스/요리별 주류 추천 → Sourcing으로 실제 제품·가격 소싱 → 구조화된 **주류 메뉴** 산출
- Supervisor 라우팅: 음식메뉴 감지 또는 "메뉴 짜줘" 의도 → Menu Architect

### P0-7. 다국어 EN/KO/ZH/JA (0.5일) — 프롬프트 레벨
- `prompts.py` Response Language 섹션: EN default + KO/ZH/JA 명시 + 예시. 주류명/생산자명은 원어 유지.
- `validation.py`: 거부 메시지 다국어(ZH/JA 예시 추가)
- `tests/golden_queries.py`: ZH/JA 쿼리 추가

### P0-8. Business Case — B2B/B2C 균형 (0.5일)
- **B2B**: BC 주정부 3년 시범(바·레스토랑이 소매점 직접 구매, FIFA 2026 대비) → F&B가 주류 메뉴를 빠르게 세팅·소싱해야 하는 수요 → Menu Architect가 직접 해결.
- **B2C**: FIFA 2026 다국어 관광객 + 로컬 소비자. 라벨 사진→정보, 음식→페어링, Maps→근처 매장.
- 차별점: 밴쿠버 주요 소매점 동시 비교(유일), 비전(라벨+음식메뉴), 다국어, 라이브 프로덕션.

### P0-9. 제출물 — Architecture Diagram + Demo Video (0.75일)
- **Architecture Diagram** (Mermaid): Supervisor+3 specialist, GCP 인프라(Cloud Run, Gemini grounding, Maps), 데이터 흐름(User→Cloudflare→Cloud Run→Graph→Tools)
- **Demo Video (3-5분, B2B/B2C 균형)**:
  - B2B: 식당 음식 메뉴 사진 → 코스별 주류 메뉴 설계 + 매장/가격 소싱
  - B2C: 라벨 사진 → 정보, 음식 → 페어링, "근처 매장"(Maps), 다국어(KO/ZH/JA)
  - 멀티에이전트 라우팅 시각화
- **Testing Access**: wineaiagent.com (라이브)

### SKIP
- **MCP**: LangChain @tool로 동등. 다이어그램 표기로 충분.
- **A2A / Agent Engine**: Track 3 전용.
- **밴쿠버 외 지역(리치먼드 등) 확장**: 범위 제외 — 밴쿠버 전용으로 집중.
- **Vertex AI Search**: stretch(여유 시에만).

---

## 일정 (6/5 목 → 6/11 수 5PM PT 마감)

| Day | Date | Focus |
|-----|------|-------|
| 1 | 6/5 (목) | Gismondi 제거 + 전 주류 확장(G5/validation) + `agents/` 스캐폴딩 |
| 2 | 6/6 (금) | Sourcing + Sommelier specialist + Google Search grounding + Maps tool |
| 3 | 6/7 (토) | Supervisor 배선 + Menu Architect(B2B) + food_menu 비전 |
| 4 | 6/8 (일) | 다국어 ZH/JA + 로컬 테스트 + golden_queries 갱신 |
| 5 | 6/9 (월) | Cloud Run 재배포 + 안정화 + eval + 아키텍처 다이어그램 + 비즈니스 케이스 문서 |
| 6 | 6/10 (화) | Demo video 촬영 + 제출 문서 정리 |
| — | 6/11 (수) | 최종 점검 + Devpost 제출 (5PM PT 이전) |

---

## 심사 어필 정리
- **Technical (30%)**: Gemini 멀티에이전트(Supervisor+3) · Google Search grounding · Maps · 비전(라벨+음식메뉴) · Cloud Run · LangSmith observability · 에러 격리/SSE/검증 게이트
- **Business (30%)**: B2B 메뉴 설계(규제완화+FIFA) + B2C 다국어 컨시어지 · 전 주류 시장 · 밴쿠버 주요 매장 동시 비교 · 라이브 프로덕션
- **Innovation (20%)**: 음식메뉴 → 주류메뉴 설계(B2B) · 비전 · 크로스스토어 소싱 · 다국어
- **Demo (20%)**: 라이브 wineaiagent.com · B2B/B2C 균형 · 멀티에이전트 라우팅 시각화 · Maps/다국어

---

## Verification
1. `python -c "from agent import build_graph; print('OK')"` — 그래프 빌드
2. Gismondi 잔재 0: `grep -ri gismondi . --include=*.py` → 없음
3. 전 주류: "IPA 맥주 추천" / "위스키" 쿼리 → 정상 응답(거부 X)
4. 멀티에이전트 라우팅: 가격→Sourcing, 페어링→Sommelier, "메뉴 짜줘"→Menu Architect
5. B2B: 음식메뉴 이미지 → 주류메뉴 + 매장/가격 산출
6. 다국어: KO/ZH/JA 쿼리 → 해당 언어 응답
7. Maps: "근처 BC Liquor" → 위치/영업시간
8. `python -m tests.quality_eval --skip-judge` 회귀 통과(CRI는 grounding 기반으로 갱신)
9. Cloud Run 재배포 후 wineaiagent.com 라이브 확인
