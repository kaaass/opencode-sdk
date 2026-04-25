# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ..._utils import PropertyInfo

__all__ = ["OutputFormatParam", "OutputFormatText", "OutputFormatJsonSchema"]


class OutputFormatText(TypedDict, total=False):
    type: Required[Literal["text"]]


class OutputFormatJsonSchema(TypedDict, total=False):
    schema: Required[Dict[str, object]]

    type: Required[Literal["json_schema"]]

    retry_count: Annotated[int, PropertyInfo(alias="retryCount")]


OutputFormatParam: TypeAlias = Union[OutputFormatText, OutputFormatJsonSchema]
