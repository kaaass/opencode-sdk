# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AgentCreateOrUpdateParams", "Permission", "Model"]


class AgentCreateOrUpdateParams(TypedDict, total=False):
    mode: Required[Literal["subagent", "primary", "all"]]

    name: Required[str]

    options: Required[Dict[str, object]]

    permission: Required[Permission]

    tools: Required[Dict[str, bool]]

    directory: str

    color: str

    description: str

    hidden: bool

    max_steps: Annotated[int, PropertyInfo(alias="maxSteps")]

    model: Model

    native: bool

    prompt: str

    temperature: float

    top_p: Annotated[float, PropertyInfo(alias="topP")]


class Permission(TypedDict, total=False):
    bash: Required[Dict[str, Literal["ask", "allow", "deny"]]]

    edit: Required[Literal["ask", "allow", "deny"]]

    doom_loop: Literal["ask", "allow", "deny"]

    external_directory: Literal["ask", "allow", "deny"]

    webfetch: Literal["ask", "allow", "deny"]


class Model(TypedDict, total=False):
    model_id: Required[Annotated[str, PropertyInfo(alias="modelID")]]

    provider_id: Required[Annotated[str, PropertyInfo(alias="providerID")]]
