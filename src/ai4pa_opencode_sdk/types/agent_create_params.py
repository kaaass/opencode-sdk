# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo
from .permission_rule_param import PermissionRuleParam

__all__ = ["AgentCreateParams", "Model"]


class AgentCreateParams(TypedDict, total=False):
    mode: Required[Literal["subagent", "primary", "all"]]

    name: Required[str]

    options: Required[Dict[str, object]]

    permission: Required[Iterable[PermissionRuleParam]]

    directory: str

    workspace: str

    color: str

    description: str

    hidden: bool

    model: Model

    native: bool

    prompt: str

    skills: Optional[SequenceNotStr[str]]

    steps: float

    sub_agents: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="subAgents")]

    temperature: float

    top_p: Annotated[float, PropertyInfo(alias="topP")]

    variant: str


class Model(TypedDict, total=False):
    model_id: Required[Annotated[str, PropertyInfo(alias="modelID")]]

    provider_id: Required[Annotated[str, PropertyInfo(alias="providerID")]]
