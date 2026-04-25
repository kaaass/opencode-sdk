# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["EventToastShow", "Properties"]


class Properties(BaseModel):
    message: str

    variant: Literal["info", "success", "warning", "error"]

    duration: Optional[float] = None
    """Duration in milliseconds"""

    title: Optional[str] = None


class EventToastShow(BaseModel):
    properties: Properties

    type: Literal["tui.toast.show"]
