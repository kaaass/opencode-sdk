# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = ["ToolListResponse", "ToolListResponseItem"]


class ToolListResponseItem(BaseModel):
    id: str

    description: str

    parameters: object


ToolListResponse: TypeAlias = List[ToolListResponseItem]
