# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["WorkspaceCreateParams"]


class WorkspaceCreateParams(TypedDict, total=False):
    branch: Required[Optional[str]]

    extra: Required[object]

    type: Required[str]

    directory: str

    workspace: str

    id: str
