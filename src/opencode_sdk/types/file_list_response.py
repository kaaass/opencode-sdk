# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = ["FileListResponse", "FileListResponseItem"]


class FileListResponseItem(BaseModel):
    absolute: str

    ignored: bool

    name: str

    path: str

    type: Literal["file", "directory"]


FileListResponse: TypeAlias = List[FileListResponseItem]
