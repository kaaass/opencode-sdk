# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .session.message.part import Part
from .session.message.message import Message

__all__ = ["SessionRunShellCommandResponse"]


class SessionRunShellCommandResponse(BaseModel):
    info: Message

    parts: List[Part]
