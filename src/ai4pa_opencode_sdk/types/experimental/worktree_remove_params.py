# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["WorktreeRemoveParams"]


class WorktreeRemoveParams(TypedDict, total=False):
    body_directory: Required[Annotated[str, PropertyInfo(alias="directory")]]

    query_directory: Annotated[str, PropertyInfo(alias="directory")]

    workspace: str
