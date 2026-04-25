# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["McpOAuthConfig"]


class McpOAuthConfig(TypedDict, total=False):
    client_id: Annotated[str, PropertyInfo(alias="clientId")]
    """OAuth client ID.

    If not provided, dynamic client registration (RFC 7591) will be attempted.
    """

    client_secret: Annotated[str, PropertyInfo(alias="clientSecret")]
    """OAuth client secret (if required by the authorization server)"""

    redirect_uri: Annotated[str, PropertyInfo(alias="redirectUri")]
    """OAuth redirect URI (default: http://127.0.0.1:19876/mcp/oauth/callback)."""

    scope: str
    """OAuth scopes to request during authorization"""
