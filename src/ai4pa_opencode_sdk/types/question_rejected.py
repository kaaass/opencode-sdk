# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["QuestionRejected", "Properties"]


class Properties(BaseModel):
    request_id: str = FieldInfo(alias="requestID")

    session_id: str = FieldInfo(alias="sessionID")


class QuestionRejected(BaseModel):
    properties: Properties

    type: Literal["question.rejected"]
