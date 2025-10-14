# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .range import Range
from .._models import BaseModel

__all__ = ["FindRetrieveSymbolResponse", "FindRetrieveSymbolResponseItem", "FindRetrieveSymbolResponseItemLocation"]


class FindRetrieveSymbolResponseItemLocation(BaseModel):
    range: Range

    uri: str


class FindRetrieveSymbolResponseItem(BaseModel):
    kind: float

    location: FindRetrieveSymbolResponseItemLocation

    name: str


FindRetrieveSymbolResponse: TypeAlias = List[FindRetrieveSymbolResponseItem]
