# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["OAuthHandleCallbackParams"]


class OAuthHandleCallbackParams(TypedDict, total=False):
    method: Required[float]
    """Auth method index"""

    directory: str

    code: str
    """OAuth authorization code"""
