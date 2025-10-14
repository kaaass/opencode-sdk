# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = [
    "ConfigListProvidersResponse",
    "Provider",
    "ProviderModels",
    "ProviderModelsCost",
    "ProviderModelsLimit",
    "ProviderModelsModalities",
    "ProviderModelsProvider",
]


class ProviderModelsCost(BaseModel):
    input: float

    output: float

    cache_read: Optional[float] = None

    cache_write: Optional[float] = None


class ProviderModelsLimit(BaseModel):
    context: float

    output: float


class ProviderModelsModalities(BaseModel):
    input: List[Literal["text", "audio", "image", "video", "pdf"]]

    output: List[Literal["text", "audio", "image", "video", "pdf"]]


class ProviderModelsProvider(BaseModel):
    npm: str


class ProviderModels(BaseModel):
    id: str

    attachment: bool

    cost: ProviderModelsCost

    limit: ProviderModelsLimit

    name: str

    options: Dict[str, object]

    reasoning: bool

    release_date: str

    temperature: bool

    tool_call: bool

    experimental: Optional[bool] = None

    modalities: Optional[ProviderModelsModalities] = None

    provider: Optional[ProviderModelsProvider] = None


class Provider(BaseModel):
    id: str

    env: List[str]

    models: Dict[str, ProviderModels]

    name: str

    api: Optional[str] = None

    npm: Optional[str] = None


class ConfigListProvidersResponse(BaseModel):
    default: Dict[str, str]

    providers: List[Provider]
