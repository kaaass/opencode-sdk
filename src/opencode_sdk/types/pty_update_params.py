# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["PtyUpdateParams", "Size"]


class PtyUpdateParams(TypedDict, total=False):
    directory: str

    size: Size

    title: str


class Size(TypedDict, total=False):
    cols: Required[float]

    rows: Required[float]
