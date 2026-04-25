# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .assistant_message import AssistantMessage
from .session.message.part import Part

__all__ = ["SessionSendCommandResponse"]


class SessionSendCommandResponse(BaseModel):
    info: AssistantMessage

    parts: List[Part]
