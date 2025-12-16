# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Union
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = [
    "McpReloadResponse",
    "McpReloadResponseItem",
    "McpReloadResponseItemMcpStatusConnected",
    "McpReloadResponseItemMcpStatusDisabled",
    "McpReloadResponseItemMcpStatusFailed",
    "McpReloadResponseItemMcpStatusNeedsAuth",
    "McpReloadResponseItemMcpStatusNeedsClientRegistration",
]


class McpReloadResponseItemMcpStatusConnected(BaseModel):
    status: Literal["connected"]


class McpReloadResponseItemMcpStatusDisabled(BaseModel):
    status: Literal["disabled"]


class McpReloadResponseItemMcpStatusFailed(BaseModel):
    error: str

    status: Literal["failed"]


class McpReloadResponseItemMcpStatusNeedsAuth(BaseModel):
    status: Literal["needs_auth"]


class McpReloadResponseItemMcpStatusNeedsClientRegistration(BaseModel):
    error: str

    status: Literal["needs_client_registration"]


McpReloadResponseItem: TypeAlias = Union[
    McpReloadResponseItemMcpStatusConnected,
    McpReloadResponseItemMcpStatusDisabled,
    McpReloadResponseItemMcpStatusFailed,
    McpReloadResponseItemMcpStatusNeedsAuth,
    McpReloadResponseItemMcpStatusNeedsClientRegistration,
]

McpReloadResponse: TypeAlias = Dict[str, McpReloadResponseItem]
