# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["GlobalGetVersionResponse", "Upstream"]


class Upstream(BaseModel):
    commit: str

    version: str


class GlobalGetVersionResponse(BaseModel):
    api: str

    channel: str

    upstream: Upstream

    version: str
