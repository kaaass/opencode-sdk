# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["OutputFormatJsonSchemaParam"]


class OutputFormatJsonSchemaParam(TypedDict, total=False):
    schema: Required[Dict[str, object]]

    type: Required[Literal["json_schema"]]

    retry_count: Annotated[int, PropertyInfo(alias="retryCount")]
