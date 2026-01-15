# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .part import Part
from ..._models import BaseModel
from .message.message import Message

__all__ = ["MessageGetAllResponse", "MessageGetAllResponseItem"]


class MessageGetAllResponseItem(BaseModel):
    info: Message

    parts: List[Part]


MessageGetAllResponse: TypeAlias = List[MessageGetAllResponseItem]
