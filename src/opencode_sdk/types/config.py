# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "Config",
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


class AgentBuildPermission(BaseModel):
    bash: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]], None] = None

    edit: Optional[Literal["ask", "allow", "deny"]] = None

    webfetch: Optional[Literal["ask", "allow", "deny"]] = None


class AgentBuild(BaseModel):
    description: Optional[str] = None
    """Description of when to use the agent"""

    disable: Optional[bool] = None

    mode: Optional[Literal["subagent", "primary", "all"]] = None

    model: Optional[str] = None

    permission: Optional[AgentBuildPermission] = None

    prompt: Optional[str] = None

    temperature: Optional[float] = None

    tools: Optional[Dict[str, bool]] = None

    top_p: Optional[float] = None

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


class AgentGeneralPermission(BaseModel):
    bash: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]], None] = None

    edit: Optional[Literal["ask", "allow", "deny"]] = None

    webfetch: Optional[Literal["ask", "allow", "deny"]] = None


class AgentGeneral(BaseModel):
    description: Optional[str] = None
    """Description of when to use the agent"""

    disable: Optional[bool] = None

    mode: Optional[Literal["subagent", "primary", "all"]] = None

    model: Optional[str] = None

    permission: Optional[AgentGeneralPermission] = None

    prompt: Optional[str] = None

    temperature: Optional[float] = None

    tools: Optional[Dict[str, bool]] = None

    top_p: Optional[float] = None

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


class AgentPlanPermission(BaseModel):
    bash: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]], None] = None

    edit: Optional[Literal["ask", "allow", "deny"]] = None

    webfetch: Optional[Literal["ask", "allow", "deny"]] = None


class AgentPlan(BaseModel):
    description: Optional[str] = None
    """Description of when to use the agent"""

    disable: Optional[bool] = None

    mode: Optional[Literal["subagent", "primary", "all"]] = None

    model: Optional[str] = None

    permission: Optional[AgentPlanPermission] = None

    prompt: Optional[str] = None

    temperature: Optional[float] = None

    tools: Optional[Dict[str, bool]] = None

    top_p: Optional[float] = None

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


class AgentAgentItemPermission(BaseModel):
    bash: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]], None] = None

    edit: Optional[Literal["ask", "allow", "deny"]] = None

    webfetch: Optional[Literal["ask", "allow", "deny"]] = None


class AgentAgentItem(BaseModel):
    description: Optional[str] = None
    """Description of when to use the agent"""

    disable: Optional[bool] = None

    mode: Optional[Literal["subagent", "primary", "all"]] = None

    model: Optional[str] = None

    permission: Optional[AgentAgentItemPermission] = None

    prompt: Optional[str] = None

    temperature: Optional[float] = None

    tools: Optional[Dict[str, bool]] = None

    top_p: Optional[float] = None

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
    """Agent configuration, see https://opencode.ai/docs/agent"""

    build: Optional[AgentBuild] = None

    general: Optional[AgentGeneral] = None

    plan: Optional[AgentPlan] = None

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


class ExperimentalHookFileEdited(BaseModel):
    command: List[str]

    environment: Optional[Dict[str, str]] = None


class ExperimentalHookSessionCompleted(BaseModel):
    command: List[str]

    environment: Optional[Dict[str, str]] = None


class ExperimentalHook(BaseModel):
    file_edited: Optional[Dict[str, List[ExperimentalHookFileEdited]]] = None

    session_completed: Optional[List[ExperimentalHookSessionCompleted]] = None


class Experimental(BaseModel):
    disable_paste_summary: Optional[bool] = None

    hook: Optional[ExperimentalHook] = None


class Formatter(BaseModel):
    command: Optional[List[str]] = None

    disabled: Optional[bool] = None

    environment: Optional[Dict[str, str]] = None

    extensions: Optional[List[str]] = None


class Keybinds(BaseModel):
    """Custom keybind configurations"""

    agent_cycle: Optional[str] = None
    """Next agent"""

    agent_cycle_reverse: Optional[str] = None
    """Previous agent"""

    agent_list: Optional[str] = None
    """List agents"""

    app_exit: Optional[str] = None
    """Exit the application"""

    app_help: Optional[str] = None
    """Show help dialog"""

    editor_open: Optional[str] = None
    """Open external editor"""

    file_close: Optional[str] = None
    """@deprecated Close file"""

    file_diff_toggle: Optional[str] = None
    """@deprecated Split/unified diff"""

    file_list: Optional[str] = None
    """@deprecated Currently not available. List files"""

    file_search: Optional[str] = None
    """@deprecated Search file"""

    input_clear: Optional[str] = None
    """Clear input field"""

    input_newline: Optional[str] = None
    """Insert newline in input"""

    input_paste: Optional[str] = None
    """Paste from clipboard"""

    input_submit: Optional[str] = None
    """Submit input"""

    leader: Optional[str] = None
    """Leader key for keybind combinations"""

    messages_copy: Optional[str] = None
    """Copy message"""

    messages_first: Optional[str] = None
    """Navigate to first message"""

    messages_half_page_down: Optional[str] = None
    """Scroll messages down by half page"""

    messages_half_page_up: Optional[str] = None
    """Scroll messages up by half page"""

    messages_last: Optional[str] = None
    """Navigate to last message"""

    messages_layout_toggle: Optional[str] = None
    """@deprecated Toggle layout"""

    messages_next: Optional[str] = None
    """@deprecated Navigate to next message"""

    messages_page_down: Optional[str] = None
    """Scroll messages down by one page"""

    messages_page_up: Optional[str] = None
    """Scroll messages up by one page"""

    messages_previous: Optional[str] = None
    """@deprecated Navigate to previous message"""

    messages_redo: Optional[str] = None
    """Redo message"""

    messages_revert: Optional[str] = None
    """@deprecated use messages_undo. Revert message"""

    messages_undo: Optional[str] = None
    """Undo message"""

    api_model_cycle_recent: Optional[str] = FieldInfo(alias="model_cycle_recent", default=None)
    """Next recent model"""

    api_model_cycle_recent_reverse: Optional[str] = FieldInfo(alias="model_cycle_recent_reverse", default=None)
    """Previous recent model"""

    api_model_list: Optional[str] = FieldInfo(alias="model_list", default=None)
    """List available models"""

    project_init: Optional[str] = None
    """Create/update AGENTS.md"""

    session_child_cycle: Optional[str] = None
    """Cycle to next child session"""

    session_child_cycle_reverse: Optional[str] = None
    """Cycle to previous child session"""

    session_compact: Optional[str] = None
    """Compact the session"""

    session_export: Optional[str] = None
    """Export session to editor"""

    session_interrupt: Optional[str] = None
    """Interrupt current session"""

    session_list: Optional[str] = None
    """List all sessions"""

    session_new: Optional[str] = None
    """Create a new session"""

    session_share: Optional[str] = None
    """Share current session"""

    session_timeline: Optional[str] = None
    """Show session timeline"""

    session_unshare: Optional[str] = None
    """Unshare current session"""

    switch_agent: Optional[str] = None
    """@deprecated use agent_cycle. Next agent"""

    switch_agent_reverse: Optional[str] = None
    """@deprecated use agent_cycle_reverse. Previous agent"""

    switch_mode: Optional[str] = None
    """@deprecated use agent_cycle. Next mode"""

    switch_mode_reverse: Optional[str] = None
    """@deprecated use agent_cycle_reverse. Previous mode"""

    theme_list: Optional[str] = None
    """List available themes"""

    thinking_blocks: Optional[str] = None
    """Toggle thinking blocks"""

    tool_details: Optional[str] = None
    """Toggle tool details"""


class LspDisabled(BaseModel):
    disabled: Literal[True]


class LspUnionMember1(BaseModel):
    command: List[str]

    disabled: Optional[bool] = None

    env: Optional[Dict[str, str]] = None

    extensions: Optional[List[str]] = None

    initialization: Optional[Dict[str, object]] = None


Lsp: TypeAlias = Union[LspDisabled, LspUnionMember1]


class McpMcpLocalConfig(BaseModel):
    command: List[str]
    """Command and arguments to run the MCP server"""

    type: Literal["local"]
    """Type of MCP server connection"""

    enabled: Optional[bool] = None
    """Enable or disable the MCP server on startup"""

    environment: Optional[Dict[str, str]] = None
    """Environment variables to set when running the MCP server"""


class McpMcpRemoteConfig(BaseModel):
    type: Literal["remote"]
    """Type of MCP server connection"""

    url: str
    """URL of the remote MCP server"""

    enabled: Optional[bool] = None
    """Enable or disable the MCP server on startup"""

    headers: Optional[Dict[str, str]] = None
    """Headers to send with the request"""


Mcp: TypeAlias = Union[McpMcpLocalConfig, McpMcpRemoteConfig]


class ModeBuildPermission(BaseModel):
    bash: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]], None] = None

    edit: Optional[Literal["ask", "allow", "deny"]] = None

    webfetch: Optional[Literal["ask", "allow", "deny"]] = None


class ModeBuild(BaseModel):
    description: Optional[str] = None
    """Description of when to use the agent"""

    disable: Optional[bool] = None

    mode: Optional[Literal["subagent", "primary", "all"]] = None

    model: Optional[str] = None

    permission: Optional[ModeBuildPermission] = None

    prompt: Optional[str] = None

    temperature: Optional[float] = None

    tools: Optional[Dict[str, bool]] = None

    top_p: Optional[float] = None

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


class ModePlanPermission(BaseModel):
    bash: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]], None] = None

    edit: Optional[Literal["ask", "allow", "deny"]] = None

    webfetch: Optional[Literal["ask", "allow", "deny"]] = None


class ModePlan(BaseModel):
    description: Optional[str] = None
    """Description of when to use the agent"""

    disable: Optional[bool] = None

    mode: Optional[Literal["subagent", "primary", "all"]] = None

    model: Optional[str] = None

    permission: Optional[ModePlanPermission] = None

    prompt: Optional[str] = None

    temperature: Optional[float] = None

    tools: Optional[Dict[str, bool]] = None

    top_p: Optional[float] = None

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


class ModeModeItemPermission(BaseModel):
    bash: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]], None] = None

    edit: Optional[Literal["ask", "allow", "deny"]] = None

    webfetch: Optional[Literal["ask", "allow", "deny"]] = None


class ModeModeItem(BaseModel):
    description: Optional[str] = None
    """Description of when to use the agent"""

    disable: Optional[bool] = None

    mode: Optional[Literal["subagent", "primary", "all"]] = None

    model: Optional[str] = None

    permission: Optional[ModeModeItemPermission] = None

    prompt: Optional[str] = None

    temperature: Optional[float] = None

    tools: Optional[Dict[str, bool]] = None

    top_p: Optional[float] = None

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


class Permission(BaseModel):
    bash: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]], None] = None

    edit: Optional[Literal["ask", "allow", "deny"]] = None

    webfetch: Optional[Literal["ask", "allow", "deny"]] = None


class ProviderModelsCost(BaseModel):
    input: float

    output: float

    cache_read: Optional[float] = None

    cache_write: Optional[float] = None


class ProviderModelsLimit(BaseModel):
    context: float

    output: float


class ProviderModelsModalities(BaseModel):
    input: List[Literal["text", "audio", "image", "video", "pdf"]]

    output: List[Literal["text", "audio", "image", "video", "pdf"]]


class ProviderModelsProvider(BaseModel):
    npm: str


class ProviderModels(BaseModel):
    id: Optional[str] = None

    attachment: Optional[bool] = None

    cost: Optional[ProviderModelsCost] = None

    experimental: Optional[bool] = None

    limit: Optional[ProviderModelsLimit] = None

    modalities: Optional[ProviderModelsModalities] = None

    name: Optional[str] = None

    options: Optional[Dict[str, object]] = None

    provider: Optional[ProviderModelsProvider] = None

    reasoning: Optional[bool] = None

    release_date: Optional[str] = None

    temperature: Optional[bool] = None

    tool_call: Optional[bool] = None


class ProviderOptions(BaseModel):
    api_key: Optional[str] = FieldInfo(alias="apiKey", default=None)

    base_url: Optional[str] = FieldInfo(alias="baseURL", default=None)

    timeout: Union[int, bool, None] = None
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

    env: Optional[List[str]] = None

    models: Optional[Dict[str, ProviderModels]] = None

    name: Optional[str] = None

    npm: Optional[str] = None

    options: Optional[ProviderOptions] = None


class Tui(BaseModel):
    """TUI specific settings"""

    scroll_speed: Optional[float] = None
    """TUI scroll speed"""


class Watcher(BaseModel):
    ignore: Optional[List[str]] = None


class Config(BaseModel):
    schema_: Optional[str] = FieldInfo(alias="$schema", default=None)
    """JSON schema reference for configuration validation"""

    agent: Optional[Agent] = None
    """Agent configuration, see https://opencode.ai/docs/agent"""

    autoshare: Optional[bool] = None
    """@deprecated Use 'share' field instead.

    Share newly created sessions automatically
    """

    autoupdate: Optional[bool] = None
    """Automatically update to the latest version"""

    command: Optional[Dict[str, Command]] = None
    """Command configuration, see https://opencode.ai/docs/commands"""

    disabled_providers: Optional[List[str]] = None
    """Disable providers that are loaded automatically"""

    experimental: Optional[Experimental] = None

    formatter: Optional[Dict[str, Formatter]] = None

    instructions: Optional[List[str]] = None
    """Additional instruction files or patterns to include"""

    keybinds: Optional[Keybinds] = None
    """Custom keybind configurations"""

    layout: Optional[Literal["auto", "stretch"]] = None
    """@deprecated Always uses stretch layout."""

    lsp: Optional[Dict[str, Lsp]] = None

    mcp: Optional[Dict[str, Mcp]] = None
    """MCP (Model Context Protocol) server configurations"""

    mode: Optional[Mode] = None
    """@deprecated Use `agent` field instead."""

    model: Optional[str] = None
    """Model to use in the format of provider/model, eg anthropic/claude-2"""

    permission: Optional[Permission] = None

    plugin: Optional[List[str]] = None

    provider: Optional[Dict[str, Provider]] = None
    """Custom provider configurations and model overrides"""

    share: Optional[Literal["manual", "auto", "disabled"]] = None
    """
    Control sharing behavior:'manual' allows manual sharing via commands, 'auto'
    enables automatic sharing, 'disabled' disables all sharing
    """

    small_model: Optional[str] = None
    """
    Small model to use for tasks like title generation in the format of
    provider/model
    """

    snapshot: Optional[bool] = None

    theme: Optional[str] = None
    """Theme name to use for the interface"""

    tools: Optional[Dict[str, bool]] = None

    tui: Optional[Tui] = None
    """TUI specific settings"""

    username: Optional[str] = None
    """Custom username to display in conversations instead of system username"""

    watcher: Optional[Watcher] = None
