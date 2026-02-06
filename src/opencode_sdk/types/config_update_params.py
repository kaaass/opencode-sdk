# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = [
    "ConfigUpdateParams",
    "Agent",
    "AgentBuild",
    "AgentBuildPermission",
    "AgentBuildPermissionUnionMember0",
    "AgentCompaction",
    "AgentCompactionPermission",
    "AgentCompactionPermissionUnionMember0",
    "AgentExplore",
    "AgentExplorePermission",
    "AgentExplorePermissionUnionMember0",
    "AgentGeneral",
    "AgentGeneralPermission",
    "AgentGeneralPermissionUnionMember0",
    "AgentPlan",
    "AgentPlanPermission",
    "AgentPlanPermissionUnionMember0",
    "AgentSummary",
    "AgentSummaryPermission",
    "AgentSummaryPermissionUnionMember0",
    "AgentTitle",
    "AgentTitlePermission",
    "AgentTitlePermissionUnionMember0",
    "AgentAgentItem",
    "AgentAgentItemPermission",
    "AgentAgentItemPermissionUnionMember0",
    "Command",
    "Compaction",
    "Enterprise",
    "Experimental",
    "ExperimentalHook",
    "ExperimentalHookFileEdited",
    "ExperimentalHookSessionCompleted",
    "FormatterUnionMember1FormatterUnionMember1Item",
    "Keybinds",
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
    "ModeBuildPermission",
    "ModeBuildPermissionUnionMember0",
    "ModePlan",
    "ModePlanPermission",
    "ModePlanPermissionUnionMember0",
    "ModeModeItem",
    "ModeModeItemPermission",
    "ModeModeItemPermissionUnionMember0",
    "Permission",
    "PermissionUnionMember0",
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
    "Tui",
    "TuiScrollAcceleration",
    "Watcher",
]


class ConfigUpdateParams(TypedDict, total=False):
    directory: str

    schema: Annotated[str, PropertyInfo(alias="$schema")]
    """JSON schema reference for configuration validation"""

    agent: Agent
    """Agent configuration, see https://opencode.ai/docs/agent"""

    artifact_allowed_paths: SequenceNotStr[str]
    """
    允许创建 artifact 的文件路径前缀白名单。路径将被 resolve 为绝对路径后进行前缀匹
    配。默认允许 /tmp 路径。
    """

    autoshare: bool
    """@deprecated Use 'share' field instead.

    Share newly created sessions automatically
    """

    autoupdate: Union[bool, Literal["notify"]]
    """Automatically update to the latest version.

    Set to true to auto-update, false to disable, or 'notify' to show update
    notifications
    """

    command: Dict[str, Command]
    """Command configuration, see https://opencode.ai/docs/commands"""

    compaction: Compaction

    custom_provider_npm_whitelist: SequenceNotStr[str]
    """允许用于 custom provider 的 npm 包白名单"""

    default_agent: str
    """Default agent to use when none is specified.

    Must be a primary agent. Falls back to 'build' if not set or if the specified
    agent is invalid.
    """

    disabled_providers: SequenceNotStr[str]
    """Disable providers that are loaded automatically"""

    enabled_providers: SequenceNotStr[str]
    """When set, ONLY these providers will be enabled.

    All other providers will be ignored
    """

    enterprise: Enterprise

    experimental: Experimental

    formatter: Union[Literal[False], Dict[str, FormatterUnionMember1FormatterUnionMember1Item]]

    instructions: SequenceNotStr[str]
    """Additional instruction files or patterns to include"""

    keybinds: Keybinds
    """Custom keybind configurations"""

    layout: Literal["auto", "stretch"]
    """@deprecated Always uses stretch layout."""

    log_level: Annotated[Literal["DEBUG", "INFO", "WARN", "ERROR"], PropertyInfo(alias="logLevel")]
    """Log level"""

    lsp: Union[Literal[False], Dict[str, LspUnionMember1LspUnionMember1Item]]

    mcp: Dict[str, Mcp]
    """MCP (Model Context Protocol) server configurations"""

    mode: Mode
    """@deprecated Use `agent` field instead."""

    model: str
    """Model to use in the format of provider/model, eg anthropic/claude-2"""

    permission: Permission

    plugin: SequenceNotStr[str]

    provider: Dict[str, Provider]
    """Custom provider configurations and model overrides"""

    server: Server
    """Server configuration for opencode serve and web commands"""

    share: Literal["manual", "auto", "disabled"]
    """
    Control sharing behavior:'manual' allows manual sharing via commands, 'auto'
    enables automatic sharing, 'disabled' disables all sharing
    """

    small_model: str
    """
    Small model to use for tasks like title generation in the format of
    provider/model
    """

    snapshot: bool

    theme: str
    """Theme name to use for the interface"""

    tools: Dict[str, bool]

    tui: Tui
    """TUI specific settings"""

    username: str
    """Custom username to display in conversations instead of system username"""

    watcher: Watcher


class AgentBuildPermissionUnionMember0Typed(TypedDict, total=False):
    _original_keys: Annotated[SequenceNotStr[str], PropertyInfo(alias="__originalKeys")]

    bash: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]

    codesearch: Literal["ask", "allow", "deny"]

    doom_loop: Literal["ask", "allow", "deny"]

    edit: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]

    external_directory: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]

    glob: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]

    grep: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]

    list: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]

    lsp: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]

    question: Literal["ask", "allow", "deny"]

    read: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]

    task: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]

    todoread: Literal["ask", "allow", "deny"]

    todowrite: Literal["ask", "allow", "deny"]

    webfetch: Literal["ask", "allow", "deny"]

    websearch: Literal["ask", "allow", "deny"]


AgentBuildPermissionUnionMember0: TypeAlias = Union[
    AgentBuildPermissionUnionMember0Typed,
    Dict[str, Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]],
]

AgentBuildPermission: TypeAlias = Union[AgentBuildPermissionUnionMember0, Literal["ask", "allow", "deny"]]


class AgentBuildTyped(TypedDict, total=False):
    color: str
    """Hex color code for the agent (e.g., #FF5733)"""

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

    permission: AgentBuildPermission

    prompt: str

    skills: Optional[SequenceNotStr[str]]
    """List of skill names that can be invoked by this agent"""

    steps: int
    """Maximum number of agentic iterations before forcing text-only response"""

    sub_agents: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="subAgents")]
    """List of sub-agent names that can be invoked by this agent"""

    temperature: float

    tools: Dict[str, bool]
    """@deprecated Use 'permission' field instead"""

    top_p: float


AgentBuild: TypeAlias = Union[AgentBuildTyped, Dict[str, object]]


class AgentCompactionPermissionUnionMember0Typed(TypedDict, total=False):
    _original_keys: Annotated[SequenceNotStr[str], PropertyInfo(alias="__originalKeys")]

    bash: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]

    codesearch: Literal["ask", "allow", "deny"]

    doom_loop: Literal["ask", "allow", "deny"]

    edit: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]

    external_directory: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]

    glob: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]

    grep: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]

    list: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]

    lsp: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]

    question: Literal["ask", "allow", "deny"]

    read: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]

    task: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]

    todoread: Literal["ask", "allow", "deny"]

    todowrite: Literal["ask", "allow", "deny"]

    webfetch: Literal["ask", "allow", "deny"]

    websearch: Literal["ask", "allow", "deny"]


AgentCompactionPermissionUnionMember0: TypeAlias = Union[
    AgentCompactionPermissionUnionMember0Typed,
    Dict[str, Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]],
]

AgentCompactionPermission: TypeAlias = Union[AgentCompactionPermissionUnionMember0, Literal["ask", "allow", "deny"]]


class AgentCompactionTyped(TypedDict, total=False):
    color: str
    """Hex color code for the agent (e.g., #FF5733)"""

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

    permission: AgentCompactionPermission

    prompt: str

    skills: Optional[SequenceNotStr[str]]
    """List of skill names that can be invoked by this agent"""

    steps: int
    """Maximum number of agentic iterations before forcing text-only response"""

    sub_agents: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="subAgents")]
    """List of sub-agent names that can be invoked by this agent"""

    temperature: float

    tools: Dict[str, bool]
    """@deprecated Use 'permission' field instead"""

    top_p: float


AgentCompaction: TypeAlias = Union[AgentCompactionTyped, Dict[str, object]]


class AgentExplorePermissionUnionMember0Typed(TypedDict, total=False):
    _original_keys: Annotated[SequenceNotStr[str], PropertyInfo(alias="__originalKeys")]

    bash: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]

    codesearch: Literal["ask", "allow", "deny"]

    doom_loop: Literal["ask", "allow", "deny"]

    edit: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]

    external_directory: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]

    glob: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]

    grep: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]

    list: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]

    lsp: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]

    question: Literal["ask", "allow", "deny"]

    read: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]

    task: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]

    todoread: Literal["ask", "allow", "deny"]

    todowrite: Literal["ask", "allow", "deny"]

    webfetch: Literal["ask", "allow", "deny"]

    websearch: Literal["ask", "allow", "deny"]


AgentExplorePermissionUnionMember0: TypeAlias = Union[
    AgentExplorePermissionUnionMember0Typed,
    Dict[str, Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]],
]

AgentExplorePermission: TypeAlias = Union[AgentExplorePermissionUnionMember0, Literal["ask", "allow", "deny"]]


class AgentExploreTyped(TypedDict, total=False):
    color: str
    """Hex color code for the agent (e.g., #FF5733)"""

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

    permission: AgentExplorePermission

    prompt: str

    skills: Optional[SequenceNotStr[str]]
    """List of skill names that can be invoked by this agent"""

    steps: int
    """Maximum number of agentic iterations before forcing text-only response"""

    sub_agents: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="subAgents")]
    """List of sub-agent names that can be invoked by this agent"""

    temperature: float

    tools: Dict[str, bool]
    """@deprecated Use 'permission' field instead"""

    top_p: float


AgentExplore: TypeAlias = Union[AgentExploreTyped, Dict[str, object]]


class AgentGeneralPermissionUnionMember0Typed(TypedDict, total=False):
    _original_keys: Annotated[SequenceNotStr[str], PropertyInfo(alias="__originalKeys")]

    bash: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]

    codesearch: Literal["ask", "allow", "deny"]

    doom_loop: Literal["ask", "allow", "deny"]

    edit: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]

    external_directory: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]

    glob: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]

    grep: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]

    list: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]

    lsp: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]

    question: Literal["ask", "allow", "deny"]

    read: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]

    task: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]

    todoread: Literal["ask", "allow", "deny"]

    todowrite: Literal["ask", "allow", "deny"]

    webfetch: Literal["ask", "allow", "deny"]

    websearch: Literal["ask", "allow", "deny"]


AgentGeneralPermissionUnionMember0: TypeAlias = Union[
    AgentGeneralPermissionUnionMember0Typed,
    Dict[str, Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]],
]

AgentGeneralPermission: TypeAlias = Union[AgentGeneralPermissionUnionMember0, Literal["ask", "allow", "deny"]]


class AgentGeneralTyped(TypedDict, total=False):
    color: str
    """Hex color code for the agent (e.g., #FF5733)"""

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

    permission: AgentGeneralPermission

    prompt: str

    skills: Optional[SequenceNotStr[str]]
    """List of skill names that can be invoked by this agent"""

    steps: int
    """Maximum number of agentic iterations before forcing text-only response"""

    sub_agents: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="subAgents")]
    """List of sub-agent names that can be invoked by this agent"""

    temperature: float

    tools: Dict[str, bool]
    """@deprecated Use 'permission' field instead"""

    top_p: float


AgentGeneral: TypeAlias = Union[AgentGeneralTyped, Dict[str, object]]


class AgentPlanPermissionUnionMember0Typed(TypedDict, total=False):
    _original_keys: Annotated[SequenceNotStr[str], PropertyInfo(alias="__originalKeys")]

    bash: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]

    codesearch: Literal["ask", "allow", "deny"]

    doom_loop: Literal["ask", "allow", "deny"]

    edit: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]

    external_directory: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]

    glob: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]

    grep: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]

    list: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]

    lsp: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]

    question: Literal["ask", "allow", "deny"]

    read: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]

    task: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]

    todoread: Literal["ask", "allow", "deny"]

    todowrite: Literal["ask", "allow", "deny"]

    webfetch: Literal["ask", "allow", "deny"]

    websearch: Literal["ask", "allow", "deny"]


AgentPlanPermissionUnionMember0: TypeAlias = Union[
    AgentPlanPermissionUnionMember0Typed,
    Dict[str, Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]],
]

AgentPlanPermission: TypeAlias = Union[AgentPlanPermissionUnionMember0, Literal["ask", "allow", "deny"]]


class AgentPlanTyped(TypedDict, total=False):
    color: str
    """Hex color code for the agent (e.g., #FF5733)"""

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

    permission: AgentPlanPermission

    prompt: str

    skills: Optional[SequenceNotStr[str]]
    """List of skill names that can be invoked by this agent"""

    steps: int
    """Maximum number of agentic iterations before forcing text-only response"""

    sub_agents: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="subAgents")]
    """List of sub-agent names that can be invoked by this agent"""

    temperature: float

    tools: Dict[str, bool]
    """@deprecated Use 'permission' field instead"""

    top_p: float


AgentPlan: TypeAlias = Union[AgentPlanTyped, Dict[str, object]]


class AgentSummaryPermissionUnionMember0Typed(TypedDict, total=False):
    _original_keys: Annotated[SequenceNotStr[str], PropertyInfo(alias="__originalKeys")]

    bash: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]

    codesearch: Literal["ask", "allow", "deny"]

    doom_loop: Literal["ask", "allow", "deny"]

    edit: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]

    external_directory: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]

    glob: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]

    grep: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]

    list: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]

    lsp: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]

    question: Literal["ask", "allow", "deny"]

    read: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]

    task: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]

    todoread: Literal["ask", "allow", "deny"]

    todowrite: Literal["ask", "allow", "deny"]

    webfetch: Literal["ask", "allow", "deny"]

    websearch: Literal["ask", "allow", "deny"]


AgentSummaryPermissionUnionMember0: TypeAlias = Union[
    AgentSummaryPermissionUnionMember0Typed,
    Dict[str, Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]],
]

AgentSummaryPermission: TypeAlias = Union[AgentSummaryPermissionUnionMember0, Literal["ask", "allow", "deny"]]


class AgentSummaryTyped(TypedDict, total=False):
    color: str
    """Hex color code for the agent (e.g., #FF5733)"""

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

    permission: AgentSummaryPermission

    prompt: str

    skills: Optional[SequenceNotStr[str]]
    """List of skill names that can be invoked by this agent"""

    steps: int
    """Maximum number of agentic iterations before forcing text-only response"""

    sub_agents: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="subAgents")]
    """List of sub-agent names that can be invoked by this agent"""

    temperature: float

    tools: Dict[str, bool]
    """@deprecated Use 'permission' field instead"""

    top_p: float


AgentSummary: TypeAlias = Union[AgentSummaryTyped, Dict[str, object]]


class AgentTitlePermissionUnionMember0Typed(TypedDict, total=False):
    _original_keys: Annotated[SequenceNotStr[str], PropertyInfo(alias="__originalKeys")]

    bash: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]

    codesearch: Literal["ask", "allow", "deny"]

    doom_loop: Literal["ask", "allow", "deny"]

    edit: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]

    external_directory: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]

    glob: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]

    grep: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]

    list: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]

    lsp: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]

    question: Literal["ask", "allow", "deny"]

    read: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]

    task: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]

    todoread: Literal["ask", "allow", "deny"]

    todowrite: Literal["ask", "allow", "deny"]

    webfetch: Literal["ask", "allow", "deny"]

    websearch: Literal["ask", "allow", "deny"]


AgentTitlePermissionUnionMember0: TypeAlias = Union[
    AgentTitlePermissionUnionMember0Typed,
    Dict[str, Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]],
]

AgentTitlePermission: TypeAlias = Union[AgentTitlePermissionUnionMember0, Literal["ask", "allow", "deny"]]


class AgentTitleTyped(TypedDict, total=False):
    color: str
    """Hex color code for the agent (e.g., #FF5733)"""

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

    permission: AgentTitlePermission

    prompt: str

    skills: Optional[SequenceNotStr[str]]
    """List of skill names that can be invoked by this agent"""

    steps: int
    """Maximum number of agentic iterations before forcing text-only response"""

    sub_agents: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="subAgents")]
    """List of sub-agent names that can be invoked by this agent"""

    temperature: float

    tools: Dict[str, bool]
    """@deprecated Use 'permission' field instead"""

    top_p: float


AgentTitle: TypeAlias = Union[AgentTitleTyped, Dict[str, object]]


class AgentAgentItemPermissionUnionMember0Typed(TypedDict, total=False):
    _original_keys: Annotated[SequenceNotStr[str], PropertyInfo(alias="__originalKeys")]

    bash: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]

    codesearch: Literal["ask", "allow", "deny"]

    doom_loop: Literal["ask", "allow", "deny"]

    edit: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]

    external_directory: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]

    glob: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]

    grep: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]

    list: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]

    lsp: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]

    question: Literal["ask", "allow", "deny"]

    read: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]

    task: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]

    todoread: Literal["ask", "allow", "deny"]

    todowrite: Literal["ask", "allow", "deny"]

    webfetch: Literal["ask", "allow", "deny"]

    websearch: Literal["ask", "allow", "deny"]


AgentAgentItemPermissionUnionMember0: TypeAlias = Union[
    AgentAgentItemPermissionUnionMember0Typed,
    Dict[str, Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]],
]

AgentAgentItemPermission: TypeAlias = Union[AgentAgentItemPermissionUnionMember0, Literal["ask", "allow", "deny"]]


class AgentAgentItemTyped(TypedDict, total=False):
    color: str
    """Hex color code for the agent (e.g., #FF5733)"""

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

    permission: AgentAgentItemPermission

    prompt: str

    skills: Optional[SequenceNotStr[str]]
    """List of skill names that can be invoked by this agent"""

    steps: int
    """Maximum number of agentic iterations before forcing text-only response"""

    sub_agents: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="subAgents")]
    """List of sub-agent names that can be invoked by this agent"""

    temperature: float

    tools: Dict[str, bool]
    """@deprecated Use 'permission' field instead"""

    top_p: float


AgentAgentItem: TypeAlias = Union[AgentAgentItemTyped, Dict[str, object]]


class AgentTyped(TypedDict, total=False):
    """Agent configuration, see https://opencode.ai/docs/agent"""

    build: AgentBuild

    compaction: AgentCompaction

    explore: AgentExplore

    general: AgentGeneral

    plan: AgentPlan

    summary: AgentSummary

    title: AgentTitle


Agent: TypeAlias = Union[AgentTyped, Dict[str, AgentAgentItem]]


class Command(TypedDict, total=False):
    template: Required[str]

    agent: str

    description: str

    model: str

    subtask: bool


class Compaction(TypedDict, total=False):
    auto: bool
    """Enable automatic compaction when context is full (default: true)"""

    prune: bool
    """Enable pruning of old tool outputs (default: true)"""


class Enterprise(TypedDict, total=False):
    url: str
    """Enterprise URL"""


class ExperimentalHookFileEdited(TypedDict, total=False):
    command: Required[SequenceNotStr[str]]

    environment: Dict[str, str]


class ExperimentalHookSessionCompleted(TypedDict, total=False):
    command: Required[SequenceNotStr[str]]

    environment: Dict[str, str]


class ExperimentalHook(TypedDict, total=False):
    file_edited: Dict[str, Iterable[ExperimentalHookFileEdited]]

    session_completed: Iterable[ExperimentalHookSessionCompleted]


class Experimental(TypedDict, total=False):
    batch_tool: bool
    """Enable the batch tool"""

    chat_max_retries: Annotated[float, PropertyInfo(alias="chatMaxRetries")]
    """Number of retries for chat completions on failure"""

    continue_loop_on_deny: bool
    """Continue the agent loop when a tool call is denied"""

    disable_paste_summary: bool

    hook: ExperimentalHook

    mcp_timeout: int
    """Timeout in milliseconds for model context protocol (MCP) requests"""

    open_telemetry: Annotated[bool, PropertyInfo(alias="openTelemetry")]
    """
    Enable OpenTelemetry spans for AI SDK calls (using the 'experimental_telemetry'
    flag)
    """

    primary_tools: SequenceNotStr[str]
    """Tools that should only be available to primary agents."""


class FormatterUnionMember1FormatterUnionMember1Item(TypedDict, total=False):
    command: SequenceNotStr[str]

    disabled: bool

    environment: Dict[str, str]

    extensions: SequenceNotStr[str]


class Keybinds(TypedDict, total=False):
    """Custom keybind configurations"""

    agent_cycle: str
    """Next agent"""

    agent_cycle_reverse: str
    """Previous agent"""

    agent_list: str
    """List agents"""

    app_exit: str
    """Exit the application"""

    artifacts_list: str
    """View artifacts"""

    command_list: str
    """List available commands"""

    editor_open: str
    """Open external editor"""

    history_next: str
    """Next history item"""

    history_previous: str
    """Previous history item"""

    input_backspace: str
    """Backspace in input"""

    input_buffer_end: str
    """Move to end of buffer in input"""

    input_buffer_home: str
    """Move to start of buffer in input"""

    input_clear: str
    """Clear input field"""

    input_delete: str
    """Delete character in input"""

    input_delete_line: str
    """Delete line in input"""

    input_delete_to_line_end: str
    """Delete to end of line in input"""

    input_delete_to_line_start: str
    """Delete to start of line in input"""

    input_delete_word_backward: str
    """Delete word backward in input"""

    input_delete_word_forward: str
    """Delete word forward in input"""

    input_line_end: str
    """Move to end of line in input"""

    input_line_home: str
    """Move to start of line in input"""

    input_move_down: str
    """Move cursor down in input"""

    input_move_left: str
    """Move cursor left in input"""

    input_move_right: str
    """Move cursor right in input"""

    input_move_up: str
    """Move cursor up in input"""

    input_newline: str
    """Insert newline in input"""

    input_paste: str
    """Paste from clipboard"""

    input_redo: str
    """Redo in input"""

    input_select_buffer_end: str
    """Select to end of buffer in input"""

    input_select_buffer_home: str
    """Select to start of buffer in input"""

    input_select_down: str
    """Select down in input"""

    input_select_left: str
    """Select left in input"""

    input_select_line_end: str
    """Select to end of line in input"""

    input_select_line_home: str
    """Select to start of line in input"""

    input_select_right: str
    """Select right in input"""

    input_select_up: str
    """Select up in input"""

    input_select_visual_line_end: str
    """Select to end of visual line in input"""

    input_select_visual_line_home: str
    """Select to start of visual line in input"""

    input_select_word_backward: str
    """Select word backward in input"""

    input_select_word_forward: str
    """Select word forward in input"""

    input_submit: str
    """Submit input"""

    input_undo: str
    """Undo in input"""

    input_visual_line_end: str
    """Move to end of visual line in input"""

    input_visual_line_home: str
    """Move to start of visual line in input"""

    input_word_backward: str
    """Move word backward in input"""

    input_word_forward: str
    """Move word forward in input"""

    leader: str
    """Leader key for keybind combinations"""

    messages_copy: str
    """Copy message"""

    messages_first: str
    """Navigate to first message"""

    messages_half_page_down: str
    """Scroll messages down by half page"""

    messages_half_page_up: str
    """Scroll messages up by half page"""

    messages_last: str
    """Navigate to last message"""

    messages_last_user: str
    """Navigate to last user message"""

    messages_next: str
    """Navigate to next message"""

    messages_page_down: str
    """Scroll messages down by one page"""

    messages_page_up: str
    """Scroll messages up by one page"""

    messages_previous: str
    """Navigate to previous message"""

    messages_redo: str
    """Redo message"""

    messages_toggle_conceal: str
    """Toggle code block concealment in messages"""

    messages_undo: str
    """Undo message"""

    model_cycle_favorite: str
    """Next favorite model"""

    model_cycle_favorite_reverse: str
    """Previous favorite model"""

    model_cycle_recent: str
    """Next recently used model"""

    model_cycle_recent_reverse: str
    """Previous recently used model"""

    model_list: str
    """List available models"""

    scrollbar_toggle: str
    """Toggle session scrollbar"""

    session_child_cycle: str
    """Next child session"""

    session_child_cycle_reverse: str
    """Previous child session"""

    session_compact: str
    """Compact the session"""

    session_export: str
    """Export session to editor"""

    session_fork: str
    """Fork session from message"""

    session_interrupt: str
    """Interrupt current session"""

    session_list: str
    """List all sessions"""

    session_new: str
    """Create a new session"""

    session_parent: str
    """Go to parent session"""

    session_rename: str
    """Rename session"""

    session_share: str
    """Share current session"""

    session_timeline: str
    """Show session timeline"""

    session_unshare: str
    """Unshare current session"""

    sidebar_toggle: str
    """Toggle sidebar"""

    status_view: str
    """View status"""

    terminal_suspend: str
    """Suspend terminal"""

    terminal_title_toggle: str
    """Toggle terminal title"""

    theme_list: str
    """List available themes"""

    tips_toggle: str
    """Toggle tips on home screen"""

    tool_details: str
    """Toggle tool details visibility"""

    username_toggle: str
    """Toggle username visibility"""

    variant_cycle: str
    """Cycle model variants"""


class LspUnionMember1LspUnionMember1ItemDisabled(TypedDict, total=False):
    disabled: Required[Literal[True]]


class LspUnionMember1LspUnionMember1ItemUnionMember1(TypedDict, total=False):
    command: Required[SequenceNotStr[str]]

    disabled: bool

    env: Dict[str, str]

    extensions: SequenceNotStr[str]

    initialization: Dict[str, object]


LspUnionMember1LspUnionMember1Item: TypeAlias = Union[
    LspUnionMember1LspUnionMember1ItemDisabled, LspUnionMember1LspUnionMember1ItemUnionMember1
]


class McpMcpLocalConfig(TypedDict, total=False):
    command: Required[SequenceNotStr[str]]
    """Command and arguments to run the MCP server"""

    type: Required[Literal["local"]]
    """Type of MCP server connection"""

    enabled: bool
    """Enable or disable the MCP server on startup"""

    environment: Dict[str, str]
    """Environment variables to set when running the MCP server"""

    timeout: int
    """Timeout in ms for fetching tools from the MCP server.

    Defaults to 5000 (5 seconds) if not specified.
    """


class McpMcpRemoteConfigOAuthMcpOAuthConfig(TypedDict, total=False):
    client_id: Annotated[str, PropertyInfo(alias="clientId")]
    """OAuth client ID.

    If not provided, dynamic client registration (RFC 7591) will be attempted.
    """

    client_secret: Annotated[str, PropertyInfo(alias="clientSecret")]
    """OAuth client secret (if required by the authorization server)"""

    scope: str
    """OAuth scopes to request during authorization"""


McpMcpRemoteConfigOAuth: TypeAlias = Union[McpMcpRemoteConfigOAuthMcpOAuthConfig, Literal[False]]


class McpMcpRemoteConfig(TypedDict, total=False):
    type: Required[Literal["remote"]]
    """Type of MCP server connection"""

    url: Required[str]
    """URL of the remote MCP server"""

    enabled: bool
    """Enable or disable the MCP server on startup"""

    headers: Dict[str, str]
    """Headers to send with the request"""

    oauth: McpMcpRemoteConfigOAuth
    """OAuth authentication configuration for the MCP server.

    Set to false to disable OAuth auto-detection.
    """

    timeout: int
    """Timeout in ms for fetching tools from the MCP server.

    Defaults to 5000 (5 seconds) if not specified.
    """


class McpEnabled(TypedDict, total=False):
    enabled: Required[bool]


Mcp: TypeAlias = Union[McpMcpLocalConfig, McpMcpRemoteConfig, McpEnabled]


class ModeBuildPermissionUnionMember0Typed(TypedDict, total=False):
    _original_keys: Annotated[SequenceNotStr[str], PropertyInfo(alias="__originalKeys")]

    bash: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]

    codesearch: Literal["ask", "allow", "deny"]

    doom_loop: Literal["ask", "allow", "deny"]

    edit: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]

    external_directory: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]

    glob: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]

    grep: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]

    list: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]

    lsp: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]

    question: Literal["ask", "allow", "deny"]

    read: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]

    task: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]

    todoread: Literal["ask", "allow", "deny"]

    todowrite: Literal["ask", "allow", "deny"]

    webfetch: Literal["ask", "allow", "deny"]

    websearch: Literal["ask", "allow", "deny"]


ModeBuildPermissionUnionMember0: TypeAlias = Union[
    ModeBuildPermissionUnionMember0Typed,
    Dict[str, Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]],
]

ModeBuildPermission: TypeAlias = Union[ModeBuildPermissionUnionMember0, Literal["ask", "allow", "deny"]]


class ModeBuildTyped(TypedDict, total=False):
    color: str
    """Hex color code for the agent (e.g., #FF5733)"""

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

    permission: ModeBuildPermission

    prompt: str

    skills: Optional[SequenceNotStr[str]]
    """List of skill names that can be invoked by this agent"""

    steps: int
    """Maximum number of agentic iterations before forcing text-only response"""

    sub_agents: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="subAgents")]
    """List of sub-agent names that can be invoked by this agent"""

    temperature: float

    tools: Dict[str, bool]
    """@deprecated Use 'permission' field instead"""

    top_p: float


ModeBuild: TypeAlias = Union[ModeBuildTyped, Dict[str, object]]


class ModePlanPermissionUnionMember0Typed(TypedDict, total=False):
    _original_keys: Annotated[SequenceNotStr[str], PropertyInfo(alias="__originalKeys")]

    bash: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]

    codesearch: Literal["ask", "allow", "deny"]

    doom_loop: Literal["ask", "allow", "deny"]

    edit: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]

    external_directory: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]

    glob: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]

    grep: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]

    list: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]

    lsp: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]

    question: Literal["ask", "allow", "deny"]

    read: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]

    task: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]

    todoread: Literal["ask", "allow", "deny"]

    todowrite: Literal["ask", "allow", "deny"]

    webfetch: Literal["ask", "allow", "deny"]

    websearch: Literal["ask", "allow", "deny"]


ModePlanPermissionUnionMember0: TypeAlias = Union[
    ModePlanPermissionUnionMember0Typed,
    Dict[str, Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]],
]

ModePlanPermission: TypeAlias = Union[ModePlanPermissionUnionMember0, Literal["ask", "allow", "deny"]]


class ModePlanTyped(TypedDict, total=False):
    color: str
    """Hex color code for the agent (e.g., #FF5733)"""

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

    permission: ModePlanPermission

    prompt: str

    skills: Optional[SequenceNotStr[str]]
    """List of skill names that can be invoked by this agent"""

    steps: int
    """Maximum number of agentic iterations before forcing text-only response"""

    sub_agents: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="subAgents")]
    """List of sub-agent names that can be invoked by this agent"""

    temperature: float

    tools: Dict[str, bool]
    """@deprecated Use 'permission' field instead"""

    top_p: float


ModePlan: TypeAlias = Union[ModePlanTyped, Dict[str, object]]


class ModeModeItemPermissionUnionMember0Typed(TypedDict, total=False):
    _original_keys: Annotated[SequenceNotStr[str], PropertyInfo(alias="__originalKeys")]

    bash: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]

    codesearch: Literal["ask", "allow", "deny"]

    doom_loop: Literal["ask", "allow", "deny"]

    edit: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]

    external_directory: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]

    glob: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]

    grep: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]

    list: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]

    lsp: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]

    question: Literal["ask", "allow", "deny"]

    read: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]

    task: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]

    todoread: Literal["ask", "allow", "deny"]

    todowrite: Literal["ask", "allow", "deny"]

    webfetch: Literal["ask", "allow", "deny"]

    websearch: Literal["ask", "allow", "deny"]


ModeModeItemPermissionUnionMember0: TypeAlias = Union[
    ModeModeItemPermissionUnionMember0Typed,
    Dict[str, Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]],
]

ModeModeItemPermission: TypeAlias = Union[ModeModeItemPermissionUnionMember0, Literal["ask", "allow", "deny"]]


class ModeModeItemTyped(TypedDict, total=False):
    color: str
    """Hex color code for the agent (e.g., #FF5733)"""

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

    permission: ModeModeItemPermission

    prompt: str

    skills: Optional[SequenceNotStr[str]]
    """List of skill names that can be invoked by this agent"""

    steps: int
    """Maximum number of agentic iterations before forcing text-only response"""

    sub_agents: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="subAgents")]
    """List of sub-agent names that can be invoked by this agent"""

    temperature: float

    tools: Dict[str, bool]
    """@deprecated Use 'permission' field instead"""

    top_p: float


ModeModeItem: TypeAlias = Union[ModeModeItemTyped, Dict[str, object]]


class ModeTyped(TypedDict, total=False):
    """@deprecated Use `agent` field instead."""

    build: ModeBuild

    plan: ModePlan


Mode: TypeAlias = Union[ModeTyped, Dict[str, ModeModeItem]]


class PermissionUnionMember0Typed(TypedDict, total=False):
    _original_keys: Annotated[SequenceNotStr[str], PropertyInfo(alias="__originalKeys")]

    bash: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]

    codesearch: Literal["ask", "allow", "deny"]

    doom_loop: Literal["ask", "allow", "deny"]

    edit: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]

    external_directory: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]

    glob: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]

    grep: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]

    list: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]

    lsp: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]

    question: Literal["ask", "allow", "deny"]

    read: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]

    task: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]

    todoread: Literal["ask", "allow", "deny"]

    todowrite: Literal["ask", "allow", "deny"]

    webfetch: Literal["ask", "allow", "deny"]

    websearch: Literal["ask", "allow", "deny"]


PermissionUnionMember0: TypeAlias = Union[
    PermissionUnionMember0Typed,
    Dict[str, Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]],
]

Permission: TypeAlias = Union[PermissionUnionMember0, Literal["ask", "allow", "deny"]]


class ProviderModelsCostContextOver200k(TypedDict, total=False):
    input: Required[float]

    output: Required[float]

    cache_read: float

    cache_write: float


class ProviderModelsCost(TypedDict, total=False):
    input: Required[float]

    output: Required[float]

    cache_read: float

    cache_write: float

    context_over_200k: ProviderModelsCostContextOver200k


class ProviderModelsInterleavedField(TypedDict, total=False):
    field: Required[Literal["reasoning_content", "reasoning_details"]]


ProviderModelsInterleaved: TypeAlias = Union[Literal[True], ProviderModelsInterleavedField]


class ProviderModelsLimit(TypedDict, total=False):
    context: Required[float]

    output: Required[float]


class ProviderModelsModalities(TypedDict, total=False):
    input: Required[List[Literal["text", "audio", "image", "video", "pdf"]]]

    output: Required[List[Literal["text", "audio", "image", "video", "pdf"]]]


class ProviderModelsProvider(TypedDict, total=False):
    npm: Required[str]


class ProviderModelsVariantsTyped(TypedDict, total=False):
    disabled: bool
    """Disable this variant for the model"""


ProviderModelsVariants: TypeAlias = Union[ProviderModelsVariantsTyped, Dict[str, object]]


class ProviderModels(TypedDict, total=False):
    id: str

    attachment: bool

    cost: ProviderModelsCost

    experimental: bool

    family: str

    headers: Dict[str, str]

    interleaved: ProviderModelsInterleaved

    limit: ProviderModelsLimit

    modalities: ProviderModelsModalities

    name: str

    options: Dict[str, object]

    provider: ProviderModelsProvider

    reasoning: bool

    release_date: str

    status: Literal["alpha", "beta", "deprecated"]

    temperature: bool

    tool_call: bool

    variants: Dict[str, ProviderModelsVariants]
    """Variant-specific configuration"""


class ProviderOptionsTyped(TypedDict, total=False):
    api_key: Annotated[str, PropertyInfo(alias="apiKey")]

    base_url: Annotated[str, PropertyInfo(alias="baseURL")]

    enterprise_url: Annotated[str, PropertyInfo(alias="enterpriseUrl")]
    """GitHub Enterprise URL for copilot authentication"""

    set_cache_key: Annotated[bool, PropertyInfo(alias="setCacheKey")]
    """Enable promptCacheKey for this provider (default false)"""

    timeout: Union[int, Literal[False]]
    """Timeout in milliseconds for requests to this provider.

    Default is 300000 (5 minutes). Set to false to disable timeout.
    """


ProviderOptions: TypeAlias = Union[ProviderOptionsTyped, Dict[str, object]]


class Provider(TypedDict, total=False):
    id: str

    api: str

    blacklist: SequenceNotStr[str]

    env: SequenceNotStr[str]

    models: Dict[str, ProviderModels]

    name: str

    npm: str

    options: ProviderOptions

    whitelist: SequenceNotStr[str]


class Server(TypedDict, total=False):
    """Server configuration for opencode serve and web commands"""

    cors: SequenceNotStr[str]
    """Additional domains to allow for CORS"""

    hostname: str
    """Hostname to listen on"""

    mdns: bool
    """Enable mDNS service discovery"""

    port: int
    """Port to listen on"""


class TuiScrollAcceleration(TypedDict, total=False):
    """Scroll acceleration settings"""

    enabled: Required[bool]
    """Enable scroll acceleration"""


class Tui(TypedDict, total=False):
    """TUI specific settings"""

    diff_style: Literal["auto", "stacked"]
    """
    Control diff rendering style: 'auto' adapts to terminal width, 'stacked' always
    shows single column
    """

    scroll_acceleration: TuiScrollAcceleration
    """Scroll acceleration settings"""

    scroll_speed: float
    """TUI scroll speed"""


class Watcher(TypedDict, total=False):
    ignore: SequenceNotStr[str]
