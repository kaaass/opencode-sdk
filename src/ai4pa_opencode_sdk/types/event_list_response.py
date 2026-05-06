# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
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
from .project_updated import ProjectUpdated
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
from .vcs_branch_updated import VcsBranchUpdated
from .event_prompt_append import EventPromptAppend
from .event_session_select import EventSessionSelect
from .file_watcher_updated import FileWatcherUpdated
from .installation_updated import InstallationUpdated
from .message_part_removed import MessagePartRemoved
from .message_part_updated import MessagePartUpdated
from .session_event_status import SessionEventStatus
from .event_command_execute import EventCommandExecute
from .lsp_client_diagnostics import LspClientDiagnostics
from .mcp_browser_open_failed import McpBrowserOpenFailed
from .server_instance_disposed import ServerInstanceDisposed
from .installation_update_available import InstallationUpdateAvailable

__all__ = ["EventListResponse", "EventWorkspaceRestore", "EventWorkspaceRestoreProperties"]


class EventWorkspaceRestoreProperties(BaseModel):
    session_id: str = FieldInfo(alias="sessionID")

    step: int

    total: int

    workspace_id: str = FieldInfo(alias="workspaceID")


class EventWorkspaceRestore(BaseModel):
    properties: EventWorkspaceRestoreProperties

    type: Literal["workspace.restore"]


EventListResponse: TypeAlias = Union[
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
    EventWorkspaceRestore,
    WorkspaceStatus,
    MessageUpdated,
    MessageRemoved,
    MessagePartUpdated,
    MessagePartRemoved,
    SessionCreated,
    SessionUpdated,
    SessionDeleted,
]
