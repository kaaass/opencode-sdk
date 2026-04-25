# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from ...._models import BaseModel
from ...file_part import FilePart

__all__ = ["ToolStateCompleted", "Time"]


class Time(BaseModel):
    end: float

    start: float

    compacted: Optional[float] = None


class ToolStateCompleted(BaseModel):
    input: Dict[str, object]

    metadata: Dict[str, object]

    output: str

    status: Literal["completed"]

    time: Time

    title: str

    attachments: Optional[List[FilePart]] = None
