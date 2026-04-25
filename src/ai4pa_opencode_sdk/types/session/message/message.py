# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ...._models import BaseModel
from ..output_format import OutputFormat
from ...assistant_message import AssistantMessage
from ...snapshot_file_diff import SnapshotFileDiff

__all__ = ["Message", "UserMessage", "UserMessageModel", "UserMessageTime", "UserMessageSummary"]


class UserMessageModel(BaseModel):
    api_model_id: str = FieldInfo(alias="modelID")

    provider_id: str = FieldInfo(alias="providerID")

    variant: Optional[str] = None


class UserMessageTime(BaseModel):
    created: float


class UserMessageSummary(BaseModel):
    diffs: List[SnapshotFileDiff]

    body: Optional[str] = None

    title: Optional[str] = None


class UserMessage(BaseModel):
    id: str

    agent: str

    model: UserMessageModel

    role: Literal["user"]

    session_id: str = FieldInfo(alias="sessionID")

    time: UserMessageTime

    format: Optional[OutputFormat] = None

    summary: Optional[UserMessageSummary] = None

    system: Optional[str] = None

    tools: Optional[Dict[str, bool]] = None


Message: TypeAlias = Union[UserMessage, AssistantMessage]
