# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = ["ProviderGetAuthMethodsResponse", "ProviderGetAuthMethodsResponseItem"]


class ProviderGetAuthMethodsResponseItem(BaseModel):
    label: str

    type: Literal["oauth", "api"]


ProviderGetAuthMethodsResponse: TypeAlias = Dict[str, List[ProviderGetAuthMethodsResponseItem]]
