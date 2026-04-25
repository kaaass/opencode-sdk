# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["EventToastShowParam", "Properties"]


class Properties(TypedDict, total=False):
    message: Required[str]

    variant: Required[Literal["info", "success", "warning", "error"]]

    duration: float
    """Duration in milliseconds"""

    title: str


class EventToastShowParam(TypedDict, total=False):
    properties: Required[Properties]

    type: Required[Literal["tui.toast.show"]]
