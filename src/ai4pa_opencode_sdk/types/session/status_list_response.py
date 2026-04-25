# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict
from typing_extensions import TypeAlias

from .session_status_detail import SessionStatusDetail

__all__ = ["StatusListResponse"]

StatusListResponse: TypeAlias = Dict[str, SessionStatusDetail]
