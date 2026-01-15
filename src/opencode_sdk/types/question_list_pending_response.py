# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "QuestionListPendingResponse",
    "QuestionListPendingResponseItem",
    "QuestionListPendingResponseItemQuestion",
    "QuestionListPendingResponseItemQuestionOption",
    "QuestionListPendingResponseItemTool",
]


class QuestionListPendingResponseItemQuestionOption(BaseModel):
    description: str
    """Explanation of choice"""

    label: str
    """Display text (1-5 words, concise)"""


class QuestionListPendingResponseItemQuestion(BaseModel):
    header: str
    """Very short label (max 12 chars)"""

    options: List[QuestionListPendingResponseItemQuestionOption]
    """Available choices"""

    question: str
    """Complete question"""

    custom: Optional[bool] = None
    """Allow typing a custom answer (default: true)"""

    multiple: Optional[bool] = None
    """Allow selecting multiple choices"""


class QuestionListPendingResponseItemTool(BaseModel):
    call_id: str = FieldInfo(alias="callID")

    message_id: str = FieldInfo(alias="messageID")


class QuestionListPendingResponseItem(BaseModel):
    id: str

    questions: List[QuestionListPendingResponseItemQuestion]
    """Questions to ask"""

    session_id: str = FieldInfo(alias="sessionID")

    tool: Optional[QuestionListPendingResponseItemTool] = None


QuestionListPendingResponse: TypeAlias = List[QuestionListPendingResponseItem]
