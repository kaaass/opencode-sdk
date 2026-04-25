# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo
from .permission_rule_param import PermissionRuleParam

__all__ = ["SessionCreateParams"]


class SessionCreateParams(TypedDict, total=False):
    directory: str

    workspace: str

    extra_info: Annotated[Dict[str, str], PropertyInfo(alias="extraInfo")]

    managed_by: Annotated[Literal["tui", "tui-debugger", "sdk", "cc-companion"], PropertyInfo(alias="managedBy")]

    parent_id: Annotated[str, PropertyInfo(alias="parentID")]

    permission: Iterable[PermissionRuleParam]

    title: str

    workspace_id: Annotated[str, PropertyInfo(alias="workspaceID")]
