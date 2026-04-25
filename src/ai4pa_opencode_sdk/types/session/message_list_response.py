# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from ..._models import BaseModel
from .message.part import Part
from .message.message import Message

__all__ = ["MessageListResponse", "MessageListResponseItem"]


class MessageListResponseItem(BaseModel):
    info: Message

    parts: List[Part]


MessageListResponse: TypeAlias = List[MessageListResponseItem]
