# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = [
    "ProviderListResponse",
    "All",
    "AllModels",
    "AllModelsLimit",
    "AllModelsCost",
    "AllModelsCostContextOver200k",
    "AllModelsInterleaved",
    "AllModelsInterleavedField",
    "AllModelsModalities",
    "AllModelsProvider",
]


class AllModelsLimit(BaseModel):
    context: float

    output: float


class AllModelsCostContextOver200k(BaseModel):
    input: float

    output: float

    cache_read: Optional[float] = None

    cache_write: Optional[float] = None


class AllModelsCost(BaseModel):
    input: float

    output: float

    cache_read: Optional[float] = None

    cache_write: Optional[float] = None

    context_over_200k: Optional[AllModelsCostContextOver200k] = None


class AllModelsInterleavedField(BaseModel):
    field: Literal["reasoning_content", "reasoning_details"]


AllModelsInterleaved: TypeAlias = Union[Literal[True], AllModelsInterleavedField]


class AllModelsModalities(BaseModel):
    input: List[Literal["text", "audio", "image", "video", "pdf"]]

    output: List[Literal["text", "audio", "image", "video", "pdf"]]


class AllModelsProvider(BaseModel):
    npm: str


class AllModels(BaseModel):
    id: str

    attachment: bool

    limit: AllModelsLimit

    name: str

    options: Dict[str, object]

    reasoning: bool

    release_date: str

    temperature: bool

    tool_call: bool

    cost: Optional[AllModelsCost] = None

    experimental: Optional[bool] = None

    family: Optional[str] = None

    headers: Optional[Dict[str, str]] = None

    interleaved: Optional[AllModelsInterleaved] = None

    modalities: Optional[AllModelsModalities] = None

    provider: Optional[AllModelsProvider] = None

    status: Optional[Literal["alpha", "beta", "deprecated"]] = None


class All(BaseModel):
    id: str

    env: List[str]

    models: Dict[str, AllModels]

    name: str

    api: Optional[str] = None

    npm: Optional[str] = None


class ProviderListResponse(BaseModel):
    all: List[All]

    connected: List[str]

    default: Dict[str, str]
