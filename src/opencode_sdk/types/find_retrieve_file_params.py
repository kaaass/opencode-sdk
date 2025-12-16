# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["FindRetrieveFileParams"]


class FindRetrieveFileParams(TypedDict, total=False):
    query: Required[str]

    directory: str

    dirs: Literal["true", "false"]
