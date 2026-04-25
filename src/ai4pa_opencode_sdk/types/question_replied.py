# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["QuestionReplied", "Properties"]


class Properties(BaseModel):
    answers: List[List[str]]

    request_id: str = FieldInfo(alias="requestID")

    session_id: str = FieldInfo(alias="sessionID")


class QuestionReplied(BaseModel):
    properties: Properties

    type: Literal["question.replied"]
