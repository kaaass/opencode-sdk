# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo
from .global_.permission_config_param import PermissionConfigParam

__all__ = [
    "ConfigUpdateParams",
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


class ConfigUpdateParams(TypedDict, total=False):
    directory: str

    workspace: str

    schema: Annotated[str, PropertyInfo(alias="$schema")]
    """JSON schema reference for configuration validation"""

    agent: Agent
    """Agent configuration, see https://opencode.ai/docs/agents"""

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

    permission: PermissionConfigParam

    plugin: SequenceNotStr[Union[str, Iterable[object]]]

    provider: Dict[str, Provider]
    """Custom provider configurations and model overrides"""

    server: Server
    """Server configuration for opencode serve and web commands"""

    share: Literal["manual", "auto", "disabled"]
    """
    Control sharing behavior:'manual' allows manual sharing via commands, 'auto'
    enables automatic sharing, 'disabled' disables all sharing
    """

    skills: Skills
    """Additional skill folder paths"""

    small_model: str
    """
    Small model to use for tasks like title generation in the format of
    provider/model
    """

    snapshot: bool
    """Enable or disable snapshot tracking.

    When false, filesystem snapshots are not recorded and undoing or reverting will
    not undo/redo file changes. Defaults to true.
    """

    tools: Dict[str, bool]

    username: str
    """Custom username to display in conversations instead of system username"""

    watcher: Watcher


class AgentBuild(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
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
    """List of skill names that can be invoked by this agent"""

    steps: int
    """Maximum number of agentic iterations before forcing text-only response"""

    sub_agents: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="subAgents")]
    """List of sub-agent names that can be invoked by this agent"""

    temperature: float

    tools: Dict[str, bool]
    """@deprecated Use 'permission' field instead"""

    top_p: float

    variant: str
    """
    Default model variant for this agent (applies only when using the agent's
    configured model).
    """


class AgentCompaction(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
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
    """List of skill names that can be invoked by this agent"""

    steps: int
    """Maximum number of agentic iterations before forcing text-only response"""

    sub_agents: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="subAgents")]
    """List of sub-agent names that can be invoked by this agent"""

    temperature: float

    tools: Dict[str, bool]
    """@deprecated Use 'permission' field instead"""

    top_p: float

    variant: str
    """
    Default model variant for this agent (applies only when using the agent's
    configured model).
    """


class AgentExplore(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
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
    """List of skill names that can be invoked by this agent"""

    steps: int
    """Maximum number of agentic iterations before forcing text-only response"""

    sub_agents: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="subAgents")]
    """List of sub-agent names that can be invoked by this agent"""

    temperature: float

    tools: Dict[str, bool]
    """@deprecated Use 'permission' field instead"""

    top_p: float

    variant: str
    """
    Default model variant for this agent (applies only when using the agent's
    configured model).
    """


class AgentGeneral(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
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
    """List of skill names that can be invoked by this agent"""

    steps: int
    """Maximum number of agentic iterations before forcing text-only response"""

    sub_agents: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="subAgents")]
    """List of sub-agent names that can be invoked by this agent"""

    temperature: float

    tools: Dict[str, bool]
    """@deprecated Use 'permission' field instead"""

    top_p: float

    variant: str
    """
    Default model variant for this agent (applies only when using the agent's
    configured model).
    """


class AgentPlan(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
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
    """List of skill names that can be invoked by this agent"""

    steps: int
    """Maximum number of agentic iterations before forcing text-only response"""

    sub_agents: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="subAgents")]
    """List of sub-agent names that can be invoked by this agent"""

    temperature: float

    tools: Dict[str, bool]
    """@deprecated Use 'permission' field instead"""

    top_p: float

    variant: str
    """
    Default model variant for this agent (applies only when using the agent's
    configured model).
    """


class AgentSummary(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
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
    """List of skill names that can be invoked by this agent"""

    steps: int
    """Maximum number of agentic iterations before forcing text-only response"""

    sub_agents: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="subAgents")]
    """List of sub-agent names that can be invoked by this agent"""

    temperature: float

    tools: Dict[str, bool]
    """@deprecated Use 'permission' field instead"""

    top_p: float

    variant: str
    """
    Default model variant for this agent (applies only when using the agent's
    configured model).
    """


class AgentTitle(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
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
    """List of skill names that can be invoked by this agent"""

    steps: int
    """Maximum number of agentic iterations before forcing text-only response"""

    sub_agents: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="subAgents")]
    """List of sub-agent names that can be invoked by this agent"""

    temperature: float

    tools: Dict[str, bool]
    """@deprecated Use 'permission' field instead"""

    top_p: float

    variant: str
    """
    Default model variant for this agent (applies only when using the agent's
    configured model).
    """


class AgentAgentItem(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
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
    """List of skill names that can be invoked by this agent"""

    steps: int
    """Maximum number of agentic iterations before forcing text-only response"""

    sub_agents: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="subAgents")]
    """List of sub-agent names that can be invoked by this agent"""

    temperature: float

    tools: Dict[str, bool]
    """@deprecated Use 'permission' field instead"""

    top_p: float

    variant: str
    """
    Default model variant for this agent (applies only when using the agent's
    configured model).
    """


class Agent(TypedDict, total=False, extra_items=AgentAgentItem):  # type: ignore[call-arg]
    """Agent configuration, see https://opencode.ai/docs/agents"""

    build: AgentBuild

    compaction: AgentCompaction

    explore: AgentExplore

    general: AgentGeneral

    plan: AgentPlan

    summary: AgentSummary

    title: AgentTitle


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

    reserved: int
    """Token buffer for compaction.

    Leaves enough window to avoid overflow during compaction.
    """


class Enterprise(TypedDict, total=False):
    url: str
    """Enterprise URL"""


class Experimental(TypedDict, total=False):
    batch_tool: bool
    """Enable the batch tool"""

    continue_loop_on_deny: bool
    """Continue the agent loop when a tool call is denied"""

    disable_paste_summary: bool

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
    """Timeout in ms for MCP server requests.

    Defaults to 5000 (5 seconds) if not specified.
    """


class McpMcpRemoteConfigOAuthMcpOAuthConfig(TypedDict, total=False):
    client_id: Annotated[str, PropertyInfo(alias="clientId")]
    """OAuth client ID.

    If not provided, dynamic client registration (RFC 7591) will be attempted.
    """

    client_secret: Annotated[str, PropertyInfo(alias="clientSecret")]
    """OAuth client secret (if required by the authorization server)"""

    redirect_uri: Annotated[str, PropertyInfo(alias="redirectUri")]
    """OAuth redirect URI (default: http://127.0.0.1:19876/mcp/oauth/callback)."""

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
    """Timeout in ms for MCP server requests.

    Defaults to 5000 (5 seconds) if not specified.
    """


class McpEnabled(TypedDict, total=False):
    enabled: Required[bool]


Mcp: TypeAlias = Union[McpMcpLocalConfig, McpMcpRemoteConfig, McpEnabled]


class ModeBuild(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
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
    """List of skill names that can be invoked by this agent"""

    steps: int
    """Maximum number of agentic iterations before forcing text-only response"""

    sub_agents: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="subAgents")]
    """List of sub-agent names that can be invoked by this agent"""

    temperature: float

    tools: Dict[str, bool]
    """@deprecated Use 'permission' field instead"""

    top_p: float

    variant: str
    """
    Default model variant for this agent (applies only when using the agent's
    configured model).
    """


class ModePlan(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
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
    """List of skill names that can be invoked by this agent"""

    steps: int
    """Maximum number of agentic iterations before forcing text-only response"""

    sub_agents: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="subAgents")]
    """List of sub-agent names that can be invoked by this agent"""

    temperature: float

    tools: Dict[str, bool]
    """@deprecated Use 'permission' field instead"""

    top_p: float

    variant: str
    """
    Default model variant for this agent (applies only when using the agent's
    configured model).
    """


class ModeModeItem(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
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
    """List of skill names that can be invoked by this agent"""

    steps: int
    """Maximum number of agentic iterations before forcing text-only response"""

    sub_agents: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="subAgents")]
    """List of sub-agent names that can be invoked by this agent"""

    temperature: float

    tools: Dict[str, bool]
    """@deprecated Use 'permission' field instead"""

    top_p: float

    variant: str
    """
    Default model variant for this agent (applies only when using the agent's
    configured model).
    """


class Mode(TypedDict, total=False, extra_items=ModeModeItem):  # type: ignore[call-arg]
    """@deprecated Use `agent` field instead."""

    build: ModeBuild

    plan: ModePlan


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

    input: float


class ProviderModelsModalities(TypedDict, total=False):
    input: Required[List[Literal["text", "audio", "image", "video", "pdf"]]]

    output: Required[List[Literal["text", "audio", "image", "video", "pdf"]]]


class ProviderModelsProvider(TypedDict, total=False):
    api: str

    npm: str


class ProviderModelsVariants(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    disabled: bool
    """Disable this variant for the model"""


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


class ProviderOptions(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    api_key: Annotated[str, PropertyInfo(alias="apiKey")]

    base_url: Annotated[str, PropertyInfo(alias="baseURL")]

    chunk_timeout: Annotated[int, PropertyInfo(alias="chunkTimeout")]
    """Timeout in milliseconds between streamed SSE chunks for this provider.

    If no chunk arrives within this window, the request is aborted.
    """

    enterprise_url: Annotated[str, PropertyInfo(alias="enterpriseUrl")]
    """GitHub Enterprise URL for copilot authentication"""

    set_cache_key: Annotated[bool, PropertyInfo(alias="setCacheKey")]
    """Enable promptCacheKey for this provider (default false)"""

    timeout: Union[int, Literal[False]]
    """Timeout in milliseconds for requests to this provider.

    Default is 300000 (5 minutes). Set to false to disable timeout.
    """


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

    mdns_domain: Annotated[str, PropertyInfo(alias="mdnsDomain")]
    """Custom domain name for mDNS service (default: opencode.local)"""

    port: int
    """Port to listen on"""


class Skills(TypedDict, total=False):
    """Additional skill folder paths"""

    paths: SequenceNotStr[str]
    """Additional paths to skill folders"""

    urls: SequenceNotStr[str]
    """URLs to fetch skills from (e.g., https://example.com/.well-known/skills/)"""


class Watcher(TypedDict, total=False):
    ignore: SequenceNotStr[str]
