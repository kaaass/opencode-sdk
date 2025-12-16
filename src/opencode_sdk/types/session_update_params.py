# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["SessionUpdateParams", "Time"]


class SessionUpdateParams(TypedDict, total=False):
    directory: str

    time: Time

    title: str


class Time(TypedDict, total=False):
    archived: float
