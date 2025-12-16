# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["FileReadResponse", "Patch", "PatchHunk"]


class PatchHunk(BaseModel):
    lines: List[str]

    new_lines: float = FieldInfo(alias="newLines")

    new_start: float = FieldInfo(alias="newStart")

    old_lines: float = FieldInfo(alias="oldLines")

    old_start: float = FieldInfo(alias="oldStart")


class Patch(BaseModel):
    hunks: List[PatchHunk]

    new_file_name: str = FieldInfo(alias="newFileName")

    old_file_name: str = FieldInfo(alias="oldFileName")

    index: Optional[str] = None

    new_header: Optional[str] = FieldInfo(alias="newHeader", default=None)

    old_header: Optional[str] = FieldInfo(alias="oldHeader", default=None)


class FileReadResponse(BaseModel):
    content: str

    type: Literal["text"]

    diff: Optional[str] = None

    encoding: Optional[Literal["base64"]] = None

    mime_type: Optional[str] = FieldInfo(alias="mimeType", default=None)

    patch: Optional[Patch] = None
