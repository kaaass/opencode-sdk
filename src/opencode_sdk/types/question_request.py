# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["QuestionRequest", "Question", "QuestionOption", "Tool"]


class QuestionOption(BaseModel):
    description: str
    """Explanation of choice"""

    label: str
    """Display text (1-5 words, concise)"""


class Question(BaseModel):
    header: str
    """Very short label (max 30 chars)"""

    options: List[QuestionOption]
    """Available choices"""

    question: str
    """Complete question"""

    custom: Optional[bool] = None
    """Allow typing a custom answer (default: true)"""

    multiple: Optional[bool] = None
    """Allow selecting multiple choices"""


class Tool(BaseModel):
    call_id: str = FieldInfo(alias="callID")

    message_id: str = FieldInfo(alias="messageID")


class QuestionRequest(BaseModel):
    id: str

    questions: List[Question]
    """Questions to ask"""

    session_id: str = FieldInfo(alias="sessionID")

    tool: Optional[Tool] = None
