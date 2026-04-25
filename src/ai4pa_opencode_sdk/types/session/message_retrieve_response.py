# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from .message.part import Part
from .message.message import Message

__all__ = ["MessageRetrieveResponse"]


class MessageRetrieveResponse(BaseModel):
    info: Message

    parts: List[Part]
