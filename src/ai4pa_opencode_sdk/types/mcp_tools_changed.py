# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["McpToolsChanged", "Properties"]


class Properties(BaseModel):
    server: str


class McpToolsChanged(BaseModel):
    properties: Properties

    type: Literal["mcp.tools.changed"]
