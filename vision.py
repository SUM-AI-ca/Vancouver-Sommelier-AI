"""Vision extraction for the BC Wine AI Agent.

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

from typing import Literal

from langchain_core.messages import BaseMessage, HumanMessage, SystemMessage
from pydantic import BaseModel, Field

from models import get_llm
from prompts import VISION_EXTRACTION_PROMPT


# ── Extraction schema ────────────────────────────────────────────────

class WineLabelExtraction(BaseModel):
    producer: str | None = Field(None, description="Winery / producer, as printed.")
    wine_name: str | None = Field(None, description="Cuvée / product name, as printed.")
    varietal: str | None = Field(None, description="Grape variety or blend, as printed.")
    vintage: str | None = Field(None, description='Year as a string, or "NV". Null if absent.')
    region: str | None = Field(None, description="Region / appellation, as printed.")
    country: str | None = None
    abv: str | None = Field(None, description='Alcohol, as printed (e.g. "13.5%").')
    legible: bool = Field(True, description="False when the label is too blurry/cropped to read reliably.")
    other_text: list[str] = Field(
        default_factory=list,
        description="Any other visible label text not captured above — verbatim. Loss-less catch-all.",
    )


class WineListItem(BaseModel):
    raw_text: str = Field(description="The line copied EXACTLY as printed. The verbatim anchor.")
    wine_name: str | None = None
    producer: str | None = None
    varietal: str | None = None
    vintage: str | None = None
    region: str | None = None
    price: str | None = Field(None, description='Price exactly as printed, incl. currency / glass-bottle split (e.g. "14 / 58").')
    by_the_glass: bool | None = None
    section: str | None = Field(None, description='Menu section heading (e.g. "Reds", "By the Glass").')


class WineListExtraction(BaseModel):
    items: list[WineListItem] = Field(default_factory=list)


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
    document_type: Literal["label", "wine_list", "food_menu", "other"]
    label: WineLabelExtraction | None = None
    wine_list: WineListExtraction | None = None
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

async def extract_vision(image_urls: list[str], user_text: str = "") -> VisionExtraction:
    """Run the multimodal extraction pass over one or more image data-URLs.

    Returns a VisionExtraction. On any failure, degrades to document_type="other"
    with a note so the graph keeps moving (the orchestrator handles "other").
    """
    if not image_urls:
        return VisionExtraction(document_type="other", notes="No image found in the message.")

    user_hint = user_text.strip()
    preamble = (
        "Transcribe the attached wine image(s) into the structured schema."
        + (f' The user also wrote: "{user_hint}".' if user_hint else "")
    )
    parts: list[dict] = [{"type": "text", "text": preamble}]
    for url in image_urls:
        parts.append({"type": "image_url", "image_url": {"url": url}})

    llm = get_llm(temperature=0.0).with_structured_output(VisionExtraction)
    try:
        result = await llm.ainvoke([
            SystemMessage(content=VISION_EXTRACTION_PROMPT),
            HumanMessage(content=parts),
        ])
    except Exception as e:  # noqa: BLE001 — never let a vision failure kill the turn
        return VisionExtraction(
            document_type="other",
            notes=f"Image could not be analyzed ({type(e).__name__}).",
        )

    if isinstance(result, VisionExtraction):
        return result
    # Defensive: some configs return a plain dict instead of the model instance.
    if isinstance(result, dict):
        try:
            return VisionExtraction(**result)
        except Exception:  # noqa: BLE001
            pass
    return VisionExtraction(document_type="other", notes="Unrecognized extraction result.")


# ── Formatting for the orchestrator ──────────────────────────────────

def _kv_lines(pairs: list[tuple[str, str | None]]) -> list[str]:
    return [f"- {label}: {value}" for label, value in pairs if value]


def format_extraction(extraction: VisionExtraction) -> str:
    """Render the extraction as a complete, well-organized text block for the
    orchestrator. Loss-less: every captured field is surfaced; nothing invented."""
    dt = extraction.document_type

    if dt == "label" and extraction.label is not None:
        lab = extraction.label
        lines = ["Document type: wine label (one wine)."]
        lines += _kv_lines([
            ("Producer", lab.producer),
            ("Wine name", lab.wine_name),
            ("Varietal", lab.varietal),
            ("Vintage", lab.vintage),
            ("Region", lab.region),
            ("Country", lab.country),
            ("ABV", lab.abv),
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

    if dt == "wine_list" and extraction.wine_list is not None:
        items = extraction.wine_list.items
        lines = [f"Document type: wine list / menu ({len(items)} wines extracted)."]
        if extraction.notes:
            lines.append(f"Image notes: {extraction.notes}")
        for i, it in enumerate(items, 1):
            head = f"{i}. {it.raw_text}".rstrip()
            lines.append(head)
            detail = _kv_lines([
                ("producer", it.producer),
                ("wine", it.wine_name),
                ("varietal", it.varietal),
                ("vintage", it.vintage),
                ("region", it.region),
                ("price", it.price),
                ("section", it.section),
            ])
            if it.by_the_glass is True:
                detail.append("- by the glass")
            # Indent the parsed detail under its verbatim line.
            lines += ["  " + d for d in detail]
        if not items:
            lines.append("(No wines could be read from the list.)")
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
        label=WineLabelExtraction(
            producer="Quails' Gate", wine_name="Stewart Family Reserve",
            varietal="Pinot Noir", vintage="2021", region="Okanagan Valley",
            country="Canada", abv="13.5%", other_text=["VQA", "BC"],
        ),
    )
    wine_list = VisionExtraction(
        document_type="wine_list",
        wine_list=WineListExtraction(items=[
            WineListItem(raw_text="Mission Hill Reserve Chardonnay 2020 — 16 / 64",
                         producer="Mission Hill", wine_name="Reserve Chardonnay",
                         varietal="Chardonnay", vintage="2020", price="16 / 64",
                         by_the_glass=True, section="By the Glass"),
            WineListItem(raw_text="Blue Mountain Brut NV ... 78", producer="Blue Mountain",
                         vintage="NV", price="78", section="Sparkling"),
        ]),
        notes="lower-right corner slightly out of frame",
    )
    other = VisionExtraction(document_type="other", notes="Looks like a coffee menu.")

    for ex in (label, wine_list, other):
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
