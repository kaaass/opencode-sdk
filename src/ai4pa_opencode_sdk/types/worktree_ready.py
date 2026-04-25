# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["WorktreeReady", "Properties"]


class Properties(BaseModel):
    branch: str

    name: str


class WorktreeReady(BaseModel):
    properties: Properties

    type: Literal["worktree.ready"]
