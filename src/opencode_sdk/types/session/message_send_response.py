# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from pydantic import Field as FieldInfo

from .part import Part
from ..._models import BaseModel
from ..assistant_message import AssistantMessage

__all__ = ["MessageSendResponse", "PendingRemoteCall"]


class PendingRemoteCall(BaseModel):
    call_id: str = FieldInfo(alias="callID")

    input: Dict[str, object]

    tool: str


class MessageSendResponse(BaseModel):
    info: AssistantMessage

    parts: List[Part]

    pending_remote_calls: Optional[List[PendingRemoteCall]] = FieldInfo(alias="pendingRemoteCalls", default=None)
    """Remote tool calls waiting for external results"""
