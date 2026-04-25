# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["MessageGetAllParams"]


class MessageGetAllParams(TypedDict, total=False):
    before: str

    directory: str

    limit: int
    """Maximum number of messages to return"""

    workspace: str
