# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["CommandExecuted", "Properties"]


class Properties(BaseModel):
    arguments: str

    message_id: str = FieldInfo(alias="messageID")

    name: str

    session_id: str = FieldInfo(alias="sessionID")


class CommandExecuted(BaseModel):
    properties: Properties

    type: Literal["command.executed"]
