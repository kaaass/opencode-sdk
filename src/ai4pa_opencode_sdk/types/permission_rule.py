# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["PermissionRule"]


class PermissionRule(BaseModel):
    action: Literal["allow", "deny", "ask"]

    pattern: str

    permission: str
