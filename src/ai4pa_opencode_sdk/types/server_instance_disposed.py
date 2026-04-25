# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ServerInstanceDisposed", "Properties"]


class Properties(BaseModel):
    directory: str


class ServerInstanceDisposed(BaseModel):
    properties: Properties

    type: Literal["server.instance.disposed"]
