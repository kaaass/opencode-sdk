# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["WorktreeCreateParams"]


class WorktreeCreateParams(TypedDict, total=False):
    directory: str

    name: str

    start_command: Annotated[str, PropertyInfo(alias="startCommand")]
