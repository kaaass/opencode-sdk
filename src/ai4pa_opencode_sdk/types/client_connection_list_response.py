# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "ClientConnectionListResponse",
    "ClientConnectionListResponseItem",
    "ClientConnectionListResponseItemResources",
]


class ClientConnectionListResponseItemResources(BaseModel):
    agents: float

    skills: float

    tools: float


class ClientConnectionListResponseItem(BaseModel):
    id: str

    client_type: Literal["tui", "sdk", "cc-companion", "phone", "unknown"] = FieldInfo(alias="clientType")

    last_seen_at: float = FieldInfo(alias="lastSeenAt")

    participating: List[str]

    resources: ClientConnectionListResponseItemResources

    sessions: List[str]


ClientConnectionListResponse: TypeAlias = List[ClientConnectionListResponseItem]
