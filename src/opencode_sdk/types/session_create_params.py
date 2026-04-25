# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SessionCreateParams", "Permission"]


class SessionCreateParams(TypedDict, total=False):
    directory: str

    workspace: str

    extra_info: Annotated[Dict[str, str], PropertyInfo(alias="extraInfo")]

    managed_by: Annotated[Literal["tui", "tui-debugger", "sdk", "cc-companion"], PropertyInfo(alias="managedBy")]

    parent_id: Annotated[str, PropertyInfo(alias="parentID")]

    permission: Iterable[Permission]

    title: str

    workspace_id: Annotated[str, PropertyInfo(alias="workspaceID")]


class Permission(TypedDict, total=False):
    action: Required[Literal["allow", "deny", "ask"]]

    pattern: Required[str]

    permission: Required[str]
