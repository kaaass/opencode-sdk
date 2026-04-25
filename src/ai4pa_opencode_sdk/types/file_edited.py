# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["FileEdited", "Properties"]


class Properties(BaseModel):
    file: str


class FileEdited(BaseModel):
    properties: Properties

    type: Literal["file.edited"]
