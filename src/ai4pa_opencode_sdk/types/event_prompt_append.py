# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["EventPromptAppend", "Properties"]


class Properties(BaseModel):
    text: str


class EventPromptAppend(BaseModel):
    properties: Properties

    type: Literal["tui.prompt.append"]
