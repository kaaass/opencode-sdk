# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Dict, List, Union, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["AgentConfig"]


class AgentConfig(BaseModel):
    color: Union[str, Literal["primary", "secondary", "accent", "success", "warning", "error", "info"], None] = None
    """Hex color code (e.g., #FF5733) or theme color (e.g., primary)"""

    description: Optional[str] = None
    """Description of when to use the agent"""

    disable: Optional[bool] = None

    hidden: Optional[bool] = None
    """
    Hide this subagent from the @ autocomplete menu (default: false, only applies to
    mode: subagent)
    """

    max_steps: Optional[int] = FieldInfo(alias="maxSteps", default=None)
    """@deprecated Use 'steps' field instead."""

    mode: Optional[Literal["subagent", "primary", "all"]] = None

    model: Optional[str] = None

    options: Optional[Dict[str, object]] = None

    permission: Optional[PermissionConfig] = None

    prompt: Optional[str] = None

    skills: Optional[List[str]] = None
    """Restrict which skills this agent may load via the skill tool.

    Empty/null = no restriction.
    """

    steps: Optional[int] = None
    """Maximum number of agentic iterations before forcing text-only response"""

    sub_agents: Optional[List[str]] = FieldInfo(alias="subAgents", default=None)
    """Restrict which subagents this agent may invoke via the task tool.

    Empty/null = no restriction.
    """

    temperature: Optional[float] = None

    tools: Optional[Dict[str, bool]] = None
    """@deprecated Use 'permission' field instead"""

    top_p: Optional[float] = None

    variant: Optional[str] = None
    """
    Default model variant for this agent (applies only when using the agent's
    configured model).
    """

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


# Deferred import to break the circular dependency with ..global_.config, which
# transitively imports AgentConfig. The PermissionConfig field on AgentConfig is
# resolved lazily via the `from __future__ import annotations` string form.
from ..global_.permission_config import PermissionConfig as PermissionConfig  # noqa: E402
