# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["RangeParam", "End", "Start"]


class End(TypedDict, total=False):
    character: Required[float]

    line: Required[float]


class Start(TypedDict, total=False):
    character: Required[float]

    line: Required[float]


class RangeParam(TypedDict, total=False):
    end: Required[End]

    start: Required[Start]
