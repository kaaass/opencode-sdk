# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ConsoleListOrgsResponse", "Org"]


class Org(BaseModel):
    account_email: str = FieldInfo(alias="accountEmail")

    account_id: str = FieldInfo(alias="accountID")

    account_url: str = FieldInfo(alias="accountUrl")

    active: bool

    org_id: str = FieldInfo(alias="orgID")

    org_name: str = FieldInfo(alias="orgName")


class ConsoleListOrgsResponse(BaseModel):
    orgs: List[Org]
