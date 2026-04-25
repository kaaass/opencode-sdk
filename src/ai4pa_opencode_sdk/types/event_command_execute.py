# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["EventCommandExecute", "Properties"]


class Properties(BaseModel):
    command: Union[
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


class EventCommandExecute(BaseModel):
    properties: Properties

    type: Literal["tui.command.execute"]
