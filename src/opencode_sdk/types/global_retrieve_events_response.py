# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .todo import Todo
from .project import Project
from .._models import BaseModel
from .session.part import Part
from .unknown_error import UnknownError
from .session.session import Session
from .provider_auth_error import ProviderAuthError
from .message_aborted_error import MessageAbortedError
from .session.message.message import Message
from .message_output_length_error import MessageOutputLengthError

__all__ = [
    "GlobalRetrieveEventsResponse",
    "Payload",
    "PayloadEventInstallationUpdated",
    "PayloadEventInstallationUpdatedProperties",
    "PayloadEventInstallationUpdateAvailable",
    "PayloadEventInstallationUpdateAvailableProperties",
    "PayloadEventProjectUpdated",
    "PayloadEventServerInstanceDisposed",
    "PayloadEventServerInstanceDisposedProperties",
    "PayloadEventLspClientDiagnostics",
    "PayloadEventLspClientDiagnosticsProperties",
    "PayloadEventLspUpdated",
    "PayloadEventMessageUpdated",
    "PayloadEventMessageUpdatedProperties",
    "PayloadEventMessageRemoved",
    "PayloadEventMessageRemovedProperties",
    "PayloadEventMessagePartUpdated",
    "PayloadEventMessagePartUpdatedProperties",
    "PayloadEventMessagePartRemoved",
    "PayloadEventMessagePartRemovedProperties",
    "PayloadEventPermissionAsked",
    "PayloadEventPermissionAskedProperties",
    "PayloadEventPermissionAskedPropertiesTool",
    "PayloadEventPermissionReplied",
    "PayloadEventPermissionRepliedProperties",
    "PayloadEventSessionStatus",
    "PayloadEventSessionStatusProperties",
    "PayloadEventSessionStatusPropertiesStatus",
    "PayloadEventSessionStatusPropertiesStatusType",
    "PayloadEventSessionStatusPropertiesStatusUnionMember1",
    "PayloadEventSessionStatusPropertiesStatusUnionMember3",
    "PayloadEventSessionStatusPropertiesStatusUnionMember3PendingCall",
    "PayloadEventSessionIdle",
    "PayloadEventSessionIdleProperties",
    "PayloadEventQuestionAsked",
    "PayloadEventQuestionAskedProperties",
    "PayloadEventQuestionAskedPropertiesQuestion",
    "PayloadEventQuestionAskedPropertiesQuestionOption",
    "PayloadEventQuestionAskedPropertiesTool",
    "PayloadEventQuestionReplied",
    "PayloadEventQuestionRepliedProperties",
    "PayloadEventQuestionRejected",
    "PayloadEventQuestionRejectedProperties",
    "PayloadEventSessionCompacted",
    "PayloadEventSessionCompactedProperties",
    "PayloadEventFileEdited",
    "PayloadEventFileEditedProperties",
    "PayloadEventTodoUpdated",
    "PayloadEventTodoUpdatedProperties",
    "PayloadEventTuiPromptAppend",
    "PayloadEventTuiPromptAppendProperties",
    "PayloadEventTuiCommandExecute",
    "PayloadEventTuiCommandExecuteProperties",
    "PayloadEventTuiToastShow",
    "PayloadEventTuiToastShowProperties",
    "PayloadEventTuiSessionSelect",
    "PayloadEventTuiSessionSelectProperties",
    "PayloadEventMcpToolsChanged",
    "PayloadEventMcpToolsChangedProperties",
    "PayloadEventCommandExecuted",
    "PayloadEventCommandExecutedProperties",
    "PayloadEventSessionCreated",
    "PayloadEventSessionCreatedProperties",
    "PayloadEventSessionUpdated",
    "PayloadEventSessionUpdatedProperties",
    "PayloadEventSessionDeleted",
    "PayloadEventSessionDeletedProperties",
    "PayloadEventSessionDiff",
    "PayloadEventSessionDiffProperties",
    "PayloadEventSessionDiffPropertiesDiff",
    "PayloadEventSessionError",
    "PayloadEventSessionErrorProperties",
    "PayloadEventSessionErrorPropertiesError",
    "PayloadEventSessionErrorPropertiesErrorAPIError",
    "PayloadEventSessionErrorPropertiesErrorAPIErrorData",
    "PayloadEventFileWatcherUpdated",
    "PayloadEventFileWatcherUpdatedProperties",
    "PayloadEventVcsBranchUpdated",
    "PayloadEventVcsBranchUpdatedProperties",
    "PayloadEventPtyCreated",
    "PayloadEventPtyCreatedProperties",
    "PayloadEventPtyCreatedPropertiesInfo",
    "PayloadEventPtyUpdated",
    "PayloadEventPtyUpdatedProperties",
    "PayloadEventPtyUpdatedPropertiesInfo",
    "PayloadEventPtyExited",
    "PayloadEventPtyExitedProperties",
    "PayloadEventPtyDeleted",
    "PayloadEventPtyDeletedProperties",
    "PayloadEventServerConnected",
    "PayloadEventGlobalDisposed",
]


class PayloadEventInstallationUpdatedProperties(BaseModel):
    version: str


class PayloadEventInstallationUpdated(BaseModel):
    properties: PayloadEventInstallationUpdatedProperties

    type: Literal["installation.updated"]


class PayloadEventInstallationUpdateAvailableProperties(BaseModel):
    version: str


class PayloadEventInstallationUpdateAvailable(BaseModel):
    properties: PayloadEventInstallationUpdateAvailableProperties

    type: Literal["installation.update-available"]


class PayloadEventProjectUpdated(BaseModel):
    properties: Project

    type: Literal["project.updated"]


class PayloadEventServerInstanceDisposedProperties(BaseModel):
    directory: str


class PayloadEventServerInstanceDisposed(BaseModel):
    properties: PayloadEventServerInstanceDisposedProperties

    type: Literal["server.instance.disposed"]


class PayloadEventLspClientDiagnosticsProperties(BaseModel):
    path: str

    server_id: str = FieldInfo(alias="serverID")


class PayloadEventLspClientDiagnostics(BaseModel):
    properties: PayloadEventLspClientDiagnosticsProperties

    type: Literal["lsp.client.diagnostics"]


class PayloadEventLspUpdated(BaseModel):
    properties: object

    type: Literal["lsp.updated"]


class PayloadEventMessageUpdatedProperties(BaseModel):
    info: Message


class PayloadEventMessageUpdated(BaseModel):
    properties: PayloadEventMessageUpdatedProperties

    type: Literal["message.updated"]


class PayloadEventMessageRemovedProperties(BaseModel):
    message_id: str = FieldInfo(alias="messageID")

    session_id: str = FieldInfo(alias="sessionID")


class PayloadEventMessageRemoved(BaseModel):
    properties: PayloadEventMessageRemovedProperties

    type: Literal["message.removed"]


class PayloadEventMessagePartUpdatedProperties(BaseModel):
    part: Part

    delta: Optional[str] = None


class PayloadEventMessagePartUpdated(BaseModel):
    properties: PayloadEventMessagePartUpdatedProperties

    type: Literal["message.part.updated"]


class PayloadEventMessagePartRemovedProperties(BaseModel):
    message_id: str = FieldInfo(alias="messageID")

    part_id: str = FieldInfo(alias="partID")

    session_id: str = FieldInfo(alias="sessionID")


class PayloadEventMessagePartRemoved(BaseModel):
    properties: PayloadEventMessagePartRemovedProperties

    type: Literal["message.part.removed"]


class PayloadEventPermissionAskedPropertiesTool(BaseModel):
    call_id: str = FieldInfo(alias="callID")

    message_id: str = FieldInfo(alias="messageID")


class PayloadEventPermissionAskedProperties(BaseModel):
    id: str

    always: List[str]

    metadata: Dict[str, object]

    patterns: List[str]

    permission: str

    session_id: str = FieldInfo(alias="sessionID")

    tool: Optional[PayloadEventPermissionAskedPropertiesTool] = None


class PayloadEventPermissionAsked(BaseModel):
    properties: PayloadEventPermissionAskedProperties

    type: Literal["permission.asked"]


class PayloadEventPermissionRepliedProperties(BaseModel):
    reply: Literal["once", "always", "reject"]

    request_id: str = FieldInfo(alias="requestID")

    session_id: str = FieldInfo(alias="sessionID")


class PayloadEventPermissionReplied(BaseModel):
    properties: PayloadEventPermissionRepliedProperties

    type: Literal["permission.replied"]


class PayloadEventSessionStatusPropertiesStatusType(BaseModel):
    type: Literal["idle"]


class PayloadEventSessionStatusPropertiesStatusUnionMember1(BaseModel):
    attempt: float

    message: str

    next: float

    type: Literal["retry"]


class PayloadEventSessionStatusPropertiesStatusUnionMember3PendingCall(BaseModel):
    call_id: str = FieldInfo(alias="callID")

    input: Dict[str, object]

    tool: str


class PayloadEventSessionStatusPropertiesStatusUnionMember3(BaseModel):
    pending_calls: List[PayloadEventSessionStatusPropertiesStatusUnionMember3PendingCall] = FieldInfo(
        alias="pendingCalls"
    )

    type: Literal["wait-tool-result"]


PayloadEventSessionStatusPropertiesStatus: TypeAlias = Union[
    PayloadEventSessionStatusPropertiesStatusType,
    PayloadEventSessionStatusPropertiesStatusUnionMember1,
    PayloadEventSessionStatusPropertiesStatusType,
    PayloadEventSessionStatusPropertiesStatusUnionMember3,
]


class PayloadEventSessionStatusProperties(BaseModel):
    session_id: str = FieldInfo(alias="sessionID")

    status: PayloadEventSessionStatusPropertiesStatus


class PayloadEventSessionStatus(BaseModel):
    properties: PayloadEventSessionStatusProperties

    type: Literal["session.status"]


class PayloadEventSessionIdleProperties(BaseModel):
    session_id: str = FieldInfo(alias="sessionID")


class PayloadEventSessionIdle(BaseModel):
    properties: PayloadEventSessionIdleProperties

    type: Literal["session.idle"]


class PayloadEventQuestionAskedPropertiesQuestionOption(BaseModel):
    description: str
    """Explanation of choice"""

    label: str
    """Display text (1-5 words, concise)"""


class PayloadEventQuestionAskedPropertiesQuestion(BaseModel):
    header: str
    """Very short label (max 12 chars)"""

    options: List[PayloadEventQuestionAskedPropertiesQuestionOption]
    """Available choices"""

    question: str
    """Complete question"""

    custom: Optional[bool] = None
    """Allow typing a custom answer (default: true)"""

    multiple: Optional[bool] = None
    """Allow selecting multiple choices"""


class PayloadEventQuestionAskedPropertiesTool(BaseModel):
    call_id: str = FieldInfo(alias="callID")

    message_id: str = FieldInfo(alias="messageID")


class PayloadEventQuestionAskedProperties(BaseModel):
    id: str

    questions: List[PayloadEventQuestionAskedPropertiesQuestion]
    """Questions to ask"""

    session_id: str = FieldInfo(alias="sessionID")

    tool: Optional[PayloadEventQuestionAskedPropertiesTool] = None


class PayloadEventQuestionAsked(BaseModel):
    properties: PayloadEventQuestionAskedProperties

    type: Literal["question.asked"]


class PayloadEventQuestionRepliedProperties(BaseModel):
    answers: List[List[str]]

    request_id: str = FieldInfo(alias="requestID")

    session_id: str = FieldInfo(alias="sessionID")


class PayloadEventQuestionReplied(BaseModel):
    properties: PayloadEventQuestionRepliedProperties

    type: Literal["question.replied"]


class PayloadEventQuestionRejectedProperties(BaseModel):
    request_id: str = FieldInfo(alias="requestID")

    session_id: str = FieldInfo(alias="sessionID")


class PayloadEventQuestionRejected(BaseModel):
    properties: PayloadEventQuestionRejectedProperties

    type: Literal["question.rejected"]


class PayloadEventSessionCompactedProperties(BaseModel):
    session_id: str = FieldInfo(alias="sessionID")


class PayloadEventSessionCompacted(BaseModel):
    properties: PayloadEventSessionCompactedProperties

    type: Literal["session.compacted"]


class PayloadEventFileEditedProperties(BaseModel):
    file: str


class PayloadEventFileEdited(BaseModel):
    properties: PayloadEventFileEditedProperties

    type: Literal["file.edited"]


class PayloadEventTodoUpdatedProperties(BaseModel):
    session_id: str = FieldInfo(alias="sessionID")

    todos: List[Todo]


class PayloadEventTodoUpdated(BaseModel):
    properties: PayloadEventTodoUpdatedProperties

    type: Literal["todo.updated"]


class PayloadEventTuiPromptAppendProperties(BaseModel):
    text: str


class PayloadEventTuiPromptAppend(BaseModel):
    properties: PayloadEventTuiPromptAppendProperties

    type: Literal["tui.prompt.append"]


class PayloadEventTuiCommandExecuteProperties(BaseModel):
    command: Union[
        Literal[
            "session.list",
            "session.new",
            "session.share",
            "session.interrupt",
            "session.compact",
            "session.page.up",
            "session.page.down",
            "session.half.page.up",
            "session.half.page.down",
            "session.first",
            "session.last",
            "prompt.clear",
            "prompt.submit",
            "agent.cycle",
        ],
        str,
    ]


class PayloadEventTuiCommandExecute(BaseModel):
    properties: PayloadEventTuiCommandExecuteProperties

    type: Literal["tui.command.execute"]


class PayloadEventTuiToastShowProperties(BaseModel):
    message: str

    variant: Literal["info", "success", "warning", "error"]

    duration: Optional[float] = None
    """Duration in milliseconds"""

    title: Optional[str] = None


class PayloadEventTuiToastShow(BaseModel):
    properties: PayloadEventTuiToastShowProperties

    type: Literal["tui.toast.show"]


class PayloadEventTuiSessionSelectProperties(BaseModel):
    session_id: str = FieldInfo(alias="sessionID")
    """Session ID to navigate to"""


class PayloadEventTuiSessionSelect(BaseModel):
    properties: PayloadEventTuiSessionSelectProperties

    type: Literal["tui.session.select"]


class PayloadEventMcpToolsChangedProperties(BaseModel):
    server: str


class PayloadEventMcpToolsChanged(BaseModel):
    properties: PayloadEventMcpToolsChangedProperties

    type: Literal["mcp.tools.changed"]


class PayloadEventCommandExecutedProperties(BaseModel):
    arguments: str

    message_id: str = FieldInfo(alias="messageID")

    name: str

    session_id: str = FieldInfo(alias="sessionID")


class PayloadEventCommandExecuted(BaseModel):
    properties: PayloadEventCommandExecutedProperties

    type: Literal["command.executed"]


class PayloadEventSessionCreatedProperties(BaseModel):
    info: Session


class PayloadEventSessionCreated(BaseModel):
    properties: PayloadEventSessionCreatedProperties

    type: Literal["session.created"]


class PayloadEventSessionUpdatedProperties(BaseModel):
    info: Session


class PayloadEventSessionUpdated(BaseModel):
    properties: PayloadEventSessionUpdatedProperties

    type: Literal["session.updated"]


class PayloadEventSessionDeletedProperties(BaseModel):
    info: Session


class PayloadEventSessionDeleted(BaseModel):
    properties: PayloadEventSessionDeletedProperties

    type: Literal["session.deleted"]


class PayloadEventSessionDiffPropertiesDiff(BaseModel):
    additions: float

    after: str

    before: str

    deletions: float

    file: str


class PayloadEventSessionDiffProperties(BaseModel):
    diff: List[PayloadEventSessionDiffPropertiesDiff]

    session_id: str = FieldInfo(alias="sessionID")


class PayloadEventSessionDiff(BaseModel):
    properties: PayloadEventSessionDiffProperties

    type: Literal["session.diff"]


class PayloadEventSessionErrorPropertiesErrorAPIErrorData(BaseModel):
    is_retryable: bool = FieldInfo(alias="isRetryable")

    message: str

    metadata: Optional[Dict[str, str]] = None

    response_body: Optional[str] = FieldInfo(alias="responseBody", default=None)

    response_headers: Optional[Dict[str, str]] = FieldInfo(alias="responseHeaders", default=None)

    status_code: Optional[float] = FieldInfo(alias="statusCode", default=None)


class PayloadEventSessionErrorPropertiesErrorAPIError(BaseModel):
    data: PayloadEventSessionErrorPropertiesErrorAPIErrorData

    name: Literal["APIError"]


PayloadEventSessionErrorPropertiesError: TypeAlias = Union[
    ProviderAuthError,
    UnknownError,
    MessageOutputLengthError,
    MessageAbortedError,
    PayloadEventSessionErrorPropertiesErrorAPIError,
]


class PayloadEventSessionErrorProperties(BaseModel):
    error: Optional[PayloadEventSessionErrorPropertiesError] = None

    session_id: Optional[str] = FieldInfo(alias="sessionID", default=None)


class PayloadEventSessionError(BaseModel):
    properties: PayloadEventSessionErrorProperties

    type: Literal["session.error"]


class PayloadEventFileWatcherUpdatedProperties(BaseModel):
    event: Literal["add", "change", "unlink"]

    file: str


class PayloadEventFileWatcherUpdated(BaseModel):
    properties: PayloadEventFileWatcherUpdatedProperties

    type: Literal["file.watcher.updated"]


class PayloadEventVcsBranchUpdatedProperties(BaseModel):
    branch: Optional[str] = None


class PayloadEventVcsBranchUpdated(BaseModel):
    properties: PayloadEventVcsBranchUpdatedProperties

    type: Literal["vcs.branch.updated"]


class PayloadEventPtyCreatedPropertiesInfo(BaseModel):
    id: str

    args: List[str]

    command: str

    cwd: str

    pid: float

    status: Literal["running", "exited"]

    title: str


class PayloadEventPtyCreatedProperties(BaseModel):
    info: PayloadEventPtyCreatedPropertiesInfo


class PayloadEventPtyCreated(BaseModel):
    properties: PayloadEventPtyCreatedProperties

    type: Literal["pty.created"]


class PayloadEventPtyUpdatedPropertiesInfo(BaseModel):
    id: str

    args: List[str]

    command: str

    cwd: str

    pid: float

    status: Literal["running", "exited"]

    title: str


class PayloadEventPtyUpdatedProperties(BaseModel):
    info: PayloadEventPtyUpdatedPropertiesInfo


class PayloadEventPtyUpdated(BaseModel):
    properties: PayloadEventPtyUpdatedProperties

    type: Literal["pty.updated"]


class PayloadEventPtyExitedProperties(BaseModel):
    id: str

    exit_code: float = FieldInfo(alias="exitCode")


class PayloadEventPtyExited(BaseModel):
    properties: PayloadEventPtyExitedProperties

    type: Literal["pty.exited"]


class PayloadEventPtyDeletedProperties(BaseModel):
    id: str


class PayloadEventPtyDeleted(BaseModel):
    properties: PayloadEventPtyDeletedProperties

    type: Literal["pty.deleted"]


class PayloadEventServerConnected(BaseModel):
    properties: object

    type: Literal["server.connected"]


class PayloadEventGlobalDisposed(BaseModel):
    properties: object

    type: Literal["global.disposed"]


Payload: TypeAlias = Union[
    PayloadEventInstallationUpdated,
    PayloadEventInstallationUpdateAvailable,
    PayloadEventProjectUpdated,
    PayloadEventServerInstanceDisposed,
    PayloadEventLspClientDiagnostics,
    PayloadEventLspUpdated,
    PayloadEventMessageUpdated,
    PayloadEventMessageRemoved,
    PayloadEventMessagePartUpdated,
    PayloadEventMessagePartRemoved,
    PayloadEventPermissionAsked,
    PayloadEventPermissionReplied,
    PayloadEventSessionStatus,
    PayloadEventSessionIdle,
    PayloadEventQuestionAsked,
    PayloadEventQuestionReplied,
    PayloadEventQuestionRejected,
    PayloadEventSessionCompacted,
    PayloadEventFileEdited,
    PayloadEventTodoUpdated,
    PayloadEventTuiPromptAppend,
    PayloadEventTuiCommandExecute,
    PayloadEventTuiToastShow,
    PayloadEventTuiSessionSelect,
    PayloadEventMcpToolsChanged,
    PayloadEventCommandExecuted,
    PayloadEventSessionCreated,
    PayloadEventSessionUpdated,
    PayloadEventSessionDeleted,
    PayloadEventSessionDiff,
    PayloadEventSessionError,
    PayloadEventFileWatcherUpdated,
    PayloadEventVcsBranchUpdated,
    PayloadEventPtyCreated,
    PayloadEventPtyUpdated,
    PayloadEventPtyExited,
    PayloadEventPtyDeleted,
    PayloadEventServerConnected,
    PayloadEventGlobalDisposed,
]


class GlobalRetrieveEventsResponse(BaseModel):
    directory: str

    payload: Payload
