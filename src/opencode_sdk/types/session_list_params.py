# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["SessionListParams"]


class SessionListParams(TypedDict, total=False):
    directory: str

    limit: float
    """Maximum number of sessions to return"""

    search: str
    """Filter sessions by title (case-insensitive)"""

    start: float
    """Filter sessions updated on or after this timestamp (milliseconds since epoch)"""
