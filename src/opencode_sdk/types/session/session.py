# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..permission_rule import PermissionRule
from ..snapshot_file_diff import SnapshotFileDiff

__all__ = ["Session", "Time", "Metadata", "Revert", "Share", "Summary"]


class Time(BaseModel):
    created: float

    updated: float

    archived: Optional[float] = None

    compacting: Optional[float] = None


class Metadata(BaseModel):
    extra_info: Optional[Dict[str, str]] = FieldInfo(alias="extraInfo", default=None)

    managed_by: Optional[Literal["tui", "tui-debugger", "sdk", "cc-companion"]] = FieldInfo(
        alias="managedBy", default=None
    )


class Revert(BaseModel):
    message_id: str = FieldInfo(alias="messageID")

    diff: Optional[str] = None

    part_id: Optional[str] = FieldInfo(alias="partID", default=None)

    snapshot: Optional[str] = None


class Share(BaseModel):
    url: str


class Summary(BaseModel):
    additions: float

    deletions: float

    files: float

    diffs: Optional[List[SnapshotFileDiff]] = None


class Session(BaseModel):
    id: str

    directory: str

    project_id: str = FieldInfo(alias="projectID")

    slug: str

    time: Time

    title: str

    version: str

    metadata: Optional[Metadata] = None

    parent_id: Optional[str] = FieldInfo(alias="parentID", default=None)

    permission: Optional[List[PermissionRule]] = None

    revert: Optional[Revert] = None

    share: Optional[Share] = None

    summary: Optional[Summary] = None

    workspace_id: Optional[str] = FieldInfo(alias="workspaceID", default=None)
