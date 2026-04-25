# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Literal, Required, TypedDict

from .file_part_param import FilePartParam

__all__ = ["ToolStateCompletedParam", "Time"]


class Time(TypedDict, total=False):
    end: Required[float]

    start: Required[float]

    compacted: float


class ToolStateCompletedParam(TypedDict, total=False):
    input: Required[Dict[str, object]]

    metadata: Required[Dict[str, object]]

    output: Required[str]

    status: Required[Literal["completed"]]

    time: Required[Time]

    title: Required[str]

    attachments: Iterable[FilePartParam]
