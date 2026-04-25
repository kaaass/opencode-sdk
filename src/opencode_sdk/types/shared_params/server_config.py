# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["ServerConfig"]


class ServerConfig(TypedDict, total=False):
    """Server configuration for opencode serve and web commands"""

    cors: SequenceNotStr[str]
    """Additional domains to allow for CORS"""

    hostname: str
    """Hostname to listen on"""

    mdns: bool
    """Enable mDNS service discovery"""

    mdns_domain: Annotated[str, PropertyInfo(alias="mdnsDomain")]
    """Custom domain name for mDNS service (default: opencode.local)"""

    port: int
    """Port to listen on"""
