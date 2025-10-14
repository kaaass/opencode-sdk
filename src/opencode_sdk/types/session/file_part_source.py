# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Literal, TypeAlias

from ..range import Range
from ..._models import BaseModel
from .file_part_source_text import FilePartSourceText

__all__ = ["FilePartSource", "FileSource", "SymbolSource"]


class FileSource(BaseModel):
    path: str

    text: FilePartSourceText

    type: Literal["file"]


class SymbolSource(BaseModel):
    kind: int

    name: str

    path: str

    range: Range

    text: FilePartSourceText

    type: Literal["symbol"]


FilePartSource: TypeAlias = Union[FileSource, SymbolSource]
