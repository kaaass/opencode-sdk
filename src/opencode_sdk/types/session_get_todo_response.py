# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .todo import Todo

__all__ = ["SessionGetTodoResponse"]

SessionGetTodoResponse: TypeAlias = List[Todo]
