# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = ["AuthSetCredentialsParams", "OAuth", "APIAuth", "WellKnownAuth"]


class OAuth(TypedDict, total=False):
    access: Required[str]

    expires: Required[float]

    refresh: Required[str]

    type: Required[Literal["oauth"]]

    directory: str

    account_id: Annotated[str, PropertyInfo(alias="accountId")]

    enterprise_url: Annotated[str, PropertyInfo(alias="enterpriseUrl")]


class APIAuth(TypedDict, total=False):
    key: Required[str]

    type: Required[Literal["api"]]

    directory: str


class WellKnownAuth(TypedDict, total=False):
    token: Required[str]

    key: Required[str]

    type: Required[Literal["wellknown"]]

    directory: str


AuthSetCredentialsParams: TypeAlias = Union[OAuth, APIAuth, WellKnownAuth]
