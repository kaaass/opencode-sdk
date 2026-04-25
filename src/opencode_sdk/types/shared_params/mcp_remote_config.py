# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .mcp_oauth_config import McpOAuthConfig

__all__ = ["McpRemoteConfig", "OAuth"]

OAuth: TypeAlias = Union[McpOAuthConfig, Literal[False]]


class McpRemoteConfig(TypedDict, total=False):
    type: Required[Literal["remote"]]
    """Type of MCP server connection"""

    url: Required[str]
    """URL of the remote MCP server"""

    enabled: bool
    """Enable or disable the MCP server on startup"""

    headers: Dict[str, str]
    """Headers to send with the request"""

    oauth: OAuth
    """OAuth authentication configuration for the MCP server.

    Set to false to disable OAuth auto-detection.
    """

    timeout: int
    """Timeout in ms for MCP server requests.

    Defaults to 5000 (5 seconds) if not specified.
    """
