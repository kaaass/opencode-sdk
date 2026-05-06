# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo
from ...api_error_param import APIErrorParam
from .tool_state_error_param import ToolStateErrorParam
from ...file_part_source_param import FilePartSourceParam
from .tool_state_pending_param import ToolStatePendingParam
from .tool_state_running_param import ToolStateRunningParam
from .tool_state_completed_param import ToolStateCompletedParam

__all__ = [
    "PartUpdateParams",
    "TextPart",
    "TextPartTime",
    "SubtaskPart",
    "SubtaskPartModel",
    "ReasoningPart",
    "ReasoningPartTime",
    "FilePart",
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


class TextPart(TypedDict, total=False):
    path_session_id: Required[Annotated[str, PropertyInfo(alias="sessionID")]]

    path_message_id: Required[Annotated[str, PropertyInfo(alias="messageID")]]

    id: Required[str]

    body_message_id: Required[Annotated[str, PropertyInfo(alias="messageID")]]

    body_session_id: Required[Annotated[str, PropertyInfo(alias="sessionID")]]

    text: Required[str]

    type: Required[Literal["text"]]

    directory: str

    workspace: str

    ignored: bool

    metadata: Dict[str, object]

    synthetic: bool

    time: TextPartTime


class TextPartTime(TypedDict, total=False):
    start: Required[float]

    end: float


class SubtaskPart(TypedDict, total=False):
    path_session_id: Required[Annotated[str, PropertyInfo(alias="sessionID")]]

    path_message_id: Required[Annotated[str, PropertyInfo(alias="messageID")]]

    id: Required[str]

    agent: Required[str]

    description: Required[str]

    body_message_id: Required[Annotated[str, PropertyInfo(alias="messageID")]]

    prompt: Required[str]

    body_session_id: Required[Annotated[str, PropertyInfo(alias="sessionID")]]

    type: Required[Literal["subtask"]]

    directory: str

    workspace: str

    command: str

    model: SubtaskPartModel


class SubtaskPartModel(TypedDict, total=False):
    model_id: Required[Annotated[str, PropertyInfo(alias="modelID")]]

    provider_id: Required[Annotated[str, PropertyInfo(alias="providerID")]]


class ReasoningPart(TypedDict, total=False):
    path_session_id: Required[Annotated[str, PropertyInfo(alias="sessionID")]]

    path_message_id: Required[Annotated[str, PropertyInfo(alias="messageID")]]

    id: Required[str]

    body_message_id: Required[Annotated[str, PropertyInfo(alias="messageID")]]

    body_session_id: Required[Annotated[str, PropertyInfo(alias="sessionID")]]

    text: Required[str]

    time: Required[ReasoningPartTime]

    type: Required[Literal["reasoning"]]

    directory: str

    workspace: str

    metadata: Dict[str, object]


class ReasoningPartTime(TypedDict, total=False):
    start: Required[float]

    end: float


class FilePart(TypedDict, total=False):
    path_session_id: Required[Annotated[str, PropertyInfo(alias="sessionID")]]

    path_message_id: Required[Annotated[str, PropertyInfo(alias="messageID")]]

    id: Required[str]

    body_message_id: Required[Annotated[str, PropertyInfo(alias="messageID")]]

    mime: Required[str]

    body_session_id: Required[Annotated[str, PropertyInfo(alias="sessionID")]]

    type: Required[Literal["file"]]

    url: Required[str]

    directory: str

    workspace: str

    filename: str

    source: FilePartSourceParam


class ToolPart(TypedDict, total=False):
    path_session_id: Required[Annotated[str, PropertyInfo(alias="sessionID")]]

    path_message_id: Required[Annotated[str, PropertyInfo(alias="messageID")]]

    id: Required[str]

    call_id: Required[Annotated[str, PropertyInfo(alias="callID")]]

    body_message_id: Required[Annotated[str, PropertyInfo(alias="messageID")]]

    body_session_id: Required[Annotated[str, PropertyInfo(alias="sessionID")]]

    state: Required[ToolPartState]

    tool: Required[str]

    type: Required[Literal["tool"]]

    directory: str

    workspace: str

    metadata: Dict[str, object]


ToolPartState: TypeAlias = Union[
    ToolStatePendingParam, ToolStateRunningParam, ToolStateCompletedParam, ToolStateErrorParam
]


class StepStartPart(TypedDict, total=False):
    path_session_id: Required[Annotated[str, PropertyInfo(alias="sessionID")]]

    path_message_id: Required[Annotated[str, PropertyInfo(alias="messageID")]]

    id: Required[str]

    body_message_id: Required[Annotated[str, PropertyInfo(alias="messageID")]]

    body_session_id: Required[Annotated[str, PropertyInfo(alias="sessionID")]]

    type: Required[Literal["step-start"]]

    directory: str

    workspace: str

    snapshot: str


class StepFinishPart(TypedDict, total=False):
    path_session_id: Required[Annotated[str, PropertyInfo(alias="sessionID")]]

    path_message_id: Required[Annotated[str, PropertyInfo(alias="messageID")]]

    id: Required[str]

    cost: Required[float]

    body_message_id: Required[Annotated[str, PropertyInfo(alias="messageID")]]

    reason: Required[str]

    body_session_id: Required[Annotated[str, PropertyInfo(alias="sessionID")]]

    tokens: Required[StepFinishPartTokens]

    type: Required[Literal["step-finish"]]

    directory: str

    workspace: str

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


class SnapshotPart(TypedDict, total=False):
    path_session_id: Required[Annotated[str, PropertyInfo(alias="sessionID")]]

    path_message_id: Required[Annotated[str, PropertyInfo(alias="messageID")]]

    id: Required[str]

    body_message_id: Required[Annotated[str, PropertyInfo(alias="messageID")]]

    body_session_id: Required[Annotated[str, PropertyInfo(alias="sessionID")]]

    snapshot: Required[str]

    type: Required[Literal["snapshot"]]

    directory: str

    workspace: str


class PatchPart(TypedDict, total=False):
    path_session_id: Required[Annotated[str, PropertyInfo(alias="sessionID")]]

    path_message_id: Required[Annotated[str, PropertyInfo(alias="messageID")]]

    id: Required[str]

    files: Required[SequenceNotStr[str]]

    hash: Required[str]

    body_message_id: Required[Annotated[str, PropertyInfo(alias="messageID")]]

    body_session_id: Required[Annotated[str, PropertyInfo(alias="sessionID")]]

    type: Required[Literal["patch"]]

    directory: str

    workspace: str


class AgentPart(TypedDict, total=False):
    path_session_id: Required[Annotated[str, PropertyInfo(alias="sessionID")]]

    path_message_id: Required[Annotated[str, PropertyInfo(alias="messageID")]]

    id: Required[str]

    body_message_id: Required[Annotated[str, PropertyInfo(alias="messageID")]]

    name: Required[str]

    body_session_id: Required[Annotated[str, PropertyInfo(alias="sessionID")]]

    type: Required[Literal["agent"]]

    directory: str

    workspace: str

    source: AgentPartSource


class AgentPartSource(TypedDict, total=False):
    end: Required[int]

    start: Required[int]

    value: Required[str]


class RetryPart(TypedDict, total=False):
    path_session_id: Required[Annotated[str, PropertyInfo(alias="sessionID")]]

    path_message_id: Required[Annotated[str, PropertyInfo(alias="messageID")]]

    id: Required[str]

    attempt: Required[float]

    error: Required[APIErrorParam]

    body_message_id: Required[Annotated[str, PropertyInfo(alias="messageID")]]

    body_session_id: Required[Annotated[str, PropertyInfo(alias="sessionID")]]

    time: Required[RetryPartTime]

    type: Required[Literal["retry"]]

    directory: str

    workspace: str


class RetryPartTime(TypedDict, total=False):
    created: Required[float]


class CompactionPart(TypedDict, total=False):
    path_session_id: Required[Annotated[str, PropertyInfo(alias="sessionID")]]

    path_message_id: Required[Annotated[str, PropertyInfo(alias="messageID")]]

    id: Required[str]

    auto: Required[bool]

    body_message_id: Required[Annotated[str, PropertyInfo(alias="messageID")]]

    body_session_id: Required[Annotated[str, PropertyInfo(alias="sessionID")]]

    type: Required[Literal["compaction"]]

    directory: str

    workspace: str

    overflow: bool

    tail_start_id: str


PartUpdateParams: TypeAlias = Union[
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
