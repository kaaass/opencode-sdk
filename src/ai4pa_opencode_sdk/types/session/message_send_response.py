# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .message.part import Part
from ..assistant_message import AssistantMessage

__all__ = ["MessageSendResponse", "PendingClientCall"]


class PendingClientCall(BaseModel):
    call_id: str = FieldInfo(alias="callID")

    input: Dict[str, object]

    tool: str


class MessageSendResponse(BaseModel):
    info: AssistantMessage

    parts: List[Part]

    pending_client_calls: Optional[List[PendingClientCall]] = FieldInfo(alias="pendingClientCalls", default=None)
