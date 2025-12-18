# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["SessionRetrieveStatusResponse", "Type", "UnionMember1", "UnionMember3", "UnionMember3PendingCall"]


class Type(BaseModel):
    type: Literal["idle"]


class UnionMember1(BaseModel):
    attempt: float

    message: str

    next: float

    type: Literal["retry"]


class UnionMember3PendingCall(BaseModel):
    call_id: str = FieldInfo(alias="callID")

    input: Dict[str, object]

    tool: str


class UnionMember3(BaseModel):
    pending_calls: List[UnionMember3PendingCall] = FieldInfo(alias="pendingCalls")

    type: Literal["wait-tool-result"]


SessionRetrieveStatusResponse: TypeAlias = Union[Type, UnionMember1, Type, UnionMember3]
