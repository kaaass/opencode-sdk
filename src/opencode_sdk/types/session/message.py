# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..assistant_message import AssistantMessage

__all__ = ["Message", "UserMessage", "UserMessageTime"]


class UserMessageTime(BaseModel):
    created: float


class UserMessage(BaseModel):
    id: str

    role: Literal["user"]

    session_id: str = FieldInfo(alias="sessionID")

    time: UserMessageTime


Message: TypeAlias = Union[UserMessage, AssistantMessage]
