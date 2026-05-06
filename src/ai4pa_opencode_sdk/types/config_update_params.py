# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo
from .shared_params.agent_config import AgentConfig
from .shared_params.server_config import ServerConfig
from .shared_params.provider_config import ProviderConfig
from .shared_params.mcp_local_config import McpLocalConfig
from .global_.permission_config_param import PermissionConfigParam
from .shared_params.mcp_remote_config import McpRemoteConfig

__all__ = [
    "ConfigUpdateParams",
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
    """自定义 provider 允许加载的 npm 包白名单。"""

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

    formatter: Union[bool, Dict[str, FormatterUnionMember1FormatterUnionMember1Item]]

    instructions: SequenceNotStr[str]
    """Additional instruction files or patterns to include"""

    layout: Literal["auto", "stretch"]
    """@deprecated Always uses stretch layout."""

    log_level: Annotated[Literal["DEBUG", "INFO", "WARN", "ERROR"], PropertyInfo(alias="logLevel")]
    """Log level"""

    lsp: Union[bool, Dict[str, LspUnionMember1LspUnionMember1Item]]

    mcp: Dict[str, Mcp]
    """MCP (Model Context Protocol) server configurations"""

    mode: Mode
    """@deprecated Use `agent` field instead."""

    model: str
    """Model to use in the format of provider/model, eg anthropic/claude-2"""

    permission: PermissionConfigParam

    plugin: SequenceNotStr[Union[str, Iterable[object]]]

    provider: Dict[str, ProviderConfig]
    """Custom provider configurations and model overrides"""

    server: ServerConfig
    """Server configuration for opencode serve and web commands"""

    share: Literal["manual", "auto", "disabled"]
    """
    Control sharing behavior:'manual' allows manual sharing via commands, 'auto'
    enables automatic sharing, 'disabled' disables all sharing
    """

    shell: str
    """Default shell to use for terminal and bash tool"""

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

    tool_output: ToolOutput
    """Thresholds for truncating tool output.

    When output exceeds either limit, the full text is written to the truncation
    directory and a preview is returned.
    """

    tools: Dict[str, bool]

    username: str
    """Custom username to display in conversations instead of system username"""

    watcher: Watcher


class Agent(TypedDict, total=False, extra_items=AgentConfig):  # type: ignore[call-arg]
    """Agent configuration, see https://opencode.ai/docs/agents"""

    build: AgentConfig

    compaction: AgentConfig

    explore: AgentConfig

    general: AgentConfig

    plan: AgentConfig

    summary: AgentConfig

    title: AgentConfig


class Command(TypedDict, total=False):
    template: Required[str]

    agent: str

    description: str

    model: str

    subtask: bool


class Compaction(TypedDict, total=False):
    auto: bool
    """Enable automatic compaction when context is full (default: true)"""

    preserve_recent_tokens: int
    """
    Maximum number of tokens from recent turns to preserve verbatim after compaction
    """

    prune: bool
    """Enable pruning of old tool outputs (default: true)"""

    reserved: int
    """Token buffer for compaction.

    Leaves enough window to avoid overflow during compaction.
    """

    tail_turns: int
    """
    Number of recent user turns, including their following assistant/tool responses,
    to keep verbatim during compaction (default: 2)
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


class McpEnabled(TypedDict, total=False):
    enabled: Required[bool]


Mcp: TypeAlias = Union[McpLocalConfig, McpRemoteConfig, McpEnabled]


class Mode(TypedDict, total=False, extra_items=AgentConfig):  # type: ignore[call-arg]
    """@deprecated Use `agent` field instead."""

    build: AgentConfig

    plan: AgentConfig


class Skills(TypedDict, total=False):
    """Additional skill folder paths"""

    paths: SequenceNotStr[str]
    """Additional paths to skill folders"""

    urls: SequenceNotStr[str]
    """URLs to fetch skills from (e.g., https://example.com/.well-known/skills/)"""


class ToolOutput(TypedDict, total=False):
    """Thresholds for truncating tool output.

    When output exceeds either limit, the full text is written to the truncation directory and a preview is returned.
    """

    max_bytes: int
    """
    Maximum bytes of tool output before it is truncated and saved to disk
    (default: 51200)
    """

    max_lines: int
    """
    Maximum lines of tool output before it is truncated and saved to disk
    (default: 2000)
    """


class Watcher(TypedDict, total=False):
    ignore: SequenceNotStr[str]
