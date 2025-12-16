# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ProjectUpdateParams", "Icon"]


class ProjectUpdateParams(TypedDict, total=False):
    directory: str

    icon: Icon

    name: str


class Icon(TypedDict, total=False):
    color: str

    url: str
