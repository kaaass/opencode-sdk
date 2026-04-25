# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .permission_config import PermissionConfig

__all__ = [
    "Config",
    "Agent",
    "AgentBuild",
    "AgentCompaction",
    "AgentExplore",
    "AgentGeneral",
    "AgentPlan",
    "AgentSummary",
    "AgentTitle",
    "AgentAgentItem",
    "Command",
    "Compaction",
    "Enterprise",
    "Experimental",
    "FormatterUnionMember1FormatterUnionMember1Item",
    "LspUnionMember1LspUnionMember1Item",
    "LspUnionMember1LspUnionMember1ItemDisabled",
    "LspUnionMember1LspUnionMember1ItemUnionMember1",
    "Mcp",
    "McpMcpLocalConfig",
    "McpMcpRemoteConfig",
    "McpMcpRemoteConfigOAuth",
    "McpMcpRemoteConfigOAuthMcpOAuthConfig",
    "McpEnabled",
    "Mode",
    "ModeBuild",
    "ModePlan",
    "ModeModeItem",
    "Provider",
    "ProviderModels",
    "ProviderModelsCost",
    "ProviderModelsCostContextOver200k",
    "ProviderModelsInterleaved",
    "ProviderModelsInterleavedField",
    "ProviderModelsLimit",
    "ProviderModelsModalities",
    "ProviderModelsProvider",
    "ProviderModelsVariants",
    "ProviderOptions",
    "Server",
    "Skills",
    "Watcher",
]


class AgentBuild(BaseModel):
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
    """List of skill names that can be invoked by this agent"""

    steps: Optional[int] = None
    """Maximum number of agentic iterations before forcing text-only response"""

    sub_agents: Optional[List[str]] = FieldInfo(alias="subAgents", default=None)
    """List of sub-agent names that can be invoked by this agent"""

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


class AgentCompaction(BaseModel):
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
    """List of skill names that can be invoked by this agent"""

    steps: Optional[int] = None
    """Maximum number of agentic iterations before forcing text-only response"""

    sub_agents: Optional[List[str]] = FieldInfo(alias="subAgents", default=None)
    """List of sub-agent names that can be invoked by this agent"""

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


class AgentExplore(BaseModel):
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
    """List of skill names that can be invoked by this agent"""

    steps: Optional[int] = None
    """Maximum number of agentic iterations before forcing text-only response"""

    sub_agents: Optional[List[str]] = FieldInfo(alias="subAgents", default=None)
    """List of sub-agent names that can be invoked by this agent"""

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


class AgentGeneral(BaseModel):
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
    """List of skill names that can be invoked by this agent"""

    steps: Optional[int] = None
    """Maximum number of agentic iterations before forcing text-only response"""

    sub_agents: Optional[List[str]] = FieldInfo(alias="subAgents", default=None)
    """List of sub-agent names that can be invoked by this agent"""

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


class AgentPlan(BaseModel):
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
    """List of skill names that can be invoked by this agent"""

    steps: Optional[int] = None
    """Maximum number of agentic iterations before forcing text-only response"""

    sub_agents: Optional[List[str]] = FieldInfo(alias="subAgents", default=None)
    """List of sub-agent names that can be invoked by this agent"""

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


class AgentSummary(BaseModel):
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
    """List of skill names that can be invoked by this agent"""

    steps: Optional[int] = None
    """Maximum number of agentic iterations before forcing text-only response"""

    sub_agents: Optional[List[str]] = FieldInfo(alias="subAgents", default=None)
    """List of sub-agent names that can be invoked by this agent"""

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


class AgentTitle(BaseModel):
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
    """List of skill names that can be invoked by this agent"""

    steps: Optional[int] = None
    """Maximum number of agentic iterations before forcing text-only response"""

    sub_agents: Optional[List[str]] = FieldInfo(alias="subAgents", default=None)
    """List of sub-agent names that can be invoked by this agent"""

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


class AgentAgentItem(BaseModel):
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
    """List of skill names that can be invoked by this agent"""

    steps: Optional[int] = None
    """Maximum number of agentic iterations before forcing text-only response"""

    sub_agents: Optional[List[str]] = FieldInfo(alias="subAgents", default=None)
    """List of sub-agent names that can be invoked by this agent"""

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


class Agent(BaseModel):
    """Agent configuration, see https://opencode.ai/docs/agents"""

    build: Optional[AgentBuild] = None

    compaction: Optional[AgentCompaction] = None

    explore: Optional[AgentExplore] = None

    general: Optional[AgentGeneral] = None

    plan: Optional[AgentPlan] = None

    summary: Optional[AgentSummary] = None

    title: Optional[AgentTitle] = None

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, AgentAgentItem] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> AgentAgentItem: ...
    else:
        __pydantic_extra__: Dict[str, AgentAgentItem]


class Command(BaseModel):
    template: str

    agent: Optional[str] = None

    description: Optional[str] = None

    model: Optional[str] = None

    subtask: Optional[bool] = None


class Compaction(BaseModel):
    auto: Optional[bool] = None
    """Enable automatic compaction when context is full (default: true)"""

    prune: Optional[bool] = None
    """Enable pruning of old tool outputs (default: true)"""

    reserved: Optional[int] = None
    """Token buffer for compaction.

    Leaves enough window to avoid overflow during compaction.
    """


class Enterprise(BaseModel):
    url: Optional[str] = None
    """Enterprise URL"""


class Experimental(BaseModel):
    batch_tool: Optional[bool] = None
    """Enable the batch tool"""

    continue_loop_on_deny: Optional[bool] = None
    """Continue the agent loop when a tool call is denied"""

    disable_paste_summary: Optional[bool] = None

    mcp_timeout: Optional[int] = None
    """Timeout in milliseconds for model context protocol (MCP) requests"""

    open_telemetry: Optional[bool] = FieldInfo(alias="openTelemetry", default=None)
    """
    Enable OpenTelemetry spans for AI SDK calls (using the 'experimental_telemetry'
    flag)
    """

    primary_tools: Optional[List[str]] = None
    """Tools that should only be available to primary agents."""


class FormatterUnionMember1FormatterUnionMember1Item(BaseModel):
    command: Optional[List[str]] = None

    disabled: Optional[bool] = None

    environment: Optional[Dict[str, str]] = None

    extensions: Optional[List[str]] = None


class LspUnionMember1LspUnionMember1ItemDisabled(BaseModel):
    disabled: Literal[True]


class LspUnionMember1LspUnionMember1ItemUnionMember1(BaseModel):
    command: List[str]

    disabled: Optional[bool] = None

    env: Optional[Dict[str, str]] = None

    extensions: Optional[List[str]] = None

    initialization: Optional[Dict[str, object]] = None


LspUnionMember1LspUnionMember1Item: TypeAlias = Union[
    LspUnionMember1LspUnionMember1ItemDisabled, LspUnionMember1LspUnionMember1ItemUnionMember1
]


class McpMcpLocalConfig(BaseModel):
    command: List[str]
    """Command and arguments to run the MCP server"""

    type: Literal["local"]
    """Type of MCP server connection"""

    enabled: Optional[bool] = None
    """Enable or disable the MCP server on startup"""

    environment: Optional[Dict[str, str]] = None
    """Environment variables to set when running the MCP server"""

    timeout: Optional[int] = None
    """Timeout in ms for MCP server requests.

    Defaults to 5000 (5 seconds) if not specified.
    """


class McpMcpRemoteConfigOAuthMcpOAuthConfig(BaseModel):
    client_id: Optional[str] = FieldInfo(alias="clientId", default=None)
    """OAuth client ID.

    If not provided, dynamic client registration (RFC 7591) will be attempted.
    """

    client_secret: Optional[str] = FieldInfo(alias="clientSecret", default=None)
    """OAuth client secret (if required by the authorization server)"""

    redirect_uri: Optional[str] = FieldInfo(alias="redirectUri", default=None)
    """OAuth redirect URI (default: http://127.0.0.1:19876/mcp/oauth/callback)."""

    scope: Optional[str] = None
    """OAuth scopes to request during authorization"""


McpMcpRemoteConfigOAuth: TypeAlias = Union[McpMcpRemoteConfigOAuthMcpOAuthConfig, Literal[False]]


class McpMcpRemoteConfig(BaseModel):
    type: Literal["remote"]
    """Type of MCP server connection"""

    url: str
    """URL of the remote MCP server"""

    enabled: Optional[bool] = None
    """Enable or disable the MCP server on startup"""

    headers: Optional[Dict[str, str]] = None
    """Headers to send with the request"""

    oauth: Optional[McpMcpRemoteConfigOAuth] = None
    """OAuth authentication configuration for the MCP server.

    Set to false to disable OAuth auto-detection.
    """

    timeout: Optional[int] = None
    """Timeout in ms for MCP server requests.

    Defaults to 5000 (5 seconds) if not specified.
    """


class McpEnabled(BaseModel):
    enabled: bool


Mcp: TypeAlias = Union[McpMcpLocalConfig, McpMcpRemoteConfig, McpEnabled]


class ModeBuild(BaseModel):
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
    """List of skill names that can be invoked by this agent"""

    steps: Optional[int] = None
    """Maximum number of agentic iterations before forcing text-only response"""

    sub_agents: Optional[List[str]] = FieldInfo(alias="subAgents", default=None)
    """List of sub-agent names that can be invoked by this agent"""

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


class ModePlan(BaseModel):
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
    """List of skill names that can be invoked by this agent"""

    steps: Optional[int] = None
    """Maximum number of agentic iterations before forcing text-only response"""

    sub_agents: Optional[List[str]] = FieldInfo(alias="subAgents", default=None)
    """List of sub-agent names that can be invoked by this agent"""

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


class ModeModeItem(BaseModel):
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
    """List of skill names that can be invoked by this agent"""

    steps: Optional[int] = None
    """Maximum number of agentic iterations before forcing text-only response"""

    sub_agents: Optional[List[str]] = FieldInfo(alias="subAgents", default=None)
    """List of sub-agent names that can be invoked by this agent"""

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


class Mode(BaseModel):
    """@deprecated Use `agent` field instead."""

    build: Optional[ModeBuild] = None

    plan: Optional[ModePlan] = None

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, ModeModeItem] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> ModeModeItem: ...
    else:
        __pydantic_extra__: Dict[str, ModeModeItem]


class ProviderModelsCostContextOver200k(BaseModel):
    input: float

    output: float

    cache_read: Optional[float] = None

    cache_write: Optional[float] = None


class ProviderModelsCost(BaseModel):
    input: float

    output: float

    cache_read: Optional[float] = None

    cache_write: Optional[float] = None

    context_over_200k: Optional[ProviderModelsCostContextOver200k] = None


class ProviderModelsInterleavedField(BaseModel):
    field: Literal["reasoning_content", "reasoning_details"]


ProviderModelsInterleaved: TypeAlias = Union[Literal[True], ProviderModelsInterleavedField]


class ProviderModelsLimit(BaseModel):
    context: float

    output: float

    input: Optional[float] = None


class ProviderModelsModalities(BaseModel):
    input: List[Literal["text", "audio", "image", "video", "pdf"]]

    output: List[Literal["text", "audio", "image", "video", "pdf"]]


class ProviderModelsProvider(BaseModel):
    api: Optional[str] = None

    npm: Optional[str] = None


class ProviderModelsVariants(BaseModel):
    disabled: Optional[bool] = None
    """Disable this variant for the model"""

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


class ProviderModels(BaseModel):
    id: Optional[str] = None

    attachment: Optional[bool] = None

    cost: Optional[ProviderModelsCost] = None

    experimental: Optional[bool] = None

    family: Optional[str] = None

    headers: Optional[Dict[str, str]] = None

    interleaved: Optional[ProviderModelsInterleaved] = None

    limit: Optional[ProviderModelsLimit] = None

    modalities: Optional[ProviderModelsModalities] = None

    name: Optional[str] = None

    options: Optional[Dict[str, object]] = None

    provider: Optional[ProviderModelsProvider] = None

    reasoning: Optional[bool] = None

    release_date: Optional[str] = None

    status: Optional[Literal["alpha", "beta", "deprecated"]] = None

    temperature: Optional[bool] = None

    tool_call: Optional[bool] = None

    variants: Optional[Dict[str, ProviderModelsVariants]] = None
    """Variant-specific configuration"""


class ProviderOptions(BaseModel):
    api_key: Optional[str] = FieldInfo(alias="apiKey", default=None)

    base_url: Optional[str] = FieldInfo(alias="baseURL", default=None)

    chunk_timeout: Optional[int] = FieldInfo(alias="chunkTimeout", default=None)
    """Timeout in milliseconds between streamed SSE chunks for this provider.

    If no chunk arrives within this window, the request is aborted.
    """

    enterprise_url: Optional[str] = FieldInfo(alias="enterpriseUrl", default=None)
    """GitHub Enterprise URL for copilot authentication"""

    set_cache_key: Optional[bool] = FieldInfo(alias="setCacheKey", default=None)
    """Enable promptCacheKey for this provider (default false)"""

    timeout: Union[int, Literal[False], None] = None
    """Timeout in milliseconds for requests to this provider.

    Default is 300000 (5 minutes). Set to false to disable timeout.
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


class Provider(BaseModel):
    id: Optional[str] = None

    api: Optional[str] = None

    blacklist: Optional[List[str]] = None

    env: Optional[List[str]] = None

    models: Optional[Dict[str, ProviderModels]] = None

    name: Optional[str] = None

    npm: Optional[str] = None

    options: Optional[ProviderOptions] = None

    whitelist: Optional[List[str]] = None


class Server(BaseModel):
    """Server configuration for opencode serve and web commands"""

    cors: Optional[List[str]] = None
    """Additional domains to allow for CORS"""

    hostname: Optional[str] = None
    """Hostname to listen on"""

    mdns: Optional[bool] = None
    """Enable mDNS service discovery"""

    mdns_domain: Optional[str] = FieldInfo(alias="mdnsDomain", default=None)
    """Custom domain name for mDNS service (default: opencode.local)"""

    port: Optional[int] = None
    """Port to listen on"""


class Skills(BaseModel):
    """Additional skill folder paths"""

    paths: Optional[List[str]] = None
    """Additional paths to skill folders"""

    urls: Optional[List[str]] = None
    """URLs to fetch skills from (e.g., https://example.com/.well-known/skills/)"""


class Watcher(BaseModel):
    ignore: Optional[List[str]] = None


class Config(BaseModel):
    schema_: Optional[str] = FieldInfo(alias="$schema", default=None)
    """JSON schema reference for configuration validation"""

    agent: Optional[Agent] = None
    """Agent configuration, see https://opencode.ai/docs/agents"""

    artifact_allowed_paths: Optional[List[str]] = None
    """
    允许创建 artifact 的文件路径前缀白名单。路径将被 resolve 为绝对路径后进行前缀匹
    配。默认允许 /tmp 路径。
    """

    autoshare: Optional[bool] = None
    """@deprecated Use 'share' field instead.

    Share newly created sessions automatically
    """

    autoupdate: Union[bool, Literal["notify"], None] = None
    """Automatically update to the latest version.

    Set to true to auto-update, false to disable, or 'notify' to show update
    notifications
    """

    command: Optional[Dict[str, Command]] = None
    """Command configuration, see https://opencode.ai/docs/commands"""

    compaction: Optional[Compaction] = None

    custom_provider_npm_whitelist: Optional[List[str]] = None
    """允许用于 custom provider 的 npm 包白名单"""

    default_agent: Optional[str] = None
    """Default agent to use when none is specified.

    Must be a primary agent. Falls back to 'build' if not set or if the specified
    agent is invalid.
    """

    disabled_providers: Optional[List[str]] = None
    """Disable providers that are loaded automatically"""

    enabled_providers: Optional[List[str]] = None
    """When set, ONLY these providers will be enabled.

    All other providers will be ignored
    """

    enterprise: Optional[Enterprise] = None

    experimental: Optional[Experimental] = None

    formatter: Union[Literal[False], Dict[str, FormatterUnionMember1FormatterUnionMember1Item], None] = None

    instructions: Optional[List[str]] = None
    """Additional instruction files or patterns to include"""

    layout: Optional[Literal["auto", "stretch"]] = None
    """@deprecated Always uses stretch layout."""

    log_level: Optional[Literal["DEBUG", "INFO", "WARN", "ERROR"]] = FieldInfo(alias="logLevel", default=None)
    """Log level"""

    lsp: Union[Literal[False], Dict[str, LspUnionMember1LspUnionMember1Item], None] = None

    mcp: Optional[Dict[str, Mcp]] = None
    """MCP (Model Context Protocol) server configurations"""

    mode: Optional[Mode] = None
    """@deprecated Use `agent` field instead."""

    model: Optional[str] = None
    """Model to use in the format of provider/model, eg anthropic/claude-2"""

    permission: Optional[PermissionConfig] = None

    plugin: Optional[List[Union[str, List[object]]]] = None

    provider: Optional[Dict[str, Provider]] = None
    """Custom provider configurations and model overrides"""

    server: Optional[Server] = None
    """Server configuration for opencode serve and web commands"""

    share: Optional[Literal["manual", "auto", "disabled"]] = None
    """
    Control sharing behavior:'manual' allows manual sharing via commands, 'auto'
    enables automatic sharing, 'disabled' disables all sharing
    """

    skills: Optional[Skills] = None
    """Additional skill folder paths"""

    small_model: Optional[str] = None
    """
    Small model to use for tasks like title generation in the format of
    provider/model
    """

    snapshot: Optional[bool] = None
    """Enable or disable snapshot tracking.

    When false, filesystem snapshots are not recorded and undoing or reverting will
    not undo/redo file changes. Defaults to true.
    """

    tools: Optional[Dict[str, bool]] = None

    username: Optional[str] = None
    """Custom username to display in conversations instead of system username"""

    watcher: Optional[Watcher] = None
