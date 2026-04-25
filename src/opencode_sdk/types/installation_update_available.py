# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["InstallationUpdateAvailable", "Properties"]


class Properties(BaseModel):
    version: str


class InstallationUpdateAvailable(BaseModel):
    properties: Properties

    type: Literal["installation.update-available"]
