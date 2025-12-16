# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["RemoteToolListResponse", "RemoteToolListResponseItem"]


class RemoteToolListResponseItem(BaseModel):
    id: str

    description: str

    parameters: Dict[str, object]


RemoteToolListResponse: TypeAlias = List[RemoteToolListResponseItem]
