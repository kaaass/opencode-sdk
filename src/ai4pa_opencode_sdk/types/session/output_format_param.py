# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import TypeAlias

from .output_format_text_param import OutputFormatTextParam
from .output_format_json_schema_param import OutputFormatJsonSchemaParam

__all__ = ["OutputFormatParam"]

OutputFormatParam: TypeAlias = Union[OutputFormatTextParam, OutputFormatJsonSchemaParam]
