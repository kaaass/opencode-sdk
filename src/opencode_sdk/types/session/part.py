# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .file_part import FilePart
from ..api_error import APIError
from .tool_state_error import ToolStateError
from .tool_state_pending import ToolStatePending
from .tool_state_running import ToolStateRunning
from .tool_state_completed import ToolStateCompleted

__all__ = [
    "Part",
    "TextPart",
    "TextPartTime",
    "SubtaskPart",
    "SubtaskPartModel",
    "ReasoningPart",
    "ReasoningPartTime",
    "ToolPart",
    "ToolPartState",
    "StepStartPart",
    "StepFinishPart",
    "StepFinishPartTokens",
    "StepFinishPartTokensCache",
    "SnapshotPart",
    "PatchPart",
    "AgentPart",
    "AgentPartSource",
    "RetryPart",
    "RetryPartTime",
    "CompactionPart",
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

    ignored: Optional[bool] = None

    metadata: Optional[Dict[str, object]] = None

    synthetic: Optional[bool] = None

    time: Optional[TextPartTime] = None


class SubtaskPartModel(BaseModel):
    api_model_id: str = FieldInfo(alias="modelID")

    provider_id: str = FieldInfo(alias="providerID")


class SubtaskPart(BaseModel):
    id: str

    agent: str

    description: str

    message_id: str = FieldInfo(alias="messageID")

    prompt: str

    session_id: str = FieldInfo(alias="sessionID")

    type: Literal["subtask"]

    command: Optional[str] = None

    model: Optional[SubtaskPartModel] = None


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


ToolPartState: TypeAlias = Union[ToolStatePending, ToolStateRunning, ToolStateCompleted, ToolStateError]


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

    snapshot: Optional[str] = None


class StepFinishPartTokensCache(BaseModel):
    read: float

    write: float


class StepFinishPartTokens(BaseModel):
    cache: StepFinishPartTokensCache

    input: float

    output: float

    reasoning: float

    total: Optional[float] = None


class StepFinishPart(BaseModel):
    id: str

    cost: float

    message_id: str = FieldInfo(alias="messageID")

    reason: str

    session_id: str = FieldInfo(alias="sessionID")

    tokens: StepFinishPartTokens

    type: Literal["step-finish"]

    snapshot: Optional[str] = None


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


class RetryPartTime(BaseModel):
    created: float


class RetryPart(BaseModel):
    id: str

    attempt: float

    error: APIError

    message_id: str = FieldInfo(alias="messageID")

    session_id: str = FieldInfo(alias="sessionID")

    time: RetryPartTime

    type: Literal["retry"]


class CompactionPart(BaseModel):
    id: str

    auto: bool

    message_id: str = FieldInfo(alias="messageID")

    session_id: str = FieldInfo(alias="sessionID")

    type: Literal["compaction"]

    overflow: Optional[bool] = None


Part: TypeAlias = Union[
    TextPart,
    SubtaskPart,
    ReasoningPart,
    FilePart,
    ToolPart,
    StepStartPart,
    StepFinishPart,
    SnapshotPart,
    PatchPart,
    AgentPart,
    RetryPart,
    CompactionPart,
]
