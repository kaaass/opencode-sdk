# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["OutputFormat", "OutputFormatText", "OutputFormatJsonSchema"]


class OutputFormatText(BaseModel):
    type: Literal["text"]


class OutputFormatJsonSchema(BaseModel):
    schema_: Dict[str, object] = FieldInfo(alias="schema")

    type: Literal["json_schema"]

    retry_count: Optional[int] = FieldInfo(alias="retryCount", default=None)


OutputFormat: TypeAlias = Union[OutputFormatText, OutputFormatJsonSchema]
