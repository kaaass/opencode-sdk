# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["McpBrowserOpenFailed", "Properties"]


class Properties(BaseModel):
    mcp_name: str = FieldInfo(alias="mcpName")

    url: str


class McpBrowserOpenFailed(BaseModel):
    properties: Properties

    type: Literal["mcp.browser.open.failed"]
