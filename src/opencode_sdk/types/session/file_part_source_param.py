# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from ..range_param import RangeParam
from .file_part_source_text_param import FilePartSourceTextParam

__all__ = ["FilePartSourceParam", "FileSource", "SymbolSource"]


class FileSource(TypedDict, total=False):
    path: Required[str]

    text: Required[FilePartSourceTextParam]

    type: Required[Literal["file"]]


class SymbolSource(TypedDict, total=False):
    kind: Required[int]

    name: Required[str]

    path: Required[str]

    range: Required[RangeParam]

    text: Required[FilePartSourceTextParam]

    type: Required[Literal["symbol"]]


FilePartSourceParam: TypeAlias = Union[FileSource, SymbolSource]
