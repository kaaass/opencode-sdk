# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ArtifactDeleted", "Properties"]


class Properties(BaseModel):
    artifact_id: str = FieldInfo(alias="artifactID")

    session_id: str = FieldInfo(alias="sessionID")


class ArtifactDeleted(BaseModel):
    properties: Properties

    type: Literal["artifact.deleted"]
