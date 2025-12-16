# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = [
    "McpCreateParams",
    "Config",
    "ConfigMcpLocalConfig",
    "ConfigMcpRemoteConfig",
    "ConfigMcpRemoteConfigOAuth",
    "ConfigMcpRemoteConfigOAuthMcpOAuthConfig",
]


class McpCreateParams(TypedDict, total=False):
    config: Required[Config]

    name: Required[str]

    directory: str


class ConfigMcpLocalConfig(TypedDict, total=False):
    command: Required[SequenceNotStr[str]]
    """Command and arguments to run the MCP server"""

    type: Required[Literal["local"]]
    """Type of MCP server connection"""

    enabled: bool
    """Enable or disable the MCP server on startup"""

    environment: Dict[str, str]
    """Environment variables to set when running the MCP server"""

    timeout: int
    """Timeout in ms for fetching tools from the MCP server.

    Defaults to 5000 (5 seconds) if not specified.
    """


class ConfigMcpRemoteConfigOAuthMcpOAuthConfig(TypedDict, total=False):
    client_id: Annotated[str, PropertyInfo(alias="clientId")]
    """OAuth client ID.

    If not provided, dynamic client registration (RFC 7591) will be attempted.
    """

    client_secret: Annotated[str, PropertyInfo(alias="clientSecret")]
    """OAuth client secret (if required by the authorization server)"""

    scope: str
    """OAuth scopes to request during authorization"""


ConfigMcpRemoteConfigOAuth: TypeAlias = Union[ConfigMcpRemoteConfigOAuthMcpOAuthConfig, bool]


class ConfigMcpRemoteConfig(TypedDict, total=False):
    type: Required[Literal["remote"]]
    """Type of MCP server connection"""

    url: Required[str]
    """URL of the remote MCP server"""

    enabled: bool
    """Enable or disable the MCP server on startup"""

    headers: Dict[str, str]
    """Headers to send with the request"""

    oauth: ConfigMcpRemoteConfigOAuth
    """OAuth authentication configuration for the MCP server.

    Set to false to disable OAuth auto-detection.
    """

    timeout: int
    """Timeout in ms for fetching tools from the MCP server.

    Defaults to 5000 (5 seconds) if not specified.
    """


Config: TypeAlias = Union[ConfigMcpLocalConfig, ConfigMcpRemoteConfig]
