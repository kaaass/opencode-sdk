# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AuthCompleteOAuthParams"]


class AuthCompleteOAuthParams(TypedDict, total=False):
    code: Required[str]
    """Authorization code from OAuth callback"""

    directory: str

    workspace: str
