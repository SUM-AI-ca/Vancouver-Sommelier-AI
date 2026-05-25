"""AgentState and related schemas for the BC Wine AI Agent."""

from typing import Annotated, NotRequired, TypedDict

from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages


class StorePrice(TypedDict):
    store: str  # "bcliquor" | "marquis" | "okanagan" | "everythingwine"
    price: float
    on_sale: bool
    in_stock: bool
    url: str | None
    stock_qty: int | None


class CriticReviewMerged(TypedDict):
    source: str  # "winealign" | "gismondi" | "robert_parker"
    critic_name: str
    score: str
    tasting_notes: str
    value_rating: int | None
    drink_window: str | None


class MergedWineRecord(TypedDict):
    normalized_key: str  # producer_slug + wine_slug + vintage
    display_name: str
    producer: str
    vintage: int | None
    grape: list[str]
    prices: list[StorePrice]
    best_price: StorePrice | None
    critic_reviews: list[CriticReviewMerged]
    avg_critic_score: float | None
    consumer_rating: float | None
    consumer_votes: int | None
    is_bc_vqa: bool
    tasting_notes_consolidated: str | None


class UserPreferences(TypedDict, total=False):
    budget_max: float
    preferred_varietals: list[str]
    sweetness: str  # "dry" | "off-dry" | "sweet"
    style: str  # "elegant" | "powerful" | "fresh"


class AgentState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]
    wine_context: NotRequired[dict[str, MergedWineRecord]]
    user_preferences: NotRequired[UserPreferences]
    last_recommendations: NotRequired[list[str]]
    tool_call_log: NotRequired[list[dict]]
