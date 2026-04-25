# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypedDict

__all__ = ["EventCommandExecuteParam", "Properties"]


class Properties(TypedDict, total=False):
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


class EventCommandExecuteParam(TypedDict, total=False):
    properties: Required[Properties]

    type: Required[Literal["tui.command.execute"]]
