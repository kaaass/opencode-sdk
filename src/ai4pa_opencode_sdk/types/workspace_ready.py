# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["WorkspaceReady", "Properties"]


class Properties(BaseModel):
    name: str


class WorkspaceReady(BaseModel):
    properties: Properties

    type: Literal["workspace.ready"]
