# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ToolStatePending"]


class ToolStatePending(BaseModel):
    input: Dict[str, object]

    raw: str

    status: Literal["pending"]
