# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["WorktreeFailed", "Properties"]


class Properties(BaseModel):
    message: str


class WorktreeFailed(BaseModel):
    properties: Properties

    type: Literal["worktree.failed"]
