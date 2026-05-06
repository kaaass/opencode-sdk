# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ArtifactCreated", "Properties"]


class Properties(BaseModel):
    info: Dict[str, object]


class ArtifactCreated(BaseModel):
    properties: Properties

    type: Literal["artifact.created"]
