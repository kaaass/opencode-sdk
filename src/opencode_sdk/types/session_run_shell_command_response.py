# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .session.part import Part
from .assistant_message import AssistantMessage

__all__ = ["SessionRunShellCommandResponse", "PendingRemoteCall"]


class PendingRemoteCall(BaseModel):
    call_id: str = FieldInfo(alias="callID")

    input: Dict[str, object]

    tool: str


class SessionRunShellCommandResponse(BaseModel):
    info: AssistantMessage

    parts: List[Part]

    pending_remote_calls: Optional[List[PendingRemoteCall]] = FieldInfo(alias="pendingRemoteCalls", default=None)
    """Remote tool calls waiting for external results"""
