# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel

__all__ = [
    "AuthAuthenticateResponse",
    "McpStatusConnected",
    "McpStatusDisabled",
    "McpStatusFailed",
    "McpStatusNeedsAuth",
    "McpStatusNeedsClientRegistration",
]


class McpStatusConnected(BaseModel):
    status: Literal["connected"]


class McpStatusDisabled(BaseModel):
    status: Literal["disabled"]


class McpStatusFailed(BaseModel):
    error: str

    status: Literal["failed"]


class McpStatusNeedsAuth(BaseModel):
    status: Literal["needs_auth"]


class McpStatusNeedsClientRegistration(BaseModel):
    error: str

    status: Literal["needs_client_registration"]


AuthAuthenticateResponse: TypeAlias = Union[
    McpStatusConnected, McpStatusDisabled, McpStatusFailed, McpStatusNeedsAuth, McpStatusNeedsClientRegistration
]
