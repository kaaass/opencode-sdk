# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "SessionGetStatusResponse",
    "SessionGetStatusResponseItem",
    "SessionGetStatusResponseItemType",
    "SessionGetStatusResponseItemUnionMember1",
    "SessionGetStatusResponseItemUnionMember3",
    "SessionGetStatusResponseItemUnionMember3PendingCall",
]


class SessionGetStatusResponseItemType(BaseModel):
    type: Literal["idle"]


class SessionGetStatusResponseItemUnionMember1(BaseModel):
    attempt: float

    message: str

    next: float

    type: Literal["retry"]


class SessionGetStatusResponseItemUnionMember3PendingCall(BaseModel):
    call_id: str = FieldInfo(alias="callID")

    input: Dict[str, object]

    tool: str


class SessionGetStatusResponseItemUnionMember3(BaseModel):
    pending_calls: List[SessionGetStatusResponseItemUnionMember3PendingCall] = FieldInfo(alias="pendingCalls")

    type: Literal["wait-tool-result"]


SessionGetStatusResponseItem: TypeAlias = Union[
    SessionGetStatusResponseItemType,
    SessionGetStatusResponseItemUnionMember1,
    SessionGetStatusResponseItemType,
    SessionGetStatusResponseItemUnionMember3,
]

SessionGetStatusResponse: TypeAlias = Dict[str, SessionGetStatusResponseItem]
