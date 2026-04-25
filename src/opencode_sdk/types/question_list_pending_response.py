# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .question_request import QuestionRequest

__all__ = ["QuestionListPendingResponse"]

QuestionListPendingResponse: TypeAlias = List[QuestionRequest]
