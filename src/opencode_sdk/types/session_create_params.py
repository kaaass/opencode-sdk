# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SessionCreateParams", "Permission"]


class SessionCreateParams(TypedDict, total=False):
    directory: str

    parent_id: Annotated[str, PropertyInfo(alias="parentID")]

    permission: Iterable[Permission]

    title: str


class Permission(TypedDict, total=False):
    action: Required[Literal["allow", "deny", "ask"]]

    pattern: Required[str]

    permission: Required[str]
