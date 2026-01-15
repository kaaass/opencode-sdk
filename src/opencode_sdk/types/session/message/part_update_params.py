# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo
from ..file_part_param import FilePartParam
from ..file_part_source_param import FilePartSourceParam

__all__ = [
    "PartUpdateParams",
    "TextPart",
    "TextPartTime",
    "Variant1",
    "ReasoningPart",
    "ReasoningPartTime",
    "FilePart",
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
    "RetryPart",
    "RetryPartError",
    "RetryPartErrorData",
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

    ignored: bool

    metadata: Dict[str, object]

    synthetic: bool

    time: TextPartTime


class TextPartTime(TypedDict, total=False):
    start: Required[float]

    end: float


class Variant1(TypedDict, total=False):
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

    command: str


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

    metadata: Dict[str, object]


class ToolPartStateToolStatePending(TypedDict, total=False):
    input: Required[Dict[str, object]]

    raw: Required[str]

    status: Required[Literal["pending"]]


class ToolPartStateToolStateRunningTime(TypedDict, total=False):
    start: Required[float]


class ToolPartStateToolStateRunning(TypedDict, total=False):
    input: Required[Dict[str, object]]

    status: Required[Literal["running"]]

    time: Required[ToolPartStateToolStateRunningTime]

    metadata: Dict[str, object]

    title: str


class ToolPartStateToolStateCompletedTime(TypedDict, total=False):
    end: Required[float]

    start: Required[float]

    compacted: float


class ToolPartStateToolStateCompleted(TypedDict, total=False):
    input: Required[Dict[str, object]]

    metadata: Required[Dict[str, object]]

    output: Required[str]

    status: Required[Literal["completed"]]

    time: Required[ToolPartStateToolStateCompletedTime]

    title: Required[str]

    attachments: Iterable[FilePartParam]


class ToolPartStateToolStateErrorTime(TypedDict, total=False):
    end: Required[float]

    start: Required[float]


class ToolPartStateToolStateError(TypedDict, total=False):
    error: Required[str]

    input: Required[Dict[str, object]]

    status: Required[Literal["error"]]

    time: Required[ToolPartStateToolStateErrorTime]

    metadata: Dict[str, object]


ToolPartState: TypeAlias = Union[
    ToolPartStateToolStatePending,
    ToolPartStateToolStateRunning,
    ToolPartStateToolStateCompleted,
    ToolPartStateToolStateError,
]


class StepStartPart(TypedDict, total=False):
    path_session_id: Required[Annotated[str, PropertyInfo(alias="sessionID")]]

    path_message_id: Required[Annotated[str, PropertyInfo(alias="messageID")]]

    id: Required[str]

    body_message_id: Required[Annotated[str, PropertyInfo(alias="messageID")]]

    body_session_id: Required[Annotated[str, PropertyInfo(alias="sessionID")]]

    type: Required[Literal["step-start"]]

    directory: str

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

    snapshot: str


class StepFinishPartTokensCache(TypedDict, total=False):
    read: Required[float]

    write: Required[float]


class StepFinishPartTokens(TypedDict, total=False):
    cache: Required[StepFinishPartTokensCache]

    input: Required[float]

    output: Required[float]

    reasoning: Required[float]


class SnapshotPart(TypedDict, total=False):
    path_session_id: Required[Annotated[str, PropertyInfo(alias="sessionID")]]

    path_message_id: Required[Annotated[str, PropertyInfo(alias="messageID")]]

    id: Required[str]

    body_message_id: Required[Annotated[str, PropertyInfo(alias="messageID")]]

    body_session_id: Required[Annotated[str, PropertyInfo(alias="sessionID")]]

    snapshot: Required[str]

    type: Required[Literal["snapshot"]]

    directory: str


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


class AgentPart(TypedDict, total=False):
    path_session_id: Required[Annotated[str, PropertyInfo(alias="sessionID")]]

    path_message_id: Required[Annotated[str, PropertyInfo(alias="messageID")]]

    id: Required[str]

    body_message_id: Required[Annotated[str, PropertyInfo(alias="messageID")]]

    name: Required[str]

    body_session_id: Required[Annotated[str, PropertyInfo(alias="sessionID")]]

    type: Required[Literal["agent"]]

    directory: str

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

    error: Required[RetryPartError]

    body_message_id: Required[Annotated[str, PropertyInfo(alias="messageID")]]

    body_session_id: Required[Annotated[str, PropertyInfo(alias="sessionID")]]

    time: Required[RetryPartTime]

    type: Required[Literal["retry"]]

    directory: str


class RetryPartErrorData(TypedDict, total=False):
    is_retryable: Required[Annotated[bool, PropertyInfo(alias="isRetryable")]]

    message: Required[str]

    metadata: Dict[str, str]

    response_body: Annotated[str, PropertyInfo(alias="responseBody")]

    response_headers: Annotated[Dict[str, str], PropertyInfo(alias="responseHeaders")]

    status_code: Annotated[float, PropertyInfo(alias="statusCode")]


class RetryPartError(TypedDict, total=False):
    data: Required[RetryPartErrorData]

    name: Required[Literal["APIError"]]


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


PartUpdateParams: TypeAlias = Union[
    TextPart,
    Variant1,
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
