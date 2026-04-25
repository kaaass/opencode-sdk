# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["PtyExited", "Properties"]


class Properties(BaseModel):
    id: str

    exit_code: float = FieldInfo(alias="exitCode")


class PtyExited(BaseModel):
    properties: Properties

    type: Literal["pty.exited"]
