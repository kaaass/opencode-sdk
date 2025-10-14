# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .part import Part
from ..._models import BaseModel
from ..assistant_message import AssistantMessage

__all__ = ["MessageCreateResponse"]


class MessageCreateResponse(BaseModel):
    info: AssistantMessage

    parts: List[Part]
