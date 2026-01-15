# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Project", "Time", "Icon"]


class Time(BaseModel):
    created: float

    updated: float

    initialized: Optional[float] = None


class Icon(BaseModel):
    color: Optional[str] = None

    url: Optional[str] = None


class Project(BaseModel):
    id: str

    sandboxes: List[str]

    time: Time

    worktree: str

    icon: Optional[Icon] = None

    name: Optional[str] = None

    vcs: Optional[Literal["git"]] = None
