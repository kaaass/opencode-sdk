# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, Union, Optional
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .permission_rule_config import PermissionRuleConfig
from .permission_action_config import PermissionActionConfig

__all__ = ["PermissionConfig", "UnionMember1"]


class UnionMember1(BaseModel):
    bash: Optional[PermissionRuleConfig] = None

    codesearch: Optional[PermissionActionConfig] = None

    doom_loop: Optional[PermissionActionConfig] = None

    edit: Optional[PermissionRuleConfig] = None

    external_directory: Optional[PermissionRuleConfig] = None

    glob: Optional[PermissionRuleConfig] = None

    grep: Optional[PermissionRuleConfig] = None

    list: Optional[PermissionRuleConfig] = None

    lsp: Optional[PermissionRuleConfig] = None

    question: Optional[PermissionActionConfig] = None

    read: Optional[PermissionRuleConfig] = None

    skill: Optional[PermissionRuleConfig] = None

    task: Optional[PermissionRuleConfig] = None

    todowrite: Optional[PermissionActionConfig] = None

    webfetch: Optional[PermissionActionConfig] = None

    websearch: Optional[PermissionActionConfig] = None

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, PermissionRuleConfig] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> PermissionRuleConfig: ...
    else:
        __pydantic_extra__: Dict[str, PermissionRuleConfig]


PermissionConfig: TypeAlias = Union[PermissionActionConfig, UnionMember1]
