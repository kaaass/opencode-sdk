# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .session.message.part import Part

__all__ = ["MessagePartUpdated", "Properties"]


class Properties(BaseModel):
    part: Part

    session_id: str = FieldInfo(alias="sessionID")

    time: float


class MessagePartUpdated(BaseModel):
    properties: Properties

    type: Literal["message.part.updated"]
