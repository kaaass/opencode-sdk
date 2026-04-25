# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ConsoleSwitchOrgParams"]


class ConsoleSwitchOrgParams(TypedDict, total=False):
    account_id: Required[Annotated[str, PropertyInfo(alias="accountID")]]

    org_id: Required[Annotated[str, PropertyInfo(alias="orgID")]]

    directory: str

    workspace: str
