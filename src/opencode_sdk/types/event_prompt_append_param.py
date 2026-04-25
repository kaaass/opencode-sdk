# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["EventPromptAppendParam", "Properties"]


class Properties(TypedDict, total=False):
    text: Required[str]


class EventPromptAppendParam(TypedDict, total=False):
    properties: Required[Properties]

    type: Required[Literal["tui.prompt.append"]]
