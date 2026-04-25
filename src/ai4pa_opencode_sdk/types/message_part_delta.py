# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["MessagePartDelta", "Properties"]


class Properties(BaseModel):
    delta: str

    field: str

    message_id: str = FieldInfo(alias="messageID")

    part_id: str = FieldInfo(alias="partID")

    session_id: str = FieldInfo(alias="sessionID")


class MessagePartDelta(BaseModel):
    properties: Properties

    type: Literal["message.part.delta"]
