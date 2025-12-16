# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["SessionGetDiffResponse", "SessionGetDiffResponseItem"]


class SessionGetDiffResponseItem(BaseModel):
    additions: float

    after: str

    before: str

    deletions: float

    file: str


SessionGetDiffResponse: TypeAlias = List[SessionGetDiffResponseItem]
