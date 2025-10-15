# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AgentCreateOrUpdateParams", "Permission", "Model"]


class AgentCreateOrUpdateParams(TypedDict, total=False):
    built_in: Required[Annotated[bool, PropertyInfo(alias="builtIn")]]

    mode: Required[Literal["subagent", "primary", "all"]]

    name: Required[str]

    options: Required[Dict[str, object]]

    permission: Required[Permission]

    tools: Required[Dict[str, bool]]

    directory: str

    description: str

    model: Model

    prompt: str

    temperature: float

    top_p: Annotated[float, PropertyInfo(alias="topP")]


class Permission(TypedDict, total=False):
    bash: Required[Dict[str, Literal["ask", "allow", "deny"]]]

    edit: Required[Literal["ask", "allow", "deny"]]

    webfetch: Literal["ask", "allow", "deny"]


class Model(TypedDict, total=False):
    model_id: Required[Annotated[str, PropertyInfo(alias="modelID")]]

    provider_id: Required[Annotated[str, PropertyInfo(alias="providerID")]]
