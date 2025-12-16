# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = ["LspRetrieveStatusResponse", "LspRetrieveStatusResponseItem"]


class LspRetrieveStatusResponseItem(BaseModel):
    id: str

    name: str

    root: str

    status: Literal["connected", "error"]


LspRetrieveStatusResponse: TypeAlias = List[LspRetrieveStatusResponseItem]
