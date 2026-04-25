# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "ProviderListResponse",
    "All",
    "AllModels",
    "AllModelsAPI",
    "AllModelsCapabilities",
    "AllModelsCapabilitiesInput",
    "AllModelsCapabilitiesInterleaved",
    "AllModelsCapabilitiesInterleavedField",
    "AllModelsCapabilitiesOutput",
    "AllModelsCost",
    "AllModelsCostCache",
    "AllModelsCostExperimentalOver200K",
    "AllModelsCostExperimentalOver200KCache",
    "AllModelsLimit",
]


class AllModelsAPI(BaseModel):
    id: str

    npm: str

    url: str


class AllModelsCapabilitiesInput(BaseModel):
    audio: bool

    image: bool

    pdf: bool

    text: bool

    video: bool


class AllModelsCapabilitiesInterleavedField(BaseModel):
    field: Literal["reasoning_content", "reasoning_details"]


AllModelsCapabilitiesInterleaved: TypeAlias = Union[bool, AllModelsCapabilitiesInterleavedField]


class AllModelsCapabilitiesOutput(BaseModel):
    audio: bool

    image: bool

    pdf: bool

    text: bool

    video: bool


class AllModelsCapabilities(BaseModel):
    attachment: bool

    input: AllModelsCapabilitiesInput

    interleaved: AllModelsCapabilitiesInterleaved

    output: AllModelsCapabilitiesOutput

    reasoning: bool

    temperature: bool

    toolcall: bool


class AllModelsCostCache(BaseModel):
    read: float

    write: float


class AllModelsCostExperimentalOver200KCache(BaseModel):
    read: float

    write: float


class AllModelsCostExperimentalOver200K(BaseModel):
    cache: AllModelsCostExperimentalOver200KCache

    input: float

    output: float


class AllModelsCost(BaseModel):
    cache: AllModelsCostCache

    input: float

    output: float

    experimental_over200_k: Optional[AllModelsCostExperimentalOver200K] = FieldInfo(
        alias="experimentalOver200K", default=None
    )


class AllModelsLimit(BaseModel):
    context: float

    output: float

    input: Optional[float] = None


class AllModels(BaseModel):
    id: str

    api: AllModelsAPI

    capabilities: AllModelsCapabilities

    cost: AllModelsCost

    headers: Dict[str, str]

    limit: AllModelsLimit

    name: str

    options: Dict[str, object]

    provider_id: str = FieldInfo(alias="providerID")

    release_date: str

    status: Literal["alpha", "beta", "deprecated", "active"]

    family: Optional[str] = None

    variants: Optional[Dict[str, Dict[str, object]]] = None


class All(BaseModel):
    id: str

    env: List[str]

    models: Dict[str, AllModels]

    name: str

    options: Dict[str, object]

    source: Literal["env", "config", "custom", "api"]

    key: Optional[str] = None


class ProviderListResponse(BaseModel):
    all: List[All]

    connected: List[str]

    default: Dict[str, str]
