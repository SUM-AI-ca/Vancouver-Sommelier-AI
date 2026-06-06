"""Vision extraction for Vancouver Drinks AI.

A multimodal Gemini pass that reads an attached photo — a single wine **label** or a
restaurant **wine list** — and transcribes what is printed into a structured record
(`VisionExtraction`). The `vision_node` in agent.py calls `extract_vision`, then folds
`format_extraction` text into the user turn so the (text-only) orchestrator can search
and recommend with its existing tools.

Design notes live in docs/VISION_NODE_DESIGN.md. Two rules drive the schema:
  1. Never invent — every field is optional; unknown/illegible ⇒ null.
  2. Never lose info — verbatim catch-alls (`other_text`, each item's `raw_text`)
     guarantee that anything visible survives even if it doesn't fit a named field.
"""

import asyncio
import json
import logging
from typing import Literal

from langchain_core.messages import BaseMessage, HumanMessage, SystemMessage
from pydantic import BaseModel, Field

from models import get_llm
from prompts import VISION_EXTRACTION_PROMPT

log = logging.getLogger(__name__)


# ── Extraction schema ────────────────────────────────────────────────

class DrinkLabelExtraction(BaseModel):
    category: str | None = Field(None, description="Drink category: wine, beer, spirits, cider, sake, etc.")
    producer: str | None = Field(None, description="Producer / winery / brewery / distillery, as printed.")
    product_name: str | None = Field(None, description="Product / cuvée / brand name, as printed.")
    style: str | None = Field(None, description="Grape variety, beer style, spirit type, etc., as printed.")
    vintage: str | None = Field(None, description='Year as a string, or "NV". Null if absent.')
    region: str | None = Field(None, description="Region / appellation, as printed.")
    country: str | None = None
    abv: str | None = Field(None, description='Alcohol, as printed (e.g. "13.5%").')
    volume: str | None = Field(None, description='Volume as printed (e.g. "750ml", "355ml").')
    legible: bool = Field(True, description="False when the label is too blurry/cropped to read reliably.")
    other_text: list[str] = Field(
        default_factory=list,
        description="Any other visible label text not captured above — verbatim. Loss-less catch-all.",
    )


class DrinkListItem(BaseModel):
    raw_text: str = Field(description="The line copied EXACTLY as printed. The verbatim anchor.")
    product_name: str | None = None
    producer: str | None = None
    style: str | None = Field(None, description="Grape variety, beer style, spirit type, cocktail name, etc.")
    vintage: str | None = None
    region: str | None = None
    price: str | None = Field(None, description='Price exactly as printed, incl. currency / glass-bottle split (e.g. "14 / 58").')
    by_the_glass: bool | None = None
    section: str | None = Field(None, description='Menu section heading (e.g. "Reds", "By the Glass", "Draft Beer", "Cocktails").')
    category: str | None = Field(None, description="wine, beer, spirits, cocktail, cider, sake, etc.")


class DrinkListExtraction(BaseModel):
    items: list[DrinkListItem] = Field(default_factory=list)


class FoodMenuItem(BaseModel):
    raw_text: str = Field(description="The dish line copied EXACTLY as printed. The verbatim anchor.")
    dish_name: str | None = None
    description: str | None = Field(None, description="Printed description / key ingredients, as shown.")
    price: str | None = Field(None, description="Price exactly as printed, incl. currency.")
    section: str | None = Field(None, description='Menu section / course (e.g. "Starters", "Mains", "Desserts").')


class FoodMenuExtraction(BaseModel):
    items: list[FoodMenuItem] = Field(default_factory=list)
    cuisine: str | None = Field(None, description="Overall cuisine / style if evident (e.g. Italian, Korean BBQ).")


class VisionExtraction(BaseModel):
    document_type: Literal["label", "drink_list", "food_menu", "other"]
    label: DrinkLabelExtraction | None = None
    drink_list: DrinkListExtraction | None = None
    food_menu: FoodMenuExtraction | None = None
    notes: str | None = Field(None, description="Image quality issues: blur, crop, glare, handwriting, etc.")


# ── HumanMessage image helpers ───────────────────────────────────────

_IMAGE_PART_TYPES = ("image_url", "image")


def latest_human_message(messages: list[BaseMessage]) -> HumanMessage | None:
    for m in reversed(messages):
        if isinstance(m, HumanMessage):
            return m
    return None


def _image_url_from_part(part: dict) -> str | None:
    """Pull the data-URL/url out of a content part, tolerating both the
    {"image_url": {"url": ...}} and {"image_url": "..."} shapes."""
    img = part.get("image_url")
    if isinstance(img, dict):
        url = img.get("url")
        return url if isinstance(url, str) else None
    if isinstance(img, str):
        return img
    return None


def message_has_image(msg: BaseMessage | None) -> bool:
    if msg is None:
        return False
    content = getattr(msg, "content", None)
    return isinstance(content, list) and any(
        isinstance(p, dict) and p.get("type") in _IMAGE_PART_TYPES for p in content
    )


def extract_image_urls(msg: BaseMessage) -> list[str]:
    content = getattr(msg, "content", None)
    if not isinstance(content, list):
        return []
    urls: list[str] = []
    for p in content:
        if isinstance(p, dict) and p.get("type") in _IMAGE_PART_TYPES:
            url = _image_url_from_part(p)
            if url:
                urls.append(url)
    return urls


def extract_text(msg: BaseMessage) -> str:
    """Flatten the text parts of a (possibly multimodal) message into a string."""
    content = getattr(msg, "content", "")
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        parts = []
        for p in content:
            if isinstance(p, dict) and p.get("type") == "text":
                t = p.get("text")
                if isinstance(t, str):
                    parts.append(t)
            elif isinstance(p, str):
                parts.append(p)
        return " ".join(parts).strip()
    return ""


# ── Extraction ───────────────────────────────────────────────────────

def _parse_raw_to_extraction(raw_content) -> VisionExtraction | None:
    """Best-effort parse of raw LLM text into VisionExtraction.

    Gemini's function-calling mode sometimes produces a valid JSON body that the
    automatic Pydantic parser rejects (e.g. food_menu with many items). This
    fallback manually extracts the JSON and validates it.
    """
    text = raw_content
    if not isinstance(text, str):
        if isinstance(text, list):
            text = "".join(
                p.get("text", "") if isinstance(p, dict) else str(p) for p in text
            )
        else:
            return None
    text = text.strip()
    if not text:
        return None
    # Strip markdown fences if present
    if text.startswith("```"):
        text = text.split("\n", 1)[-1].rsplit("```", 1)[0].strip()
    try:
        data = json.loads(text)
    except (json.JSONDecodeError, TypeError):
        return None
    if isinstance(data, dict):
        try:
            return VisionExtraction.model_validate(data)
        except Exception:  # noqa: BLE001
            pass
    return None


_VISION_TIMEOUT = 45.0

_JSON_FALLBACK_SUFFIX = """

## Output format
Return your answer as a SINGLE JSON object (no markdown fences, no commentary).
Schema: {"document_type": "label"|"wine_list"|"food_menu"|"other", "label": {...}|null, "wine_list": {"items":[...]}|null, "food_menu": {"items":[...], "cuisine":...|null}|null, "notes":...|null}
"""


async def extract_vision(image_urls: list[str], user_text: str = "") -> VisionExtraction:
    """Run the multimodal extraction pass over one or more image data-URLs.

    Returns a VisionExtraction. On any failure, degrades to document_type="other"
    with a note so the graph keeps moving (the orchestrator handles "other").
    """
    if not image_urls:
        return VisionExtraction(document_type="other", notes="No image found in the message.")

    user_hint = user_text.strip()
    preamble = (
        "Transcribe the attached image(s) into the structured schema."
        + (f' The user also wrote: "{user_hint}".' if user_hint else "")
    )
    parts: list[dict] = [{"type": "text", "text": preamble}]
    for url in image_urls:
        parts.append({"type": "image_url", "image_url": {"url": url}})

    messages = [
        SystemMessage(content=VISION_EXTRACTION_PROMPT),
        HumanMessage(content=parts),
    ]

    # Fast path: function-calling structured output (reliable for labels).
    try:
        llm = get_llm(temperature=0.0).with_structured_output(VisionExtraction)
        result = await asyncio.wait_for(llm.ainvoke(messages), timeout=_VISION_TIMEOUT)
        if isinstance(result, VisionExtraction):
            return result
    except asyncio.TimeoutError:
        log.warning("vision: structured output timed out after %ss", _VISION_TIMEOUT)
    except Exception as e:  # noqa: BLE001
        log.warning("vision: structured output failed (%s: %s)", type(e).__name__, e)

    # Fallback: plain LLM call + manual JSON parsing. Complex schemas
    # (food_menu with many items) can fail function-calling but succeed
    # when Gemini outputs free-form JSON.
    try:
        raw_messages = [
            SystemMessage(content=VISION_EXTRACTION_PROMPT + _JSON_FALLBACK_SUFFIX),
            HumanMessage(content=parts),
        ]
        llm_raw = get_llm(temperature=0.0)
        response = await asyncio.wait_for(llm_raw.ainvoke(raw_messages), timeout=_VISION_TIMEOUT)
        fallback = _parse_raw_to_extraction(response.content)
        if fallback is not None:
            log.info("vision: used raw-content fallback parsing")
            return fallback
        log.warning("vision: raw fallback returned unparseable content")
    except asyncio.TimeoutError:
        log.warning("vision: raw fallback timed out after %ss", _VISION_TIMEOUT)
    except Exception as e:  # noqa: BLE001
        log.warning("vision: raw fallback also failed (%s: %s)", type(e).__name__, e)

    return VisionExtraction(document_type="other", notes="Image extraction parsing failed.")


# ── Formatting for the orchestrator ──────────────────────────────────

def _kv_lines(pairs: list[tuple[str, str | None]]) -> list[str]:
    return [f"- {label}: {value}" for label, value in pairs if value]


def format_extraction(extraction: VisionExtraction) -> str:
    """Render the extraction as a complete, well-organized text block for the
    orchestrator. Loss-less: every captured field is surfaced; nothing invented."""
    dt = extraction.document_type

    if dt == "label" and extraction.label is not None:
        lab = extraction.label
        cat = lab.category or "drink"
        lines = [f"Document type: {cat} label (one product)."]
        lines += _kv_lines([
            ("Category", lab.category),
            ("Producer", lab.producer),
            ("Product name", lab.product_name),
            ("Style", lab.style),
            ("Vintage", lab.vintage),
            ("Region", lab.region),
            ("Country", lab.country),
            ("ABV", lab.abv),
            ("Volume", lab.volume),
        ])
        if not lab.legible:
            lines.append("- Legibility: LOW — read with caution, ask the user to confirm.")
        if lab.other_text:
            lines.append("- Other text on label: " + " | ".join(lab.other_text))
        if extraction.notes:
            lines.append(f"- Image notes: {extraction.notes}")
        if len(lines) == 1:
            lines.append("- (No label text could be read.)")
        return "\n".join(lines)

    if dt == "drink_list" and extraction.drink_list is not None:
        items = extraction.drink_list.items
        lines = [f"Document type: drink list / menu ({len(items)} items extracted)."]
        if extraction.notes:
            lines.append(f"Image notes: {extraction.notes}")
        for i, it in enumerate(items, 1):
            head = f"{i}. {it.raw_text}".rstrip()
            lines.append(head)
            detail = _kv_lines([
                ("category", it.category),
                ("producer", it.producer),
                ("product", it.product_name),
                ("style", it.style),
                ("vintage", it.vintage),
                ("region", it.region),
                ("price", it.price),
                ("section", it.section),
            ])
            if it.by_the_glass is True:
                detail.append("- by the glass")
            lines += ["  " + d for d in detail]
        if not items:
            lines.append("(No drinks could be read from the list.)")
        return "\n".join(lines)

    if dt == "food_menu" and extraction.food_menu is not None:
        fm = extraction.food_menu
        items = fm.items
        lines = [f"Document type: food menu ({len(items)} dishes extracted)."]
        if fm.cuisine:
            lines.append(f"Cuisine: {fm.cuisine}")
        if extraction.notes:
            lines.append(f"Image notes: {extraction.notes}")
        for i, it in enumerate(items, 1):
            lines.append(f"{i}. {it.raw_text}".rstrip())
            detail = _kv_lines([
                ("dish", it.dish_name),
                ("description", it.description),
                ("price", it.price),
                ("section", it.section),
            ])
            lines += ["  " + d for d in detail]
        if not items:
            lines.append("(No dishes could be read from the menu.)")
        return "\n".join(lines)

    # document_type == "other" (or malformed)
    note = extraction.notes or "The image does not appear to be a drink label, drink list, or food menu."
    return f"Document type: not a recognized drink/menu image.\n- {note}"


# ── Offline smoke test (no LLM / credentials) ────────────────────────

if __name__ == "__main__":
    label = VisionExtraction(
        document_type="label",
        label=DrinkLabelExtraction(
            category="wine", producer="Quails' Gate", product_name="Stewart Family Reserve",
            style="Pinot Noir", vintage="2021", region="Okanagan Valley",
            country="Canada", abv="13.5%", volume="750ml", other_text=["VQA", "BC"],
        ),
    )
    drink_list = VisionExtraction(
        document_type="drink_list",
        drink_list=DrinkListExtraction(items=[
            DrinkListItem(raw_text="Mission Hill Reserve Chardonnay 2020 — 16 / 64",
                          producer="Mission Hill", product_name="Reserve Chardonnay",
                          style="Chardonnay", vintage="2020", price="16 / 64",
                          by_the_glass=True, section="By the Glass", category="wine"),
            DrinkListItem(raw_text="33 Acres of Sunshine — 9",
                          producer="33 Acres", product_name="Sunshine",
                          style="French Blanche", price="9",
                          section="Draft Beer", category="beer"),
        ]),
        notes="lower-right corner slightly out of frame",
    )
    other = VisionExtraction(document_type="other", notes="Looks like a coffee menu.")

    for ex in (label, drink_list, other):
        print("=" * 64)
        print(format_extraction(ex))
    print("=" * 64)

    # Image-part helpers
    msg = HumanMessage(content=[
        {"type": "text", "text": "이 와인 어때?"},
        {"type": "image_url", "image_url": {"url": "data:image/jpeg;base64,AAAA"}},
    ])
    assert message_has_image(msg) is True
    assert extract_image_urls(msg) == ["data:image/jpeg;base64,AAAA"]
    assert extract_text(msg) == "이 와인 어때?"
    assert message_has_image(HumanMessage(content="plain text")) is False
    print("helper asserts: OK")
