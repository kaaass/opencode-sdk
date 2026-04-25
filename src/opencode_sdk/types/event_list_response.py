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
    "EventListResponse",
    "EventInstallationUpdated",
    "EventInstallationUpdatedProperties",
    "EventInstallationUpdateAvailable",
    "EventInstallationUpdateAvailableProperties",
    "EventProjectUpdated",
    "EventServerInstanceDisposed",
    "EventServerInstanceDisposedProperties",
    "EventServerConnected",
    "EventServerConnectedProperties",
    "EventServerConnectedPropertiesVersion",
    "EventServerConnectedPropertiesVersionUpstream",
    "EventGlobalDisposed",
    "EventFileEdited",
    "EventFileEditedProperties",
    "EventFileWatcherUpdated",
    "EventFileWatcherUpdatedProperties",
    "EventLspClientDiagnostics",
    "EventLspClientDiagnosticsProperties",
    "EventLspUpdated",
    "EventMessagePartDelta",
    "EventMessagePartDeltaProperties",
    "EventPermissionAsked",
    "EventPermissionAskedProperties",
    "EventPermissionAskedPropertiesTool",
    "EventPermissionReplied",
    "EventPermissionRepliedProperties",
    "EventSessionDiff",
    "EventSessionDiffProperties",
    "EventSessionDiffPropertiesDiff",
    "EventSessionError",
    "EventSessionErrorProperties",
    "EventSessionErrorPropertiesError",
    "EventSessionErrorPropertiesErrorStructuredOutputError",
    "EventSessionErrorPropertiesErrorStructuredOutputErrorData",
    "EventSessionErrorPropertiesErrorContextOverflowError",
    "EventSessionErrorPropertiesErrorContextOverflowErrorData",
    "EventSessionErrorPropertiesErrorAPIError",
    "EventSessionErrorPropertiesErrorAPIErrorData",
    "EventQuestionAsked",
    "EventQuestionAskedProperties",
    "EventQuestionAskedPropertiesQuestion",
    "EventQuestionAskedPropertiesQuestionOption",
    "EventQuestionAskedPropertiesTool",
    "EventQuestionReplied",
    "EventQuestionRepliedProperties",
    "EventQuestionRejected",
    "EventQuestionRejectedProperties",
    "EventTodoUpdated",
    "EventTodoUpdatedProperties",
    "EventSessionStatus",
    "EventSessionStatusProperties",
    "EventSessionStatusPropertiesStatus",
    "EventSessionStatusPropertiesStatusType",
    "EventSessionStatusPropertiesStatusUnionMember1",
    "EventSessionStatusPropertiesStatusUnionMember3",
    "EventSessionStatusPropertiesStatusUnionMember3PendingCall",
    "EventSessionIdle",
    "EventSessionIdleProperties",
    "EventSessionCompacted",
    "EventSessionCompactedProperties",
    "EventArtifactCreated",
    "EventArtifactCreatedProperties",
    "EventArtifactCreatedPropertiesInfo",
    "EventArtifactCreatedPropertiesInfoTime",
    "EventArtifactDeleted",
    "EventArtifactDeletedProperties",
    "EventTuiPromptAppend",
    "EventTuiPromptAppendProperties",
    "EventTuiCommandExecute",
    "EventTuiCommandExecuteProperties",
    "EventTuiToastShow",
    "EventTuiToastShowProperties",
    "EventTuiSessionSelect",
    "EventTuiSessionSelectProperties",
    "EventMcpToolsChanged",
    "EventMcpToolsChangedProperties",
    "EventMcpBrowserOpenFailed",
    "EventMcpBrowserOpenFailedProperties",
    "EventCommandExecuted",
    "EventCommandExecutedProperties",
    "EventVcsBranchUpdated",
    "EventVcsBranchUpdatedProperties",
    "EventWorktreeReady",
    "EventWorktreeReadyProperties",
    "EventWorktreeFailed",
    "EventWorktreeFailedProperties",
    "EventPtyCreated",
    "EventPtyCreatedProperties",
    "EventPtyCreatedPropertiesInfo",
    "EventPtyUpdated",
    "EventPtyUpdatedProperties",
    "EventPtyUpdatedPropertiesInfo",
    "EventPtyExited",
    "EventPtyExitedProperties",
    "EventPtyDeleted",
    "EventPtyDeletedProperties",
    "EventWorkspaceReady",
    "EventWorkspaceReadyProperties",
    "EventWorkspaceFailed",
    "EventWorkspaceFailedProperties",
    "EventWorkspaceStatus",
    "EventWorkspaceStatusProperties",
    "EventMessageUpdated",
    "EventMessageUpdatedProperties",
    "EventMessageRemoved",
    "EventMessageRemovedProperties",
    "EventMessagePartUpdated",
    "EventMessagePartUpdatedProperties",
    "EventMessagePartRemoved",
    "EventMessagePartRemovedProperties",
    "EventSessionCreated",
    "EventSessionCreatedProperties",
    "EventSessionUpdated",
    "EventSessionUpdatedProperties",
    "EventSessionDeleted",
    "EventSessionDeletedProperties",
]


class EventInstallationUpdatedProperties(BaseModel):
    version: str


class EventInstallationUpdated(BaseModel):
    properties: EventInstallationUpdatedProperties

    type: Literal["installation.updated"]


class EventInstallationUpdateAvailableProperties(BaseModel):
    version: str


class EventInstallationUpdateAvailable(BaseModel):
    properties: EventInstallationUpdateAvailableProperties

    type: Literal["installation.update-available"]


class EventProjectUpdated(BaseModel):
    properties: Project

    type: Literal["project.updated"]


class EventServerInstanceDisposedProperties(BaseModel):
    directory: str


class EventServerInstanceDisposed(BaseModel):
    properties: EventServerInstanceDisposedProperties

    type: Literal["server.instance.disposed"]


class EventServerConnectedPropertiesVersionUpstream(BaseModel):
    commit: str

    version: str


class EventServerConnectedPropertiesVersion(BaseModel):
    api: str

    channel: str

    upstream: EventServerConnectedPropertiesVersionUpstream

    version: str


class EventServerConnectedProperties(BaseModel):
    version: EventServerConnectedPropertiesVersion


class EventServerConnected(BaseModel):
    properties: EventServerConnectedProperties

    type: Literal["server.connected"]


class EventGlobalDisposed(BaseModel):
    properties: object

    type: Literal["global.disposed"]


class EventFileEditedProperties(BaseModel):
    file: str


class EventFileEdited(BaseModel):
    properties: EventFileEditedProperties

    type: Literal["file.edited"]


class EventFileWatcherUpdatedProperties(BaseModel):
    event: Literal["add", "change", "unlink"]

    file: str


class EventFileWatcherUpdated(BaseModel):
    properties: EventFileWatcherUpdatedProperties

    type: Literal["file.watcher.updated"]


class EventLspClientDiagnosticsProperties(BaseModel):
    path: str

    server_id: str = FieldInfo(alias="serverID")


class EventLspClientDiagnostics(BaseModel):
    properties: EventLspClientDiagnosticsProperties

    type: Literal["lsp.client.diagnostics"]


class EventLspUpdated(BaseModel):
    properties: object

    type: Literal["lsp.updated"]


class EventMessagePartDeltaProperties(BaseModel):
    delta: str

    field: str

    message_id: str = FieldInfo(alias="messageID")

    part_id: str = FieldInfo(alias="partID")

    session_id: str = FieldInfo(alias="sessionID")


class EventMessagePartDelta(BaseModel):
    properties: EventMessagePartDeltaProperties

    type: Literal["message.part.delta"]


class EventPermissionAskedPropertiesTool(BaseModel):
    call_id: str = FieldInfo(alias="callID")

    message_id: str = FieldInfo(alias="messageID")


class EventPermissionAskedProperties(BaseModel):
    id: str

    always: List[str]

    metadata: Dict[str, object]

    patterns: List[str]

    permission: str

    session_id: str = FieldInfo(alias="sessionID")

    tool: Optional[EventPermissionAskedPropertiesTool] = None


class EventPermissionAsked(BaseModel):
    properties: EventPermissionAskedProperties

    type: Literal["permission.asked"]


class EventPermissionRepliedProperties(BaseModel):
    reply: Literal["once", "always", "reject"]

    request_id: str = FieldInfo(alias="requestID")

    session_id: str = FieldInfo(alias="sessionID")


class EventPermissionReplied(BaseModel):
    properties: EventPermissionRepliedProperties

    type: Literal["permission.replied"]


class EventSessionDiffPropertiesDiff(BaseModel):
    additions: float

    deletions: float

    file: str

    patch: str

    status: Optional[Literal["added", "deleted", "modified"]] = None


class EventSessionDiffProperties(BaseModel):
    diff: List[EventSessionDiffPropertiesDiff]

    session_id: str = FieldInfo(alias="sessionID")


class EventSessionDiff(BaseModel):
    properties: EventSessionDiffProperties

    type: Literal["session.diff"]


class EventSessionErrorPropertiesErrorStructuredOutputErrorData(BaseModel):
    message: str

    retries: float


class EventSessionErrorPropertiesErrorStructuredOutputError(BaseModel):
    data: EventSessionErrorPropertiesErrorStructuredOutputErrorData

    name: Literal["StructuredOutputError"]


class EventSessionErrorPropertiesErrorContextOverflowErrorData(BaseModel):
    message: str

    response_body: Optional[str] = FieldInfo(alias="responseBody", default=None)


class EventSessionErrorPropertiesErrorContextOverflowError(BaseModel):
    data: EventSessionErrorPropertiesErrorContextOverflowErrorData

    name: Literal["ContextOverflowError"]


class EventSessionErrorPropertiesErrorAPIErrorData(BaseModel):
    is_retryable: bool = FieldInfo(alias="isRetryable")

    message: str

    metadata: Optional[Dict[str, str]] = None

    response_body: Optional[str] = FieldInfo(alias="responseBody", default=None)

    response_headers: Optional[Dict[str, str]] = FieldInfo(alias="responseHeaders", default=None)

    status_code: Optional[float] = FieldInfo(alias="statusCode", default=None)


class EventSessionErrorPropertiesErrorAPIError(BaseModel):
    data: EventSessionErrorPropertiesErrorAPIErrorData

    name: Literal["APIError"]


EventSessionErrorPropertiesError: TypeAlias = Union[
    ProviderAuthError,
    UnknownError,
    MessageOutputLengthError,
    MessageAbortedError,
    EventSessionErrorPropertiesErrorStructuredOutputError,
    EventSessionErrorPropertiesErrorContextOverflowError,
    EventSessionErrorPropertiesErrorAPIError,
]


class EventSessionErrorProperties(BaseModel):
    error: Optional[EventSessionErrorPropertiesError] = None

    session_id: Optional[str] = FieldInfo(alias="sessionID", default=None)


class EventSessionError(BaseModel):
    properties: EventSessionErrorProperties

    type: Literal["session.error"]


class EventQuestionAskedPropertiesQuestionOption(BaseModel):
    description: str
    """Explanation of choice"""

    label: str
    """Display text (1-5 words, concise)"""


class EventQuestionAskedPropertiesQuestion(BaseModel):
    header: str
    """Very short label (max 30 chars)"""

    options: List[EventQuestionAskedPropertiesQuestionOption]
    """Available choices"""

    question: str
    """Complete question"""

    custom: Optional[bool] = None
    """Allow typing a custom answer (default: true)"""

    multiple: Optional[bool] = None
    """Allow selecting multiple choices"""


class EventQuestionAskedPropertiesTool(BaseModel):
    call_id: str = FieldInfo(alias="callID")

    message_id: str = FieldInfo(alias="messageID")


class EventQuestionAskedProperties(BaseModel):
    id: str

    questions: List[EventQuestionAskedPropertiesQuestion]
    """Questions to ask"""

    session_id: str = FieldInfo(alias="sessionID")

    tool: Optional[EventQuestionAskedPropertiesTool] = None


class EventQuestionAsked(BaseModel):
    properties: EventQuestionAskedProperties

    type: Literal["question.asked"]


class EventQuestionRepliedProperties(BaseModel):
    answers: List[List[str]]

    request_id: str = FieldInfo(alias="requestID")

    session_id: str = FieldInfo(alias="sessionID")


class EventQuestionReplied(BaseModel):
    properties: EventQuestionRepliedProperties

    type: Literal["question.replied"]


class EventQuestionRejectedProperties(BaseModel):
    request_id: str = FieldInfo(alias="requestID")

    session_id: str = FieldInfo(alias="sessionID")


class EventQuestionRejected(BaseModel):
    properties: EventQuestionRejectedProperties

    type: Literal["question.rejected"]


class EventTodoUpdatedProperties(BaseModel):
    session_id: str = FieldInfo(alias="sessionID")

    todos: List[Todo]


class EventTodoUpdated(BaseModel):
    properties: EventTodoUpdatedProperties

    type: Literal["todo.updated"]


class EventSessionStatusPropertiesStatusType(BaseModel):
    type: Literal["idle"]


class EventSessionStatusPropertiesStatusUnionMember1(BaseModel):
    attempt: float

    message: str

    next: float

    type: Literal["retry"]


class EventSessionStatusPropertiesStatusUnionMember3PendingCall(BaseModel):
    call_id: str = FieldInfo(alias="callID")

    input: Dict[str, object]

    tool: str


class EventSessionStatusPropertiesStatusUnionMember3(BaseModel):
    pending_calls: List[EventSessionStatusPropertiesStatusUnionMember3PendingCall] = FieldInfo(alias="pendingCalls")

    type: Literal["wait-tool-result"]


EventSessionStatusPropertiesStatus: TypeAlias = Union[
    EventSessionStatusPropertiesStatusType,
    EventSessionStatusPropertiesStatusUnionMember1,
    EventSessionStatusPropertiesStatusType,
    EventSessionStatusPropertiesStatusUnionMember3,
]


class EventSessionStatusProperties(BaseModel):
    session_id: str = FieldInfo(alias="sessionID")

    status: EventSessionStatusPropertiesStatus


class EventSessionStatus(BaseModel):
    properties: EventSessionStatusProperties

    type: Literal["session.status"]


class EventSessionIdleProperties(BaseModel):
    session_id: str = FieldInfo(alias="sessionID")


class EventSessionIdle(BaseModel):
    properties: EventSessionIdleProperties

    type: Literal["session.idle"]


class EventSessionCompactedProperties(BaseModel):
    session_id: str = FieldInfo(alias="sessionID")


class EventSessionCompacted(BaseModel):
    properties: EventSessionCompactedProperties

    type: Literal["session.compacted"]


class EventArtifactCreatedPropertiesInfoTime(BaseModel):
    created: float


class EventArtifactCreatedPropertiesInfo(BaseModel):
    id: str

    filename: str

    hash: str

    mime: str

    session_id: str = FieldInfo(alias="sessionID")

    size: int

    time: EventArtifactCreatedPropertiesInfoTime

    metadata: Optional[Dict[str, object]] = None


class EventArtifactCreatedProperties(BaseModel):
    info: EventArtifactCreatedPropertiesInfo


class EventArtifactCreated(BaseModel):
    properties: EventArtifactCreatedProperties

    type: Literal["artifact.created"]


class EventArtifactDeletedProperties(BaseModel):
    artifact_id: str = FieldInfo(alias="artifactID")

    session_id: str = FieldInfo(alias="sessionID")


class EventArtifactDeleted(BaseModel):
    properties: EventArtifactDeletedProperties

    type: Literal["artifact.deleted"]


class EventTuiPromptAppendProperties(BaseModel):
    text: str


class EventTuiPromptAppend(BaseModel):
    properties: EventTuiPromptAppendProperties

    type: Literal["tui.prompt.append"]


class EventTuiCommandExecuteProperties(BaseModel):
    command: Union[
        Literal[
            "session.list",
            "session.new",
            "session.share",
            "session.interrupt",
            "session.compact",
            "session.page.up",
            "session.page.down",
            "session.line.up",
            "session.line.down",
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


class EventTuiCommandExecute(BaseModel):
    properties: EventTuiCommandExecuteProperties

    type: Literal["tui.command.execute"]


class EventTuiToastShowProperties(BaseModel):
    message: str

    variant: Literal["info", "success", "warning", "error"]

    duration: Optional[float] = None
    """Duration in milliseconds"""

    title: Optional[str] = None


class EventTuiToastShow(BaseModel):
    properties: EventTuiToastShowProperties

    type: Literal["tui.toast.show"]


class EventTuiSessionSelectProperties(BaseModel):
    session_id: str = FieldInfo(alias="sessionID")
    """Session ID to navigate to"""


class EventTuiSessionSelect(BaseModel):
    properties: EventTuiSessionSelectProperties

    type: Literal["tui.session.select"]


class EventMcpToolsChangedProperties(BaseModel):
    server: str


class EventMcpToolsChanged(BaseModel):
    properties: EventMcpToolsChangedProperties

    type: Literal["mcp.tools.changed"]


class EventMcpBrowserOpenFailedProperties(BaseModel):
    mcp_name: str = FieldInfo(alias="mcpName")

    url: str


class EventMcpBrowserOpenFailed(BaseModel):
    properties: EventMcpBrowserOpenFailedProperties

    type: Literal["mcp.browser.open.failed"]


class EventCommandExecutedProperties(BaseModel):
    arguments: str

    message_id: str = FieldInfo(alias="messageID")

    name: str

    session_id: str = FieldInfo(alias="sessionID")


class EventCommandExecuted(BaseModel):
    properties: EventCommandExecutedProperties

    type: Literal["command.executed"]


class EventVcsBranchUpdatedProperties(BaseModel):
    branch: Optional[str] = None


class EventVcsBranchUpdated(BaseModel):
    properties: EventVcsBranchUpdatedProperties

    type: Literal["vcs.branch.updated"]


class EventWorktreeReadyProperties(BaseModel):
    branch: str

    name: str


class EventWorktreeReady(BaseModel):
    properties: EventWorktreeReadyProperties

    type: Literal["worktree.ready"]


class EventWorktreeFailedProperties(BaseModel):
    message: str


class EventWorktreeFailed(BaseModel):
    properties: EventWorktreeFailedProperties

    type: Literal["worktree.failed"]


class EventPtyCreatedPropertiesInfo(BaseModel):
    id: str

    args: List[str]

    command: str

    cwd: str

    pid: float

    status: Literal["running", "exited"]

    title: str


class EventPtyCreatedProperties(BaseModel):
    info: EventPtyCreatedPropertiesInfo


class EventPtyCreated(BaseModel):
    properties: EventPtyCreatedProperties

    type: Literal["pty.created"]


class EventPtyUpdatedPropertiesInfo(BaseModel):
    id: str

    args: List[str]

    command: str

    cwd: str

    pid: float

    status: Literal["running", "exited"]

    title: str


class EventPtyUpdatedProperties(BaseModel):
    info: EventPtyUpdatedPropertiesInfo


class EventPtyUpdated(BaseModel):
    properties: EventPtyUpdatedProperties

    type: Literal["pty.updated"]


class EventPtyExitedProperties(BaseModel):
    id: str

    exit_code: float = FieldInfo(alias="exitCode")


class EventPtyExited(BaseModel):
    properties: EventPtyExitedProperties

    type: Literal["pty.exited"]


class EventPtyDeletedProperties(BaseModel):
    id: str


class EventPtyDeleted(BaseModel):
    properties: EventPtyDeletedProperties

    type: Literal["pty.deleted"]


class EventWorkspaceReadyProperties(BaseModel):
    name: str


class EventWorkspaceReady(BaseModel):
    properties: EventWorkspaceReadyProperties

    type: Literal["workspace.ready"]


class EventWorkspaceFailedProperties(BaseModel):
    message: str


class EventWorkspaceFailed(BaseModel):
    properties: EventWorkspaceFailedProperties

    type: Literal["workspace.failed"]


class EventWorkspaceStatusProperties(BaseModel):
    status: Literal["connected", "connecting", "disconnected", "error"]

    workspace_id: str = FieldInfo(alias="workspaceID")

    error: Optional[str] = None


class EventWorkspaceStatus(BaseModel):
    properties: EventWorkspaceStatusProperties

    type: Literal["workspace.status"]


class EventMessageUpdatedProperties(BaseModel):
    info: Message

    session_id: str = FieldInfo(alias="sessionID")


class EventMessageUpdated(BaseModel):
    properties: EventMessageUpdatedProperties

    type: Literal["message.updated"]


class EventMessageRemovedProperties(BaseModel):
    message_id: str = FieldInfo(alias="messageID")

    session_id: str = FieldInfo(alias="sessionID")


class EventMessageRemoved(BaseModel):
    properties: EventMessageRemovedProperties

    type: Literal["message.removed"]


class EventMessagePartUpdatedProperties(BaseModel):
    part: Part

    session_id: str = FieldInfo(alias="sessionID")

    time: float


class EventMessagePartUpdated(BaseModel):
    properties: EventMessagePartUpdatedProperties

    type: Literal["message.part.updated"]


class EventMessagePartRemovedProperties(BaseModel):
    message_id: str = FieldInfo(alias="messageID")

    part_id: str = FieldInfo(alias="partID")

    session_id: str = FieldInfo(alias="sessionID")


class EventMessagePartRemoved(BaseModel):
    properties: EventMessagePartRemovedProperties

    type: Literal["message.part.removed"]


class EventSessionCreatedProperties(BaseModel):
    info: Session

    session_id: str = FieldInfo(alias="sessionID")


class EventSessionCreated(BaseModel):
    properties: EventSessionCreatedProperties

    type: Literal["session.created"]


class EventSessionUpdatedProperties(BaseModel):
    info: Session

    session_id: str = FieldInfo(alias="sessionID")


class EventSessionUpdated(BaseModel):
    properties: EventSessionUpdatedProperties

    type: Literal["session.updated"]


class EventSessionDeletedProperties(BaseModel):
    info: Session

    session_id: str = FieldInfo(alias="sessionID")


class EventSessionDeleted(BaseModel):
    properties: EventSessionDeletedProperties

    type: Literal["session.deleted"]


EventListResponse: TypeAlias = Union[
    EventInstallationUpdated,
    EventInstallationUpdateAvailable,
    EventProjectUpdated,
    EventServerInstanceDisposed,
    EventServerConnected,
    EventGlobalDisposed,
    EventFileEdited,
    EventFileWatcherUpdated,
    EventLspClientDiagnostics,
    EventLspUpdated,
    EventMessagePartDelta,
    EventPermissionAsked,
    EventPermissionReplied,
    EventSessionDiff,
    EventSessionError,
    EventQuestionAsked,
    EventQuestionReplied,
    EventQuestionRejected,
    EventTodoUpdated,
    EventSessionStatus,
    EventSessionIdle,
    EventSessionCompacted,
    EventArtifactCreated,
    EventArtifactDeleted,
    EventTuiPromptAppend,
    EventTuiCommandExecute,
    EventTuiToastShow,
    EventTuiSessionSelect,
    EventMcpToolsChanged,
    EventMcpBrowserOpenFailed,
    EventCommandExecuted,
    EventVcsBranchUpdated,
    EventWorktreeReady,
    EventWorktreeFailed,
    EventPtyCreated,
    EventPtyUpdated,
    EventPtyExited,
    EventPtyDeleted,
    EventWorkspaceReady,
    EventWorkspaceFailed,
    EventWorkspaceStatus,
    EventMessageUpdated,
    EventMessageRemoved,
    EventMessagePartUpdated,
    EventMessagePartRemoved,
    EventSessionCreated,
    EventSessionUpdated,
    EventSessionDeleted,
]
