# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["APIErrorParam", "Data"]


class Data(TypedDict, total=False):
    is_retryable: Required[Annotated[bool, PropertyInfo(alias="isRetryable")]]

    message: Required[str]

    metadata: Dict[str, str]

    response_body: Annotated[str, PropertyInfo(alias="responseBody")]

    response_headers: Annotated[Dict[str, str], PropertyInfo(alias="responseHeaders")]

    status_code: Annotated[float, PropertyInfo(alias="statusCode")]


class APIErrorParam(TypedDict, total=False):
    data: Required[Data]

    name: Required[Literal["APIError"]]
