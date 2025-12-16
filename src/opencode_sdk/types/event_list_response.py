# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .todo import Todo
from .project import Project
from .._models import BaseModel
from .session.part import Part
from .unknown_error import UnknownError
from .session.message import Message
from .session.session import Session
from .provider_auth_error import ProviderAuthError
from .message_aborted_error import MessageAbortedError
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
    "EventLspClientDiagnostics",
    "EventLspClientDiagnosticsProperties",
    "EventLspUpdated",
    "EventMessageUpdated",
    "EventMessageUpdatedProperties",
    "EventMessageRemoved",
    "EventMessageRemovedProperties",
    "EventMessagePartUpdated",
    "EventMessagePartUpdatedProperties",
    "EventMessagePartRemoved",
    "EventMessagePartRemovedProperties",
    "EventPermissionUpdated",
    "EventPermissionUpdatedProperties",
    "EventPermissionUpdatedPropertiesTime",
    "EventPermissionReplied",
    "EventPermissionRepliedProperties",
    "EventFileEdited",
    "EventFileEditedProperties",
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
    "EventCommandExecuted",
    "EventCommandExecutedProperties",
    "EventSessionCreated",
    "EventSessionCreatedProperties",
    "EventSessionUpdated",
    "EventSessionUpdatedProperties",
    "EventSessionDeleted",
    "EventSessionDeletedProperties",
    "EventSessionDiff",
    "EventSessionDiffProperties",
    "EventSessionDiffPropertiesDiff",
    "EventSessionError",
    "EventSessionErrorProperties",
    "EventSessionErrorPropertiesError",
    "EventSessionErrorPropertiesErrorAPIError",
    "EventSessionErrorPropertiesErrorAPIErrorData",
    "EventFileWatcherUpdated",
    "EventFileWatcherUpdatedProperties",
    "EventVcsBranchUpdated",
    "EventVcsBranchUpdatedProperties",
    "EventTuiPromptAppend",
    "EventTuiPromptAppendProperties",
    "EventTuiCommandExecute",
    "EventTuiCommandExecuteProperties",
    "EventTuiToastShow",
    "EventTuiToastShowProperties",
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
    "EventServerConnected",
    "EventGlobalDisposed",
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


class EventLspClientDiagnosticsProperties(BaseModel):
    path: str

    server_id: str = FieldInfo(alias="serverID")


class EventLspClientDiagnostics(BaseModel):
    properties: EventLspClientDiagnosticsProperties

    type: Literal["lsp.client.diagnostics"]


class EventLspUpdated(BaseModel):
    properties: object

    type: Literal["lsp.updated"]


class EventMessageUpdatedProperties(BaseModel):
    info: Message


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

    delta: Optional[str] = None


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


class EventPermissionUpdatedPropertiesTime(BaseModel):
    created: float


class EventPermissionUpdatedProperties(BaseModel):
    id: str

    message_id: str = FieldInfo(alias="messageID")

    metadata: Dict[str, object]

    session_id: str = FieldInfo(alias="sessionID")

    time: EventPermissionUpdatedPropertiesTime

    title: str

    type: str

    call_id: Optional[str] = FieldInfo(alias="callID", default=None)

    pattern: Union[str, List[str], None] = None


class EventPermissionUpdated(BaseModel):
    properties: EventPermissionUpdatedProperties

    type: Literal["permission.updated"]


class EventPermissionRepliedProperties(BaseModel):
    permission_id: str = FieldInfo(alias="permissionID")

    response: str

    session_id: str = FieldInfo(alias="sessionID")


class EventPermissionReplied(BaseModel):
    properties: EventPermissionRepliedProperties

    type: Literal["permission.replied"]


class EventFileEditedProperties(BaseModel):
    file: str


class EventFileEdited(BaseModel):
    properties: EventFileEditedProperties

    type: Literal["file.edited"]


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


class EventCommandExecutedProperties(BaseModel):
    arguments: str

    message_id: str = FieldInfo(alias="messageID")

    name: str

    session_id: str = FieldInfo(alias="sessionID")


class EventCommandExecuted(BaseModel):
    properties: EventCommandExecutedProperties

    type: Literal["command.executed"]


class EventSessionCreatedProperties(BaseModel):
    info: Session


class EventSessionCreated(BaseModel):
    properties: EventSessionCreatedProperties

    type: Literal["session.created"]


class EventSessionUpdatedProperties(BaseModel):
    info: Session


class EventSessionUpdated(BaseModel):
    properties: EventSessionUpdatedProperties

    type: Literal["session.updated"]


class EventSessionDeletedProperties(BaseModel):
    info: Session


class EventSessionDeleted(BaseModel):
    properties: EventSessionDeletedProperties

    type: Literal["session.deleted"]


class EventSessionDiffPropertiesDiff(BaseModel):
    additions: float

    after: str

    before: str

    deletions: float

    file: str


class EventSessionDiffProperties(BaseModel):
    diff: List[EventSessionDiffPropertiesDiff]

    session_id: str = FieldInfo(alias="sessionID")


class EventSessionDiff(BaseModel):
    properties: EventSessionDiffProperties

    type: Literal["session.diff"]


class EventSessionErrorPropertiesErrorAPIErrorData(BaseModel):
    is_retryable: bool = FieldInfo(alias="isRetryable")

    message: str

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
    EventSessionErrorPropertiesErrorAPIError,
]


class EventSessionErrorProperties(BaseModel):
    error: Optional[EventSessionErrorPropertiesError] = None

    session_id: Optional[str] = FieldInfo(alias="sessionID", default=None)


class EventSessionError(BaseModel):
    properties: EventSessionErrorProperties

    type: Literal["session.error"]


class EventFileWatcherUpdatedProperties(BaseModel):
    event: Literal["add", "change", "unlink"]

    file: str


class EventFileWatcherUpdated(BaseModel):
    properties: EventFileWatcherUpdatedProperties

    type: Literal["file.watcher.updated"]


class EventVcsBranchUpdatedProperties(BaseModel):
    branch: Optional[str] = None


class EventVcsBranchUpdated(BaseModel):
    properties: EventVcsBranchUpdatedProperties

    type: Literal["vcs.branch.updated"]


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


class EventServerConnected(BaseModel):
    properties: object

    type: Literal["server.connected"]


class EventGlobalDisposed(BaseModel):
    properties: object

    type: Literal["global.disposed"]


EventListResponse: TypeAlias = Union[
    EventInstallationUpdated,
    EventInstallationUpdateAvailable,
    EventProjectUpdated,
    EventServerInstanceDisposed,
    EventLspClientDiagnostics,
    EventLspUpdated,
    EventMessageUpdated,
    EventMessageRemoved,
    EventMessagePartUpdated,
    EventMessagePartRemoved,
    EventPermissionUpdated,
    EventPermissionReplied,
    EventFileEdited,
    EventTodoUpdated,
    EventSessionStatus,
    EventSessionIdle,
    EventSessionCompacted,
    EventCommandExecuted,
    EventSessionCreated,
    EventSessionUpdated,
    EventSessionDeleted,
    EventSessionDiff,
    EventSessionError,
    EventFileWatcherUpdated,
    EventVcsBranchUpdated,
    EventTuiPromptAppend,
    EventTuiCommandExecute,
    EventTuiToastShow,
    EventPtyCreated,
    EventPtyUpdated,
    EventPtyExited,
    EventPtyDeleted,
    EventServerConnected,
    EventGlobalDisposed,
]
