# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["LspUpdated"]


class LspUpdated(BaseModel):
    properties: object

    type: Literal["lsp.updated"]
