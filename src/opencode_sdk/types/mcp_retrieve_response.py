# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Union
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = [
    "McpRetrieveResponse",
    "McpRetrieveResponseItem",
    "McpRetrieveResponseItemMcpStatusConnected",
    "McpRetrieveResponseItemMcpStatusDisabled",
    "McpRetrieveResponseItemMcpStatusFailed",
    "McpRetrieveResponseItemMcpStatusNeedsAuth",
    "McpRetrieveResponseItemMcpStatusNeedsClientRegistration",
]


class McpRetrieveResponseItemMcpStatusConnected(BaseModel):
    status: Literal["connected"]


class McpRetrieveResponseItemMcpStatusDisabled(BaseModel):
    status: Literal["disabled"]


class McpRetrieveResponseItemMcpStatusFailed(BaseModel):
    error: str

    status: Literal["failed"]


class McpRetrieveResponseItemMcpStatusNeedsAuth(BaseModel):
    status: Literal["needs_auth"]


class McpRetrieveResponseItemMcpStatusNeedsClientRegistration(BaseModel):
    error: str

    status: Literal["needs_client_registration"]


McpRetrieveResponseItem: TypeAlias = Union[
    McpRetrieveResponseItemMcpStatusConnected,
    McpRetrieveResponseItemMcpStatusDisabled,
    McpRetrieveResponseItemMcpStatusFailed,
    McpRetrieveResponseItemMcpStatusNeedsAuth,
    McpRetrieveResponseItemMcpStatusNeedsClientRegistration,
]

McpRetrieveResponse: TypeAlias = Dict[str, McpRetrieveResponseItem]
