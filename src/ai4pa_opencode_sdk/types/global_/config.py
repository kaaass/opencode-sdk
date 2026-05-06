# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .permission_config import PermissionConfig
from ..shared.agent_config import AgentConfig
from ..shared.server_config import ServerConfig
from ..shared.provider_config import ProviderConfig
from ..shared.mcp_local_config import McpLocalConfig
from ..shared.mcp_remote_config import McpRemoteConfig

__all__ = [
    "Config",
    "Agent",
    "Command",
    "Compaction",
    "Enterprise",
    "Experimental",
    "FormatterUnionMember1FormatterUnionMember1Item",
    "LspUnionMember1LspUnionMember1Item",
    "LspUnionMember1LspUnionMember1ItemDisabled",
    "LspUnionMember1LspUnionMember1ItemUnionMember1",
    "Mcp",
    "McpEnabled",
    "Mode",
    "Skills",
    "ToolOutput",
    "Watcher",
]


class Agent(BaseModel):
    """Agent configuration, see https://opencode.ai/docs/agents"""

    build: Optional[AgentConfig] = None

    compaction: Optional[AgentConfig] = None

    explore: Optional[AgentConfig] = None

    general: Optional[AgentConfig] = None

    plan: Optional[AgentConfig] = None

    summary: Optional[AgentConfig] = None

    title: Optional[AgentConfig] = None

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, AgentConfig] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> AgentConfig: ...
    else:
        __pydantic_extra__: Dict[str, AgentConfig]


class Command(BaseModel):
    template: str

    agent: Optional[str] = None

    description: Optional[str] = None

    model: Optional[str] = None

    subtask: Optional[bool] = None


class Compaction(BaseModel):
    auto: Optional[bool] = None
    """Enable automatic compaction when context is full (default: true)"""

    preserve_recent_tokens: Optional[int] = None
    """
    Maximum number of tokens from recent turns to preserve verbatim after compaction
    """

    prune: Optional[bool] = None
    """Enable pruning of old tool outputs (default: true)"""

    reserved: Optional[int] = None
    """Token buffer for compaction.

    Leaves enough window to avoid overflow during compaction.
    """

    tail_turns: Optional[int] = None
    """
    Number of recent user turns, including their following assistant/tool responses,
    to keep verbatim during compaction (default: 2)
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


class McpEnabled(BaseModel):
    enabled: bool


Mcp: TypeAlias = Union[McpLocalConfig, McpRemoteConfig, McpEnabled]


class Mode(BaseModel):
    """@deprecated Use `agent` field instead."""

    build: Optional[AgentConfig] = None

    plan: Optional[AgentConfig] = None

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, AgentConfig] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> AgentConfig: ...
    else:
        __pydantic_extra__: Dict[str, AgentConfig]


class Skills(BaseModel):
    """Additional skill folder paths"""

    paths: Optional[List[str]] = None
    """Additional paths to skill folders"""

    urls: Optional[List[str]] = None
    """URLs to fetch skills from (e.g., https://example.com/.well-known/skills/)"""


class ToolOutput(BaseModel):
    """Thresholds for truncating tool output.

    When output exceeds either limit, the full text is written to the truncation directory and a preview is returned.
    """

    max_bytes: Optional[int] = None
    """
    Maximum bytes of tool output before it is truncated and saved to disk
    (default: 51200)
    """

    max_lines: Optional[int] = None
    """
    Maximum lines of tool output before it is truncated and saved to disk
    (default: 2000)
    """


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
    """自定义 provider 允许加载的 npm 包白名单。"""

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

    formatter: Union[bool, Dict[str, FormatterUnionMember1FormatterUnionMember1Item], None] = None

    instructions: Optional[List[str]] = None
    """Additional instruction files or patterns to include"""

    layout: Optional[Literal["auto", "stretch"]] = None
    """@deprecated Always uses stretch layout."""

    log_level: Optional[Literal["DEBUG", "INFO", "WARN", "ERROR"]] = FieldInfo(alias="logLevel", default=None)
    """Log level"""

    lsp: Union[bool, Dict[str, LspUnionMember1LspUnionMember1Item], None] = None

    mcp: Optional[Dict[str, Mcp]] = None
    """MCP (Model Context Protocol) server configurations"""

    mode: Optional[Mode] = None
    """@deprecated Use `agent` field instead."""

    model: Optional[str] = None
    """Model to use in the format of provider/model, eg anthropic/claude-2"""

    permission: Optional[PermissionConfig] = None

    plugin: Optional[List[Union[str, List[object]]]] = None

    provider: Optional[Dict[str, ProviderConfig]] = None
    """Custom provider configurations and model overrides"""

    server: Optional[ServerConfig] = None
    """Server configuration for opencode serve and web commands"""

    share: Optional[Literal["manual", "auto", "disabled"]] = None
    """
    Control sharing behavior:'manual' allows manual sharing via commands, 'auto'
    enables automatic sharing, 'disabled' disables all sharing
    """

    shell: Optional[str] = None
    """Default shell to use for terminal and bash tool"""

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

    tool_output: Optional[ToolOutput] = None
    """Thresholds for truncating tool output.

    When output exceeds either limit, the full text is written to the truncation
    directory and a preview is returned.
    """

    tools: Optional[Dict[str, bool]] = None

    username: Optional[str] = None
    """Custom username to display in conversations instead of system username"""

    watcher: Optional[Watcher] = None
