# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .snapshot_file_diff import SnapshotFileDiff

__all__ = ["SessionDiff", "Properties"]


class Properties(BaseModel):
    diff: List[SnapshotFileDiff]

    session_id: str = FieldInfo(alias="sessionID")


class SessionDiff(BaseModel):
    properties: Properties

    type: Literal["session.diff"]
