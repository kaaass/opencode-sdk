# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel
from .project.project import Project

__all__ = ["ProjectUpdated"]


class ProjectUpdated(BaseModel):
    properties: Project

    type: Literal["project.updated"]
