# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["ClientToolListResponse", "ClientToolListResponseItem"]


class ClientToolListResponseItem(BaseModel):
    id: str

    description: str

    parameters: Dict[str, object]


ClientToolListResponse: TypeAlias = List[ClientToolListResponseItem]
