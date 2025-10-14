# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ..._utils import PropertyInfo
from .file_part_source_param import FilePartSourceParam

__all__ = [
    "MessageCreateParams",
    "Part",
    "PartTextPartInput",
    "PartTextPartInputTime",
    "PartFilePartInput",
    "PartAgentPartInput",
    "PartAgentPartInputSource",
    "Model",
]


class MessageCreateParams(TypedDict, total=False):
    parts: Required[Iterable[Part]]

    directory: str

    agent: str

    message_id: Annotated[str, PropertyInfo(alias="messageID")]

    model: Model

    system: str

    tools: Dict[str, bool]


class PartTextPartInputTime(TypedDict, total=False):
    start: Required[float]

    end: float


class PartTextPartInput(TypedDict, total=False):
    text: Required[str]

    type: Required[Literal["text"]]

    id: str

    metadata: Dict[str, object]

    synthetic: bool

    time: PartTextPartInputTime


class PartFilePartInput(TypedDict, total=False):
    mime: Required[str]

    type: Required[Literal["file"]]

    url: Required[str]

    id: str

    filename: str

    source: FilePartSourceParam


class PartAgentPartInputSource(TypedDict, total=False):
    end: Required[int]

    start: Required[int]

    value: Required[str]


class PartAgentPartInput(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["agent"]]

    id: str

    source: PartAgentPartInputSource


Part: TypeAlias = Union[PartTextPartInput, PartFilePartInput, PartAgentPartInput]


class Model(TypedDict, total=False):
    model_id: Required[Annotated[str, PropertyInfo(alias="modelID")]]

    provider_id: Required[Annotated[str, PropertyInfo(alias="providerID")]]
