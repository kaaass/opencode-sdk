# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .unknown_error import UnknownError
from .provider_auth_error import ProviderAuthError
from .message_aborted_error import MessageAbortedError
from .message_output_length_error import MessageOutputLengthError

__all__ = ["AssistantMessage", "Path", "Time", "Tokens", "TokensCache", "Error", "ErrorAPIError", "ErrorAPIErrorData"]


class Path(BaseModel):
    cwd: str

    root: str


class Time(BaseModel):
    created: float

    completed: Optional[float] = None


class TokensCache(BaseModel):
    read: float

    write: float


class Tokens(BaseModel):
    cache: TokensCache

    input: float

    output: float

    reasoning: float


class ErrorAPIErrorData(BaseModel):
    is_retryable: bool = FieldInfo(alias="isRetryable")

    message: str

    metadata: Optional[Dict[str, str]] = None

    response_body: Optional[str] = FieldInfo(alias="responseBody", default=None)

    response_headers: Optional[Dict[str, str]] = FieldInfo(alias="responseHeaders", default=None)

    status_code: Optional[float] = FieldInfo(alias="statusCode", default=None)


class ErrorAPIError(BaseModel):
    data: ErrorAPIErrorData

    name: Literal["APIError"]


Error: TypeAlias = Union[ProviderAuthError, UnknownError, MessageOutputLengthError, MessageAbortedError, ErrorAPIError]


class AssistantMessage(BaseModel):
    id: str

    agent: str

    cost: float

    mode: str

    api_model_id: str = FieldInfo(alias="modelID")

    parent_id: str = FieldInfo(alias="parentID")

    path: Path

    provider_id: str = FieldInfo(alias="providerID")

    role: Literal["assistant"]

    session_id: str = FieldInfo(alias="sessionID")

    time: Time

    tokens: Tokens

    error: Optional[Error] = None

    finish: Optional[str] = None

    summary: Optional[bool] = None
