# 진행 상황 (PROGRESS) — Google AI Agents Challenge 리빌드

> 기준일: **2026-06-05**. 계획 전문은 [CHALLENGE_PLAN.md](./CHALLENGE_PLAN.md).
> 마감: **2026-06-11 17:00 PT**. 트랙: **Track 1 (Build)**.
> 상태 요약: **Day 1–3 완료**(빌드/임포트 레벨 검증), **Day 4–6 남음**. **아직 커밋/배포 안 함** (working tree only, branch `main`).

---

## 한 줄 요약
BC 와인 전용 단일 ReAct 에이전트 → **전 주류(와인·맥주·증류주·사이다·사케·칵테일) 멀티에이전트
(Supervisor + Sourcing/Sommelier/Menu Architect)** 로 리빌드 중. Gismondi 제거, Google Search
grounding + Google Maps 추가, B2B 메뉴 설계 + food_menu 비전, 다국어 EN/KO/ZH/JA.
**지역 범위: 밴쿠버 전용**(2026-06-06 결정 — 기존 밴쿠버+리치먼드에서 리치먼드 제외, Maps bias도 밴쿠버 도심으로 조정).

---

## ✅ Day 1 — Gismondi 제거 + 전 주류 확장 + 스캐폴딩 (완료)

**Gismondi 완전 제거**
- 삭제: `tools/gismondi_tool.py`, `data/wines.db`, `scripts/build_db.py`, `.github/workflows/update_db.yml`
- 서브모듈 `gismondi-canada-wines` 제거 + `.gitmodules` 삭제 + `.git/modules/` 클린업
- 코드 정리: `agent.py`(import/래퍼/TOOLS), `prompts.py`(catalog), `tests/metrics.py`(KNOWN_CRITICS + critic 정규화 맵),
  `tests/golden_queries.py`(CRI 카테고리 재정의 + 전 참조), `tests/quality_eval.py`(삭제된 DB 체크 제거 → eval 크래시 방지)
- 검증: 운영 `.py`에서 `gismondi` 0건

**전 주류로 범위 확장** (대부분 프롬프트 레벨)
- `prompts.py`: 정체성 `BC Wine Expert` → **AI Drinks Concierge**(밴쿠버 전용, B2C+B2B). **G5 뒤집기**(전 주류 허용).
  PAIRING/RELEVANCE/VALIDATION 프롬프트 일반화
- 다국어: 응답 언어 섹션 **EN default + KO/ZH/JA** + VALIDATION 거부 예시에 中文·日本語 추가
- store tool은 변경 없음(BC Liquor·Legacy가 맥주/증류주 반환)

**`agents/` 스캐폴딩**: `__init__/supervisor/sourcing_agent/sommelier_agent/menu_architect` 스켈레톤 (Day 2–3에 실제 구현으로 대체됨)

---

## ✅ Day 2 — Grounding + Maps + Specialist 배선 (완료)

**Google Search grounding (Tavily 교체)**
- `models.py`: `get_grounded_llm()` 추가
- 신규 `tools/google_search_tool.py`: `search_web_grounded(query)` — Gemini 네이티브 grounding.
  `{"google_search":{}}` → 실패 시 `{"google_search_retrieval":{}}` 폴백. 출처 URL best-effort 추출.
  **리뷰 저작권 가드레일**(출처·링크·요약만, verbatim 금지) 내장
- Tavily 전량 교체: `prompts.py`(C2·카탈로그·G2), `app.py`(배지 렌더, `search_tavily`→`search_web_grounded`),
  `tests/metrics.py`(호출 한도), `tests/quality_eval.py`(env 키), `tests/golden_queries.py`(`search_tavily_tool`→`search_web_grounded_tool`).
  `tools/tavily_tool.py` 삭제

**Google Maps Places**
- 신규 `tools/google_maps_tool.py`: Places API (New) `searchText`, 밴쿠버 locationBias(49.2827,-123.1207 / 12km).
  주소·영업시간·평점·지도링크 반환

**Specialist 배선 (핵심 구조 변경)**
- 신규 `agent_tools.py`: **모든 `@tool` 래퍼를 agent.py에서 추출**(Day 3 순환 import 방지) + 그룹 리스트
  (`SOURCING_TOOLS`/`SOMMELIER_TOOLS`/`SUPERVISOR_DIRECT_TOOLS`/`ALL_TOOLS`)
- 신규 `agents/react_subagent.py`: 공용 ReAct sub-graph 빌더 + `run_subagent` / `run_subagent_json`
- `agents/sourcing_agent.py`, `agents/sommelier_agent.py`: 실제 sub-graph + `@tool`
- `agent.py`: 래퍼 제거하고 agent_tools에서 import

---

## ✅ Day 3 — Supervisor 라이브 배선 + Menu Architect + food_menu (완료)

**Vision food_menu**
- `vision.py`: `FoodMenuItem`/`FoodMenuExtraction` + `document_type='food_menu'` + `format_extraction` 렌더
- `prompts.py` VISION 프롬프트: 음식 메뉴 추출 규칙

**Menu Architect (B2B)**
- `agents/menu_architect.py`: 실제 sub-graph. 음식메뉴 → 코스별 페어링 설계 → **`sourcing_agent_tool` 호출(A2A)**
  로 실제 제품·가격 소싱 + grounding. `menu_architect_tool` @tool (입력=food_menu 텍스트/추출)

**Supervisor를 라이브 그래프로 교체**
- `prompts.py` `SUPERVISOR_SYSTEM_PROMPT` 신규(라우팅 계약 + 전 가드레일 + 비전 처리 + 리뷰 가드레일)
- `agent.py`: 그래프를 단일 오케스트레이터 → **Supervisor + 3 specialist**로 교체.
  `TOOLS` = [ask_clarification, update_prefs, sourcing_agent_tool, sommelier_agent_tool, menu_architect_tool].
  **그래프 노드명은 `orchestrator` 유지** → app.py SSE 스트리밍/배지 필터 무변경
- specialist sub-graph는 **isolated 실행**(부모 콜백 미전파) → 내부 store/LLM 이벤트 스트림에 안 샘
- specialist `@tool`은 **JSON 엔벨로프** 반환(`run_subagent_json`) → `_summarize_tool_output`이 본문 배지로 렌더
- `app.py`: specialist answer 본문 + Maps place(주소·영업중·지도링크) 렌더 추가
- `agents/supervisor.py`: 실제 배선이 agent.py에 있음을 가리키는 문서로 갱신

---

## 검증 현황 (직접 실행함 — **빌드/임포트만**, LLM 호출 안 함)
- 전 변경 파일 AST parse OK
- 전체 import 체인 OK (순환 import 없음), `import app` OK (LangSmith tracing ENABLED)
- Supervisor 그래프 COMPILED (5 tools), sourcing/sommelier/menu_architect sub-graph COMPILED
- `format_extraction(food_menu)` 정상 렌더
- **미검증(자격증명/네트워크 필요)**: 실제 LLM 라우팅 품질, grounding 호출, Maps 호출 — 사용자가 로컬에서 확인 필요

---

## 환경/시크릿
- `.env`(gitignored)에 **`GOOGLE_MAPS_API_KEY`** 저장됨(키는 채팅에 평문 노출됐으니 GCP에서 API 제한 권장)
- **Places API (New)** GCP enable 필요(아직 미확인)
- grounding은 **별도 키 불필요** — 기존 Vertex AI 자격증명 사용

## 현재 파일 상태 (이 작업 범위)
- **신규**: `agent_tools.py`, `agents/*`(react_subagent, sourcing_agent, sommelier_agent, menu_architect, supervisor, __init__),
  `tools/google_search_tool.py`, `tools/google_maps_tool.py`, `agent_challenge/*`
- **수정**: `agent.py`, `app.py`, `models.py`, `prompts.py`, `vision.py`, `tests/{golden_queries,metrics,quality_eval}.py`
- **삭제**: `tools/{gismondi_tool,tavily_tool}.py`, `data/wines.db`, `scripts/build_db.py`, `.github/workflows/update_db.yml`, 서브모듈, `.gitmodules`
- ⚠️ **이 작업과 무관(이전부터 변경되어 있던 것)**: `frontend/worker.js`(D), `frontend/wrangler.jsonc`(M),
  `frontend/.assetsignore`(??), `frontend/_worker.js`(??), `tests/judge.py`(M) — 건드리지 않음

---

## ⏭️ 남은 작업 (Day 4–6)

### Day 4 — 다국어 마무리 + golden_queries 갱신 + 로컬 테스트
- **[중요] `tests/golden_queries.py` expected_tools 리매핑**: Supervisor가 store 툴을 직접 안 부르고
  `sourcing_agent_tool`/`sommelier_agent_tool`/`menu_architect_tool`을 호출함. 내부 store 툴은 isolated라
  eval tool_log에도 안 잡힘 → 현재 tool-orchestration 메트릭 전부 mismatch. expected_tools를 specialist 어휘로 바꿔야 함.
  (hallucination/judge 메트릭은 정상 동작)
- ZH/JA: 프롬프트/validation은 이미 반영됨. golden_queries에 ZH/JA 쿼리 추가
- B2B(menu_architect)·Maps 골든 쿼리 추가
- 로컬 테스트(아래 "이어서 하기" 참고)

### Day 5 — 배포 + 산출물
- **Cloud Run 재배포**: `gcloud run deploy bc-wine-agent --source . --region us-west1 --project wine-agent-jh-2026 --allow-unauthenticated`
  → **`GOOGLE_MAPS_API_KEY`를 Cloud Run 환경변수로 추가** 필요(`--set-env-vars` 또는 콘솔)
- eval 실행 + 안정화
- **Architecture diagram**(Mermaid): Supervisor+3 specialist, GCP 인프라
- Business case 문서(B2B/B2C 균형)
- **정리**: `prompts.py`의 미사용 `ORCHESTRATOR_SYSTEM_PROMPT` 제거, OFF-003 injection canary 문자열 갱신,
  README/docs(AGENT_DESIGN.md) 리라이트, 프론트 카피 "drinks concierge"로 리브랜딩, `scripts/test_gemini_models.py`(일회성, Gismondi 언급) 정리

### Day 6 — 데모 영상 + 제출
- Demo video(3–5분, B2B/B2C 균형): 메뉴 사진→음료 메뉴 설계 / 라벨·페어링 / Maps / 다국어
- Devpost 제출(코드·영상·아키텍처 다이어그램·테스트 접근=wineaiagent.com)

---

## ▶️ 이어서 하기 (다음 세션)
1. 이 파일 + `CHALLENGE_PLAN.md`를 읽힌다. (예: "agent_challenge/PROGRESS.md 읽고 Day 4 이어서 해줘")
2. 빌드 sanity (LLM 불필요):
   ```bash
   python -c "from agent import build_graph; build_graph(); print('graph OK')"
   ```
3. 로컬 동작 확인(자격증명 필요):
   ```bash
   python -m uvicorn app:app --port 8000
   #  B2C 페어링: "스테이크에 맞는 와인 추천하고 어디서 사는지 알려줘"  → sommelier+sourcing
   #  B2B:        "이 메뉴에 맞는 음료 메뉴 짜줘: 마르게리타 피자, 티라미수"  → menu_architect
   #  Maps:       "근처 BC Liquor Store 알려줘"                         → sourcing(maps)
   #  리뷰:        "Painted Rock Syrah 리뷰 어때?"                      → sommelier(grounding)
   #  food menu 사진 업로드 → 음료 메뉴 설계
   python -m tools.google_search_tool   # grounding 스모크
   python -m tools.google_maps_tool      # maps 스모크 (GOOGLE_MAPS_API_KEY 필요)
   ```
4. Day 4 착수: **golden_queries expected_tools를 specialist 어휘로 리매핑** 먼저.
5. eval(사용자가 직접 실행): `python -m tests.quality_eval --skip-judge`

## 아키텍처 빠른 참조
```
entry_router ──image──> vision(food_menu/label/wine_list) ──┐
             └─text──────────────────────────────────────────┤
                                                              ▼
                            orchestrator 노드 = SUPERVISOR (prompts.SUPERVISOR_SYSTEM_PROMPT)
                            tools: ask_clarification, update_prefs,
                                   sourcing_agent_tool, sommelier_agent_tool, menu_architect_tool
                                     │ (각 specialist = isolated ReAct sub-graph)
                  ┌──────────────────┼─────────────────────────┐
       sourcing_agent           sommelier_agent           menu_architect
       6 store + maps           pairing + grounding        food→음료 메뉴 + sourcing 호출
```
핵심 파일: `agent.py`(그래프), `agent_tools.py`(@tool 래퍼+그룹), `agents/react_subagent.py`(공용 빌더),
`agents/{sourcing,sommelier,menu_architect}.py`, `prompts.py`(SUPERVISOR/specialist 프롬프트는 일부 specialist 파일에 인라인),
`tools/google_search_tool.py`, `tools/google_maps_tool.py`, `vision.py`(food_menu).
