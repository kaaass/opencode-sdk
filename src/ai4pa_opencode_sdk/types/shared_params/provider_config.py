# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

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


class ModelsCostContextOver200k(TypedDict, total=False):
    input: Required[float]

    output: Required[float]

    cache_read: float

    cache_write: float


class ModelsCost(TypedDict, total=False):
    input: Required[float]

    output: Required[float]

    cache_read: float

    cache_write: float

    context_over_200k: ModelsCostContextOver200k


class ModelsInterleavedField(TypedDict, total=False):
    field: Required[Literal["reasoning_content", "reasoning_details"]]


ModelsInterleaved: TypeAlias = Union[Literal[True], ModelsInterleavedField]


class ModelsLimit(TypedDict, total=False):
    context: Required[float]

    output: Required[float]

    input: float


class ModelsModalities(TypedDict, total=False):
    input: Required[List[Literal["text", "audio", "image", "video", "pdf"]]]

    output: Required[List[Literal["text", "audio", "image", "video", "pdf"]]]


class ModelsProvider(TypedDict, total=False):
    api: str

    npm: str


class ModelsVariants(  # type: ignore[call-arg]
    TypedDict,
    total=False,
    extra_items=object,  # pyright: ignore[reportGeneralTypeIssues]
):
    disabled: bool
    """Disable this variant for the model"""


class Models(TypedDict, total=False):
    id: str

    attachment: bool

    cost: ModelsCost

    experimental: bool

    family: str

    headers: Dict[str, str]

    interleaved: ModelsInterleaved

    limit: ModelsLimit

    modalities: ModelsModalities

    name: str

    options: Dict[str, object]

    provider: ModelsProvider

    reasoning: bool

    release_date: str

    status: Literal["alpha", "beta", "deprecated"]

    temperature: bool

    tool_call: bool

    variants: Dict[str, ModelsVariants]
    """Variant-specific configuration"""


class Options(  # type: ignore[call-arg]
    TypedDict,
    total=False,
    extra_items=object,  # pyright: ignore[reportGeneralTypeIssues]
):
    api_key: Annotated[str, PropertyInfo(alias="apiKey")]

    base_url: Annotated[str, PropertyInfo(alias="baseURL")]

    chunk_timeout: Annotated[int, PropertyInfo(alias="chunkTimeout")]
    """Timeout in milliseconds between streamed SSE chunks for this provider.

    If no chunk arrives within this window, the request is aborted.
    """

    enterprise_url: Annotated[str, PropertyInfo(alias="enterpriseUrl")]
    """GitHub Enterprise URL for copilot authentication"""

    set_cache_key: Annotated[bool, PropertyInfo(alias="setCacheKey")]
    """Enable promptCacheKey for this provider (default false)"""

    timeout: Union[int, Literal[False]]
    """Timeout in milliseconds for requests to this provider.

    Default is 300000 (5 minutes). Set to false to disable timeout.
    """


class ProviderConfig(TypedDict, total=False):
    id: str

    api: str

    blacklist: SequenceNotStr[str]

    env: SequenceNotStr[str]

    models: Dict[str, Models]

    name: str

    npm: str

    options: Options

    whitelist: SequenceNotStr[str]
