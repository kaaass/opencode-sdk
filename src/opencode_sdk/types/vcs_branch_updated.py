# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["VcsBranchUpdated", "Properties"]


class Properties(BaseModel):
    branch: Optional[str] = None


class VcsBranchUpdated(BaseModel):
    properties: Properties

    type: Literal["vcs.branch.updated"]
