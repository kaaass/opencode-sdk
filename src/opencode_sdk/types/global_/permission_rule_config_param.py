# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from typing_extensions import TypeAlias

from .permission_action_config import PermissionActionConfig

__all__ = ["PermissionRuleConfigParam"]

PermissionRuleConfigParam: TypeAlias = Union[PermissionActionConfig, Dict[str, PermissionActionConfig]]
