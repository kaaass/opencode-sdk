# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "TuiPublishEventParams",
    "EventPromptAppend",
    "EventPromptAppendProperties",
    "EventCommandExecute",
    "EventCommandExecuteProperties",
    "EventToastShow",
    "EventToastShowProperties",
    "EventSessionSelect",
    "EventSessionSelectProperties",
]


class EventPromptAppend(TypedDict, total=False):
    properties: Required[EventPromptAppendProperties]

    type: Required[Literal["tui.prompt.append"]]

    directory: str

    workspace: str


class EventPromptAppendProperties(TypedDict, total=False):
    text: Required[str]


class EventCommandExecute(TypedDict, total=False):
    properties: Required[EventCommandExecuteProperties]

    type: Required[Literal["tui.command.execute"]]

    directory: str

    workspace: str


class EventCommandExecuteProperties(TypedDict, total=False):
    command: Required[
        Union[
            Literal[
                "session.list",
                "session.new",
                "session.share",
                "session.interrupt",
                "session.compact",
                "session.page.up",
                "session.page.down",
                "session.line.up",
                "session.line.down",
                "session.half.page.up",
                "session.half.page.down",
                "session.first",
                "session.last",
                "prompt.clear",
                "prompt.submit",
                "agent.cycle",
            ],
            str,
        ]
    ]


class EventToastShow(TypedDict, total=False):
    properties: Required[EventToastShowProperties]

    type: Required[Literal["tui.toast.show"]]

    directory: str

    workspace: str


class EventToastShowProperties(TypedDict, total=False):
    message: Required[str]

    variant: Required[Literal["info", "success", "warning", "error"]]

    duration: float
    """Duration in milliseconds"""

    title: str


class EventSessionSelect(TypedDict, total=False):
    properties: Required[EventSessionSelectProperties]

    type: Required[Literal["tui.session.select"]]

    directory: str

    workspace: str


class EventSessionSelectProperties(TypedDict, total=False):
    session_id: Required[Annotated[str, PropertyInfo(alias="sessionID")]]
    """Session ID to navigate to"""


TuiPublishEventParams: TypeAlias = Union[EventPromptAppend, EventCommandExecute, EventToastShow, EventSessionSelect]
