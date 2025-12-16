# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import TypedDict

from .._types import SequenceNotStr

__all__ = ["PtyCreateParams"]


class PtyCreateParams(TypedDict, total=False):
    directory: str

    args: SequenceNotStr[str]

    command: str

    cwd: str

    env: Dict[str, str]

    title: str
