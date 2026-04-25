# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["EventSessionSelect", "Properties"]


class Properties(BaseModel):
    session_id: str = FieldInfo(alias="sessionID")
    """Session ID to navigate to"""


class EventSessionSelect(BaseModel):
    properties: Properties

    type: Literal["tui.session.select"]
