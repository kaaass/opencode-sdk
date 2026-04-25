# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .session.message.message import Message

__all__ = ["MessageUpdated", "Properties"]


class Properties(BaseModel):
    info: Message

    session_id: str = FieldInfo(alias="sessionID")


class MessageUpdated(BaseModel):
    properties: Properties

    type: Literal["message.updated"]
