# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .todo import Todo
from .._models import BaseModel

__all__ = ["TodoUpdated", "Properties"]


class Properties(BaseModel):
    session_id: str = FieldInfo(alias="sessionID")

    todos: List[Todo]


class TodoUpdated(BaseModel):
    properties: Properties

    type: Literal["todo.updated"]
