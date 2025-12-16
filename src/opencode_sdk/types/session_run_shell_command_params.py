# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SessionRunShellCommandParams", "Model"]


class SessionRunShellCommandParams(TypedDict, total=False):
    agent: Required[str]

    command: Required[str]

    directory: str

    model: Model


class Model(TypedDict, total=False):
    model_id: Required[Annotated[str, PropertyInfo(alias="modelID")]]

    provider_id: Required[Annotated[str, PropertyInfo(alias="providerID")]]
