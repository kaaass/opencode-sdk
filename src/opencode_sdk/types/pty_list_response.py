# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = ["PtyListResponse", "PtyListResponseItem"]


class PtyListResponseItem(BaseModel):
    id: str

    args: List[str]

    command: str

    cwd: str

    pid: float

    status: Literal["running", "exited"]

    title: str


PtyListResponse: TypeAlias = List[PtyListResponseItem]
