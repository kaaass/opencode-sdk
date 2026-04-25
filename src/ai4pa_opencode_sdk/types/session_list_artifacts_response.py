# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .artifact import Artifact

__all__ = ["SessionListArtifactsResponse"]


class SessionListArtifactsResponse(BaseModel):
    artifacts: List[Artifact]

    total: float
