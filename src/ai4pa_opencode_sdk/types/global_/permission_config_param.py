# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import TypeAlias, TypedDict

from .permission_action_config import PermissionActionConfig
from .permission_rule_config_param import PermissionRuleConfigParam

__all__ = ["PermissionConfigParam", "UnionMember1"]


class UnionMember1(  # type: ignore[call-arg]
    TypedDict,
    total=False,
    extra_items=PermissionRuleConfigParam,  # pyright: ignore[reportGeneralTypeIssues]
):
    bash: PermissionRuleConfigParam

    codesearch: PermissionActionConfig

    doom_loop: PermissionActionConfig

    edit: PermissionRuleConfigParam

    external_directory: PermissionRuleConfigParam

    glob: PermissionRuleConfigParam

    grep: PermissionRuleConfigParam

    list: PermissionRuleConfigParam

    lsp: PermissionRuleConfigParam

    question: PermissionActionConfig

    read: PermissionRuleConfigParam

    skill: PermissionRuleConfigParam

    task: PermissionRuleConfigParam

    todowrite: PermissionActionConfig

    webfetch: PermissionActionConfig

    websearch: PermissionActionConfig


PermissionConfigParam: TypeAlias = Union[PermissionActionConfig, UnionMember1]
