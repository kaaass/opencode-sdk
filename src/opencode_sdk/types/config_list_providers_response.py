# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "ConfigListProvidersResponse",
    "Provider",
    "ProviderModels",
    "ProviderModelsAPI",
    "ProviderModelsCapabilities",
    "ProviderModelsCapabilitiesInput",
    "ProviderModelsCapabilitiesInterleaved",
    "ProviderModelsCapabilitiesInterleavedField",
    "ProviderModelsCapabilitiesOutput",
    "ProviderModelsCost",
    "ProviderModelsCostCache",
    "ProviderModelsCostExperimentalOver200K",
    "ProviderModelsCostExperimentalOver200KCache",
    "ProviderModelsLimit",
]


class ProviderModelsAPI(BaseModel):
    id: str

    npm: str

    url: str


class ProviderModelsCapabilitiesInput(BaseModel):
    audio: bool

    image: bool

    pdf: bool

    text: bool

    video: bool


class ProviderModelsCapabilitiesInterleavedField(BaseModel):
    field: Literal["reasoning_content", "reasoning_details"]


ProviderModelsCapabilitiesInterleaved: TypeAlias = Union[bool, ProviderModelsCapabilitiesInterleavedField]


class ProviderModelsCapabilitiesOutput(BaseModel):
    audio: bool

    image: bool

    pdf: bool

    text: bool

    video: bool


class ProviderModelsCapabilities(BaseModel):
    attachment: bool

    input: ProviderModelsCapabilitiesInput

    interleaved: ProviderModelsCapabilitiesInterleaved

    output: ProviderModelsCapabilitiesOutput

    reasoning: bool

    temperature: bool

    toolcall: bool


class ProviderModelsCostCache(BaseModel):
    read: float

    write: float


class ProviderModelsCostExperimentalOver200KCache(BaseModel):
    read: float

    write: float


class ProviderModelsCostExperimentalOver200K(BaseModel):
    cache: ProviderModelsCostExperimentalOver200KCache

    input: float

    output: float


class ProviderModelsCost(BaseModel):
    cache: ProviderModelsCostCache

    input: float

    output: float

    experimental_over200_k: Optional[ProviderModelsCostExperimentalOver200K] = FieldInfo(
        alias="experimentalOver200K", default=None
    )


class ProviderModelsLimit(BaseModel):
    context: float

    output: float


class ProviderModels(BaseModel):
    id: str

    api: ProviderModelsAPI

    capabilities: ProviderModelsCapabilities

    cost: ProviderModelsCost

    headers: Dict[str, str]

    limit: ProviderModelsLimit

    name: str

    options: Dict[str, object]

    provider_id: str = FieldInfo(alias="providerID")

    release_date: str

    status: Literal["alpha", "beta", "deprecated", "active"]

    family: Optional[str] = None

    variants: Optional[Dict[str, Dict[str, object]]] = None


class Provider(BaseModel):
    id: str

    env: List[str]

    models: Dict[str, ProviderModels]

    name: str

    options: Dict[str, object]

    source: Literal["env", "config", "custom", "api"]

    key: Optional[str] = None


class ConfigListProvidersResponse(BaseModel):
    default: Dict[str, str]

    providers: List[Provider]
