# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .session.file_part_param import FilePartParam

__all__ = ["SessionSubmitToolResultsParams", "Result"]


class SessionSubmitToolResultsParams(TypedDict, total=False):
    results: Required[Iterable[Result]]

    directory: str

    async_: Annotated[bool, PropertyInfo(alias="async")]

    continue_loop: Annotated[bool, PropertyInfo(alias="continueLoop")]


class Result(TypedDict, total=False):
    call_id: Required[Annotated[str, PropertyInfo(alias="callID")]]

    output: Required[str]

    attachments: Iterable[FilePartParam]

    metadata: Dict[str, object]

    title: str
