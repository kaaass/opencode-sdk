# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .pty import Pty
from .._models import BaseModel

__all__ = ["PtyCreated", "Properties"]


class Properties(BaseModel):
    info: Pty


class PtyCreated(BaseModel):
    properties: Properties

    type: Literal["pty.created"]
