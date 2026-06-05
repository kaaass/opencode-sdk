# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .pty_exited import PtyExited
from .file_edited import FileEdited
from .lsp_updated import LspUpdated
from .pty_created import PtyCreated
from .pty_deleted import PtyDeleted
from .pty_updated import PtyUpdated
from .session_diff import SessionDiff
from .session_idle import SessionIdle
from .todo_updated import TodoUpdated
from .session_error import SessionError
from .question_asked import QuestionAsked
from .worktree_ready import WorktreeReady
from .global_disposed import GlobalDisposed
from .message_removed import MessageRemoved
from .message_updated import MessageUpdated
from .permission_rule import PermissionRule
from .project_updated import ProjectUpdated
from .session.session import Session
from .session_created import SessionCreated
from .session_deleted import SessionDeleted
from .session_updated import SessionUpdated
from .workspace_ready import WorkspaceReady
from .worktree_failed import WorktreeFailed
from .artifact_created import ArtifactCreated
from .artifact_deleted import ArtifactDeleted
from .command_executed import CommandExecuted
from .event_toast_show import EventToastShow
from .permission_asked import PermissionAsked
from .question_replied import QuestionReplied
from .server_connected import ServerConnected
from .workspace_failed import WorkspaceFailed
from .workspace_status import WorkspaceStatus
from .mcp_tools_changed import McpToolsChanged
from .question_rejected import QuestionRejected
from .session_compacted import SessionCompacted
from .message_part_delta import MessagePartDelta
from .permission_replied import PermissionReplied
from .snapshot_file_diff import SnapshotFileDiff
from .vcs_branch_updated import VcsBranchUpdated
from .event_prompt_append import EventPromptAppend
from .event_session_select import EventSessionSelect
from .file_watcher_updated import FileWatcherUpdated
from .installation_updated import InstallationUpdated
from .message_part_removed import MessagePartRemoved
from .message_part_updated import MessagePartUpdated
from .session.message.part import Part
from .session_event_status import SessionEventStatus
from .event_command_execute import EventCommandExecute
from .lsp_client_diagnostics import LspClientDiagnostics
from .mcp_browser_open_failed import McpBrowserOpenFailed
from .session.message.message import Message
from .server_instance_disposed import ServerInstanceDisposed
from .installation_update_available import InstallationUpdateAvailable

__all__ = [
    "GlobalGetEventsResponse",
    "Payload",
    "PayloadEventSkillClientChanged",
    "PayloadEventWorkspaceRestore",
    "PayloadEventWorkspaceRestoreProperties",
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
    "PayloadSyncEventSessionUpdatedDataInfoRevert",
    "PayloadSyncEventSessionUpdatedDataInfoShare",
    "PayloadSyncEventSessionUpdatedDataInfoSummary",
    "PayloadSyncEventSessionUpdatedDataInfoTime",
    "PayloadSyncEventSessionDeleted",
    "PayloadSyncEventSessionDeletedData",
]


class PayloadEventSkillClientChanged(BaseModel):
    properties: object

    type: Literal["skill.client.changed"]


class PayloadEventWorkspaceRestoreProperties(BaseModel):
    session_id: str = FieldInfo(alias="sessionID")

    step: int

    total: int

    workspace_id: str = FieldInfo(alias="workspaceID")


class PayloadEventWorkspaceRestore(BaseModel):
    properties: PayloadEventWorkspaceRestoreProperties

    type: Literal["workspace.restore"]


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


class PayloadSyncEventSessionUpdatedDataInfoRevert(BaseModel):
    message_id: str = FieldInfo(alias="messageID")

    diff: Optional[str] = None

    part_id: Optional[str] = FieldInfo(alias="partID", default=None)

    snapshot: Optional[str] = None


class PayloadSyncEventSessionUpdatedDataInfoShare(BaseModel):
    url: Optional[str] = None


class PayloadSyncEventSessionUpdatedDataInfoSummary(BaseModel):
    additions: float

    deletions: float

    files: float

    diffs: Optional[List[SnapshotFileDiff]] = None


class PayloadSyncEventSessionUpdatedDataInfoTime(BaseModel):
    archived: Optional[float] = None

    compacting: Optional[float] = None

    created: Optional[float] = None

    updated: Optional[float] = None


class PayloadSyncEventSessionUpdatedDataInfo(BaseModel):
    id: Optional[str] = None

    directory: Optional[str] = None

    parent_id: Optional[str] = FieldInfo(alias="parentID", default=None)

    permission: Optional[List[PermissionRule]] = None

    project_id: Optional[str] = FieldInfo(alias="projectID", default=None)

    revert: Optional[PayloadSyncEventSessionUpdatedDataInfoRevert] = None

    share: Optional[PayloadSyncEventSessionUpdatedDataInfoShare] = None

    slug: Optional[str] = None

    summary: Optional[PayloadSyncEventSessionUpdatedDataInfoSummary] = None

    time: Optional[PayloadSyncEventSessionUpdatedDataInfoTime] = None

    title: Optional[str] = None

    version: Optional[str] = None

    workspace_id: Optional[str] = FieldInfo(alias="workspaceID", default=None)


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
    InstallationUpdated,
    InstallationUpdateAvailable,
    ProjectUpdated,
    ServerInstanceDisposed,
    ServerConnected,
    GlobalDisposed,
    FileEdited,
    FileWatcherUpdated,
    LspClientDiagnostics,
    LspUpdated,
    MessagePartDelta,
    PermissionAsked,
    PermissionReplied,
    SessionDiff,
    SessionError,
    QuestionAsked,
    QuestionReplied,
    QuestionRejected,
    ArtifactCreated,
    ArtifactDeleted,
    TodoUpdated,
    PayloadEventSkillClientChanged,
    SessionEventStatus,
    SessionIdle,
    SessionCompacted,
    EventPromptAppend,
    EventCommandExecute,
    EventToastShow,
    EventSessionSelect,
    McpToolsChanged,
    McpBrowserOpenFailed,
    CommandExecuted,
    VcsBranchUpdated,
    WorktreeReady,
    WorktreeFailed,
    PtyCreated,
    PtyUpdated,
    PtyExited,
    PtyDeleted,
    WorkspaceReady,
    WorkspaceFailed,
    PayloadEventWorkspaceRestore,
    WorkspaceStatus,
    MessageUpdated,
    MessageRemoved,
    MessagePartUpdated,
    MessagePartRemoved,
    SessionCreated,
    SessionUpdated,
    SessionDeleted,
    PayloadSyncEventMessageUpdated,
    PayloadSyncEventMessageRemoved,
    PayloadSyncEventMessagePartUpdated,
    PayloadSyncEventMessagePartRemoved,
    PayloadSyncEventSessionCreated,
    PayloadSyncEventSessionUpdated,
    PayloadSyncEventSessionDeleted,
]


class GlobalGetEventsResponse(BaseModel):
    directory: str

    payload: Payload

    project: Optional[str] = None

    workspace: Optional[str] = None
