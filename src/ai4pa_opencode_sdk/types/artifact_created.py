# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel
from .artifact import Artifact

__all__ = ["ArtifactCreated", "Properties"]


class Properties(BaseModel):
    info: Artifact


class ArtifactCreated(BaseModel):
    properties: Properties

    type: Literal["artifact.created"]
