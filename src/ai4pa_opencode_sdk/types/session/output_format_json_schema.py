# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["OutputFormatJsonSchema"]


class OutputFormatJsonSchema(BaseModel):
    schema_: Dict[str, object] = FieldInfo(alias="schema")

    type: Literal["json_schema"]

    retry_count: Optional[int] = FieldInfo(alias="retryCount", default=None)
