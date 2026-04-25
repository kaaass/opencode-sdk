# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .api_error import APIError
from .unknown_error import UnknownError
from .provider_auth_error import ProviderAuthError
from .message_aborted_error import MessageAbortedError
from .context_overflow_error import ContextOverflowError
from .structured_output_error import StructuredOutputError
from .message_output_length_error import MessageOutputLengthError

__all__ = ["SessionError", "Properties", "PropertiesError"]

PropertiesError: TypeAlias = Union[
    ProviderAuthError,
    UnknownError,
    MessageOutputLengthError,
    MessageAbortedError,
    StructuredOutputError,
    ContextOverflowError,
    APIError,
]


class Properties(BaseModel):
    error: Optional[PropertiesError] = None

    session_id: Optional[str] = FieldInfo(alias="sessionID", default=None)


class SessionError(BaseModel):
    properties: Properties

    type: Literal["session.error"]
