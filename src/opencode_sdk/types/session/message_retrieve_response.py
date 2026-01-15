# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .part import Part
from ..._models import BaseModel
from .message.message import Message

__all__ = ["MessageRetrieveResponse"]


class MessageRetrieveResponse(BaseModel):
    info: Message

    parts: List[Part]
