# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["SessionListArtifactsResponse", "Artifact", "ArtifactTime"]


class ArtifactTime(BaseModel):
    created: float


class Artifact(BaseModel):
    id: str

    filename: str

    hash: str

    mime: str

    session_id: str = FieldInfo(alias="sessionID")

    size: int

    time: ArtifactTime

    metadata: Optional[Dict[str, object]] = None


class SessionListArtifactsResponse(BaseModel):
    artifacts: List[Artifact]

    total: float
