# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = [
    "FindSearchResponse",
    "FindSearchResponseItem",
    "FindSearchResponseItemLines",
    "FindSearchResponseItemPath",
    "FindSearchResponseItemSubmatch",
    "FindSearchResponseItemSubmatchMatch",
]


class FindSearchResponseItemLines(BaseModel):
    text: str


class FindSearchResponseItemPath(BaseModel):
    text: str


class FindSearchResponseItemSubmatchMatch(BaseModel):
    text: str


class FindSearchResponseItemSubmatch(BaseModel):
    end: float

    match: FindSearchResponseItemSubmatchMatch

    start: float


class FindSearchResponseItem(BaseModel):
    absolute_offset: float

    line_number: float

    lines: FindSearchResponseItemLines

    path: FindSearchResponseItemPath

    submatches: List[FindSearchResponseItemSubmatch]


FindSearchResponse: TypeAlias = List[FindSearchResponseItem]
