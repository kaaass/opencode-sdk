# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .session.file_part_source_param import FilePartSourceParam

__all__ = ["SessionSendCommandParams", "Part"]


class SessionSendCommandParams(TypedDict, total=False):
    arguments: Required[str]

    command: Required[str]

    directory: str

    agent: str

    message_id: Annotated[str, PropertyInfo(alias="messageID")]

    model: str

    parts: Iterable[Part]

    variant: str


class Part(TypedDict, total=False):
    mime: Required[str]

    type: Required[Literal["file"]]

    url: Required[str]

    id: str

    filename: str

    source: FilePartSourceParam
