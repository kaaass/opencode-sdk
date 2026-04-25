# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo
from .session.output_format_param import OutputFormatParam
from .session.file_part_input_param import FilePartInputParam
from .session.text_part_input_param import TextPartInputParam
from .session.agent_part_input_param import AgentPartInputParam
from .session.subtask_part_input_param import SubtaskPartInputParam

__all__ = ["SessionSendAsyncMessageParams", "Part", "Model"]


class SessionSendAsyncMessageParams(TypedDict, total=False):
    parts: Required[Iterable[Part]]

    directory: str

    workspace: str

    agent: str

    format: OutputFormatParam

    message_id: Annotated[str, PropertyInfo(alias="messageID")]

    model: Model

    no_reply: Annotated[bool, PropertyInfo(alias="noReply")]

    system: str

    tools: Dict[str, bool]
    """
    @deprecated tools and permissions have been merged, you can set permissions on
    the session itself now
    """

    variant: str


Part: TypeAlias = Union[TextPartInputParam, FilePartInputParam, AgentPartInputParam, SubtaskPartInputParam]


class Model(TypedDict, total=False):
    model_id: Required[Annotated[str, PropertyInfo(alias="modelID")]]

    provider_id: Required[Annotated[str, PropertyInfo(alias="providerID")]]
