# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["WorkspaceFailed", "Properties"]


class Properties(BaseModel):
    message: str


class WorkspaceFailed(BaseModel):
    properties: Properties

    type: Literal["workspace.failed"]
