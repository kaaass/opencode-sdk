# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .session.session import Session

__all__ = ["SessionCreated", "Properties"]


class Properties(BaseModel):
    info: Session

    session_id: str = FieldInfo(alias="sessionID")


class SessionCreated(BaseModel):
    properties: Properties

    type: Literal["session.created"]
