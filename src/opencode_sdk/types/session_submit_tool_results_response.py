# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .session.part import Part
from .assistant_message import AssistantMessage

__all__ = ["SessionSubmitToolResultsResponse"]


class SessionSubmitToolResultsResponse(BaseModel):
    info: AssistantMessage

    parts: List[Part]
