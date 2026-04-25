# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ServerConnected", "Properties", "PropertiesVersion", "PropertiesVersionUpstream"]


class PropertiesVersionUpstream(BaseModel):
    commit: str

    version: str


class PropertiesVersion(BaseModel):
    api: str

    channel: str

    upstream: PropertiesVersionUpstream

    version: str


class Properties(BaseModel):
    version: PropertiesVersion


class ServerConnected(BaseModel):
    properties: Properties

    type: Literal["server.connected"]
