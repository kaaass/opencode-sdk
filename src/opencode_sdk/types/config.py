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
    "AgentCompaction",
    "AgentCompactionPermission",
    "AgentExplore",
    "AgentExplorePermission",
    "AgentGeneral",
    "AgentGeneralPermission",
    "AgentPlan",
    "AgentPlanPermission",
    "AgentSummary",
    "AgentSummaryPermission",
    "AgentTitle",
    "AgentTitlePermission",
    "AgentAgentItem",
    "AgentAgentItemPermission",
    "Command",
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
    "ProviderModelsCostContextOver200k",
    "ProviderModelsInterleaved",
    "ProviderModelsInterleavedField",
    "ProviderModelsLimit",
    "ProviderModelsModalities",
    "ProviderModelsProvider",
    "ProviderOptions",
    "Tui",
    "TuiScrollAcceleration",
    "Watcher",
]


class AgentBuildPermission(BaseModel):
    bash: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]], None] = None

    doom_loop: Optional[Literal["ask", "allow", "deny"]] = None

    edit: Optional[Literal["ask", "allow", "deny"]] = None

    external_directory: Optional[Literal["ask", "allow", "deny"]] = None

    webfetch: Optional[Literal["ask", "allow", "deny"]] = None


class AgentBuild(BaseModel):
    color: Optional[str] = None
    """Hex color code for the agent (e.g., #FF5733)"""

    description: Optional[str] = None
    """Description of when to use the agent"""

    disable: Optional[bool] = None

    max_steps: Optional[int] = FieldInfo(alias="maxSteps", default=None)
    """Maximum number of agentic iterations before forcing text-only response"""

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


class AgentCompactionPermission(BaseModel):
    bash: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]], None] = None

    doom_loop: Optional[Literal["ask", "allow", "deny"]] = None

    edit: Optional[Literal["ask", "allow", "deny"]] = None

    external_directory: Optional[Literal["ask", "allow", "deny"]] = None

    webfetch: Optional[Literal["ask", "allow", "deny"]] = None


class AgentCompaction(BaseModel):
    color: Optional[str] = None
    """Hex color code for the agent (e.g., #FF5733)"""

    description: Optional[str] = None
    """Description of when to use the agent"""

    disable: Optional[bool] = None

    max_steps: Optional[int] = FieldInfo(alias="maxSteps", default=None)
    """Maximum number of agentic iterations before forcing text-only response"""

    mode: Optional[Literal["subagent", "primary", "all"]] = None

    model: Optional[str] = None

    permission: Optional[AgentCompactionPermission] = None

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


class AgentExplorePermission(BaseModel):
    bash: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]], None] = None

    doom_loop: Optional[Literal["ask", "allow", "deny"]] = None

    edit: Optional[Literal["ask", "allow", "deny"]] = None

    external_directory: Optional[Literal["ask", "allow", "deny"]] = None

    webfetch: Optional[Literal["ask", "allow", "deny"]] = None


class AgentExplore(BaseModel):
    color: Optional[str] = None
    """Hex color code for the agent (e.g., #FF5733)"""

    description: Optional[str] = None
    """Description of when to use the agent"""

    disable: Optional[bool] = None

    max_steps: Optional[int] = FieldInfo(alias="maxSteps", default=None)
    """Maximum number of agentic iterations before forcing text-only response"""

    mode: Optional[Literal["subagent", "primary", "all"]] = None

    model: Optional[str] = None

    permission: Optional[AgentExplorePermission] = None

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

    doom_loop: Optional[Literal["ask", "allow", "deny"]] = None

    edit: Optional[Literal["ask", "allow", "deny"]] = None

    external_directory: Optional[Literal["ask", "allow", "deny"]] = None

    webfetch: Optional[Literal["ask", "allow", "deny"]] = None


class AgentGeneral(BaseModel):
    color: Optional[str] = None
    """Hex color code for the agent (e.g., #FF5733)"""

    description: Optional[str] = None
    """Description of when to use the agent"""

    disable: Optional[bool] = None

    max_steps: Optional[int] = FieldInfo(alias="maxSteps", default=None)
    """Maximum number of agentic iterations before forcing text-only response"""

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

    doom_loop: Optional[Literal["ask", "allow", "deny"]] = None

    edit: Optional[Literal["ask", "allow", "deny"]] = None

    external_directory: Optional[Literal["ask", "allow", "deny"]] = None

    webfetch: Optional[Literal["ask", "allow", "deny"]] = None


class AgentPlan(BaseModel):
    color: Optional[str] = None
    """Hex color code for the agent (e.g., #FF5733)"""

    description: Optional[str] = None
    """Description of when to use the agent"""

    disable: Optional[bool] = None

    max_steps: Optional[int] = FieldInfo(alias="maxSteps", default=None)
    """Maximum number of agentic iterations before forcing text-only response"""

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


class AgentSummaryPermission(BaseModel):
    bash: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]], None] = None

    doom_loop: Optional[Literal["ask", "allow", "deny"]] = None

    edit: Optional[Literal["ask", "allow", "deny"]] = None

    external_directory: Optional[Literal["ask", "allow", "deny"]] = None

    webfetch: Optional[Literal["ask", "allow", "deny"]] = None


class AgentSummary(BaseModel):
    color: Optional[str] = None
    """Hex color code for the agent (e.g., #FF5733)"""

    description: Optional[str] = None
    """Description of when to use the agent"""

    disable: Optional[bool] = None

    max_steps: Optional[int] = FieldInfo(alias="maxSteps", default=None)
    """Maximum number of agentic iterations before forcing text-only response"""

    mode: Optional[Literal["subagent", "primary", "all"]] = None

    model: Optional[str] = None

    permission: Optional[AgentSummaryPermission] = None

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


class AgentTitlePermission(BaseModel):
    bash: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]], None] = None

    doom_loop: Optional[Literal["ask", "allow", "deny"]] = None

    edit: Optional[Literal["ask", "allow", "deny"]] = None

    external_directory: Optional[Literal["ask", "allow", "deny"]] = None

    webfetch: Optional[Literal["ask", "allow", "deny"]] = None


class AgentTitle(BaseModel):
    color: Optional[str] = None
    """Hex color code for the agent (e.g., #FF5733)"""

    description: Optional[str] = None
    """Description of when to use the agent"""

    disable: Optional[bool] = None

    max_steps: Optional[int] = FieldInfo(alias="maxSteps", default=None)
    """Maximum number of agentic iterations before forcing text-only response"""

    mode: Optional[Literal["subagent", "primary", "all"]] = None

    model: Optional[str] = None

    permission: Optional[AgentTitlePermission] = None

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

    doom_loop: Optional[Literal["ask", "allow", "deny"]] = None

    edit: Optional[Literal["ask", "allow", "deny"]] = None

    external_directory: Optional[Literal["ask", "allow", "deny"]] = None

    webfetch: Optional[Literal["ask", "allow", "deny"]] = None


class AgentAgentItem(BaseModel):
    color: Optional[str] = None
    """Hex color code for the agent (e.g., #FF5733)"""

    description: Optional[str] = None
    """Description of when to use the agent"""

    disable: Optional[bool] = None

    max_steps: Optional[int] = FieldInfo(alias="maxSteps", default=None)
    """Maximum number of agentic iterations before forcing text-only response"""

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


class Enterprise(BaseModel):
    url: Optional[str] = None
    """Enterprise URL"""


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
    batch_tool: Optional[bool] = None
    """Enable the batch tool"""

    chat_max_retries: Optional[float] = FieldInfo(alias="chatMaxRetries", default=None)
    """Number of retries for chat completions on failure"""

    continue_loop_on_deny: Optional[bool] = None
    """Continue the agent loop when a tool call is denied"""

    disable_paste_summary: Optional[bool] = None

    hook: Optional[ExperimentalHook] = None

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

    command_list: Optional[str] = None
    """List available commands"""

    editor_open: Optional[str] = None
    """Open external editor"""

    history_next: Optional[str] = None
    """Next history item"""

    history_previous: Optional[str] = None
    """Previous history item"""

    input_backspace: Optional[str] = None
    """Backspace in input"""

    input_buffer_end: Optional[str] = None
    """Move to end of buffer in input"""

    input_buffer_home: Optional[str] = None
    """Move to start of buffer in input"""

    input_clear: Optional[str] = None
    """Clear input field"""

    input_delete: Optional[str] = None
    """Delete character in input"""

    input_delete_line: Optional[str] = None
    """Delete line in input"""

    input_delete_to_line_end: Optional[str] = None
    """Delete to end of line in input"""

    input_delete_to_line_start: Optional[str] = None
    """Delete to start of line in input"""

    input_delete_word_backward: Optional[str] = None
    """Delete word backward in input"""

    input_delete_word_forward: Optional[str] = None
    """Delete word forward in input"""

    input_line_end: Optional[str] = None
    """Move to end of line in input"""

    input_line_home: Optional[str] = None
    """Move to start of line in input"""

    input_move_down: Optional[str] = None
    """Move cursor down in input"""

    input_move_left: Optional[str] = None
    """Move cursor left in input"""

    input_move_right: Optional[str] = None
    """Move cursor right in input"""

    input_move_up: Optional[str] = None
    """Move cursor up in input"""

    input_newline: Optional[str] = None
    """Insert newline in input"""

    input_paste: Optional[str] = None
    """Paste from clipboard"""

    input_redo: Optional[str] = None
    """Redo in input"""

    input_select_buffer_end: Optional[str] = None
    """Select to end of buffer in input"""

    input_select_buffer_home: Optional[str] = None
    """Select to start of buffer in input"""

    input_select_down: Optional[str] = None
    """Select down in input"""

    input_select_left: Optional[str] = None
    """Select left in input"""

    input_select_line_end: Optional[str] = None
    """Select to end of line in input"""

    input_select_line_home: Optional[str] = None
    """Select to start of line in input"""

    input_select_right: Optional[str] = None
    """Select right in input"""

    input_select_up: Optional[str] = None
    """Select up in input"""

    input_select_visual_line_end: Optional[str] = None
    """Select to end of visual line in input"""

    input_select_visual_line_home: Optional[str] = None
    """Select to start of visual line in input"""

    input_select_word_backward: Optional[str] = None
    """Select word backward in input"""

    input_select_word_forward: Optional[str] = None
    """Select word forward in input"""

    input_submit: Optional[str] = None
    """Submit input"""

    input_undo: Optional[str] = None
    """Undo in input"""

    input_visual_line_end: Optional[str] = None
    """Move to end of visual line in input"""

    input_visual_line_home: Optional[str] = None
    """Move to start of visual line in input"""

    input_word_backward: Optional[str] = None
    """Move word backward in input"""

    input_word_forward: Optional[str] = None
    """Move word forward in input"""

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

    messages_last_user: Optional[str] = None
    """Navigate to last user message"""

    messages_page_down: Optional[str] = None
    """Scroll messages down by one page"""

    messages_page_up: Optional[str] = None
    """Scroll messages up by one page"""

    messages_redo: Optional[str] = None
    """Redo message"""

    messages_toggle_conceal: Optional[str] = None
    """Toggle code block concealment in messages"""

    messages_undo: Optional[str] = None
    """Undo message"""

    api_model_cycle_favorite: Optional[str] = FieldInfo(alias="model_cycle_favorite", default=None)
    """Next favorite model"""

    api_model_cycle_favorite_reverse: Optional[str] = FieldInfo(alias="model_cycle_favorite_reverse", default=None)
    """Previous favorite model"""

    api_model_cycle_recent: Optional[str] = FieldInfo(alias="model_cycle_recent", default=None)
    """Next recently used model"""

    api_model_cycle_recent_reverse: Optional[str] = FieldInfo(alias="model_cycle_recent_reverse", default=None)
    """Previous recently used model"""

    api_model_list: Optional[str] = FieldInfo(alias="model_list", default=None)
    """List available models"""

    scrollbar_toggle: Optional[str] = None
    """Toggle session scrollbar"""

    session_child_cycle: Optional[str] = None
    """Next child session"""

    session_child_cycle_reverse: Optional[str] = None
    """Previous child session"""

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

    sidebar_toggle: Optional[str] = None
    """Toggle sidebar"""

    status_view: Optional[str] = None
    """View status"""

    terminal_suspend: Optional[str] = None
    """Suspend terminal"""

    theme_list: Optional[str] = None
    """List available themes"""

    tool_details: Optional[str] = None
    """Toggle tool details visibility"""

    username_toggle: Optional[str] = None
    """Toggle username visibility"""


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
    """Timeout in ms for fetching tools from the MCP server.

    Defaults to 5000 (5 seconds) if not specified.
    """


class McpMcpRemoteConfigOAuthMcpOAuthConfig(BaseModel):
    client_id: Optional[str] = FieldInfo(alias="clientId", default=None)
    """OAuth client ID.

    If not provided, dynamic client registration (RFC 7591) will be attempted.
    """

    client_secret: Optional[str] = FieldInfo(alias="clientSecret", default=None)
    """OAuth client secret (if required by the authorization server)"""

    scope: Optional[str] = None
    """OAuth scopes to request during authorization"""


McpMcpRemoteConfigOAuth: TypeAlias = Union[McpMcpRemoteConfigOAuthMcpOAuthConfig, bool]


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
    """Timeout in ms for fetching tools from the MCP server.

    Defaults to 5000 (5 seconds) if not specified.
    """


Mcp: TypeAlias = Union[McpMcpLocalConfig, McpMcpRemoteConfig]


class ModeBuildPermission(BaseModel):
    bash: Union[Literal["ask", "allow", "deny"], Dict[str, Literal["ask", "allow", "deny"]], None] = None

    doom_loop: Optional[Literal["ask", "allow", "deny"]] = None

    edit: Optional[Literal["ask", "allow", "deny"]] = None

    external_directory: Optional[Literal["ask", "allow", "deny"]] = None

    webfetch: Optional[Literal["ask", "allow", "deny"]] = None


class ModeBuild(BaseModel):
    color: Optional[str] = None
    """Hex color code for the agent (e.g., #FF5733)"""

    description: Optional[str] = None
    """Description of when to use the agent"""

    disable: Optional[bool] = None

    max_steps: Optional[int] = FieldInfo(alias="maxSteps", default=None)
    """Maximum number of agentic iterations before forcing text-only response"""

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

    doom_loop: Optional[Literal["ask", "allow", "deny"]] = None

    edit: Optional[Literal["ask", "allow", "deny"]] = None

    external_directory: Optional[Literal["ask", "allow", "deny"]] = None

    webfetch: Optional[Literal["ask", "allow", "deny"]] = None


class ModePlan(BaseModel):
    color: Optional[str] = None
    """Hex color code for the agent (e.g., #FF5733)"""

    description: Optional[str] = None
    """Description of when to use the agent"""

    disable: Optional[bool] = None

    max_steps: Optional[int] = FieldInfo(alias="maxSteps", default=None)
    """Maximum number of agentic iterations before forcing text-only response"""

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

    doom_loop: Optional[Literal["ask", "allow", "deny"]] = None

    edit: Optional[Literal["ask", "allow", "deny"]] = None

    external_directory: Optional[Literal["ask", "allow", "deny"]] = None

    webfetch: Optional[Literal["ask", "allow", "deny"]] = None


class ModeModeItem(BaseModel):
    color: Optional[str] = None
    """Hex color code for the agent (e.g., #FF5733)"""

    description: Optional[str] = None
    """Description of when to use the agent"""

    disable: Optional[bool] = None

    max_steps: Optional[int] = FieldInfo(alias="maxSteps", default=None)
    """Maximum number of agentic iterations before forcing text-only response"""

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

    doom_loop: Optional[Literal["ask", "allow", "deny"]] = None

    edit: Optional[Literal["ask", "allow", "deny"]] = None

    external_directory: Optional[Literal["ask", "allow", "deny"]] = None

    webfetch: Optional[Literal["ask", "allow", "deny"]] = None


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


class ProviderOptions(BaseModel):
    api_key: Optional[str] = FieldInfo(alias="apiKey", default=None)

    base_url: Optional[str] = FieldInfo(alias="baseURL", default=None)

    enterprise_url: Optional[str] = FieldInfo(alias="enterpriseUrl", default=None)
    """GitHub Enterprise URL for copilot authentication"""

    set_cache_key: Optional[bool] = FieldInfo(alias="setCacheKey", default=None)
    """Enable promptCacheKey for this provider (default false)"""

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

    blacklist: Optional[List[str]] = None

    env: Optional[List[str]] = None

    models: Optional[Dict[str, ProviderModels]] = None

    name: Optional[str] = None

    npm: Optional[str] = None

    options: Optional[ProviderOptions] = None

    whitelist: Optional[List[str]] = None


class TuiScrollAcceleration(BaseModel):
    """Scroll acceleration settings"""

    enabled: bool
    """Enable scroll acceleration"""


class Tui(BaseModel):
    """TUI specific settings"""

    diff_style: Optional[Literal["auto", "stacked"]] = None
    """
    Control diff rendering style: 'auto' adapts to terminal width, 'stacked' always
    shows single column
    """

    scroll_acceleration: Optional[TuiScrollAcceleration] = None
    """Scroll acceleration settings"""

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

    autoupdate: Union[bool, Literal["notify"], None] = None
    """Automatically update to the latest version.

    Set to true to auto-update, false to disable, or 'notify' to show update
    notifications
    """

    command: Optional[Dict[str, Command]] = None
    """Command configuration, see https://opencode.ai/docs/commands"""

    disabled_providers: Optional[List[str]] = None
    """Disable providers that are loaded automatically"""

    enabled_providers: Optional[List[str]] = None
    """When set, ONLY these providers will be enabled.

    All other providers will be ignored
    """

    enterprise: Optional[Enterprise] = None

    experimental: Optional[Experimental] = None

    formatter: Union[bool, Dict[str, FormatterUnionMember1FormatterUnionMember1Item], None] = None

    instructions: Optional[List[str]] = None
    """Additional instruction files or patterns to include"""

    keybinds: Optional[Keybinds] = None
    """Custom keybind configurations"""

    layout: Optional[Literal["auto", "stretch"]] = None
    """@deprecated Always uses stretch layout."""

    lsp: Union[bool, Dict[str, LspUnionMember1LspUnionMember1Item], None] = None

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
