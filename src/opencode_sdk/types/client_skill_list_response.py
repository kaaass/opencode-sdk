# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["ClientSkillListResponse", "ClientSkillListResponseItem"]


class ClientSkillListResponseItem(BaseModel):
    description: str

    location: str

    name: str


ClientSkillListResponse: TypeAlias = List[ClientSkillListResponseItem]
