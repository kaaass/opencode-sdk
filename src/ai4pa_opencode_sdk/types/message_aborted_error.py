# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["MessageAbortedError", "Data"]


class Data(BaseModel):
    message: str


class MessageAbortedError(BaseModel):
    data: Data

    name: Literal["MessageAbortedError"]
