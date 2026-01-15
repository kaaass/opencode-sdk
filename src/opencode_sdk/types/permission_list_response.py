# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["PermissionListResponse", "PermissionListResponseItem", "PermissionListResponseItemTool"]


class PermissionListResponseItemTool(BaseModel):
    call_id: str = FieldInfo(alias="callID")

    message_id: str = FieldInfo(alias="messageID")


class PermissionListResponseItem(BaseModel):
    id: str

    always: List[str]

    metadata: Dict[str, object]

    patterns: List[str]

    permission: str

    session_id: str = FieldInfo(alias="sessionID")

    tool: Optional[PermissionListResponseItemTool] = None


PermissionListResponse: TypeAlias = List[PermissionListResponseItem]
