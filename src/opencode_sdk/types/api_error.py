# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["APIError", "Data"]


class Data(BaseModel):
    is_retryable: bool = FieldInfo(alias="isRetryable")

    message: str

    metadata: Optional[Dict[str, str]] = None

    response_body: Optional[str] = FieldInfo(alias="responseBody", default=None)

    response_headers: Optional[Dict[str, str]] = FieldInfo(alias="responseHeaders", default=None)

    status_code: Optional[float] = FieldInfo(alias="statusCode", default=None)


class APIError(BaseModel):
    data: Data

    name: Literal["APIError"]
