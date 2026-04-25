# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, TypeAlias, TypedDict

from .shared_params.mcp_local_config import McpLocalConfig
from .shared_params.mcp_remote_config import McpRemoteConfig

__all__ = ["McpCreateParams", "Config"]


class McpCreateParams(TypedDict, total=False):
    config: Required[Config]

    name: Required[str]

    directory: str

    workspace: str


Config: TypeAlias = Union[McpLocalConfig, McpRemoteConfig]
