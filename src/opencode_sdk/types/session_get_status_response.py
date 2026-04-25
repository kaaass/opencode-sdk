# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict
from typing_extensions import TypeAlias

from .session_status import SessionStatus

__all__ = ["SessionGetStatusResponse"]

SessionGetStatusResponse: TypeAlias = Dict[str, SessionStatus]
