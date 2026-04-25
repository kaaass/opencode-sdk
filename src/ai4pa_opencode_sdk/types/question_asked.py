# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel
from .question_request import QuestionRequest

__all__ = ["QuestionAsked"]


class QuestionAsked(BaseModel):
    properties: QuestionRequest

    type: Literal["question.asked"]
