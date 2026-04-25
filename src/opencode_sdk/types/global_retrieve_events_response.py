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
    "PayloadEventServerConnected",
    "PayloadEventServerConnectedProperties",
    "PayloadEventServerConnectedPropertiesVersion",
    "PayloadEventServerConnectedPropertiesVersionUpstream",
    "PayloadEventGlobalDisposed",
    "PayloadEventFileEdited",
    "PayloadEventFileEditedProperties",
    "PayloadEventFileWatcherUpdated",
    "PayloadEventFileWatcherUpdatedProperties",
    "PayloadEventLspClientDiagnostics",
    "PayloadEventLspClientDiagnosticsProperties",
    "PayloadEventLspUpdated",
    "PayloadEventMessagePartDelta",
    "PayloadEventMessagePartDeltaProperties",
    "PayloadEventPermissionAsked",
    "PayloadEventPermissionAskedProperties",
    "PayloadEventPermissionAskedPropertiesTool",
    "PayloadEventPermissionReplied",
    "PayloadEventPermissionRepliedProperties",
    "PayloadEventSessionDiff",
    "PayloadEventSessionDiffProperties",
    "PayloadEventSessionDiffPropertiesDiff",
    "PayloadEventSessionError",
    "PayloadEventSessionErrorProperties",
    "PayloadEventSessionErrorPropertiesError",
    "PayloadEventSessionErrorPropertiesErrorStructuredOutputError",
    "PayloadEventSessionErrorPropertiesErrorStructuredOutputErrorData",
    "PayloadEventSessionErrorPropertiesErrorContextOverflowError",
    "PayloadEventSessionErrorPropertiesErrorContextOverflowErrorData",
    "PayloadEventSessionErrorPropertiesErrorAPIError",
    "PayloadEventSessionErrorPropertiesErrorAPIErrorData",
    "PayloadEventQuestionAsked",
    "PayloadEventQuestionAskedProperties",
    "PayloadEventQuestionAskedPropertiesQuestion",
    "PayloadEventQuestionAskedPropertiesQuestionOption",
    "PayloadEventQuestionAskedPropertiesTool",
    "PayloadEventQuestionReplied",
    "PayloadEventQuestionRepliedProperties",
    "PayloadEventQuestionRejected",
    "PayloadEventQuestionRejectedProperties",
    "PayloadEventTodoUpdated",
    "PayloadEventTodoUpdatedProperties",
    "PayloadEventSessionStatus",
    "PayloadEventSessionStatusProperties",
    "PayloadEventSessionStatusPropertiesStatus",
    "PayloadEventSessionStatusPropertiesStatusType",
    "PayloadEventSessionStatusPropertiesStatusUnionMember1",
    "PayloadEventSessionStatusPropertiesStatusUnionMember3",
    "PayloadEventSessionStatusPropertiesStatusUnionMember3PendingCall",
    "PayloadEventSessionIdle",
    "PayloadEventSessionIdleProperties",
    "PayloadEventSessionCompacted",
    "PayloadEventSessionCompactedProperties",
    "PayloadEventArtifactCreated",
    "PayloadEventArtifactCreatedProperties",
    "PayloadEventArtifactCreatedPropertiesInfo",
    "PayloadEventArtifactCreatedPropertiesInfoTime",
    "PayloadEventArtifactDeleted",
    "PayloadEventArtifactDeletedProperties",
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
    "PayloadEventMcpBrowserOpenFailed",
    "PayloadEventMcpBrowserOpenFailedProperties",
    "PayloadEventCommandExecuted",
    "PayloadEventCommandExecutedProperties",
    "PayloadEventVcsBranchUpdated",
    "PayloadEventVcsBranchUpdatedProperties",
    "PayloadEventWorktreeReady",
    "PayloadEventWorktreeReadyProperties",
    "PayloadEventWorktreeFailed",
    "PayloadEventWorktreeFailedProperties",
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
    "PayloadEventWorkspaceReady",
    "PayloadEventWorkspaceReadyProperties",
    "PayloadEventWorkspaceFailed",
    "PayloadEventWorkspaceFailedProperties",
    "PayloadEventWorkspaceStatus",
    "PayloadEventWorkspaceStatusProperties",
    "PayloadEventMessageUpdated",
    "PayloadEventMessageUpdatedProperties",
    "PayloadEventMessageRemoved",
    "PayloadEventMessageRemovedProperties",
    "PayloadEventMessagePartUpdated",
    "PayloadEventMessagePartUpdatedProperties",
    "PayloadEventMessagePartRemoved",
    "PayloadEventMessagePartRemovedProperties",
    "PayloadEventSessionCreated",
    "PayloadEventSessionCreatedProperties",
    "PayloadEventSessionUpdated",
    "PayloadEventSessionUpdatedProperties",
    "PayloadEventSessionDeleted",
    "PayloadEventSessionDeletedProperties",
    "PayloadSyncEventMessageUpdated",
    "PayloadSyncEventMessageUpdatedData",
    "PayloadSyncEventMessageRemoved",
    "PayloadSyncEventMessageRemovedData",
    "PayloadSyncEventMessagePartUpdated",
    "PayloadSyncEventMessagePartUpdatedData",
    "PayloadSyncEventMessagePartRemoved",
    "PayloadSyncEventMessagePartRemovedData",
    "PayloadSyncEventSessionCreated",
    "PayloadSyncEventSessionCreatedData",
    "PayloadSyncEventSessionUpdated",
    "PayloadSyncEventSessionUpdatedData",
    "PayloadSyncEventSessionUpdatedDataInfo",
    "PayloadSyncEventSessionUpdatedDataInfoMetadata",
    "PayloadSyncEventSessionUpdatedDataInfoPermission",
    "PayloadSyncEventSessionUpdatedDataInfoRevert",
    "PayloadSyncEventSessionUpdatedDataInfoSummary",
    "PayloadSyncEventSessionUpdatedDataInfoSummaryDiff",
    "PayloadSyncEventSessionUpdatedDataInfoShare",
    "PayloadSyncEventSessionUpdatedDataInfoTime",
    "PayloadSyncEventSessionDeleted",
    "PayloadSyncEventSessionDeletedData",
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


class PayloadEventServerConnectedPropertiesVersionUpstream(BaseModel):
    commit: str

    version: str


class PayloadEventServerConnectedPropertiesVersion(BaseModel):
    api: str

    channel: str

    upstream: PayloadEventServerConnectedPropertiesVersionUpstream

    version: str


class PayloadEventServerConnectedProperties(BaseModel):
    version: PayloadEventServerConnectedPropertiesVersion


class PayloadEventServerConnected(BaseModel):
    properties: PayloadEventServerConnectedProperties

    type: Literal["server.connected"]


class PayloadEventGlobalDisposed(BaseModel):
    properties: object

    type: Literal["global.disposed"]


class PayloadEventFileEditedProperties(BaseModel):
    file: str


class PayloadEventFileEdited(BaseModel):
    properties: PayloadEventFileEditedProperties

    type: Literal["file.edited"]


class PayloadEventFileWatcherUpdatedProperties(BaseModel):
    event: Literal["add", "change", "unlink"]

    file: str


class PayloadEventFileWatcherUpdated(BaseModel):
    properties: PayloadEventFileWatcherUpdatedProperties

    type: Literal["file.watcher.updated"]


class PayloadEventLspClientDiagnosticsProperties(BaseModel):
    path: str

    server_id: str = FieldInfo(alias="serverID")


class PayloadEventLspClientDiagnostics(BaseModel):
    properties: PayloadEventLspClientDiagnosticsProperties

    type: Literal["lsp.client.diagnostics"]


class PayloadEventLspUpdated(BaseModel):
    properties: object

    type: Literal["lsp.updated"]


class PayloadEventMessagePartDeltaProperties(BaseModel):
    delta: str

    field: str

    message_id: str = FieldInfo(alias="messageID")

    part_id: str = FieldInfo(alias="partID")

    session_id: str = FieldInfo(alias="sessionID")


class PayloadEventMessagePartDelta(BaseModel):
    properties: PayloadEventMessagePartDeltaProperties

    type: Literal["message.part.delta"]


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


class PayloadEventSessionDiffPropertiesDiff(BaseModel):
    additions: float

    deletions: float

    file: str

    patch: str

    status: Optional[Literal["added", "deleted", "modified"]] = None


class PayloadEventSessionDiffProperties(BaseModel):
    diff: List[PayloadEventSessionDiffPropertiesDiff]

    session_id: str = FieldInfo(alias="sessionID")


class PayloadEventSessionDiff(BaseModel):
    properties: PayloadEventSessionDiffProperties

    type: Literal["session.diff"]


class PayloadEventSessionErrorPropertiesErrorStructuredOutputErrorData(BaseModel):
    message: str

    retries: float


class PayloadEventSessionErrorPropertiesErrorStructuredOutputError(BaseModel):
    data: PayloadEventSessionErrorPropertiesErrorStructuredOutputErrorData

    name: Literal["StructuredOutputError"]


class PayloadEventSessionErrorPropertiesErrorContextOverflowErrorData(BaseModel):
    message: str

    response_body: Optional[str] = FieldInfo(alias="responseBody", default=None)


class PayloadEventSessionErrorPropertiesErrorContextOverflowError(BaseModel):
    data: PayloadEventSessionErrorPropertiesErrorContextOverflowErrorData

    name: Literal["ContextOverflowError"]


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
    PayloadEventSessionErrorPropertiesErrorStructuredOutputError,
    PayloadEventSessionErrorPropertiesErrorContextOverflowError,
    PayloadEventSessionErrorPropertiesErrorAPIError,
]


class PayloadEventSessionErrorProperties(BaseModel):
    error: Optional[PayloadEventSessionErrorPropertiesError] = None

    session_id: Optional[str] = FieldInfo(alias="sessionID", default=None)


class PayloadEventSessionError(BaseModel):
    properties: PayloadEventSessionErrorProperties

    type: Literal["session.error"]


class PayloadEventQuestionAskedPropertiesQuestionOption(BaseModel):
    description: str
    """Explanation of choice"""

    label: str
    """Display text (1-5 words, concise)"""


class PayloadEventQuestionAskedPropertiesQuestion(BaseModel):
    header: str
    """Very short label (max 30 chars)"""

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


class PayloadEventTodoUpdatedProperties(BaseModel):
    session_id: str = FieldInfo(alias="sessionID")

    todos: List[Todo]


class PayloadEventTodoUpdated(BaseModel):
    properties: PayloadEventTodoUpdatedProperties

    type: Literal["todo.updated"]


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


class PayloadEventSessionCompactedProperties(BaseModel):
    session_id: str = FieldInfo(alias="sessionID")


class PayloadEventSessionCompacted(BaseModel):
    properties: PayloadEventSessionCompactedProperties

    type: Literal["session.compacted"]


class PayloadEventArtifactCreatedPropertiesInfoTime(BaseModel):
    created: float


class PayloadEventArtifactCreatedPropertiesInfo(BaseModel):
    id: str

    filename: str

    hash: str

    mime: str

    session_id: str = FieldInfo(alias="sessionID")

    size: int

    time: PayloadEventArtifactCreatedPropertiesInfoTime

    metadata: Optional[Dict[str, object]] = None


class PayloadEventArtifactCreatedProperties(BaseModel):
    info: PayloadEventArtifactCreatedPropertiesInfo


class PayloadEventArtifactCreated(BaseModel):
    properties: PayloadEventArtifactCreatedProperties

    type: Literal["artifact.created"]


class PayloadEventArtifactDeletedProperties(BaseModel):
    artifact_id: str = FieldInfo(alias="artifactID")

    session_id: str = FieldInfo(alias="sessionID")


class PayloadEventArtifactDeleted(BaseModel):
    properties: PayloadEventArtifactDeletedProperties

    type: Literal["artifact.deleted"]


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


class PayloadEventMcpBrowserOpenFailedProperties(BaseModel):
    mcp_name: str = FieldInfo(alias="mcpName")

    url: str


class PayloadEventMcpBrowserOpenFailed(BaseModel):
    properties: PayloadEventMcpBrowserOpenFailedProperties

    type: Literal["mcp.browser.open.failed"]


class PayloadEventCommandExecutedProperties(BaseModel):
    arguments: str

    message_id: str = FieldInfo(alias="messageID")

    name: str

    session_id: str = FieldInfo(alias="sessionID")


class PayloadEventCommandExecuted(BaseModel):
    properties: PayloadEventCommandExecutedProperties

    type: Literal["command.executed"]


class PayloadEventVcsBranchUpdatedProperties(BaseModel):
    branch: Optional[str] = None


class PayloadEventVcsBranchUpdated(BaseModel):
    properties: PayloadEventVcsBranchUpdatedProperties

    type: Literal["vcs.branch.updated"]


class PayloadEventWorktreeReadyProperties(BaseModel):
    branch: str

    name: str


class PayloadEventWorktreeReady(BaseModel):
    properties: PayloadEventWorktreeReadyProperties

    type: Literal["worktree.ready"]


class PayloadEventWorktreeFailedProperties(BaseModel):
    message: str


class PayloadEventWorktreeFailed(BaseModel):
    properties: PayloadEventWorktreeFailedProperties

    type: Literal["worktree.failed"]


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


class PayloadEventWorkspaceReadyProperties(BaseModel):
    name: str


class PayloadEventWorkspaceReady(BaseModel):
    properties: PayloadEventWorkspaceReadyProperties

    type: Literal["workspace.ready"]


class PayloadEventWorkspaceFailedProperties(BaseModel):
    message: str


class PayloadEventWorkspaceFailed(BaseModel):
    properties: PayloadEventWorkspaceFailedProperties

    type: Literal["workspace.failed"]


class PayloadEventWorkspaceStatusProperties(BaseModel):
    status: Literal["connected", "connecting", "disconnected", "error"]

    workspace_id: str = FieldInfo(alias="workspaceID")

    error: Optional[str] = None


class PayloadEventWorkspaceStatus(BaseModel):
    properties: PayloadEventWorkspaceStatusProperties

    type: Literal["workspace.status"]


class PayloadEventMessageUpdatedProperties(BaseModel):
    info: Message

    session_id: str = FieldInfo(alias="sessionID")


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

    session_id: str = FieldInfo(alias="sessionID")

    time: float


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


class PayloadEventSessionCreatedProperties(BaseModel):
    info: Session

    session_id: str = FieldInfo(alias="sessionID")


class PayloadEventSessionCreated(BaseModel):
    properties: PayloadEventSessionCreatedProperties

    type: Literal["session.created"]


class PayloadEventSessionUpdatedProperties(BaseModel):
    info: Session

    session_id: str = FieldInfo(alias="sessionID")


class PayloadEventSessionUpdated(BaseModel):
    properties: PayloadEventSessionUpdatedProperties

    type: Literal["session.updated"]


class PayloadEventSessionDeletedProperties(BaseModel):
    info: Session

    session_id: str = FieldInfo(alias="sessionID")


class PayloadEventSessionDeleted(BaseModel):
    properties: PayloadEventSessionDeletedProperties

    type: Literal["session.deleted"]


class PayloadSyncEventMessageUpdatedData(BaseModel):
    info: Message

    session_id: str = FieldInfo(alias="sessionID")


class PayloadSyncEventMessageUpdated(BaseModel):
    id: str

    aggregate_id: Literal["sessionID"] = FieldInfo(alias="aggregateID")

    data: PayloadSyncEventMessageUpdatedData

    name: Literal["message.updated.1"]

    seq: float

    type: Literal["sync"]


class PayloadSyncEventMessageRemovedData(BaseModel):
    message_id: str = FieldInfo(alias="messageID")

    session_id: str = FieldInfo(alias="sessionID")


class PayloadSyncEventMessageRemoved(BaseModel):
    id: str

    aggregate_id: Literal["sessionID"] = FieldInfo(alias="aggregateID")

    data: PayloadSyncEventMessageRemovedData

    name: Literal["message.removed.1"]

    seq: float

    type: Literal["sync"]


class PayloadSyncEventMessagePartUpdatedData(BaseModel):
    part: Part

    session_id: str = FieldInfo(alias="sessionID")

    time: float


class PayloadSyncEventMessagePartUpdated(BaseModel):
    id: str

    aggregate_id: Literal["sessionID"] = FieldInfo(alias="aggregateID")

    data: PayloadSyncEventMessagePartUpdatedData

    name: Literal["message.part.updated.1"]

    seq: float

    type: Literal["sync"]


class PayloadSyncEventMessagePartRemovedData(BaseModel):
    message_id: str = FieldInfo(alias="messageID")

    part_id: str = FieldInfo(alias="partID")

    session_id: str = FieldInfo(alias="sessionID")


class PayloadSyncEventMessagePartRemoved(BaseModel):
    id: str

    aggregate_id: Literal["sessionID"] = FieldInfo(alias="aggregateID")

    data: PayloadSyncEventMessagePartRemovedData

    name: Literal["message.part.removed.1"]

    seq: float

    type: Literal["sync"]


class PayloadSyncEventSessionCreatedData(BaseModel):
    info: Session

    session_id: str = FieldInfo(alias="sessionID")


class PayloadSyncEventSessionCreated(BaseModel):
    id: str

    aggregate_id: Literal["sessionID"] = FieldInfo(alias="aggregateID")

    data: PayloadSyncEventSessionCreatedData

    name: Literal["session.created.1"]

    seq: float

    type: Literal["sync"]


class PayloadSyncEventSessionUpdatedDataInfoMetadata(BaseModel):
    extra_info: Optional[Dict[str, str]] = FieldInfo(alias="extraInfo", default=None)

    managed_by: Optional[Literal["tui", "tui-debugger", "sdk", "cc-companion"]] = FieldInfo(
        alias="managedBy", default=None
    )


class PayloadSyncEventSessionUpdatedDataInfoPermission(BaseModel):
    action: Literal["allow", "deny", "ask"]

    pattern: str

    permission: str


class PayloadSyncEventSessionUpdatedDataInfoRevert(BaseModel):
    message_id: str = FieldInfo(alias="messageID")

    diff: Optional[str] = None

    part_id: Optional[str] = FieldInfo(alias="partID", default=None)

    snapshot: Optional[str] = None


class PayloadSyncEventSessionUpdatedDataInfoSummaryDiff(BaseModel):
    additions: float

    deletions: float

    file: str

    patch: str

    status: Optional[Literal["added", "deleted", "modified"]] = None


class PayloadSyncEventSessionUpdatedDataInfoSummary(BaseModel):
    additions: float

    deletions: float

    files: float

    diffs: Optional[List[PayloadSyncEventSessionUpdatedDataInfoSummaryDiff]] = None


class PayloadSyncEventSessionUpdatedDataInfoShare(BaseModel):
    url: Optional[str] = None


class PayloadSyncEventSessionUpdatedDataInfoTime(BaseModel):
    archived: Optional[float] = None

    compacting: Optional[float] = None

    created: Optional[float] = None

    updated: Optional[float] = None


class PayloadSyncEventSessionUpdatedDataInfo(BaseModel):
    id: Optional[str] = None

    directory: Optional[str] = None

    metadata: Optional[PayloadSyncEventSessionUpdatedDataInfoMetadata] = None

    parent_id: Optional[str] = FieldInfo(alias="parentID", default=None)

    permission: Optional[List[PayloadSyncEventSessionUpdatedDataInfoPermission]] = None

    project_id: Optional[str] = FieldInfo(alias="projectID", default=None)

    revert: Optional[PayloadSyncEventSessionUpdatedDataInfoRevert] = None

    slug: Optional[str] = None

    summary: Optional[PayloadSyncEventSessionUpdatedDataInfoSummary] = None

    title: Optional[str] = None

    version: Optional[str] = None

    workspace_id: Optional[str] = FieldInfo(alias="workspaceID", default=None)

    share: Optional[PayloadSyncEventSessionUpdatedDataInfoShare] = None

    time: Optional[PayloadSyncEventSessionUpdatedDataInfoTime] = None


class PayloadSyncEventSessionUpdatedData(BaseModel):
    info: PayloadSyncEventSessionUpdatedDataInfo

    session_id: str = FieldInfo(alias="sessionID")


class PayloadSyncEventSessionUpdated(BaseModel):
    id: str

    aggregate_id: Literal["sessionID"] = FieldInfo(alias="aggregateID")

    data: PayloadSyncEventSessionUpdatedData

    name: Literal["session.updated.1"]

    seq: float

    type: Literal["sync"]


class PayloadSyncEventSessionDeletedData(BaseModel):
    info: Session

    session_id: str = FieldInfo(alias="sessionID")


class PayloadSyncEventSessionDeleted(BaseModel):
    id: str

    aggregate_id: Literal["sessionID"] = FieldInfo(alias="aggregateID")

    data: PayloadSyncEventSessionDeletedData

    name: Literal["session.deleted.1"]

    seq: float

    type: Literal["sync"]


Payload: TypeAlias = Union[
    PayloadEventInstallationUpdated,
    PayloadEventInstallationUpdateAvailable,
    PayloadEventProjectUpdated,
    PayloadEventServerInstanceDisposed,
    PayloadEventServerConnected,
    PayloadEventGlobalDisposed,
    PayloadEventFileEdited,
    PayloadEventFileWatcherUpdated,
    PayloadEventLspClientDiagnostics,
    PayloadEventLspUpdated,
    PayloadEventMessagePartDelta,
    PayloadEventPermissionAsked,
    PayloadEventPermissionReplied,
    PayloadEventSessionDiff,
    PayloadEventSessionError,
    PayloadEventQuestionAsked,
    PayloadEventQuestionReplied,
    PayloadEventQuestionRejected,
    PayloadEventTodoUpdated,
    PayloadEventSessionStatus,
    PayloadEventSessionIdle,
    PayloadEventSessionCompacted,
    PayloadEventArtifactCreated,
    PayloadEventArtifactDeleted,
    PayloadEventTuiPromptAppend,
    PayloadEventTuiCommandExecute,
    PayloadEventTuiToastShow,
    PayloadEventTuiSessionSelect,
    PayloadEventMcpToolsChanged,
    PayloadEventMcpBrowserOpenFailed,
    PayloadEventCommandExecuted,
    PayloadEventVcsBranchUpdated,
    PayloadEventWorktreeReady,
    PayloadEventWorktreeFailed,
    PayloadEventPtyCreated,
    PayloadEventPtyUpdated,
    PayloadEventPtyExited,
    PayloadEventPtyDeleted,
    PayloadEventWorkspaceReady,
    PayloadEventWorkspaceFailed,
    PayloadEventWorkspaceStatus,
    PayloadEventMessageUpdated,
    PayloadEventMessageRemoved,
    PayloadEventMessagePartUpdated,
    PayloadEventMessagePartRemoved,
    PayloadEventSessionCreated,
    PayloadEventSessionUpdated,
    PayloadEventSessionDeleted,
    PayloadSyncEventMessageUpdated,
    PayloadSyncEventMessageRemoved,
    PayloadSyncEventMessagePartUpdated,
    PayloadSyncEventMessagePartRemoved,
    PayloadSyncEventSessionCreated,
    PayloadSyncEventSessionUpdated,
    PayloadSyncEventSessionDeleted,
]


class GlobalRetrieveEventsResponse(BaseModel):
    directory: str

    payload: Payload

    project: Optional[str] = None

    workspace: Optional[str] = None
