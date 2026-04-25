# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = ["CommandListResponse", "CommandListResponseItem"]


class CommandListResponseItem(BaseModel):
    hints: List[str]

    name: str

    template: str

    agent: Optional[str] = None

    description: Optional[str] = None

    model: Optional[str] = None

    source: Optional[Literal["command", "mcp", "skill"]] = None

    subtask: Optional[bool] = None


CommandListResponse: TypeAlias = List[CommandListResponseItem]
