# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .file_part import FilePart

__all__ = [
    "Part",
    "TextPart",
    "TextPartTime",
    "ReasoningPart",
    "ReasoningPartTime",
    "ToolPart",
    "ToolPartState",
    "ToolPartStateToolStatePending",
    "ToolPartStateToolStateRunning",
    "ToolPartStateToolStateRunningTime",
    "ToolPartStateToolStateCompleted",
    "ToolPartStateToolStateCompletedTime",
    "ToolPartStateToolStateError",
    "ToolPartStateToolStateErrorTime",
    "StepStartPart",
    "StepFinishPart",
    "StepFinishPartTokens",
    "StepFinishPartTokensCache",
    "SnapshotPart",
    "PatchPart",
    "AgentPart",
    "AgentPartSource",
]


class TextPartTime(BaseModel):
    start: float

    end: Optional[float] = None


class TextPart(BaseModel):
    id: str

    message_id: str = FieldInfo(alias="messageID")

    session_id: str = FieldInfo(alias="sessionID")

    text: str

    type: Literal["text"]

    metadata: Optional[Dict[str, object]] = None

    synthetic: Optional[bool] = None

    time: Optional[TextPartTime] = None


class ReasoningPartTime(BaseModel):
    start: float

    end: Optional[float] = None


class ReasoningPart(BaseModel):
    id: str

    message_id: str = FieldInfo(alias="messageID")

    session_id: str = FieldInfo(alias="sessionID")

    text: str

    time: ReasoningPartTime

    type: Literal["reasoning"]

    metadata: Optional[Dict[str, object]] = None


class ToolPartStateToolStatePending(BaseModel):
    status: Literal["pending"]


class ToolPartStateToolStateRunningTime(BaseModel):
    start: float


class ToolPartStateToolStateRunning(BaseModel):
    input: object

    status: Literal["running"]

    time: ToolPartStateToolStateRunningTime

    metadata: Optional[Dict[str, object]] = None

    title: Optional[str] = None


class ToolPartStateToolStateCompletedTime(BaseModel):
    end: float

    start: float

    compacted: Optional[float] = None


class ToolPartStateToolStateCompleted(BaseModel):
    input: Dict[str, object]

    metadata: Dict[str, object]

    output: str

    status: Literal["completed"]

    time: ToolPartStateToolStateCompletedTime

    title: str

    attachments: Optional[List[FilePart]] = None


class ToolPartStateToolStateErrorTime(BaseModel):
    end: float

    start: float


class ToolPartStateToolStateError(BaseModel):
    error: str

    input: Dict[str, object]

    status: Literal["error"]

    time: ToolPartStateToolStateErrorTime

    metadata: Optional[Dict[str, object]] = None


ToolPartState: TypeAlias = Union[
    ToolPartStateToolStatePending,
    ToolPartStateToolStateRunning,
    ToolPartStateToolStateCompleted,
    ToolPartStateToolStateError,
]


class ToolPart(BaseModel):
    id: str

    call_id: str = FieldInfo(alias="callID")

    message_id: str = FieldInfo(alias="messageID")

    session_id: str = FieldInfo(alias="sessionID")

    state: ToolPartState

    tool: str

    type: Literal["tool"]

    metadata: Optional[Dict[str, object]] = None


class StepStartPart(BaseModel):
    id: str

    message_id: str = FieldInfo(alias="messageID")

    session_id: str = FieldInfo(alias="sessionID")

    type: Literal["step-start"]


class StepFinishPartTokensCache(BaseModel):
    read: float

    write: float


class StepFinishPartTokens(BaseModel):
    cache: StepFinishPartTokensCache

    input: float

    output: float

    reasoning: float


class StepFinishPart(BaseModel):
    id: str

    cost: float

    message_id: str = FieldInfo(alias="messageID")

    session_id: str = FieldInfo(alias="sessionID")

    tokens: StepFinishPartTokens

    type: Literal["step-finish"]


class SnapshotPart(BaseModel):
    id: str

    message_id: str = FieldInfo(alias="messageID")

    session_id: str = FieldInfo(alias="sessionID")

    snapshot: str

    type: Literal["snapshot"]


class PatchPart(BaseModel):
    id: str

    files: List[str]

    hash: str

    message_id: str = FieldInfo(alias="messageID")

    session_id: str = FieldInfo(alias="sessionID")

    type: Literal["patch"]


class AgentPartSource(BaseModel):
    end: int

    start: int

    value: str


class AgentPart(BaseModel):
    id: str

    message_id: str = FieldInfo(alias="messageID")

    name: str

    session_id: str = FieldInfo(alias="sessionID")

    type: Literal["agent"]

    source: Optional[AgentPartSource] = None


Part: TypeAlias = Union[
    TextPart, ReasoningPart, FilePart, ToolPart, StepStartPart, StepFinishPart, SnapshotPart, PatchPart, AgentPart
]
