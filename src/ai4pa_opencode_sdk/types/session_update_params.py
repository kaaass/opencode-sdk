# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import TypedDict

from .permission_rule_param import PermissionRuleParam

__all__ = ["SessionUpdateParams", "Time"]


class SessionUpdateParams(TypedDict, total=False):
    directory: str

    workspace: str

    permission: Iterable[PermissionRuleParam]

    time: Time

    title: str


class Time(TypedDict, total=False):
    archived: float
