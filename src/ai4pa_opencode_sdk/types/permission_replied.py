# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["PermissionReplied", "Properties"]


class Properties(BaseModel):
    reply: Literal["once", "always", "reject"]

    request_id: str = FieldInfo(alias="requestID")

    session_id: str = FieldInfo(alias="sessionID")


class PermissionReplied(BaseModel):
    properties: Properties

    type: Literal["permission.replied"]
