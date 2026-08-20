# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["AuthListResponse", "AuthListResponseItem"]


class AuthListResponseItem(BaseModel):
    provider_id: str = FieldInfo(alias="providerID")

    type: Literal["oauth", "api", "wellknown"]


AuthListResponse: TypeAlias = List[AuthListResponseItem]
