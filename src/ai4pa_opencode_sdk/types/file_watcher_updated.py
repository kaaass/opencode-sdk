# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["FileWatcherUpdated", "Properties"]


class Properties(BaseModel):
    event: Literal["add", "change", "unlink"]

    file: str


class FileWatcherUpdated(BaseModel):
    properties: Properties

    type: Literal["file.watcher.updated"]
