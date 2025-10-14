# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = [
    "ConfigUpdateParams",
    "Agent",
    "AgentBuild",
    "AgentBuildPermission",
    "AgentGeneral",
    "AgentGeneralPermission",
    "AgentPlan",
    "AgentPlanPermission",
    "AgentAgentItem",
    "AgentAgentItemPermission",
    "Command",
    "Experimental",
    "ExperimentalHook",
    "ExperimentalHookFileEdited",
    "ExperimentalHookSessionCompleted",
    "Formatter",
    "Keybinds",
    "Lsp",
    "LspDisabled",
    "LspUnionMember1",
    "Mcp",
    "McpMcpLocalConfig",
    "McpMcpRemoteConfig",
    "Mode",
    "ModeBuild",
    "ModeBuildPermission",
    "ModePlan",
    "ModePlanPermission",
    "ModeModeItem",
    "ModeModeItemPermission",
    "Permission",
    "Provider",
    "ProviderModels",
    "ProviderModelsCost",
    "ProviderModelsLimit",
    "ProviderModelsModalities",
    "ProviderModelsProvider",
    "ProviderOptions",
    "Tui",
    "Watcher",
]


class ConfigUpdateParams(TypedDict, total=False):
    directory: str

    schema: Annotated[str, PropertyInfo(alias="$schema")]
    """JSON schema reference for configuration validation"""

    agent: Agent
    """Agent configuration, see https://opencode.ai/docs/agent"""

    autoshare: bool
    """@deprecated Use 'share' field instead.

    Share newly created sessions automatically
    """

    autoupdate: bool
    """Automatically update to the latest version"""

    command: Dict[str, Command]
    """Command configuration, see https://opencode.ai/docs/commands"""

    disabled_providers: SequenceNotStr[str]
    """Disable providers that are loaded automatically"""

    experimental: Experimental

    formatter: Dict[str, Formatter]

    instructions: SequenceNotStr[str]
    """Additional instruction files or patterns to include"""

    keybinds: Keybinds
    """Custom keybind configurations"""

    layout: Literal["auto", "stretch"]
    """@deprecated Always uses stretch layout."""

    lsp: Dict[str, Lsp]

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


class AgentBuildPermission(TypedDict, total=False):
    bash: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]

    edit: Literal["ask", "allow", "deny"]

    webfetch: Literal["ask", "allow", "deny"]


class AgentBuildTyped(TypedDict, total=False):
    description: str
    """Description of when to use the agent"""

    disable: bool

    mode: Literal["subagent", "primary", "all"]

    model: str

    permission: AgentBuildPermission

    prompt: str

    temperature: float

    tools: Dict[str, bool]

    top_p: float


AgentBuild: TypeAlias = Union[AgentBuildTyped, Dict[str, object]]


class AgentGeneralPermission(TypedDict, total=False):
    bash: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]

    edit: Literal["ask", "allow", "deny"]

    webfetch: Literal["ask", "allow", "deny"]


class AgentGeneralTyped(TypedDict, total=False):
    description: str
    """Description of when to use the agent"""

    disable: bool

    mode: Literal["subagent", "primary", "all"]

    model: str

    permission: AgentGeneralPermission

    prompt: str

    temperature: float

    tools: Dict[str, bool]

    top_p: float


AgentGeneral: TypeAlias = Union[AgentGeneralTyped, Dict[str, object]]


class AgentPlanPermission(TypedDict, total=False):
    bash: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]

    edit: Literal["ask", "allow", "deny"]

    webfetch: Literal["ask", "allow", "deny"]


class AgentPlanTyped(TypedDict, total=False):
    description: str
    """Description of when to use the agent"""

    disable: bool

    mode: Literal["subagent", "primary", "all"]

    model: str

    permission: AgentPlanPermission

    prompt: str

    temperature: float

    tools: Dict[str, bool]

    top_p: float


AgentPlan: TypeAlias = Union[AgentPlanTyped, Dict[str, object]]


class AgentAgentItemPermission(TypedDict, total=False):
    bash: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]

    edit: Literal["ask", "allow", "deny"]

    webfetch: Literal["ask", "allow", "deny"]


class AgentAgentItemTyped(TypedDict, total=False):
    description: str
    """Description of when to use the agent"""

    disable: bool

    mode: Literal["subagent", "primary", "all"]

    model: str

    permission: AgentAgentItemPermission

    prompt: str

    temperature: float

    tools: Dict[str, bool]

    top_p: float


AgentAgentItem: TypeAlias = Union[AgentAgentItemTyped, Dict[str, object]]


class AgentTyped(TypedDict, total=False):
    build: AgentBuild

    general: AgentGeneral

    plan: AgentPlan


Agent: TypeAlias = Union[AgentTyped, Dict[str, AgentAgentItem]]


class Command(TypedDict, total=False):
    template: Required[str]

    agent: str

    description: str

    model: str

    subtask: bool


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
    disable_paste_summary: bool

    hook: ExperimentalHook


class Formatter(TypedDict, total=False):
    command: SequenceNotStr[str]

    disabled: bool

    environment: Dict[str, str]

    extensions: SequenceNotStr[str]


class Keybinds(TypedDict, total=False):
    agent_cycle: str
    """Next agent"""

    agent_cycle_reverse: str
    """Previous agent"""

    agent_list: str
    """List agents"""

    app_exit: str
    """Exit the application"""

    app_help: str
    """Show help dialog"""

    editor_open: str
    """Open external editor"""

    file_close: str
    """@deprecated Close file"""

    file_diff_toggle: str
    """@deprecated Split/unified diff"""

    file_list: str
    """@deprecated Currently not available. List files"""

    file_search: str
    """@deprecated Search file"""

    input_clear: str
    """Clear input field"""

    input_newline: str
    """Insert newline in input"""

    input_paste: str
    """Paste from clipboard"""

    input_submit: str
    """Submit input"""

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

    messages_layout_toggle: str
    """@deprecated Toggle layout"""

    messages_next: str
    """@deprecated Navigate to next message"""

    messages_page_down: str
    """Scroll messages down by one page"""

    messages_page_up: str
    """Scroll messages up by one page"""

    messages_previous: str
    """@deprecated Navigate to previous message"""

    messages_redo: str
    """Redo message"""

    messages_revert: str
    """@deprecated use messages_undo. Revert message"""

    messages_undo: str
    """Undo message"""

    model_cycle_recent: str
    """Next recent model"""

    model_cycle_recent_reverse: str
    """Previous recent model"""

    model_list: str
    """List available models"""

    project_init: str
    """Create/update AGENTS.md"""

    session_child_cycle: str
    """Cycle to next child session"""

    session_child_cycle_reverse: str
    """Cycle to previous child session"""

    session_compact: str
    """Compact the session"""

    session_export: str
    """Export session to editor"""

    session_interrupt: str
    """Interrupt current session"""

    session_list: str
    """List all sessions"""

    session_new: str
    """Create a new session"""

    session_share: str
    """Share current session"""

    session_timeline: str
    """Show session timeline"""

    session_unshare: str
    """Unshare current session"""

    switch_agent: str
    """@deprecated use agent_cycle. Next agent"""

    switch_agent_reverse: str
    """@deprecated use agent_cycle_reverse. Previous agent"""

    switch_mode: str
    """@deprecated use agent_cycle. Next mode"""

    switch_mode_reverse: str
    """@deprecated use agent_cycle_reverse. Previous mode"""

    theme_list: str
    """List available themes"""

    thinking_blocks: str
    """Toggle thinking blocks"""

    tool_details: str
    """Toggle tool details"""


class LspDisabled(TypedDict, total=False):
    disabled: Required[Literal[True]]


class LspUnionMember1(TypedDict, total=False):
    command: Required[SequenceNotStr[str]]

    disabled: bool

    env: Dict[str, str]

    extensions: SequenceNotStr[str]

    initialization: Dict[str, object]


Lsp: TypeAlias = Union[LspDisabled, LspUnionMember1]


class McpMcpLocalConfig(TypedDict, total=False):
    command: Required[SequenceNotStr[str]]
    """Command and arguments to run the MCP server"""

    type: Required[Literal["local"]]
    """Type of MCP server connection"""

    enabled: bool
    """Enable or disable the MCP server on startup"""

    environment: Dict[str, str]
    """Environment variables to set when running the MCP server"""


class McpMcpRemoteConfig(TypedDict, total=False):
    type: Required[Literal["remote"]]
    """Type of MCP server connection"""

    url: Required[str]
    """URL of the remote MCP server"""

    enabled: bool
    """Enable or disable the MCP server on startup"""

    headers: Dict[str, str]
    """Headers to send with the request"""


Mcp: TypeAlias = Union[McpMcpLocalConfig, McpMcpRemoteConfig]


class ModeBuildPermission(TypedDict, total=False):
    bash: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]

    edit: Literal["ask", "allow", "deny"]

    webfetch: Literal["ask", "allow", "deny"]


class ModeBuildTyped(TypedDict, total=False):
    description: str
    """Description of when to use the agent"""

    disable: bool

    mode: Literal["subagent", "primary", "all"]

    model: str

    permission: ModeBuildPermission

    prompt: str

    temperature: float

    tools: Dict[str, bool]

    top_p: float


ModeBuild: TypeAlias = Union[ModeBuildTyped, Dict[str, object]]


class ModePlanPermission(TypedDict, total=False):
    bash: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]

    edit: Literal["ask", "allow", "deny"]

    webfetch: Literal["ask", "allow", "deny"]


class ModePlanTyped(TypedDict, total=False):
    description: str
    """Description of when to use the agent"""

    disable: bool

    mode: Literal["subagent", "primary", "all"]

    model: str

    permission: ModePlanPermission

    prompt: str

    temperature: float

    tools: Dict[str, bool]

    top_p: float


ModePlan: TypeAlias = Union[ModePlanTyped, Dict[str, object]]


class ModeModeItemPermission(TypedDict, total=False):
    bash: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]

    edit: Literal["ask", "allow", "deny"]

    webfetch: Literal["ask", "allow", "deny"]


class ModeModeItemTyped(TypedDict, total=False):
    description: str
    """Description of when to use the agent"""

    disable: bool

    mode: Literal["subagent", "primary", "all"]

    model: str

    permission: ModeModeItemPermission

    prompt: str

    temperature: float

    tools: Dict[str, bool]

    top_p: float


ModeModeItem: TypeAlias = Union[ModeModeItemTyped, Dict[str, object]]


class ModeTyped(TypedDict, total=False):
    build: ModeBuild

    plan: ModePlan


Mode: TypeAlias = Union[ModeTyped, Dict[str, ModeModeItem]]


class Permission(TypedDict, total=False):
    bash: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]]]

    edit: Literal["ask", "allow", "deny"]

    webfetch: Literal["ask", "allow", "deny"]


class ProviderModelsCost(TypedDict, total=False):
    input: Required[float]

    output: Required[float]

    cache_read: float

    cache_write: float


class ProviderModelsLimit(TypedDict, total=False):
    context: Required[float]

    output: Required[float]


class ProviderModelsModalities(TypedDict, total=False):
    input: Required[List[Literal["text", "audio", "image", "video", "pdf"]]]

    output: Required[List[Literal["text", "audio", "image", "video", "pdf"]]]


class ProviderModelsProvider(TypedDict, total=False):
    npm: Required[str]


class ProviderModels(TypedDict, total=False):
    id: str

    attachment: bool

    cost: ProviderModelsCost

    experimental: bool

    limit: ProviderModelsLimit

    modalities: ProviderModelsModalities

    name: str

    options: Dict[str, object]

    provider: ProviderModelsProvider

    reasoning: bool

    release_date: str

    temperature: bool

    tool_call: bool


class ProviderOptionsTyped(TypedDict, total=False):
    api_key: Annotated[str, PropertyInfo(alias="apiKey")]

    base_url: Annotated[str, PropertyInfo(alias="baseURL")]

    timeout: Union[int, bool]
    """Timeout in milliseconds for requests to this provider.

    Default is 300000 (5 minutes). Set to false to disable timeout.
    """


ProviderOptions: TypeAlias = Union[ProviderOptionsTyped, Dict[str, object]]


class Provider(TypedDict, total=False):
    id: str

    api: str

    env: SequenceNotStr[str]

    models: Dict[str, ProviderModels]

    name: str

    npm: str

    options: ProviderOptions


class Tui(TypedDict, total=False):
    scroll_speed: float
    """TUI scroll speed"""


class Watcher(TypedDict, total=False):
    ignore: SequenceNotStr[str]
