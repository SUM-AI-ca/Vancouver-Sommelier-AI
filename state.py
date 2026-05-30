"""AgentState for the BC Wine AI Agent."""

from typing import Annotated, NotRequired, TypedDict

from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages


class AgentState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]
    tool_call_log: NotRequired[list[dict]]
    # Last vision_node extraction(s) this turn, as dicts. Surfaced to the
    # frontend (vision_result SSE) so the UI can show what the image read.
    vision_extractions: NotRequired[list[dict]]
