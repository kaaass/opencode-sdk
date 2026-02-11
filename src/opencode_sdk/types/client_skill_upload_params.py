# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .._types import FileTypes

__all__ = ["ClientSkillUploadParams"]


class ClientSkillUploadParams(TypedDict, total=False):
    file: Required[FileTypes]
    """Skill package file (tar.gz format)"""

    directory: str
