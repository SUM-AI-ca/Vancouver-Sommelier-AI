"""Pre-agent query validation gate.

Classifies whether a user's message belongs to the BC Wine agent's scope.
On INVALID, also produces a polite rejection in the user's input language so
app.py can stream it directly without invoking the graph.
"""

from langchain_core.messages import HumanMessage, SystemMessage
from pydantic import BaseModel, Field

from models import get_llm
from prompts import VALIDATION_SYSTEM_PROMPT


class ValidationResult(BaseModel):
    is_valid: bool = Field(description="True if the query is in scope for the BC Wine agent.")
    rejection_message: str = Field(
        default="",
        description="Polite redirect in the user's language; empty when is_valid=True.",
    )


async def validate_query(message: str) -> ValidationResult:
    llm = get_llm(temperature=0.0).with_structured_output(ValidationResult)
    return await llm.ainvoke([
        SystemMessage(content=VALIDATION_SYSTEM_PROMPT),
        HumanMessage(content=message),
    ])
