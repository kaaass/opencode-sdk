# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Artifact", "Time"]


class Time(BaseModel):
    created: float


class Artifact(BaseModel):
    id: str

    filename: str

    hash: str

    mime: str

    session_id: str = FieldInfo(alias="sessionID")

    size: int

    time: Time

    metadata: Optional[Dict[str, object]] = None
