# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["Workspace"]


class Workspace(BaseModel):
    id: str

    branch: Optional[str] = None

    directory: Optional[str] = None

    extra: object

    name: str

    project_id: str = FieldInfo(alias="projectID")

    type: str
