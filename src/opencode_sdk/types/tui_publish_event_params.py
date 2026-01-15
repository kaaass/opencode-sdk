# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "TuiPublishEventParams",
    "EventTuiPromptAppend",
    "EventTuiPromptAppendProperties",
    "EventTuiCommandExecute",
    "EventTuiCommandExecuteProperties",
    "EventTuiToastShow",
    "EventTuiToastShowProperties",
    "EventTuiSessionSelect",
    "EventTuiSessionSelectProperties",
]


class EventTuiPromptAppend(TypedDict, total=False):
    properties: Required[EventTuiPromptAppendProperties]

    type: Required[Literal["tui.prompt.append"]]

    directory: str


class EventTuiPromptAppendProperties(TypedDict, total=False):
    text: Required[str]


class EventTuiCommandExecute(TypedDict, total=False):
    properties: Required[EventTuiCommandExecuteProperties]

    type: Required[Literal["tui.command.execute"]]

    directory: str


class EventTuiCommandExecuteProperties(TypedDict, total=False):
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


class EventTuiToastShow(TypedDict, total=False):
    properties: Required[EventTuiToastShowProperties]

    type: Required[Literal["tui.toast.show"]]

    directory: str


class EventTuiToastShowProperties(TypedDict, total=False):
    message: Required[str]

    variant: Required[Literal["info", "success", "warning", "error"]]

    duration: float
    """Duration in milliseconds"""

    title: str


class EventTuiSessionSelect(TypedDict, total=False):
    properties: Required[EventTuiSessionSelectProperties]

    type: Required[Literal["tui.session.select"]]

    directory: str


class EventTuiSessionSelectProperties(TypedDict, total=False):
    session_id: Required[Annotated[str, PropertyInfo(alias="sessionID")]]
    """Session ID to navigate to"""


TuiPublishEventParams: TypeAlias = Union[
    EventTuiPromptAppend, EventTuiCommandExecute, EventTuiToastShow, EventTuiSessionSelect
]
