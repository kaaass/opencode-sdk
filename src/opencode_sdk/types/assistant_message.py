# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .unknown_error import UnknownError
from .provider_auth_error import ProviderAuthError
from .message_aborted_error import MessageAbortedError
from .message_output_length_error import MessageOutputLengthError

__all__ = ["AssistantMessage", "Path", "Time", "Tokens", "TokensCache", "Error"]


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


Error: TypeAlias = Union[ProviderAuthError, UnknownError, MessageOutputLengthError, MessageAbortedError]


class AssistantMessage(BaseModel):
    id: str

    cost: float

    mode: str

    api_model_id: str = FieldInfo(alias="modelID")

    path: Path

    provider_id: str = FieldInfo(alias="providerID")

    role: Literal["assistant"]

    session_id: str = FieldInfo(alias="sessionID")

    system: List[str]

    time: Time

    tokens: Tokens

    error: Optional[Error] = None

    summary: Optional[bool] = None
