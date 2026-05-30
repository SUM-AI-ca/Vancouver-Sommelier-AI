# Vision Node 설계

> **목적**: 사용자가 올린 **와인 라벨 사진** 또는 **레스토랑 와인 리스트 사진**을
> multimodal model로 스캔·분석해서, 기존 BC Wine Agent의 검색/추천 흐름에
> 연결하는 `vision_node`를 추가한다.
>
> **상태: ✅ 구현 완료 (B안).** PJ의 §13 결정을 반영해 구현했다. 아래 본문은
> 이제 "as-built" 스펙이다. 실제 변경된 파일과 확인 방법은 §14에 정리.

---

## 1. 두 가지 Use Case

| | **A. 와인 라벨 스캔** | **B. 레스토랑 와인 리스트 스캔** |
|---|---|---|
| 입력 | 병 라벨 사진 1장 | 와인 리스트(메뉴) 사진 1~2장 |
| 추출 결과 | 와인 **1종**의 정체성 | 와인 **N종**의 목록 |
| 핵심 필드 | producer, wine name, varietal, vintage, region, ABV | 줄별 raw text, 와인명, 가격, 잔/병 여부, 섹션 |
| 사용자 의도 | "이 와인 어때? 평점/가격/살 곳" | "이 중에 뭐 시킬까 / 가성비 / 내 음식이랑" |
| 후속 동작 | 기존 tool로 그 1종 조회 (리뷰·가격·재고) | 리스트에서 **선별**해 조회 → 비교/추천 |

→ B가 사실상 킬러 기능. "지금 식당인데 이 리스트 중 뭐 골라?"는 모바일 카메라
사용 시나리오라서, **프론트엔드 카메라 캡처(모바일 후면)**가 중요 (§9).

---

## 2. 현재 아키텍처에서 건드려야 할 곳

지금 시스템은 **텍스트 전용**이다. 이미지가 들어올 자리가 없음.

```
[현재]
app.py    ChatRequest { thread_id, message: str }       ← 이미지 필드 없음
app.py    inputs = {"messages": [("user", req.message)]} ← 평문 문자열만
agent.py  START → orchestrator → (tools → orchestrator)* → END
models.py Gemini 3.5 Flash (이미 multimodal ✅ — 모델 교체 불필요)
```

바꿔야 하는 지점 (구현 변경 맵):

| 파일 | 변경 | 이유 |
|---|---|---|
| `static/` (app.js, index.html) | 이미지 첨부 UI + base64 인코딩 | 이미지 입력 경로 |
| `app.py` `ChatRequest` | `images: list[str] \| None` 추가 | 이미지 수신 |
| `app.py` `chat()` | 멀티모달 `HumanMessage` 구성 | 텍스트+이미지 동시 전달 |
| `app.py` 검증 게이트 | 이미지 있으면 우회 | `validate_query`는 텍스트만 봄 (§8) |
| `agent.py` `build_graph()` | `vision_node` + 조건부 진입 라우터 | 핵심 |
| `agent.py` `_filter_previous_turns` | 과거 턴 이미지 strip | 토큰 비용 (§7) |
| `prompts.py` | vision 추출 프롬프트 + orchestrator에 G7 추가 | 환각 방지·후속 동작 |
| `state.py` | (선택) 추출 결과 저장 필드 | 디버깅/프론트 표시용 |
| `models.py` | (선택) `with_structured_output` 헬퍼 | 구조화 추출 |

---

## 3. 아키텍처 결정: vision을 어디에 넣나 — ✅ **B안으로 확정 (결정 #1)**

세 가지 안을 검토하고 **B안(전용 노드 + 구조화 추출)으로 확정**해 구현했다.

### A안 — orchestrator를 그냥 멀티모달로
이미지를 orchestrator의 `HumanMessage`에 그대로 실어 보내고, orchestrator가
직접 보고 tool을 호출.
- ➕ 가장 단순. 새 노드 없음.
- ➖ orchestrator 프롬프트가 이미 매우 큼(prompts.py) → 거기에 "이미지 읽는 법"까지
  얹으면 부담. 추출 결과가 구조화되지 않아 감사/표시 어려움. 환각 통제 약함.

### B안 — 전용 `vision_node` + 구조화 추출 ✅ 추천
이미지가 있으면 **orchestrator 이전에** `vision_node`가 먼저 돌아서,
Pydantic 스키마로 **보이는 텍스트만** 구조화 추출 → 그 결과를 메시지로 주입 →
orchestrator는 평소처럼 텍스트 기반으로 기존 tool 호출.
- ➕ 관심사 분리: "이미지에 뭐가 있나"(vision) vs "그래서 뭘 하나"(orchestrator).
- ➕ 구조화 출력 → app.py의 결과 드롭다운 UI 패턴에 그대로 표시 가능.
- ➕ 환각 통제를 추출 프롬프트에 집중. orchestrator 프롬프트는 거의 그대로.
- ➕ 사용자가 말한 "vision node"와 정확히 일치.
- ➖ LLM 1라운드 추가(지연·비용). → 이미지 있을 때만 도니까 평소엔 0.

### C안 — vision을 tool로
`analyze_wine_image_tool`을 만들어 orchestrator가 호출.
- ➖ **구조적 문제**: LangGraph `ToolNode`는 tool_call의 문자열 args만 넘김.
  이미지는 args에 넣기엔 큼/지저분. state를 거쳐 전달해야 하는데 ToolNode 기본
  동작과 안 맞음. → 채택 안 함.

> **확정 = B안.** 아래 §4~§6은 B안 기준 as-built.

---

## 4. Graph 설계 (B안)

```
[변경 후]
        ┌─ (이미지 있음) ─→ vision_node ─┐
START ─ entry_router                     ├─→ orchestrator ─→ (tools → orchestrator)* ─→ END
        └─ (이미지 없음) ────────────────┘
```

- **`entry_router`** (conditional entry point): 최신 `HumanMessage`의 content에
  이미지 파트가 있으면 `"vision"`, 없으면 `"orchestrator"` 반환.
- **`vision_node`**: 이미지 추출 → 구조화 결과를 메시지로 state에 추가 →
  엣지로 `orchestrator`.
- 나머지 루프(orchestrator ↔ tools)는 **그대로**.

`agent.py` 골격 (의사코드):

```python
def _latest_human_has_image(messages) -> bool:
    for m in reversed(messages):
        if isinstance(m, HumanMessage):
            c = m.content
            return isinstance(c, list) and any(
                isinstance(p, dict) and p.get("type") in ("image_url", "image")
                for p in c
            )
    return False

def entry_router(state: AgentState) -> str:
    return "vision" if _latest_human_has_image(state["messages"]) else "orchestrator"

def build_graph(checkpointer=None):
    builder = StateGraph(AgentState)
    builder.add_node("vision", vision_node)
    builder.add_node("orchestrator", orchestrator_node)
    builder.add_node("tools", tool_node_with_logging)

    builder.set_conditional_entry_point(entry_router, {
        "vision": "vision",
        "orchestrator": "orchestrator",
    })
    builder.add_edge("vision", "orchestrator")
    builder.add_conditional_edges("orchestrator", should_continue, {
        "tools": "tools", "end": END,
    })
    builder.add_edge("tools", "orchestrator")
    return builder.compile(checkpointer=checkpointer)
```

---

## 5. `vision_node` 동작 + 추출 스키마

### 5.1 동작 (as-built: `agent.vision_node`)
1. 최신 `HumanMessage`에서 이미지 파트(들)와 사용자 텍스트를 꺼낸다.
2. `get_llm(temperature=0)`을 `with_structured_output(VisionExtraction)`으로 호출 —
   라벨 vs 리스트 자동 분류 + 필드 추출. 실패해도 `other`로 graceful degrade.
3. `format_extraction`으로 **무손실 텍스트**로 변환.
4. (토큰 최적화) **같은 id로 `HumanMessage`를 교체** — 이미지 파트를 버리고
   content를 `원본 텍스트 + "\n\n[Image analysis — vision]\n" + 추출 텍스트`로 둔다.
   추출을 user 턴에 fold하므로 멀티턴 후속질문("두 번째 거 더 알려줘")에서도 정보가
   살아남는다(§7). orchestrator는 이 시점부터 text-only로 동작.
5. `vision_extractions`(추출 dict)를 state에 같이 반환 → 프론트 뱃지용(§9).

### 5.2 Pydantic 스키마 (제안)

```python
from typing import Literal
from pydantic import BaseModel, Field

class WineLabelExtraction(BaseModel):
    producer:  str | None = None     # 와이너리/생산자
    wine_name: str | None = None     # 큐베/제품명
    varietal:  str | None = None     # 품종 (또는 블렌드)
    vintage:   str | None = None     # "2019" 또는 "NV" — 문자열 유지
    region:    str | None = None
    country:   str | None = None
    abv:       str | None = None     # "13.5%"
    legible:   bool = True           # 라벨이 읽을 만한가
    other_text: list[str] = []       # 분류 안 된 라벨 텍스트 그대로

class WineListItem(BaseModel):
    raw_text:     str                # 줄에 인쇄된 그대로 (검증용 닻)
    wine_name:    str | None = None
    producer:     str | None = None
    varietal:     str | None = None
    vintage:      str | None = None
    region:       str | None = None
    price:        str | None = None  # "$14 / $58" 등 인쇄 그대로
    by_the_glass: bool | None = None
    section:      str | None = None  # "Reds", "By the Glass", "Sparkling"...

class WineListExtraction(BaseModel):
    items: list[WineListItem] = []

class VisionExtraction(BaseModel):
    document_type: Literal["label", "wine_list", "other"]
    label:     WineLabelExtraction | None = None
    wine_list: WineListExtraction | None = None
    notes:     str | None = None     # "왼쪽 하단 잘림 / 흐림" 등 품질 메모
```

> `vintage`를 int 아닌 **str**로 둔 이유: "NV"(Non-Vintage), 안 보임(null),
> 잘못 읽은 4자리 방지. ✅ 동의(결정 #2).

---

## 6. 프롬프트 설계

### 6.1 Vision 추출 프롬프트 (환각 방지가 핵심) — prompts.py에 신규
요지:
- **보이는 것만 옮겨라.** 안 보이거나 안 읽히면 해당 필드 `null`. 추측 금지.
- producer/vintage를 부분 텍스트로 **추론하지 마라** (예: "Reserve"만 보고 생산자 짓지 말기).
- 와인 리스트면 각 줄 `raw_text`를 **인쇄된 그대로** 복사 (이게 환각 검증 닻).
- 가격은 통화기호·잔/병 표기 포함 인쇄 그대로.
- 와인 문서가 아니면 `document_type="other"`.
- 품질 문제(흐림·잘림·손글씨)는 `notes`에.

이건 C1("Never invent")의 vision 버전. orchestrator의 C1과 정합.

### 6.2 Orchestrator 프롬프트에 가이드라인 추가 (G7) — ✅ 구현됨 (prompts.py)
vision_node가 user 턴에 접어 넣은 `[Image analysis — vision]` 블록을 받았을 때:
- **라벨**: 그 1종을 기존 tool(리뷰·가격·재고)로 조회 → 평소대로 답.
  추출이 빈약하거나 `legible=false`면 읽은 것만 말하고 확인/재촬영 요청(G6).
- **리스트**: 리스트의 와인을 **전부 조회**(와인당 1콜씩 G1 병렬). 결정 #3 반영 —
  사용자가 명시적으로 좁히지 않는 한(예: "레드만", "$80 이하") 미리 선별하지 않음.
  단 C3 budget(≤5라운드·≤20콜)은 그대로 적용되므로, 리스트가 budget보다 크면 커버
  가능한 만큼(사용자 의도=가성비/페어링/스타일 우선) 조회하고 "M개 중 N개 봤다"고
  알린다. 이후 가성비·평점·음식 적합도로 비교. **각 줄의 인쇄 가격 = 그 식당 가격,
  tool 가격 = 소매 참고용.**
- `document_type="other"` → 와인 이미지가 아니라고 정중히 안내(G5 톤). tool 안 씀.

---

## 7. 멀티턴 / 토큰 비용 (⚠️ 놓치기 쉬움)

- 이미지(특히 고해상 와인 리스트)는 토큰 많이 먹음. **과거 턴 이미지가 다음 턴
  context에 계속 남으면** 비용 폭증.
- ✅ **해결 방식(결정 #4):** vision_node가 추출 직후 원본 `HumanMessage`를 **같은 id로
  교체**한다 — 이미지 파트를 버리고 `원본 텍스트 + [Image analysis — vision] 추출
  텍스트`만 남김. LangGraph `add_messages`는 동일 id 메시지를 교체하므로, 이 한 번의
  치환이 **현재 턴(orchestrator는 이미 text-only로 동작)과 미래 턴(체크포인트에 이미
  text-only로 저장됨)** 둘 다 커버한다.
- 그 결과 `_filter_previous_turns`(agent.py)는 **수정 불필요** — vision_node를 지난
  시점부터 이미지는 더 이상 존재하지 않아 자연히 텍스트만 다음 턴으로 넘어간다.
  ("이미지→text 정보 + 질문 + 답변만 가져온다"는 #4 요구를 정확히 충족.)

---

## 8. 입력 / 검증 / 이미지 포맷

- **전달 형식**: 프론트가 base64 data URL(`data:image/jpeg;base64,...`)로 인코딩해
  `ChatRequest.images`로 전송. `app.py`에서 멀티모달 `HumanMessage` 구성:
  ```python
  content = [{"type": "text", "text": req.message or "이 와인 분석해줘"}]
  for url in (req.images or []):
      content.append({"type": "image_url", "image_url": {"url": url}})
  inputs = {"messages": [HumanMessage(content=content)]}
  ```
  ✅ 채택 포맷: `{"type": "image_url", "image_url": {"url": "data:..."}}`
  (`vision.extract_vision`, `app.py` 둘 다 이 형태로 구성).
- **검증 게이트**: `validate_query`(app.py)는 텍스트만 봄. 이미지만 오고 텍스트가
  비거나 "분석해줘" 수준이면 오탐 가능 → ✅ **이미지 첨부 시 검증 우회** 구현
  (`if not is_resume and not req.images:`). 와인 여부는 vision_node의 `document_type`로
  판단(=="other"면 orchestrator가 G7대로 정중히 거절).
- **해상도 정책(결정 #5)**: ✅ 클라이언트에서 **긴 변 ≤ 2048px**로 다운스케일 후
  **JPEG(q=0.85)로 재인코딩** — 라벨/리스트 공통 단일 정책(와인 리스트 작은 글자
  가독성 위해 1568이 아닌 2048 채택). 구현: `static/app.js` `downscaleToDataUrl`
  (`MAX_DIM=2048`, canvas `toDataURL("image/jpeg", 0.85)`).
- **HEIC(결정 #5)**: ✅ 캔버스가 디코딩 가능하면(iOS Safari는 네이티브 디코딩) 그대로
  JPEG로 재인코딩되어 자동 변환. 디코딩 불가(데스크톱 Chrome/Firefox)면 `img.onerror`
  →친절한 안내 alert("JPEG/PNG로 다시 시도"). 별도 라이브러리 없음.
- **장수(결정 #6)**: ✅ 한 턴 **최대 3장**. 프론트(`MAX_IMAGES=3`)와 백엔드
  (`app.py MAX_IMAGES=3`, `req.images[:MAX_IMAGES]`) 양쪽에서 캡.

---

## 9. 프론트엔드 (static/)

- 입력 수단: ✅ 파일 선택 버튼(📷 아이콘) + 드래그드롭 + 클립보드 붙여넣기.
  파일 입력은 `accept="image/*" multiple`. **`capture="environment"`는 일부러 뺐다** —
  모바일에서 capture를 붙이면 카메라 전용으로 강제되어 갤러리 선택이 막힌다. 빼두면
  OS가 "사진 촬영 / 사진 보관함" 선택지를 모두 띄워줘서 식당 카메라 시나리오도 그대로
  커버되고 더 유연하다.
- ✅ 첨부 후 **썸네일 스트립**(`#chat-attachments`) + 개별 제거(×) 버튼.
- ✅ base64 data-URL로 `ChatRequest.images`에 실어 전송. 보낸 메시지 버블에도 썸네일
  표시(`.chat-msg-thumbs`).
- **상태 표시(결정 #7)**: ✅ 백엔드가 `vision_start`/`vision_result` SSE 이벤트 발행
  (app.py 스트림 루프). 프론트는 기존 tool-badge UI를 재사용해 "Image analysis" 뱃지를
  열고("Analyzing image" 상태), 추출 요약을 펼침 패널로 채운다. 노드 진입은
  `metadata.langgraph_node=="vision"`로 견고하게 감지하고, 종료 후 state 폴백으로 뱃지가
  반드시 닫히게 했다.
- 스트리밍 누수: vision_node 출력은 orchestrator가 아니므로 app.py의
  `node != "orchestrator"` skip 필터가 이미 막아줌 ✅. (게다가 structured_output은
  토큰 스트리밍 안 할 가능성 큼.)

---

## 10. Edge Cases / 실패 모드

| 상황 | 처리 |
|---|---|
| 흐림/잘림/저화질 | `notes`에 기록, `legible=false` → orchestrator가 확인 질문 |
| 와인 아닌 사진 | `document_type="other"` → 정중히 안내 |
| 외국어 라벨(불/이/독) | 원어 그대로 전사 (와인명은 어차피 라틴문자 유지 정책) |
| 손글씨 와인 리스트 | 추출하되 신뢰도 낮음 표시 |
| 부분 라벨(절반만) | 보이는 필드만, 나머지 null |
| 이미지 0장인데 vision 진입 | entry_router가 애초에 막음 |
| 텍스트 없이 이미지만 | 기본 프롬프트 "이 와인 분석해줘" 주입 |
| 추출은 됐는데 tool 결과 0건 | 기존 fallback 체인(C2/G6)대로 |

---

## 11. 비용 / 지연

- 이미지 있을 때만 vision LLM 1라운드 추가. 없으면 기존과 동일(0 오버헤드).
- 와인 리스트 다건 조회는 tool budget(5라운드·20콜)로 캡 → orchestrator가
  선별(§6.2). N=30짜리 리스트를 전부 조회하는 일은 없도록.
- 고해상 이미지 = 토큰 ↑. §8 다운스케일 + §7 과거턴 strip으로 통제.

---

## 12. 테스트 / Eval

- 이미지 골든 테스트: ❌ **안 함(결정 #8).** 샘플 사진 없음.
- 대신 ✅ `vision.py`에 **오프라인 스모크 테스트**(`if __name__ == "__main__"`) 추가 —
  LLM/크리덴셜 없이 `format_extraction`(라벨/리스트/other)과 이미지 파트 헬퍼를 검증.
  `python vision.py`로 즉시 확인 가능.
- **PJ 정책**: API를 때리는 테스트/eval 스크립트는 PJ가 직접 돌림 → 나는 파일만
  완성하고 실행법만 안내. (기존 합의)

---

## 13. 리뷰 체크리스트 — 여기만 답해줘도 구현 시작 가능 ✅

1. **아키텍처**(§3): B안(전용 vision_node) 가는 거 맞지? go with B
2. **추출 스키마**(§5.2): 필드 추가/삭제할 것? `vintage`=str 동의? agree
3. **리스트 N건 선별 전략**(§6.2): 기본 동작 이대로? 다른 우선순위 원해? 괜찮아 다 조회해.
4. **토큰 최적화**(§7): 과거턴 이미지 strip + 같은-id 치환 둘 다 넣을까? 최적화 시켜야지. 굳이 과거턴에 넣은 이미지를 현재턴에 가져올필요없어. 그냥 이미지를 text로 바뀐 정보 + 질문 + 답변만 가져오면 돼.
5. **해상도 정책**(§8): 라벨/리스트 다운스케일 px, HEIC 지원 여부.
   → ✅ 긴 변 ≤2048px JPEG 재인코딩, HEIC는 캔버스 디코딩 가능 시 자동변환·불가 시 안내.
6. **이미지 장수 상한**(§8). 한번 질문할때 3장으로 제한해
7. **프론트 상태 표시**(§9): 노드 이벤트 vs 클라이언트 인디케이터.
   → ✅ 백엔드 `vision_start`/`vision_result` SSE 이벤트 + 프론트 인디케이터(둘 다).
8. **이미지 골든 테스트**(§12): 추가할까? 샘플 사진 줄 수 있어? no
9. 그 외 라벨/리스트에서 **꼭 뽑아야 하는 필드** 빠진 거 있나? 그냥 정보 다 뽑아서 괜히 format화 시켜서 정보 오염시키지말고, 모든 정보 뽑아서 잘 정리해서 넘겨.
   → ✅ 무손실 추출로 반영: 라벨엔 `other_text`, 리스트 항목엔 verbatim `raw_text`
   catch-all을 둬서 named field에 안 맞는 텍스트도 안 버린다. 프롬프트도 "보이는 건
   전부 옮기되 normalize/translate/재정렬 금지(=오염 금지)"로 명시. orchestrator로
   넘기는 텍스트는 모든 필드를 빠짐없이 정돈해 전달(§5.2 / format_extraction).

> ✅ 결정 전부 반영 완료. 아래 §14가 실제 구현 결과(as-built).

---

## 14. As-built — 실제 변경 파일 & 확인 방법

### 14.1 변경/신규 파일
| 파일 | 내용 |
|---|---|
| `vision.py` **(신규)** | `VisionExtraction` 등 스키마, `extract_vision`(멀티모달 structured output, 실패 시 graceful), `format_extraction`(무손실 텍스트), 이미지 파트 헬퍼, 오프라인 스모크 테스트 |
| `prompts.py` | `VISION_EXTRACTION_PROMPT`(환각방지·무손실) 신규, `ORCHESTRATOR_SYSTEM_PROMPT`에 **G7** 추가 |
| `agent.py` | `vision_node`, `entry_router`, vision 헬퍼 import, `build_graph` 조건부 진입점으로 재배선 |
| `state.py` | `AgentState`에 `vision_extractions` 필드 |
| `app.py` | `ChatRequest.images`, `MAX_IMAGES=3`, 멀티모달 `HumanMessage`(고정 id), 이미지 시 검증 우회, `vision_start`/`vision_result` SSE + 종료 후 폴백, `_summarize_vision` |
| `static/index.html` | 📷 첨부 버튼 + 숨김 `file` 입력 + 썸네일 스트립 |
| `static/app.js` | 다운스케일(`MAX_DIM=2048`)·썸네일·제거·붙여넣기·드래그드롭, 이미지 동봉 전송, 이미지-only 전송 허용, `vision_start`/`vision_result` 처리 |
| `static/styles.css` | 첨부 버튼/썸네일/제거버튼/드롭 하이라이트 스타일 |

### 14.2 흐름 (이미지 첨부 턴)
```
프론트: 사진 첨부 → 2048px JPEG 재인코딩 → data-URL 배열로 POST /api/chat
app.py: 검증 우회 → 멀티모달 HumanMessage(id 고정) 입력
graph:  entry_router → "vision" → vision_node
        ├ extract_vision: Gemini structured output로 보이는 것만 추출
        ├ format_extraction: 무손실 텍스트
        └ 같은 id로 HumanMessage 교체(이미지 strip, 추출 텍스트 fold)  ← 토큰 최적화
        → orchestrator (이제 text-only) → 기존 tool로 조회/비교 → 답변 스트리밍
SSE:    vision_start → (tool_start/tool_end)* → token* → done
```

### 14.3 확인 방법
- **백엔드 문법**: `python -m py_compile vision.py agent.py app.py state.py prompts.py` (통과 확인됨)
- **오프라인 포맷터/헬퍼**: `python vision.py` → 라벨/리스트/other 출력 + `helper asserts: OK` (통과 확인됨)
- **JS 문법**: `node --check static/app.js` (통과 확인됨)
- **수동 E2E (PJ)**: 앱 실행(`uvicorn app:app --reload`) → 챗 열고 와인 라벨/리스트 사진
  첨부 → "Image analysis" 뱃지 펼쳐 추출 결과 확인 → 답변에 가격/평점/추천 반영 확인.
  비와인 사진 → 정중한 거절. 모바일에서 첨부 버튼 → 카메라/갤러리 선택 확인.

### 14.4 알려진 한계 / 후속 후보
- 클래리피케이션 **interrupt 재개 중 첨부**한 이미지는 무시됨(resume은 텍스트만). 드문
  케이스라 보류 — 필요하면 재개 경로에도 이미지 주입 추가.
- `with_structured_output` + 멀티모달이 설치된 `langchain-google-genai` 버전에서 실제로
  잘 도는지는 **실 호출 1회로 확인 필요**(실패해도 `extract_vision`가 `other`로 graceful
  degrade하므로 턴은 안 죽음).
- HEIC를 데스크톱에서 첨부하면 변환 실패 안내만 뜸(서버측 변환은 미도입).
