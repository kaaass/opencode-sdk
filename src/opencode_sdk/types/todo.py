# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["Todo"]


class Todo(BaseModel):
    content: str
    """Brief description of the task"""

    priority: str
    """Priority level of the task: high, medium, low"""

    status: str
    """Current status of the task: pending, in_progress, completed, cancelled"""
