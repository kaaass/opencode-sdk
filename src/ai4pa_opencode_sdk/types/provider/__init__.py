# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .custom_list_params import CustomListParams as CustomListParams
from .custom_create_params import CustomCreateParams as CustomCreateParams
from .custom_delete_params import CustomDeleteParams as CustomDeleteParams
from .custom_list_response import CustomListResponse as CustomListResponse
from .custom_create_response import CustomCreateResponse as CustomCreateResponse
from .custom_delete_response import CustomDeleteResponse as CustomDeleteResponse
from .oauth_authorize_params import OAuthAuthorizeParams as OAuthAuthorizeParams
from .oauth_authorize_response import OAuthAuthorizeResponse as OAuthAuthorizeResponse
from .oauth_handle_callback_params import OAuthHandleCallbackParams as OAuthHandleCallbackParams
from .oauth_handle_callback_response import OAuthHandleCallbackResponse as OAuthHandleCallbackResponse

__all__ = [
    "CustomListParams",
    "CustomCreateParams",
    "CustomDeleteParams",
    "CustomListResponse",
    "CustomCreateResponse",
    "CustomDeleteResponse",
    "OAuthAuthorizeParams",
    "OAuthAuthorizeResponse",
    "OAuthHandleCallbackParams",
    "OAuthHandleCallbackResponse",
    "Provider",
    "Models",
    "ModelsAPI",
    "ModelsCapabilities",
    "ModelsCapabilitiesInput",
    "ModelsCapabilitiesInterleaved",
    "ModelsCapabilitiesInterleavedField",
    "ModelsCapabilitiesOutput",
    "ModelsCost",
    "ModelsCostCache",
    "ModelsCostExperimentalOver200K",
    "ModelsCostExperimentalOver200KCache",
    "ModelsLimit",
]


class ModelsAPI(BaseModel):
    id: str

    npm: str

    url: str


class ModelsCapabilitiesInput(BaseModel):
    audio: bool

    image: bool

    pdf: bool

    text: bool

    video: bool


class ModelsCapabilitiesInterleavedField(BaseModel):
    field: Literal["reasoning_content", "reasoning_details"]


ModelsCapabilitiesInterleaved: TypeAlias = Union[bool, ModelsCapabilitiesInterleavedField]


class ModelsCapabilitiesOutput(BaseModel):
    audio: bool

    image: bool

    pdf: bool

    text: bool

    video: bool


class ModelsCapabilities(BaseModel):
    attachment: bool

    input: ModelsCapabilitiesInput

    interleaved: ModelsCapabilitiesInterleaved

    output: ModelsCapabilitiesOutput

    reasoning: bool

    temperature: bool

    toolcall: bool


class ModelsCostCache(BaseModel):
    read: float

    write: float


class ModelsCostExperimentalOver200KCache(BaseModel):
    read: float

    write: float


class ModelsCostExperimentalOver200K(BaseModel):
    cache: ModelsCostExperimentalOver200KCache

    input: float

    output: float


class ModelsCost(BaseModel):
    cache: ModelsCostCache

    input: float

    output: float

    experimental_over200_k: Optional[ModelsCostExperimentalOver200K] = FieldInfo(
        alias="experimentalOver200K", default=None
    )


class ModelsLimit(BaseModel):
    context: float

    output: float

    input: Optional[float] = None


class Models(BaseModel):
    id: str

    api: ModelsAPI

    capabilities: ModelsCapabilities

    cost: ModelsCost

    headers: Dict[str, str]

    limit: ModelsLimit

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

    models: Dict[str, Models]

    name: str

    options: Dict[str, object]

    source: Literal["env", "config", "custom", "api"]

    key: Optional[str] = None
