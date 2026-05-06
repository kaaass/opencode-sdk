# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SyncReplayParams", "Event"]


class SyncReplayParams(TypedDict, total=False):
    body_directory: Required[Annotated[str, PropertyInfo(alias="directory")]]

    events: Required[Iterable[Event]]

    query_directory: Annotated[str, PropertyInfo(alias="directory")]

    workspace: str


class Event(TypedDict, total=False):
    id: Required[str]

    aggregate_id: Required[Annotated[str, PropertyInfo(alias="aggregateID")]]

    data: Required[Dict[str, object]]

    seq: Required[int]

    type: Required[str]
