# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["FormatterRetrieveResponse", "FormatterRetrieveResponseItem"]


class FormatterRetrieveResponseItem(BaseModel):
    enabled: bool

    extensions: List[str]

    name: str


FormatterRetrieveResponse: TypeAlias = List[FormatterRetrieveResponseItem]
