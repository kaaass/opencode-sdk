# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Union
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = [
    "McpCreateResponse",
    "McpCreateResponseItem",
    "McpCreateResponseItemMcpStatusConnected",
    "McpCreateResponseItemMcpStatusDisabled",
    "McpCreateResponseItemMcpStatusFailed",
    "McpCreateResponseItemMcpStatusNeedsAuth",
    "McpCreateResponseItemMcpStatusNeedsClientRegistration",
]


class McpCreateResponseItemMcpStatusConnected(BaseModel):
    status: Literal["connected"]


class McpCreateResponseItemMcpStatusDisabled(BaseModel):
    status: Literal["disabled"]


class McpCreateResponseItemMcpStatusFailed(BaseModel):
    error: str

    status: Literal["failed"]


class McpCreateResponseItemMcpStatusNeedsAuth(BaseModel):
    status: Literal["needs_auth"]


class McpCreateResponseItemMcpStatusNeedsClientRegistration(BaseModel):
    error: str

    status: Literal["needs_client_registration"]


McpCreateResponseItem: TypeAlias = Union[
    McpCreateResponseItemMcpStatusConnected,
    McpCreateResponseItemMcpStatusDisabled,
    McpCreateResponseItemMcpStatusFailed,
    McpCreateResponseItemMcpStatusNeedsAuth,
    McpCreateResponseItemMcpStatusNeedsClientRegistration,
]

McpCreateResponse: TypeAlias = Dict[str, McpCreateResponseItem]
