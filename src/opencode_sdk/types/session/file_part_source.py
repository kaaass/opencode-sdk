# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..range import Range
from ..._models import BaseModel
from .file_part_source_text import FilePartSourceText

__all__ = ["FilePartSource", "FileSource", "SymbolSource", "ResourceSource"]


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


class ResourceSource(BaseModel):
    client_name: str = FieldInfo(alias="clientName")

    text: FilePartSourceText

    type: Literal["resource"]

    uri: str


FilePartSource: TypeAlias = Union[FileSource, SymbolSource, ResourceSource]
