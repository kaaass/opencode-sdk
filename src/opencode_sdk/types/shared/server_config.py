# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ServerConfig"]


class ServerConfig(BaseModel):
    """Server configuration for opencode serve and web commands"""

    cors: Optional[List[str]] = None
    """Additional domains to allow for CORS"""

    hostname: Optional[str] = None
    """Hostname to listen on"""

    mdns: Optional[bool] = None
    """Enable mDNS service discovery"""

    mdns_domain: Optional[str] = FieldInfo(alias="mdnsDomain", default=None)
    """Custom domain name for mDNS service (default: opencode.local)"""

    port: Optional[int] = None
    """Port to listen on"""
