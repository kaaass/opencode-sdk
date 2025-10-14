# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = [
    "FindRetrieveResponse",
    "FindRetrieveResponseItem",
    "FindRetrieveResponseItemLines",
    "FindRetrieveResponseItemPath",
    "FindRetrieveResponseItemSubmatch",
    "FindRetrieveResponseItemSubmatchMatch",
]


class FindRetrieveResponseItemLines(BaseModel):
    text: str


class FindRetrieveResponseItemPath(BaseModel):
    text: str


class FindRetrieveResponseItemSubmatchMatch(BaseModel):
    text: str


class FindRetrieveResponseItemSubmatch(BaseModel):
    end: float

    match: FindRetrieveResponseItemSubmatchMatch

    start: float


class FindRetrieveResponseItem(BaseModel):
    absolute_offset: float

    line_number: float

    lines: FindRetrieveResponseItemLines

    path: FindRetrieveResponseItemPath

    submatches: List[FindRetrieveResponseItemSubmatch]


FindRetrieveResponse: TypeAlias = List[FindRetrieveResponseItem]
