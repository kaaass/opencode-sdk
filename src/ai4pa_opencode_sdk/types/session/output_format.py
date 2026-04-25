# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import TypeAlias

from .output_format_text import OutputFormatText
from .output_format_json_schema import OutputFormatJsonSchema

__all__ = ["OutputFormat"]

OutputFormat: TypeAlias = Union[OutputFormatText, OutputFormatJsonSchema]
