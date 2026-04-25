# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ToolStateRunning", "Time"]


class Time(BaseModel):
    start: float


class ToolStateRunning(BaseModel):
    input: Dict[str, object]

    status: Literal["running"]

    time: Time

    metadata: Optional[Dict[str, object]] = None

    title: Optional[str] = None
