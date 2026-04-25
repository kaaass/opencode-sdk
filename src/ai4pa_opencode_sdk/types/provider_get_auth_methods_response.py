# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = [
    "ProviderGetAuthMethodsResponse",
    "ProviderGetAuthMethodsResponseItem",
    "ProviderGetAuthMethodsResponseItemPrompt",
    "ProviderGetAuthMethodsResponseItemPromptUnionMember0",
    "ProviderGetAuthMethodsResponseItemPromptUnionMember0When",
    "ProviderGetAuthMethodsResponseItemPromptUnionMember1",
    "ProviderGetAuthMethodsResponseItemPromptUnionMember1Option",
    "ProviderGetAuthMethodsResponseItemPromptUnionMember1When",
]


class ProviderGetAuthMethodsResponseItemPromptUnionMember0When(BaseModel):
    key: str

    op: Literal["eq", "neq"]

    value: str


class ProviderGetAuthMethodsResponseItemPromptUnionMember0(BaseModel):
    key: str

    message: str

    type: Literal["text"]

    placeholder: Optional[str] = None

    when: Optional[ProviderGetAuthMethodsResponseItemPromptUnionMember0When] = None


class ProviderGetAuthMethodsResponseItemPromptUnionMember1Option(BaseModel):
    label: str

    value: str

    hint: Optional[str] = None


class ProviderGetAuthMethodsResponseItemPromptUnionMember1When(BaseModel):
    key: str

    op: Literal["eq", "neq"]

    value: str


class ProviderGetAuthMethodsResponseItemPromptUnionMember1(BaseModel):
    key: str

    message: str

    options: List[ProviderGetAuthMethodsResponseItemPromptUnionMember1Option]

    type: Literal["select"]

    when: Optional[ProviderGetAuthMethodsResponseItemPromptUnionMember1When] = None


ProviderGetAuthMethodsResponseItemPrompt: TypeAlias = Union[
    ProviderGetAuthMethodsResponseItemPromptUnionMember0, ProviderGetAuthMethodsResponseItemPromptUnionMember1
]


class ProviderGetAuthMethodsResponseItem(BaseModel):
    label: str

    type: Literal["oauth", "api"]

    prompts: Optional[List[ProviderGetAuthMethodsResponseItemPrompt]] = None


ProviderGetAuthMethodsResponse: TypeAlias = Dict[str, List[ProviderGetAuthMethodsResponseItem]]
