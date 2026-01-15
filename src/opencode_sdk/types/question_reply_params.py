# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["QuestionReplyParams"]


class QuestionReplyParams(TypedDict, total=False):
    answers: Required[Iterable[SequenceNotStr[str]]]
    """User answers in order of questions (each answer is an array of selected labels)"""

    directory: str
