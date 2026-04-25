# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "ProviderConfig",
    "Models",
    "ModelsCost",
    "ModelsCostContextOver200k",
    "ModelsInterleaved",
    "ModelsInterleavedField",
    "ModelsLimit",
    "ModelsModalities",
    "ModelsProvider",
    "ModelsVariants",
    "Options",
]


class ModelsCostContextOver200k(BaseModel):
    input: float

    output: float

    cache_read: Optional[float] = None

    cache_write: Optional[float] = None


class ModelsCost(BaseModel):
    input: float

    output: float

    cache_read: Optional[float] = None

    cache_write: Optional[float] = None

    context_over_200k: Optional[ModelsCostContextOver200k] = None


class ModelsInterleavedField(BaseModel):
    field: Literal["reasoning_content", "reasoning_details"]


ModelsInterleaved: TypeAlias = Union[Literal[True], ModelsInterleavedField]


class ModelsLimit(BaseModel):
    context: float

    output: float

    input: Optional[float] = None


class ModelsModalities(BaseModel):
    input: List[Literal["text", "audio", "image", "video", "pdf"]]

    output: List[Literal["text", "audio", "image", "video", "pdf"]]


class ModelsProvider(BaseModel):
    api: Optional[str] = None

    npm: Optional[str] = None


class ModelsVariants(BaseModel):
    disabled: Optional[bool] = None
    """Disable this variant for the model"""

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class Models(BaseModel):
    id: Optional[str] = None

    attachment: Optional[bool] = None

    cost: Optional[ModelsCost] = None

    experimental: Optional[bool] = None

    family: Optional[str] = None

    headers: Optional[Dict[str, str]] = None

    interleaved: Optional[ModelsInterleaved] = None

    limit: Optional[ModelsLimit] = None

    modalities: Optional[ModelsModalities] = None

    name: Optional[str] = None

    options: Optional[Dict[str, object]] = None

    provider: Optional[ModelsProvider] = None

    reasoning: Optional[bool] = None

    release_date: Optional[str] = None

    status: Optional[Literal["alpha", "beta", "deprecated"]] = None

    temperature: Optional[bool] = None

    tool_call: Optional[bool] = None

    variants: Optional[Dict[str, ModelsVariants]] = None
    """Variant-specific configuration"""


class Options(BaseModel):
    api_key: Optional[str] = FieldInfo(alias="apiKey", default=None)

    base_url: Optional[str] = FieldInfo(alias="baseURL", default=None)

    chunk_timeout: Optional[int] = FieldInfo(alias="chunkTimeout", default=None)
    """Timeout in milliseconds between streamed SSE chunks for this provider.

    If no chunk arrives within this window, the request is aborted.
    """

    enterprise_url: Optional[str] = FieldInfo(alias="enterpriseUrl", default=None)
    """GitHub Enterprise URL for copilot authentication"""

    set_cache_key: Optional[bool] = FieldInfo(alias="setCacheKey", default=None)
    """Enable promptCacheKey for this provider (default false)"""

    timeout: Union[int, Literal[False], None] = None
    """Timeout in milliseconds for requests to this provider.

    Default is 300000 (5 minutes). Set to false to disable timeout.
    """

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class ProviderConfig(BaseModel):
    id: Optional[str] = None

    api: Optional[str] = None

    blacklist: Optional[List[str]] = None

    env: Optional[List[str]] = None

    models: Optional[Dict[str, Models]] = None

    name: Optional[str] = None

    npm: Optional[str] = None

    options: Optional[Options] = None

    whitelist: Optional[List[str]] = None
