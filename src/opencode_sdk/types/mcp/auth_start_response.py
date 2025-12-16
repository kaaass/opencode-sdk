# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["AuthStartResponse"]


class AuthStartResponse(BaseModel):
    authorization_url: str = FieldInfo(alias="authorizationUrl")
    """URL to open in browser for authorization"""
