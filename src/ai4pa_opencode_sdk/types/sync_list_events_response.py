# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["SyncListEventsResponse", "SyncListEventsResponseItem"]


class SyncListEventsResponseItem(BaseModel):
    id: str

    aggregate_id: str

    data: Dict[str, object]

    seq: float

    type: str


SyncListEventsResponse: TypeAlias = List[SyncListEventsResponseItem]
