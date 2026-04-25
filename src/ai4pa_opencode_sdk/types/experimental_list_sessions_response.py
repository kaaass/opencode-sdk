# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .permission_rule import PermissionRule
from .snapshot_file_diff import SnapshotFileDiff

__all__ = [
    "ExperimentalListSessionsResponse",
    "ExperimentalListSessionsResponseItem",
    "ExperimentalListSessionsResponseItemProject",
    "ExperimentalListSessionsResponseItemTime",
    "ExperimentalListSessionsResponseItemMetadata",
    "ExperimentalListSessionsResponseItemRevert",
    "ExperimentalListSessionsResponseItemShare",
    "ExperimentalListSessionsResponseItemSummary",
]


class ExperimentalListSessionsResponseItemProject(BaseModel):
    id: str

    worktree: str

    name: Optional[str] = None


class ExperimentalListSessionsResponseItemTime(BaseModel):
    created: float

    updated: float

    archived: Optional[float] = None

    compacting: Optional[float] = None


class ExperimentalListSessionsResponseItemMetadata(BaseModel):
    extra_info: Optional[Dict[str, str]] = FieldInfo(alias="extraInfo", default=None)

    managed_by: Optional[Literal["tui", "tui-debugger", "sdk", "cc-companion"]] = FieldInfo(
        alias="managedBy", default=None
    )


class ExperimentalListSessionsResponseItemRevert(BaseModel):
    message_id: str = FieldInfo(alias="messageID")

    diff: Optional[str] = None

    part_id: Optional[str] = FieldInfo(alias="partID", default=None)

    snapshot: Optional[str] = None


class ExperimentalListSessionsResponseItemShare(BaseModel):
    url: str


class ExperimentalListSessionsResponseItemSummary(BaseModel):
    additions: float

    deletions: float

    files: float

    diffs: Optional[List[SnapshotFileDiff]] = None


class ExperimentalListSessionsResponseItem(BaseModel):
    id: str

    directory: str

    project: Optional[ExperimentalListSessionsResponseItemProject] = None

    project_id: str = FieldInfo(alias="projectID")

    slug: str

    time: ExperimentalListSessionsResponseItemTime

    title: str

    version: str

    metadata: Optional[ExperimentalListSessionsResponseItemMetadata] = None

    parent_id: Optional[str] = FieldInfo(alias="parentID", default=None)

    permission: Optional[List[PermissionRule]] = None

    revert: Optional[ExperimentalListSessionsResponseItemRevert] = None

    share: Optional[ExperimentalListSessionsResponseItemShare] = None

    summary: Optional[ExperimentalListSessionsResponseItemSummary] = None

    workspace_id: Optional[str] = FieldInfo(alias="workspaceID", default=None)


ExperimentalListSessionsResponse: TypeAlias = List[ExperimentalListSessionsResponseItem]
