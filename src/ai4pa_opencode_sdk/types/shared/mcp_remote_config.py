# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Union, Optional
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel
from .mcp_oauth_config import McpOAuthConfig

__all__ = ["McpRemoteConfig", "OAuth"]

OAuth: TypeAlias = Union[McpOAuthConfig, Literal[False]]


class McpRemoteConfig(BaseModel):
    type: Literal["remote"]
    """Type of MCP server connection"""

    url: str
    """URL of the remote MCP server"""

    enabled: Optional[bool] = None
    """Enable or disable the MCP server on startup"""

    headers: Optional[Dict[str, str]] = None
    """Headers to send with the request"""

    oauth: Optional[OAuth] = None
    """OAuth authentication configuration for the MCP server.

    Set to false to disable OAuth auto-detection.
    """

    timeout: Optional[float] = None
    """Timeout in ms for MCP server requests.

    Defaults to 5000 (5 seconds) if not specified.
    """
