# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["EventSessionSelectParam", "Properties"]


class Properties(TypedDict, total=False):
    session_id: Required[Annotated[str, PropertyInfo(alias="sessionID")]]
    """Session ID to navigate to"""


class EventSessionSelectParam(TypedDict, total=False):
    properties: Required[Properties]

    type: Required[Literal["tui.session.select"]]
