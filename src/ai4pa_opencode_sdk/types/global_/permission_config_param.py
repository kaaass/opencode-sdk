# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Annotated, TypeAlias, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo
from .permission_action_config import PermissionActionConfig
from .permission_rule_config_param import PermissionRuleConfigParam

__all__ = ["PermissionConfigParam", "UnionMember0"]


class UnionMember0(TypedDict, total=False, extra_items=PermissionRuleConfigParam):  # type: ignore[call-arg]
    _original_keys: Annotated[SequenceNotStr[str], PropertyInfo(alias="__originalKeys")]

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


PermissionConfigParam: TypeAlias = Union[UnionMember0, PermissionActionConfig]
