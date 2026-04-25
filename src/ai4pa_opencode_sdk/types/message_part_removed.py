# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["MessagePartRemoved", "Properties"]


class Properties(BaseModel):
    message_id: str = FieldInfo(alias="messageID")

    part_id: str = FieldInfo(alias="partID")

    session_id: str = FieldInfo(alias="sessionID")


class MessagePartRemoved(BaseModel):
    properties: Properties

    type: Literal["message.part.removed"]
