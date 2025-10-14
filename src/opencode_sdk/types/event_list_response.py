# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .todo import Todo
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
    "EventLspClientDiagnostics",
    "EventLspClientDiagnosticsProperties",
    "EventMessageUpdated",
    "EventMessageUpdatedProperties",
    "EventMessageRemoved",
    "EventMessageRemovedProperties",
    "EventMessagePartUpdated",
    "EventMessagePartUpdatedProperties",
    "EventMessagePartRemoved",
    "EventMessagePartRemovedProperties",
    "EventSessionCompacted",
    "EventSessionCompactedProperties",
    "EventPermissionUpdated",
    "EventPermissionUpdatedProperties",
    "EventPermissionUpdatedPropertiesTime",
    "EventPermissionReplied",
    "EventPermissionRepliedProperties",
    "EventFileEdited",
    "EventFileEditedProperties",
    "EventFileWatcherUpdated",
    "EventFileWatcherUpdatedProperties",
    "EventTodoUpdated",
    "EventTodoUpdatedProperties",
    "EventSessionIdle",
    "EventSessionIdleProperties",
    "EventSessionUpdated",
    "EventSessionUpdatedProperties",
    "EventSessionDeleted",
    "EventSessionDeletedProperties",
    "EventSessionError",
    "EventSessionErrorProperties",
    "EventSessionErrorPropertiesError",
    "EventServerConnected",
    "EventIdeInstalled",
    "EventIdeInstalledProperties",
]


class EventInstallationUpdatedProperties(BaseModel):
    version: str


class EventInstallationUpdated(BaseModel):
    properties: EventInstallationUpdatedProperties

    type: Literal["installation.updated"]


class EventLspClientDiagnosticsProperties(BaseModel):
    path: str

    server_id: str = FieldInfo(alias="serverID")


class EventLspClientDiagnostics(BaseModel):
    properties: EventLspClientDiagnosticsProperties

    type: Literal["lsp.client.diagnostics"]


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


class EventSessionCompactedProperties(BaseModel):
    session_id: str = FieldInfo(alias="sessionID")


class EventSessionCompacted(BaseModel):
    properties: EventSessionCompactedProperties

    type: Literal["session.compacted"]


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


class EventFileWatcherUpdatedProperties(BaseModel):
    event: Literal["add", "change", "unlink"]

    file: str


class EventFileWatcherUpdated(BaseModel):
    properties: EventFileWatcherUpdatedProperties

    type: Literal["file.watcher.updated"]


class EventTodoUpdatedProperties(BaseModel):
    session_id: str = FieldInfo(alias="sessionID")

    todos: List[Todo]


class EventTodoUpdated(BaseModel):
    properties: EventTodoUpdatedProperties

    type: Literal["todo.updated"]


class EventSessionIdleProperties(BaseModel):
    session_id: str = FieldInfo(alias="sessionID")


class EventSessionIdle(BaseModel):
    properties: EventSessionIdleProperties

    type: Literal["session.idle"]


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


EventSessionErrorPropertiesError: TypeAlias = Union[
    ProviderAuthError, UnknownError, MessageOutputLengthError, MessageAbortedError
]


class EventSessionErrorProperties(BaseModel):
    error: Optional[EventSessionErrorPropertiesError] = None

    session_id: Optional[str] = FieldInfo(alias="sessionID", default=None)


class EventSessionError(BaseModel):
    properties: EventSessionErrorProperties

    type: Literal["session.error"]


class EventServerConnected(BaseModel):
    properties: object

    type: Literal["server.connected"]


class EventIdeInstalledProperties(BaseModel):
    ide: str


class EventIdeInstalled(BaseModel):
    properties: EventIdeInstalledProperties

    type: Literal["ide.installed"]


EventListResponse: TypeAlias = Union[
    EventInstallationUpdated,
    EventLspClientDiagnostics,
    EventMessageUpdated,
    EventMessageRemoved,
    EventMessagePartUpdated,
    EventMessagePartRemoved,
    EventSessionCompacted,
    EventPermissionUpdated,
    EventPermissionReplied,
    EventFileEdited,
    EventFileWatcherUpdated,
    EventTodoUpdated,
    EventSessionIdle,
    EventSessionUpdated,
    EventSessionDeleted,
    EventSessionError,
    EventServerConnected,
    EventIdeInstalled,
]
