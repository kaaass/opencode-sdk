# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .pty import Pty
from .._models import BaseModel

__all__ = ["PtyUpdated", "Properties"]


class Properties(BaseModel):
    info: Pty


class PtyUpdated(BaseModel):
    properties: Properties

    type: Literal["pty.updated"]
