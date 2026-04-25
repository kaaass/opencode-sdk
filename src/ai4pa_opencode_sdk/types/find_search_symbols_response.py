# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .range import Range
from .._models import BaseModel

__all__ = ["FindSearchSymbolsResponse", "FindSearchSymbolsResponseItem", "FindSearchSymbolsResponseItemLocation"]


class FindSearchSymbolsResponseItemLocation(BaseModel):
    range: Range

    uri: str


class FindSearchSymbolsResponseItem(BaseModel):
    kind: float

    location: FindSearchSymbolsResponseItemLocation

    name: str


FindSearchSymbolsResponse: TypeAlias = List[FindSearchSymbolsResponseItem]
