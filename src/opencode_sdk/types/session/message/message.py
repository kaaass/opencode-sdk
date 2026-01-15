# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ...._models import BaseModel
from ...assistant_message import AssistantMessage

__all__ = [
    "Message",
    "UserMessage",
    "UserMessageModel",
    "UserMessageTime",
    "UserMessageSummary",
    "UserMessageSummaryDiff",
]


class UserMessageModel(BaseModel):
    api_model_id: str = FieldInfo(alias="modelID")

    provider_id: str = FieldInfo(alias="providerID")


class UserMessageTime(BaseModel):
    created: float


class UserMessageSummaryDiff(BaseModel):
    additions: float

    after: str

    before: str

    deletions: float

    file: str


class UserMessageSummary(BaseModel):
    diffs: List[UserMessageSummaryDiff]

    body: Optional[str] = None

    title: Optional[str] = None


class UserMessage(BaseModel):
    id: str

    agent: str

    model: UserMessageModel

    role: Literal["user"]

    session_id: str = FieldInfo(alias="sessionID")

    time: UserMessageTime

    summary: Optional[UserMessageSummary] = None

    system: Optional[str] = None

    tools: Optional[Dict[str, bool]] = None

    variant: Optional[str] = None


Message: TypeAlias = Union[UserMessage, AssistantMessage]
