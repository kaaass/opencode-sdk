# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import TypeAlias

from .mcp_status_failed import McpStatusFailed
from .mcp_status_disabled import McpStatusDisabled
from .mcp_status_connected import McpStatusConnected
from .mcp_status_needs_auth import McpStatusNeedsAuth
from .mcp_status_needs_client_registration import McpStatusNeedsClientRegistration

__all__ = ["McpStatus"]

McpStatus: TypeAlias = Union[
    McpStatusConnected, McpStatusDisabled, McpStatusFailed, McpStatusNeedsAuth, McpStatusNeedsClientRegistration
]
