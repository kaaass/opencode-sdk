# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .session_status import SessionStatus

__all__ = ["SessionEventStatus", "Properties"]


class Properties(BaseModel):
    session_id: str = FieldInfo(alias="sessionID")

    status: SessionStatus


class SessionEventStatus(BaseModel):
    properties: Properties

    type: Literal["session.status"]
