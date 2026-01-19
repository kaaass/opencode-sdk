# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

__all__ = ["CustomCreateParams"]


class CustomCreateParams(TypedDict, total=False):
    id: Required[str]

    models: Required[Dict[str, object]]

    name: Required[str]

    npm: Required[str]

    directory: str

    options: Dict[str, object]
