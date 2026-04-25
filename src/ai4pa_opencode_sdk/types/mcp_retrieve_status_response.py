# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict
from typing_extensions import TypeAlias

from .mcp.mcp_status import McpStatus

__all__ = ["McpRetrieveStatusResponse"]

McpRetrieveStatusResponse: TypeAlias = Dict[str, McpStatus]
