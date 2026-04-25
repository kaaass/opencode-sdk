# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["SessionIdle", "Properties"]


class Properties(BaseModel):
    session_id: str = FieldInfo(alias="sessionID")


class SessionIdle(BaseModel):
    properties: Properties

    type: Literal["session.idle"]
