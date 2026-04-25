# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["McpOAuthConfig"]


class McpOAuthConfig(BaseModel):
    client_id: Optional[str] = FieldInfo(alias="clientId", default=None)
    """OAuth client ID.

    If not provided, dynamic client registration (RFC 7591) will be attempted.
    """

    client_secret: Optional[str] = FieldInfo(alias="clientSecret", default=None)
    """OAuth client secret (if required by the authorization server)"""

    redirect_uri: Optional[str] = FieldInfo(alias="redirectUri", default=None)
    """OAuth redirect URI (default: http://127.0.0.1:19876/mcp/oauth/callback)."""

    scope: Optional[str] = None
    """OAuth scopes to request during authorization"""
