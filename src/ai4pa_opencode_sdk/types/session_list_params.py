# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["SessionListParams"]


class SessionListParams(TypedDict, total=False):
    directory: str
    """Filter sessions by project directory"""

    limit: float
    """Maximum number of sessions to return"""

    roots: bool
    """Only return root sessions (no parentID)"""

    search: str
    """Filter sessions by title (case-insensitive)"""

    start: float
    """Filter sessions updated on or after this timestamp (milliseconds since epoch)"""

    workspace: str
