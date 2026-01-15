# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["WorktreeCreateResponse"]


class WorktreeCreateResponse(BaseModel):
    branch: str

    directory: str

    name: str
