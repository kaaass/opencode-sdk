# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ToolListToolsParams"]


class ToolListToolsParams(TypedDict, total=False):
    model: Required[str]

    provider: Required[str]

    directory: str
