# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = ["GlobalUpgradeOpencodeResponse", "UnionMember0", "UnionMember1"]


class UnionMember0(BaseModel):
    success: Literal[True]

    version: str


class UnionMember1(BaseModel):
    error: str

    success: Literal[False]


GlobalUpgradeOpencodeResponse: TypeAlias = Union[UnionMember0, UnionMember1]
