# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = ["WorkspaceListAdaptorsResponse", "WorkspaceListAdaptorsResponseItem"]


class WorkspaceListAdaptorsResponseItem(BaseModel):
    description: str

    name: str

    type: str


WorkspaceListAdaptorsResponse: TypeAlias = List[WorkspaceListAdaptorsResponseItem]
