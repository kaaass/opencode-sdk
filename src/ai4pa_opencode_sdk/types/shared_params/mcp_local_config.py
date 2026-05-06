# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["McpLocalConfig"]


class McpLocalConfig(TypedDict, total=False):
    command: Required[SequenceNotStr[str]]
    """Command and arguments to run the MCP server"""

    type: Required[Literal["local"]]
    """Type of MCP server connection"""

    enabled: bool
    """Enable or disable the MCP server on startup"""

    environment: Dict[str, str]
    """Environment variables to set when running the MCP server"""

    timeout: float
    """Timeout in ms for MCP server requests.

    Defaults to 5000 (5 seconds) if not specified.
    """
