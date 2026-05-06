# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo
from ...api_error_param import APIErrorParam
from ...file_part_param import FilePartParam
from .tool_state_error_param import ToolStateErrorParam
from .tool_state_pending_param import ToolStatePendingParam
from .tool_state_running_param import ToolStateRunningParam
from .tool_state_completed_param import ToolStateCompletedParam

__all__ = [
    "PartParam",
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


class TextPartTime(TypedDict, total=False):
    start: Required[float]

    end: float


class TextPart(TypedDict, total=False):
    id: Required[str]

    message_id: Required[Annotated[str, PropertyInfo(alias="messageID")]]

    session_id: Required[Annotated[str, PropertyInfo(alias="sessionID")]]

    text: Required[str]

    type: Required[Literal["text"]]

    ignored: bool

    metadata: Dict[str, object]

    synthetic: bool

    time: TextPartTime


class SubtaskPartModel(TypedDict, total=False):
    model_id: Required[Annotated[str, PropertyInfo(alias="modelID")]]

    provider_id: Required[Annotated[str, PropertyInfo(alias="providerID")]]


class SubtaskPart(TypedDict, total=False):
    id: Required[str]

    agent: Required[str]

    description: Required[str]

    message_id: Required[Annotated[str, PropertyInfo(alias="messageID")]]

    prompt: Required[str]

    session_id: Required[Annotated[str, PropertyInfo(alias="sessionID")]]

    type: Required[Literal["subtask"]]

    command: str

    model: SubtaskPartModel


class ReasoningPartTime(TypedDict, total=False):
    start: Required[float]

    end: float


class ReasoningPart(TypedDict, total=False):
    id: Required[str]

    message_id: Required[Annotated[str, PropertyInfo(alias="messageID")]]

    session_id: Required[Annotated[str, PropertyInfo(alias="sessionID")]]

    text: Required[str]

    time: Required[ReasoningPartTime]

    type: Required[Literal["reasoning"]]

    metadata: Dict[str, object]


ToolPartState: TypeAlias = Union[
    ToolStatePendingParam, ToolStateRunningParam, ToolStateCompletedParam, ToolStateErrorParam
]


class ToolPart(TypedDict, total=False):
    id: Required[str]

    call_id: Required[Annotated[str, PropertyInfo(alias="callID")]]

    message_id: Required[Annotated[str, PropertyInfo(alias="messageID")]]

    session_id: Required[Annotated[str, PropertyInfo(alias="sessionID")]]

    state: Required[ToolPartState]

    tool: Required[str]

    type: Required[Literal["tool"]]

    metadata: Dict[str, object]


class StepStartPart(TypedDict, total=False):
    id: Required[str]

    message_id: Required[Annotated[str, PropertyInfo(alias="messageID")]]

    session_id: Required[Annotated[str, PropertyInfo(alias="sessionID")]]

    type: Required[Literal["step-start"]]

    snapshot: str


class StepFinishPartTokensCache(TypedDict, total=False):
    read: Required[float]

    write: Required[float]


class StepFinishPartTokens(TypedDict, total=False):
    cache: Required[StepFinishPartTokensCache]

    input: Required[float]

    output: Required[float]

    reasoning: Required[float]

    total: float


class StepFinishPart(TypedDict, total=False):
    id: Required[str]

    cost: Required[float]

    message_id: Required[Annotated[str, PropertyInfo(alias="messageID")]]

    reason: Required[str]

    session_id: Required[Annotated[str, PropertyInfo(alias="sessionID")]]

    tokens: Required[StepFinishPartTokens]

    type: Required[Literal["step-finish"]]

    snapshot: str


class SnapshotPart(TypedDict, total=False):
    id: Required[str]

    message_id: Required[Annotated[str, PropertyInfo(alias="messageID")]]

    session_id: Required[Annotated[str, PropertyInfo(alias="sessionID")]]

    snapshot: Required[str]

    type: Required[Literal["snapshot"]]


class PatchPart(TypedDict, total=False):
    id: Required[str]

    files: Required[SequenceNotStr[str]]

    hash: Required[str]

    message_id: Required[Annotated[str, PropertyInfo(alias="messageID")]]

    session_id: Required[Annotated[str, PropertyInfo(alias="sessionID")]]

    type: Required[Literal["patch"]]


class AgentPartSource(TypedDict, total=False):
    end: Required[int]

    start: Required[int]

    value: Required[str]


class AgentPart(TypedDict, total=False):
    id: Required[str]

    message_id: Required[Annotated[str, PropertyInfo(alias="messageID")]]

    name: Required[str]

    session_id: Required[Annotated[str, PropertyInfo(alias="sessionID")]]

    type: Required[Literal["agent"]]

    source: AgentPartSource


class RetryPartTime(TypedDict, total=False):
    created: Required[float]


class RetryPart(TypedDict, total=False):
    id: Required[str]

    attempt: Required[float]

    error: Required[APIErrorParam]

    message_id: Required[Annotated[str, PropertyInfo(alias="messageID")]]

    session_id: Required[Annotated[str, PropertyInfo(alias="sessionID")]]

    time: Required[RetryPartTime]

    type: Required[Literal["retry"]]


class CompactionPart(TypedDict, total=False):
    id: Required[str]

    auto: Required[bool]

    message_id: Required[Annotated[str, PropertyInfo(alias="messageID")]]

    session_id: Required[Annotated[str, PropertyInfo(alias="sessionID")]]

    type: Required[Literal["compaction"]]

    overflow: bool

    tail_start_id: str


PartParam: TypeAlias = Union[
    TextPart,
    SubtaskPart,
    ReasoningPart,
    FilePartParam,
    ToolPart,
    StepStartPart,
    StepFinishPart,
    SnapshotPart,
    PatchPart,
    AgentPart,
    RetryPart,
    CompactionPart,
]
