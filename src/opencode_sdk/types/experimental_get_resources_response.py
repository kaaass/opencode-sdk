# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ExperimentalGetResourcesResponse", "ExperimentalGetResourcesResponseItem"]


class ExperimentalGetResourcesResponseItem(BaseModel):
    client: str

    name: str

    uri: str

    description: Optional[str] = None

    mime_type: Optional[str] = FieldInfo(alias="mimeType", default=None)


ExperimentalGetResourcesResponse: TypeAlias = Dict[str, ExperimentalGetResourcesResponseItem]
