# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Literal, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo
from ..global_.permission_config_param import PermissionConfigParam

__all__ = ["AgentConfig"]


class AgentConfig(  # type: ignore[call-arg]
    TypedDict,
    total=False,
    extra_items=object,  # pyright: ignore[reportGeneralTypeIssues]
):
    color: Union[str, Literal["primary", "secondary", "accent", "success", "warning", "error", "info"]]
    """Hex color code (e.g., #FF5733) or theme color (e.g., primary)"""

    description: str
    """Description of when to use the agent"""

    disable: bool

    hidden: bool
    """
    Hide this subagent from the @ autocomplete menu (default: false, only applies to
    mode: subagent)
    """

    max_steps: Annotated[int, PropertyInfo(alias="maxSteps")]
    """@deprecated Use 'steps' field instead."""

    mode: Literal["subagent", "primary", "all"]

    model: str

    options: Dict[str, object]

    permission: PermissionConfigParam

    prompt: str

    skills: Optional[SequenceNotStr[str]]
    """Restrict which skills this agent may load via the skill tool.

    Empty/null = no restriction.
    """

    steps: int
    """Maximum number of agentic iterations before forcing text-only response"""

    sub_agents: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="subAgents")]
    """Restrict which subagents this agent may invoke via the task tool.

    Empty/null = no restriction.
    """

    temperature: float

    tools: Dict[str, bool]
    """@deprecated Use 'permission' field instead"""

    top_p: float

    variant: str
    """
    Default model variant for this agent (applies only when using the agent's
    configured model).
    """
