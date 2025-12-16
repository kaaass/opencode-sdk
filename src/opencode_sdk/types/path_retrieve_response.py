# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["PathRetrieveResponse"]


class PathRetrieveResponse(BaseModel):
    config: str

    directory: str

    home: str

    state: str

    worktree: str
