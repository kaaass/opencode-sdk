# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = ["VcRetrieveDiffResponse", "VcRetrieveDiffResponseItem"]


class VcRetrieveDiffResponseItem(BaseModel):
    additions: float

    deletions: float

    file: str

    patch: str

    status: Optional[Literal["added", "deleted", "modified"]] = None


VcRetrieveDiffResponse: TypeAlias = List[VcRetrieveDiffResponseItem]
