# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["OAuthAuthorizeResponse"]


class OAuthAuthorizeResponse(BaseModel):
    instructions: str

    method: Literal["auto", "code"]

    url: str
