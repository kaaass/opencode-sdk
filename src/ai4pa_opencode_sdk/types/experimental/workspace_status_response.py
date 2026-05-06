# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["WorkspaceStatusResponse", "WorkspaceStatusResponseItem"]


class WorkspaceStatusResponseItem(BaseModel):
    status: Literal["connected", "connecting", "disconnected", "error"]

    workspace_id: str = FieldInfo(alias="workspaceID")


WorkspaceStatusResponse: TypeAlias = List[WorkspaceStatusResponseItem]
