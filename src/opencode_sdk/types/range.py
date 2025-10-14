# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["Range", "End", "Start"]


class End(BaseModel):
    character: float

    line: float


class Start(BaseModel):
    character: float

    line: float


class Range(BaseModel):
    end: End

    start: Start
