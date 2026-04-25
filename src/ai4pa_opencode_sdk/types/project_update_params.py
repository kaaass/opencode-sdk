# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ProjectUpdateParams", "Commands", "Icon"]


class ProjectUpdateParams(TypedDict, total=False):
    directory: str

    workspace: str

    commands: Commands

    icon: Icon

    name: str


class Commands(TypedDict, total=False):
    start: str
    """Startup script to run when creating a new workspace (worktree)"""


class Icon(TypedDict, total=False):
    color: str

    override: str

    url: str
