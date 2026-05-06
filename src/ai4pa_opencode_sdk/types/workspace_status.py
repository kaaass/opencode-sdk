# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["WorkspaceStatus", "Properties"]


class Properties(BaseModel):
    status: Literal["connected", "connecting", "disconnected", "error"]

    workspace_id: str = FieldInfo(alias="workspaceID")


class WorkspaceStatus(BaseModel):
    properties: Properties

    type: Literal["workspace.status"]
