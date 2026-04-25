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
    "UserMessageFormat",
    "UserMessageFormatOutputFormatText",
    "UserMessageFormatOutputFormatJsonSchema",
    "UserMessageSummary",
    "UserMessageSummaryDiff",
]


class UserMessageModel(BaseModel):
    api_model_id: str = FieldInfo(alias="modelID")

    provider_id: str = FieldInfo(alias="providerID")

    variant: Optional[str] = None


class UserMessageTime(BaseModel):
    created: float


class UserMessageFormatOutputFormatText(BaseModel):
    type: Literal["text"]


class UserMessageFormatOutputFormatJsonSchema(BaseModel):
    schema_: Dict[str, object] = FieldInfo(alias="schema")

    type: Literal["json_schema"]

    retry_count: Optional[int] = FieldInfo(alias="retryCount", default=None)


UserMessageFormat: TypeAlias = Union[UserMessageFormatOutputFormatText, UserMessageFormatOutputFormatJsonSchema]


class UserMessageSummaryDiff(BaseModel):
    additions: float

    deletions: float

    file: str

    patch: str

    status: Optional[Literal["added", "deleted", "modified"]] = None


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

    format: Optional[UserMessageFormat] = None

    summary: Optional[UserMessageSummary] = None

    system: Optional[str] = None

    tools: Optional[Dict[str, bool]] = None


Message: TypeAlias = Union[UserMessage, AssistantMessage]
