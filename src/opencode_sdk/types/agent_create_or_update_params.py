# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["AgentCreateOrUpdateParams", "Permission", "Model"]


class AgentCreateOrUpdateParams(TypedDict, total=False):
    mode: Required[Literal["subagent", "primary", "all"]]

    name: Required[str]

    options: Required[Dict[str, object]]

    permission: Required[Iterable[Permission]]

    directory: str

    color: str

    description: str

    hidden: bool

    model: Model

    native: bool

    prompt: str

    steps: int

    sub_agents: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="subAgents")]

    temperature: float

    top_p: Annotated[float, PropertyInfo(alias="topP")]


class Permission(TypedDict, total=False):
    action: Required[Literal["allow", "deny", "ask"]]

    pattern: Required[str]

    permission: Required[str]


class Model(TypedDict, total=False):
    model_id: Required[Annotated[str, PropertyInfo(alias="modelID")]]

    provider_id: Required[Annotated[str, PropertyInfo(alias="providerID")]]
