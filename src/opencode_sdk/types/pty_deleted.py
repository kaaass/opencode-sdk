# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["PtyDeleted", "Properties"]


class Properties(BaseModel):
    id: str


class PtyDeleted(BaseModel):
    properties: Properties

    type: Literal["pty.deleted"]
