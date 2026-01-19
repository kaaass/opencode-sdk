# Project

Types:

```python
from opencode_sdk.types import Project, ProjectListResponse
```

Methods:

- <code title="patch /project/{projectID}">client.project.<a href="./src/opencode_sdk/resources/project.py">update</a>(project_id, \*\*<a href="src/opencode_sdk/types/project_update_params.py">params</a>) -> <a href="./src/opencode_sdk/types/project.py">Project</a></code>
- <code title="get /project">client.project.<a href="./src/opencode_sdk/resources/project.py">list</a>(\*\*<a href="src/opencode_sdk/types/project_list_params.py">params</a>) -> <a href="./src/opencode_sdk/types/project_list_response.py">ProjectListResponse</a></code>
- <code title="get /project/current">client.project.<a href="./src/opencode_sdk/resources/project.py">retrieve_current</a>(\*\*<a href="src/opencode_sdk/types/project_retrieve_current_params.py">params</a>) -> <a href="./src/opencode_sdk/types/project.py">Project</a></code>

# Config

Types:

```python
from opencode_sdk.types import Config, ConfigListProvidersResponse
```

Methods:

- <code title="get /config">client.config.<a href="./src/opencode_sdk/resources/config.py">retrieve</a>(\*\*<a href="src/opencode_sdk/types/config_retrieve_params.py">params</a>) -> <a href="./src/opencode_sdk/types/config.py">Config</a></code>
- <code title="patch /config">client.config.<a href="./src/opencode_sdk/resources/config.py">update</a>(\*\*<a href="src/opencode_sdk/types/config_update_params.py">params</a>) -> <a href="./src/opencode_sdk/types/config.py">Config</a></code>
- <code title="get /config/providers">client.config.<a href="./src/opencode_sdk/resources/config.py">list_providers</a>(\*\*<a href="src/opencode_sdk/types/config_list_providers_params.py">params</a>) -> <a href="./src/opencode_sdk/types/config_list_providers_response.py">ConfigListProvidersResponse</a></code>

# Experimental

Types:

```python
from opencode_sdk.types import ExperimentalGetResourcesResponse
```

Methods:

- <code title="get /experimental/resource">client.experimental.<a href="./src/opencode_sdk/resources/experimental/experimental.py">get_resources</a>(\*\*<a href="src/opencode_sdk/types/experimental_get_resources_params.py">params</a>) -> <a href="./src/opencode_sdk/types/experimental_get_resources_response.py">ExperimentalGetResourcesResponse</a></code>

## Tool

Types:

```python
from opencode_sdk.types.experimental import ToolListIDsResponse, ToolListToolsResponse
```

Methods:

- <code title="get /experimental/tool/ids">client.experimental.tool.<a href="./src/opencode_sdk/resources/experimental/tool.py">list_ids</a>(\*\*<a href="src/opencode_sdk/types/experimental/tool_list_ids_params.py">params</a>) -> <a href="./src/opencode_sdk/types/experimental/tool_list_ids_response.py">ToolListIDsResponse</a></code>
- <code title="get /experimental/tool">client.experimental.tool.<a href="./src/opencode_sdk/resources/experimental/tool.py">list_tools</a>(\*\*<a href="src/opencode_sdk/types/experimental/tool_list_tools_params.py">params</a>) -> <a href="./src/opencode_sdk/types/experimental/tool_list_tools_response.py">ToolListToolsResponse</a></code>

## Worktree

Types:

```python
from opencode_sdk.types.experimental import WorktreeCreateResponse, WorktreeListResponse
```

Methods:

- <code title="post /experimental/worktree">client.experimental.worktree.<a href="./src/opencode_sdk/resources/experimental/worktree.py">create</a>(\*\*<a href="src/opencode_sdk/types/experimental/worktree_create_params.py">params</a>) -> <a href="./src/opencode_sdk/types/experimental/worktree_create_response.py">WorktreeCreateResponse</a></code>
- <code title="get /experimental/worktree">client.experimental.worktree.<a href="./src/opencode_sdk/resources/experimental/worktree.py">list</a>(\*\*<a href="src/opencode_sdk/types/experimental/worktree_list_params.py">params</a>) -> <a href="./src/opencode_sdk/types/experimental/worktree_list_response.py">WorktreeListResponse</a></code>

# Path

Types:

```python
from opencode_sdk.types import PathRetrieveResponse
```

Methods:

- <code title="get /path">client.path.<a href="./src/opencode_sdk/resources/path.py">retrieve</a>(\*\*<a href="src/opencode_sdk/types/path_retrieve_params.py">params</a>) -> <a href="./src/opencode_sdk/types/path_retrieve_response.py">PathRetrieveResponse</a></code>

# Session

Types:

```python
from opencode_sdk.types import (
    AssistantMessage,
    MessageAbortedError,
    MessageOutputLengthError,
    ProviderAuthError,
    Session,
    Todo,
    UnknownError,
    SessionListResponse,
    SessionDeleteResponse,
    SessionAbortResponse,
    SessionGetChildrenResponse,
    SessionGetDiffResponse,
    SessionGetStatusResponse,
    SessionGetTodoResponse,
    SessionInitializeResponse,
    SessionListArtifactsResponse,
    SessionRespondToPermissionResponse,
    SessionRetrieveStatusResponse,
    SessionSendCommandResponse,
    SessionSubmitToolResultsResponse,
    SessionSummarizeResponse,
)
```

Methods:

- <code title="post /session">client.session.<a href="./src/opencode_sdk/resources/session/session.py">create</a>(\*\*<a href="src/opencode_sdk/types/session_create_params.py">params</a>) -> <a href="./src/opencode_sdk/types/session/session.py">Session</a></code>
- <code title="get /session/{sessionID}">client.session.<a href="./src/opencode_sdk/resources/session/session.py">retrieve</a>(session_id, \*\*<a href="src/opencode_sdk/types/session_retrieve_params.py">params</a>) -> <a href="./src/opencode_sdk/types/session/session.py">Session</a></code>
- <code title="patch /session/{sessionID}">client.session.<a href="./src/opencode_sdk/resources/session/session.py">update</a>(session_id, \*\*<a href="src/opencode_sdk/types/session_update_params.py">params</a>) -> <a href="./src/opencode_sdk/types/session/session.py">Session</a></code>
- <code title="get /session">client.session.<a href="./src/opencode_sdk/resources/session/session.py">list</a>(\*\*<a href="src/opencode_sdk/types/session_list_params.py">params</a>) -> <a href="./src/opencode_sdk/types/session_list_response.py">SessionListResponse</a></code>
- <code title="delete /session/{sessionID}">client.session.<a href="./src/opencode_sdk/resources/session/session.py">delete</a>(session_id, \*\*<a href="src/opencode_sdk/types/session_delete_params.py">params</a>) -> <a href="./src/opencode_sdk/types/session_delete_response.py">SessionDeleteResponse</a></code>
- <code title="post /session/{sessionID}/abort">client.session.<a href="./src/opencode_sdk/resources/session/session.py">abort</a>(session_id, \*\*<a href="src/opencode_sdk/types/session_abort_params.py">params</a>) -> <a href="./src/opencode_sdk/types/session_abort_response.py">SessionAbortResponse</a></code>
- <code title="post /session/{sessionID}/fork">client.session.<a href="./src/opencode_sdk/resources/session/session.py">fork</a>(session_id, \*\*<a href="src/opencode_sdk/types/session_fork_params.py">params</a>) -> <a href="./src/opencode_sdk/types/session/session.py">Session</a></code>
- <code title="get /session/{sessionID}/children">client.session.<a href="./src/opencode_sdk/resources/session/session.py">get_children</a>(session_id, \*\*<a href="src/opencode_sdk/types/session_get_children_params.py">params</a>) -> <a href="./src/opencode_sdk/types/session_get_children_response.py">SessionGetChildrenResponse</a></code>
- <code title="get /session/{sessionID}/diff">client.session.<a href="./src/opencode_sdk/resources/session/session.py">get_diff</a>(session_id, \*\*<a href="src/opencode_sdk/types/session_get_diff_params.py">params</a>) -> <a href="./src/opencode_sdk/types/session_get_diff_response.py">SessionGetDiffResponse</a></code>
- <code title="get /session/status">client.session.<a href="./src/opencode_sdk/resources/session/session.py">get_status</a>(\*\*<a href="src/opencode_sdk/types/session_get_status_params.py">params</a>) -> <a href="./src/opencode_sdk/types/session_get_status_response.py">SessionGetStatusResponse</a></code>
- <code title="get /session/{sessionID}/todo">client.session.<a href="./src/opencode_sdk/resources/session/session.py">get_todo</a>(session_id, \*\*<a href="src/opencode_sdk/types/session_get_todo_params.py">params</a>) -> <a href="./src/opencode_sdk/types/session_get_todo_response.py">SessionGetTodoResponse</a></code>
- <code title="post /session/{sessionID}/init">client.session.<a href="./src/opencode_sdk/resources/session/session.py">initialize</a>(session_id, \*\*<a href="src/opencode_sdk/types/session_initialize_params.py">params</a>) -> <a href="./src/opencode_sdk/types/session_initialize_response.py">SessionInitializeResponse</a></code>
- <code title="get /session/{sessionID}/artifacts">client.session.<a href="./src/opencode_sdk/resources/session/session.py">list_artifacts</a>(session_id, \*\*<a href="src/opencode_sdk/types/session_list_artifacts_params.py">params</a>) -> <a href="./src/opencode_sdk/types/session_list_artifacts_response.py">SessionListArtifactsResponse</a></code>
- <code title="post /session/{sessionID}/permissions/{permissionID}">client.session.<a href="./src/opencode_sdk/resources/session/session.py">respond_to_permission</a>(permission_id, \*, session_id, \*\*<a href="src/opencode_sdk/types/session_respond_to_permission_params.py">params</a>) -> <a href="./src/opencode_sdk/types/session_respond_to_permission_response.py">SessionRespondToPermissionResponse</a></code>
- <code title="post /session/{sessionID}/unrevert">client.session.<a href="./src/opencode_sdk/resources/session/session.py">restore_reverted_messages</a>(session_id, \*\*<a href="src/opencode_sdk/types/session_restore_reverted_messages_params.py">params</a>) -> <a href="./src/opencode_sdk/types/session/session.py">Session</a></code>
- <code title="get /session/{sessionID}/status">client.session.<a href="./src/opencode_sdk/resources/session/session.py">retrieve_status</a>(session_id, \*\*<a href="src/opencode_sdk/types/session_retrieve_status_params.py">params</a>) -> <a href="./src/opencode_sdk/types/session_retrieve_status_response.py">SessionRetrieveStatusResponse</a></code>
- <code title="post /session/{sessionID}/revert">client.session.<a href="./src/opencode_sdk/resources/session/session.py">revert_message</a>(session_id, \*\*<a href="src/opencode_sdk/types/session_revert_message_params.py">params</a>) -> <a href="./src/opencode_sdk/types/session/session.py">Session</a></code>
- <code title="post /session/{sessionID}/shell">client.session.<a href="./src/opencode_sdk/resources/session/session.py">run_shell_command</a>(session_id, \*\*<a href="src/opencode_sdk/types/session_run_shell_command_params.py">params</a>) -> <a href="./src/opencode_sdk/types/assistant_message.py">AssistantMessage</a></code>
- <code title="post /session/{sessionID}/prompt_async">client.session.<a href="./src/opencode_sdk/resources/session/session.py">send_async_message</a>(session_id, \*\*<a href="src/opencode_sdk/types/session_send_async_message_params.py">params</a>) -> None</code>
- <code title="post /session/{sessionID}/command">client.session.<a href="./src/opencode_sdk/resources/session/session.py">send_command</a>(session_id, \*\*<a href="src/opencode_sdk/types/session_send_command_params.py">params</a>) -> <a href="./src/opencode_sdk/types/session_send_command_response.py">SessionSendCommandResponse</a></code>
- <code title="post /session/{sessionID}/tool-results">client.session.<a href="./src/opencode_sdk/resources/session/session.py">submit_tool_results</a>(session_id, \*\*<a href="src/opencode_sdk/types/session_submit_tool_results_params.py">params</a>) -> <a href="./src/opencode_sdk/types/session_submit_tool_results_response.py">SessionSubmitToolResultsResponse</a></code>
- <code title="post /session/{sessionID}/summarize">client.session.<a href="./src/opencode_sdk/resources/session/session.py">summarize</a>(session_id, \*\*<a href="src/opencode_sdk/types/session_summarize_params.py">params</a>) -> <a href="./src/opencode_sdk/types/session_summarize_response.py">SessionSummarizeResponse</a></code>

## Share

Methods:

- <code title="post /session/{sessionID}/share">client.session.share.<a href="./src/opencode_sdk/resources/session/share.py">create</a>(session_id, \*\*<a href="src/opencode_sdk/types/session/share_create_params.py">params</a>) -> <a href="./src/opencode_sdk/types/session/session.py">Session</a></code>
- <code title="delete /session/{sessionID}/share">client.session.share.<a href="./src/opencode_sdk/resources/session/share.py">delete</a>(session_id, \*\*<a href="src/opencode_sdk/types/session/share_delete_params.py">params</a>) -> <a href="./src/opencode_sdk/types/session/session.py">Session</a></code>

## Message

Types:

```python
from opencode_sdk.types.session import (
    FilePart,
    FilePartSource,
    FilePartSourceText,
    Message,
    Part,
    MessageRetrieveResponse,
    MessageGetAllResponse,
    MessageSendResponse,
)
```

Methods:

- <code title="get /session/{sessionID}/message/{messageID}">client.session.message.<a href="./src/opencode_sdk/resources/session/message/message.py">retrieve</a>(message_id, \*, session_id, \*\*<a href="src/opencode_sdk/types/session/message_retrieve_params.py">params</a>) -> <a href="./src/opencode_sdk/types/session/message_retrieve_response.py">MessageRetrieveResponse</a></code>
- <code title="get /session/{sessionID}/message">client.session.message.<a href="./src/opencode_sdk/resources/session/message/message.py">get_all</a>(session_id, \*\*<a href="src/opencode_sdk/types/session/message_get_all_params.py">params</a>) -> <a href="./src/opencode_sdk/types/session/message_get_all_response.py">MessageGetAllResponse</a></code>
- <code title="post /session/{sessionID}/message">client.session.message.<a href="./src/opencode_sdk/resources/session/message/message.py">send</a>(session_id, \*\*<a href="src/opencode_sdk/types/session/message_send_params.py">params</a>) -> <a href="./src/opencode_sdk/types/session/message_send_response.py">MessageSendResponse</a></code>

### Part

Types:

```python
from opencode_sdk.types.session.message import PartDeleteResponse
```

Methods:

- <code title="patch /session/{sessionID}/message/{messageID}/part/{partID}">client.session.message.part.<a href="./src/opencode_sdk/resources/session/message/part.py">update</a>(part_id, \*, path_session_id, path_message_id, \*\*<a href="src/opencode_sdk/types/session/message/part_update_params.py">params</a>) -> <a href="./src/opencode_sdk/types/session/part.py">Part</a></code>
- <code title="delete /session/{sessionID}/message/{messageID}/part/{partID}">client.session.message.part.<a href="./src/opencode_sdk/resources/session/message/part.py">delete</a>(part_id, \*, session_id, message_id, \*\*<a href="src/opencode_sdk/types/session/message/part_delete_params.py">params</a>) -> <a href="./src/opencode_sdk/types/session/message/part_delete_response.py">PartDeleteResponse</a></code>

# Command

Types:

```python
from opencode_sdk.types import CommandListResponse
```

Methods:

- <code title="get /command">client.command.<a href="./src/opencode_sdk/resources/command.py">list</a>(\*\*<a href="src/opencode_sdk/types/command_list_params.py">params</a>) -> <a href="./src/opencode_sdk/types/command_list_response.py">CommandListResponse</a></code>

# Find

Types:

```python
from opencode_sdk.types import (
    Range,
    FindRetrieveResponse,
    FindRetrieveFileResponse,
    FindRetrieveSymbolResponse,
)
```

Methods:

- <code title="get /find">client.find.<a href="./src/opencode_sdk/resources/find.py">retrieve</a>(\*\*<a href="src/opencode_sdk/types/find_retrieve_params.py">params</a>) -> <a href="./src/opencode_sdk/types/find_retrieve_response.py">FindRetrieveResponse</a></code>
- <code title="get /find/file">client.find.<a href="./src/opencode_sdk/resources/find.py">retrieve_file</a>(\*\*<a href="src/opencode_sdk/types/find_retrieve_file_params.py">params</a>) -> <a href="./src/opencode_sdk/types/find_retrieve_file_response.py">FindRetrieveFileResponse</a></code>
- <code title="get /find/symbol">client.find.<a href="./src/opencode_sdk/resources/find.py">retrieve_symbol</a>(\*\*<a href="src/opencode_sdk/types/find_retrieve_symbol_params.py">params</a>) -> <a href="./src/opencode_sdk/types/find_retrieve_symbol_response.py">FindRetrieveSymbolResponse</a></code>

# File

Types:

```python
from opencode_sdk.types import FileListResponse, FileGetStatusResponse, FileReadResponse
```

Methods:

- <code title="get /file">client.file.<a href="./src/opencode_sdk/resources/file.py">list</a>(\*\*<a href="src/opencode_sdk/types/file_list_params.py">params</a>) -> <a href="./src/opencode_sdk/types/file_list_response.py">FileListResponse</a></code>
- <code title="get /file/status">client.file.<a href="./src/opencode_sdk/resources/file.py">get_status</a>(\*\*<a href="src/opencode_sdk/types/file_get_status_params.py">params</a>) -> <a href="./src/opencode_sdk/types/file_get_status_response.py">FileGetStatusResponse</a></code>
- <code title="get /file/content">client.file.<a href="./src/opencode_sdk/resources/file.py">read</a>(\*\*<a href="src/opencode_sdk/types/file_read_params.py">params</a>) -> <a href="./src/opencode_sdk/types/file_read_response.py">FileReadResponse</a></code>

# Log

Types:

```python
from opencode_sdk.types import LogWriteResponse
```

Methods:

- <code title="post /log">client.log.<a href="./src/opencode_sdk/resources/log.py">write</a>(\*\*<a href="src/opencode_sdk/types/log_write_params.py">params</a>) -> <a href="./src/opencode_sdk/types/log_write_response.py">LogWriteResponse</a></code>

# Agent

Types:

```python
from opencode_sdk.types import AgentListResponse, AgentDeleteResponse, AgentCreateOrUpdateResponse
```

Methods:

- <code title="get /agent">client.agent.<a href="./src/opencode_sdk/resources/agent.py">list</a>(\*\*<a href="src/opencode_sdk/types/agent_list_params.py">params</a>) -> <a href="./src/opencode_sdk/types/agent_list_response.py">AgentListResponse</a></code>
- <code title="delete /agent/{name}">client.agent.<a href="./src/opencode_sdk/resources/agent.py">delete</a>(name, \*\*<a href="src/opencode_sdk/types/agent_delete_params.py">params</a>) -> <a href="./src/opencode_sdk/types/agent_delete_response.py">AgentDeleteResponse</a></code>
- <code title="post /agent">client.agent.<a href="./src/opencode_sdk/resources/agent.py">create_or_update</a>(\*\*<a href="src/opencode_sdk/types/agent_create_or_update_params.py">params</a>) -> <a href="./src/opencode_sdk/types/agent_create_or_update_response.py">AgentCreateOrUpdateResponse</a></code>

# Mcp

Types:

```python
from opencode_sdk.types import (
    McpCreateResponse,
    McpRetrieveResponse,
    McpConnectResponse,
    McpDisconnectResponse,
    McpReloadResponse,
)
```

Methods:

- <code title="post /mcp">client.mcp.<a href="./src/opencode_sdk/resources/mcp/mcp.py">create</a>(\*\*<a href="src/opencode_sdk/types/mcp_create_params.py">params</a>) -> <a href="./src/opencode_sdk/types/mcp_create_response.py">McpCreateResponse</a></code>
- <code title="get /mcp">client.mcp.<a href="./src/opencode_sdk/resources/mcp/mcp.py">retrieve</a>(\*\*<a href="src/opencode_sdk/types/mcp_retrieve_params.py">params</a>) -> <a href="./src/opencode_sdk/types/mcp_retrieve_response.py">McpRetrieveResponse</a></code>
- <code title="post /mcp/{name}/connect">client.mcp.<a href="./src/opencode_sdk/resources/mcp/mcp.py">connect</a>(name, \*\*<a href="src/opencode_sdk/types/mcp_connect_params.py">params</a>) -> <a href="./src/opencode_sdk/types/mcp_connect_response.py">McpConnectResponse</a></code>
- <code title="post /mcp/{name}/disconnect">client.mcp.<a href="./src/opencode_sdk/resources/mcp/mcp.py">disconnect</a>(name, \*\*<a href="src/opencode_sdk/types/mcp_disconnect_params.py">params</a>) -> <a href="./src/opencode_sdk/types/mcp_disconnect_response.py">McpDisconnectResponse</a></code>
- <code title="post /mcp/reload">client.mcp.<a href="./src/opencode_sdk/resources/mcp/mcp.py">reload</a>(\*\*<a href="src/opencode_sdk/types/mcp_reload_params.py">params</a>) -> <a href="./src/opencode_sdk/types/mcp_reload_response.py">McpReloadResponse</a></code>

## Auth

Types:

```python
from opencode_sdk.types.mcp import (
    AuthAuthenticateResponse,
    AuthCompleteResponse,
    AuthRemoveResponse,
    AuthStartResponse,
)
```

Methods:

- <code title="post /mcp/{name}/auth/authenticate">client.mcp.auth.<a href="./src/opencode_sdk/resources/mcp/auth.py">authenticate</a>(name, \*\*<a href="src/opencode_sdk/types/mcp/auth_authenticate_params.py">params</a>) -> <a href="./src/opencode_sdk/types/mcp/auth_authenticate_response.py">AuthAuthenticateResponse</a></code>
- <code title="post /mcp/{name}/auth/callback">client.mcp.auth.<a href="./src/opencode_sdk/resources/mcp/auth.py">complete</a>(name, \*\*<a href="src/opencode_sdk/types/mcp/auth_complete_params.py">params</a>) -> <a href="./src/opencode_sdk/types/mcp/auth_complete_response.py">AuthCompleteResponse</a></code>
- <code title="delete /mcp/{name}/auth">client.mcp.auth.<a href="./src/opencode_sdk/resources/mcp/auth.py">remove</a>(name, \*\*<a href="src/opencode_sdk/types/mcp/auth_remove_params.py">params</a>) -> <a href="./src/opencode_sdk/types/mcp/auth_remove_response.py">AuthRemoveResponse</a></code>
- <code title="post /mcp/{name}/auth">client.mcp.auth.<a href="./src/opencode_sdk/resources/mcp/auth.py">start</a>(name, \*\*<a href="src/opencode_sdk/types/mcp/auth_start_params.py">params</a>) -> <a href="./src/opencode_sdk/types/mcp/auth_start_response.py">AuthStartResponse</a></code>

# Tui

Types:

```python
from opencode_sdk.types import (
    TuiAppendPromptResponse,
    TuiClearPromptResponse,
    TuiExecuteCommandResponse,
    TuiOpenHelpResponse,
    TuiOpenModelsResponse,
    TuiOpenSessionsResponse,
    TuiOpenThemesResponse,
    TuiPublishEventResponse,
    TuiSelectSessionResponse,
    TuiShowToastResponse,
    TuiSubmitPromptResponse,
)
```

Methods:

- <code title="post /tui/append-prompt">client.tui.<a href="./src/opencode_sdk/resources/tui/tui.py">append_prompt</a>(\*\*<a href="src/opencode_sdk/types/tui_append_prompt_params.py">params</a>) -> <a href="./src/opencode_sdk/types/tui_append_prompt_response.py">TuiAppendPromptResponse</a></code>
- <code title="post /tui/clear-prompt">client.tui.<a href="./src/opencode_sdk/resources/tui/tui.py">clear_prompt</a>(\*\*<a href="src/opencode_sdk/types/tui_clear_prompt_params.py">params</a>) -> <a href="./src/opencode_sdk/types/tui_clear_prompt_response.py">TuiClearPromptResponse</a></code>
- <code title="post /tui/execute-command">client.tui.<a href="./src/opencode_sdk/resources/tui/tui.py">execute_command</a>(\*\*<a href="src/opencode_sdk/types/tui_execute_command_params.py">params</a>) -> <a href="./src/opencode_sdk/types/tui_execute_command_response.py">TuiExecuteCommandResponse</a></code>
- <code title="post /tui/open-help">client.tui.<a href="./src/opencode_sdk/resources/tui/tui.py">open_help</a>(\*\*<a href="src/opencode_sdk/types/tui_open_help_params.py">params</a>) -> <a href="./src/opencode_sdk/types/tui_open_help_response.py">TuiOpenHelpResponse</a></code>
- <code title="post /tui/open-models">client.tui.<a href="./src/opencode_sdk/resources/tui/tui.py">open_models</a>(\*\*<a href="src/opencode_sdk/types/tui_open_models_params.py">params</a>) -> <a href="./src/opencode_sdk/types/tui_open_models_response.py">TuiOpenModelsResponse</a></code>
- <code title="post /tui/open-sessions">client.tui.<a href="./src/opencode_sdk/resources/tui/tui.py">open_sessions</a>(\*\*<a href="src/opencode_sdk/types/tui_open_sessions_params.py">params</a>) -> <a href="./src/opencode_sdk/types/tui_open_sessions_response.py">TuiOpenSessionsResponse</a></code>
- <code title="post /tui/open-themes">client.tui.<a href="./src/opencode_sdk/resources/tui/tui.py">open_themes</a>(\*\*<a href="src/opencode_sdk/types/tui_open_themes_params.py">params</a>) -> <a href="./src/opencode_sdk/types/tui_open_themes_response.py">TuiOpenThemesResponse</a></code>
- <code title="post /tui/publish">client.tui.<a href="./src/opencode_sdk/resources/tui/tui.py">publish_event</a>(\*\*<a href="src/opencode_sdk/types/tui_publish_event_params.py">params</a>) -> <a href="./src/opencode_sdk/types/tui_publish_event_response.py">TuiPublishEventResponse</a></code>
- <code title="post /tui/select-session">client.tui.<a href="./src/opencode_sdk/resources/tui/tui.py">select_session</a>(\*\*<a href="src/opencode_sdk/types/tui_select_session_params.py">params</a>) -> <a href="./src/opencode_sdk/types/tui_select_session_response.py">TuiSelectSessionResponse</a></code>
- <code title="post /tui/show-toast">client.tui.<a href="./src/opencode_sdk/resources/tui/tui.py">show_toast</a>(\*\*<a href="src/opencode_sdk/types/tui_show_toast_params.py">params</a>) -> <a href="./src/opencode_sdk/types/tui_show_toast_response.py">TuiShowToastResponse</a></code>
- <code title="post /tui/submit-prompt">client.tui.<a href="./src/opencode_sdk/resources/tui/tui.py">submit_prompt</a>(\*\*<a href="src/opencode_sdk/types/tui_submit_prompt_params.py">params</a>) -> <a href="./src/opencode_sdk/types/tui_submit_prompt_response.py">TuiSubmitPromptResponse</a></code>

## Control

Types:

```python
from opencode_sdk.types.tui import ControlGetNextRequestResponse, ControlSubmitResponseResponse
```

Methods:

- <code title="get /tui/control/next">client.tui.control.<a href="./src/opencode_sdk/resources/tui/control.py">get_next_request</a>(\*\*<a href="src/opencode_sdk/types/tui/control_get_next_request_params.py">params</a>) -> <a href="./src/opencode_sdk/types/tui/control_get_next_request_response.py">ControlGetNextRequestResponse</a></code>
- <code title="post /tui/control/response">client.tui.control.<a href="./src/opencode_sdk/resources/tui/control.py">submit_response</a>(\*\*<a href="src/opencode_sdk/types/tui/control_submit_response_params.py">params</a>) -> <a href="./src/opencode_sdk/types/tui/control_submit_response_response.py">ControlSubmitResponseResponse</a></code>

# Auth

Types:

```python
from opencode_sdk.types import AuthSetCredentialsResponse
```

Methods:

- <code title="put /auth/{providerID}">client.auth.<a href="./src/opencode_sdk/resources/auth.py">set_credentials</a>(provider_id, \*\*<a href="src/opencode_sdk/types/auth_set_credentials_params.py">params</a>) -> <a href="./src/opencode_sdk/types/auth_set_credentials_response.py">AuthSetCredentialsResponse</a></code>

# Event

Types:

```python
from opencode_sdk.types import EventListResponse
```

Methods:

- <code title="get /event">client.event.<a href="./src/opencode_sdk/resources/event.py">list</a>(\*\*<a href="src/opencode_sdk/types/event_list_params.py">params</a>) -> <a href="./src/opencode_sdk/types/event_list_response.py">EventListResponse</a></code>

# Global

Types:

```python
from opencode_sdk.types import (
    GlobalDisposeInstanceResponse,
    GlobalGetHealthResponse,
    GlobalGetVersionResponse,
    GlobalRetrieveEventsResponse,
)
```

Methods:

- <code title="post /global/dispose">client.global*.<a href="./src/opencode_sdk/resources/global*.py">dispose_instance</a>() -> <a href="./src/opencode_sdk/types/global_dispose_instance_response.py">GlobalDisposeInstanceResponse</a></code>
- <code title="get /global/health">client.global*.<a href="./src/opencode_sdk/resources/global*.py">get_health</a>() -> <a href="./src/opencode_sdk/types/global_get_health_response.py">GlobalGetHealthResponse</a></code>
- <code title="get /global/version">client.global*.<a href="./src/opencode_sdk/resources/global*.py">get_version</a>() -> <a href="./src/opencode_sdk/types/global_get_version_response.py">GlobalGetVersionResponse</a></code>
- <code title="get /global/event">client.global*.<a href="./src/opencode_sdk/resources/global*.py">retrieve_events</a>() -> <a href="./src/opencode_sdk/types/global_retrieve_events_response.py">GlobalRetrieveEventsResponse</a></code>

# Pty

Types:

```python
from opencode_sdk.types import (
    PtyCreateResponse,
    PtyRetrieveResponse,
    PtyUpdateResponse,
    PtyListResponse,
    PtyDeleteResponse,
    PtyConnectResponse,
)
```

Methods:

- <code title="post /pty">client.pty.<a href="./src/opencode_sdk/resources/pty.py">create</a>(\*\*<a href="src/opencode_sdk/types/pty_create_params.py">params</a>) -> <a href="./src/opencode_sdk/types/pty_create_response.py">PtyCreateResponse</a></code>
- <code title="get /pty/{ptyID}">client.pty.<a href="./src/opencode_sdk/resources/pty.py">retrieve</a>(pty_id, \*\*<a href="src/opencode_sdk/types/pty_retrieve_params.py">params</a>) -> <a href="./src/opencode_sdk/types/pty_retrieve_response.py">PtyRetrieveResponse</a></code>
- <code title="put /pty/{ptyID}">client.pty.<a href="./src/opencode_sdk/resources/pty.py">update</a>(pty_id, \*\*<a href="src/opencode_sdk/types/pty_update_params.py">params</a>) -> <a href="./src/opencode_sdk/types/pty_update_response.py">PtyUpdateResponse</a></code>
- <code title="get /pty">client.pty.<a href="./src/opencode_sdk/resources/pty.py">list</a>(\*\*<a href="src/opencode_sdk/types/pty_list_params.py">params</a>) -> <a href="./src/opencode_sdk/types/pty_list_response.py">PtyListResponse</a></code>
- <code title="delete /pty/{ptyID}">client.pty.<a href="./src/opencode_sdk/resources/pty.py">delete</a>(pty_id, \*\*<a href="src/opencode_sdk/types/pty_delete_params.py">params</a>) -> <a href="./src/opencode_sdk/types/pty_delete_response.py">PtyDeleteResponse</a></code>
- <code title="get /pty/{ptyID}/connect">client.pty.<a href="./src/opencode_sdk/resources/pty.py">connect</a>(pty_id, \*\*<a href="src/opencode_sdk/types/pty_connect_params.py">params</a>) -> <a href="./src/opencode_sdk/types/pty_connect_response.py">PtyConnectResponse</a></code>

# Instance

Types:

```python
from opencode_sdk.types import InstanceDisposeResponse
```

Methods:

- <code title="post /instance/dispose">client.instance.<a href="./src/opencode_sdk/resources/instance.py">dispose</a>(\*\*<a href="src/opencode_sdk/types/instance_dispose_params.py">params</a>) -> <a href="./src/opencode_sdk/types/instance_dispose_response.py">InstanceDisposeResponse</a></code>

# Vcs

Types:

```python
from opencode_sdk.types import VcRetrieveResponse
```

Methods:

- <code title="get /vcs">client.vcs.<a href="./src/opencode_sdk/resources/vcs.py">retrieve</a>(\*\*<a href="src/opencode_sdk/types/vc_retrieve_params.py">params</a>) -> <a href="./src/opencode_sdk/types/vc_retrieve_response.py">VcRetrieveResponse</a></code>

# Provider

Types:

```python
from opencode_sdk.types import ProviderListResponse, ProviderGetAuthMethodsResponse
```

Methods:

- <code title="get /provider">client.provider.<a href="./src/opencode_sdk/resources/provider/provider.py">list</a>(\*\*<a href="src/opencode_sdk/types/provider_list_params.py">params</a>) -> <a href="./src/opencode_sdk/types/provider_list_response.py">ProviderListResponse</a></code>
- <code title="get /provider/auth">client.provider.<a href="./src/opencode_sdk/resources/provider/provider.py">get_auth_methods</a>(\*\*<a href="src/opencode_sdk/types/provider_get_auth_methods_params.py">params</a>) -> <a href="./src/opencode_sdk/types/provider_get_auth_methods_response.py">ProviderGetAuthMethodsResponse</a></code>

## OAuth

Types:

```python
from opencode_sdk.types.provider import OAuthAuthorizeResponse, OAuthHandleCallbackResponse
```

Methods:

- <code title="post /provider/{providerID}/oauth/authorize">client.provider.oauth.<a href="./src/opencode_sdk/resources/provider/oauth.py">authorize</a>(provider_id, \*\*<a href="src/opencode_sdk/types/provider/oauth_authorize_params.py">params</a>) -> <a href="./src/opencode_sdk/types/provider/oauth_authorize_response.py">OAuthAuthorizeResponse</a></code>
- <code title="post /provider/{providerID}/oauth/callback">client.provider.oauth.<a href="./src/opencode_sdk/resources/provider/oauth.py">handle_callback</a>(provider_id, \*\*<a href="src/opencode_sdk/types/provider/oauth_handle_callback_params.py">params</a>) -> <a href="./src/opencode_sdk/types/provider/oauth_handle_callback_response.py">OAuthHandleCallbackResponse</a></code>

## Custom

Types:

```python
from opencode_sdk.types.provider import (
    CustomCreateResponse,
    CustomListResponse,
    CustomDeleteResponse,
)
```

Methods:

- <code title="post /provider/custom">client.provider.custom.<a href="./src/opencode_sdk/resources/provider/custom.py">create</a>(\*\*<a href="src/opencode_sdk/types/provider/custom_create_params.py">params</a>) -> <a href="./src/opencode_sdk/types/provider/custom_create_response.py">CustomCreateResponse</a></code>
- <code title="get /provider/custom">client.provider.custom.<a href="./src/opencode_sdk/resources/provider/custom.py">list</a>(\*\*<a href="src/opencode_sdk/types/provider/custom_list_params.py">params</a>) -> <a href="./src/opencode_sdk/types/provider/custom_list_response.py">CustomListResponse</a></code>
- <code title="delete /provider/custom/{id}">client.provider.custom.<a href="./src/opencode_sdk/resources/provider/custom.py">delete</a>(id, \*\*<a href="src/opencode_sdk/types/provider/custom_delete_params.py">params</a>) -> <a href="./src/opencode_sdk/types/provider/custom_delete_response.py">CustomDeleteResponse</a></code>

# ClientTool

Types:

```python
from opencode_sdk.types import (
    ClientToolCreateResponse,
    ClientToolListResponse,
    ClientToolDeleteResponse,
)
```

Methods:

- <code title="post /client-tool">client.client_tool.<a href="./src/opencode_sdk/resources/client_tool.py">create</a>(\*\*<a href="src/opencode_sdk/types/client_tool_create_params.py">params</a>) -> <a href="./src/opencode_sdk/types/client_tool_create_response.py">ClientToolCreateResponse</a></code>
- <code title="get /client-tool">client.client_tool.<a href="./src/opencode_sdk/resources/client_tool.py">list</a>(\*\*<a href="src/opencode_sdk/types/client_tool_list_params.py">params</a>) -> <a href="./src/opencode_sdk/types/client_tool_list_response.py">ClientToolListResponse</a></code>
- <code title="delete /client-tool/{id}">client.client_tool.<a href="./src/opencode_sdk/resources/client_tool.py">delete</a>(id, \*\*<a href="src/opencode_sdk/types/client_tool_delete_params.py">params</a>) -> <a href="./src/opencode_sdk/types/client_tool_delete_response.py">ClientToolDeleteResponse</a></code>

# Lsp

Types:

```python
from opencode_sdk.types import LspRetrieveStatusResponse
```

Methods:

- <code title="get /lsp">client.lsp.<a href="./src/opencode_sdk/resources/lsp.py">retrieve_status</a>(\*\*<a href="src/opencode_sdk/types/lsp_retrieve_status_params.py">params</a>) -> <a href="./src/opencode_sdk/types/lsp_retrieve_status_response.py">LspRetrieveStatusResponse</a></code>

# Formatter

Types:

```python
from opencode_sdk.types import FormatterRetrieveResponse
```

Methods:

- <code title="get /formatter">client.formatter.<a href="./src/opencode_sdk/resources/formatter.py">retrieve</a>(\*\*<a href="src/opencode_sdk/types/formatter_retrieve_params.py">params</a>) -> <a href="./src/opencode_sdk/types/formatter_retrieve_response.py">FormatterRetrieveResponse</a></code>

# Permission

Types:

```python
from opencode_sdk.types import PermissionListResponse, PermissionReplyResponse
```

Methods:

- <code title="get /permission">client.permission.<a href="./src/opencode_sdk/resources/permission.py">list</a>(\*\*<a href="src/opencode_sdk/types/permission_list_params.py">params</a>) -> <a href="./src/opencode_sdk/types/permission_list_response.py">PermissionListResponse</a></code>
- <code title="post /permission/{requestID}/reply">client.permission.<a href="./src/opencode_sdk/resources/permission.py">reply</a>(request_id, \*\*<a href="src/opencode_sdk/types/permission_reply_params.py">params</a>) -> <a href="./src/opencode_sdk/types/permission_reply_response.py">PermissionReplyResponse</a></code>

# Question

Types:

```python
from opencode_sdk.types import (
    QuestionListPendingResponse,
    QuestionRejectResponse,
    QuestionReplyResponse,
)
```

Methods:

- <code title="get /question">client.question.<a href="./src/opencode_sdk/resources/question.py">list_pending</a>(\*\*<a href="src/opencode_sdk/types/question_list_pending_params.py">params</a>) -> <a href="./src/opencode_sdk/types/question_list_pending_response.py">QuestionListPendingResponse</a></code>
- <code title="post /question/{requestID}/reject">client.question.<a href="./src/opencode_sdk/resources/question.py">reject</a>(request_id, \*\*<a href="src/opencode_sdk/types/question_reject_params.py">params</a>) -> <a href="./src/opencode_sdk/types/question_reject_response.py">QuestionRejectResponse</a></code>
- <code title="post /question/{requestID}/reply">client.question.<a href="./src/opencode_sdk/resources/question.py">reply</a>(request_id, \*\*<a href="src/opencode_sdk/types/question_reply_params.py">params</a>) -> <a href="./src/opencode_sdk/types/question_reply_response.py">QuestionReplyResponse</a></code>

# Artifact

Types:

```python
from opencode_sdk.types import ArtifactDeleteResponse
```

Methods:

- <code title="delete /artifact/{artifactID}">client.artifact.<a href="./src/opencode_sdk/resources/artifact.py">delete</a>(artifact_id, \*\*<a href="src/opencode_sdk/types/artifact_delete_params.py">params</a>) -> <a href="./src/opencode_sdk/types/artifact_delete_response.py">ArtifactDeleteResponse</a></code>
- <code title="get /artifact/{artifactID}/download">client.artifact.<a href="./src/opencode_sdk/resources/artifact.py">download</a>(artifact_id, \*\*<a href="src/opencode_sdk/types/artifact_download_params.py">params</a>) -> BinaryAPIResponse</code>

# Skill

Types:

```python
from opencode_sdk.types import SkillListResponse
```

Methods:

- <code title="get /skill">client.skill.<a href="./src/opencode_sdk/resources/skill.py">list</a>(\*\*<a href="src/opencode_sdk/types/skill_list_params.py">params</a>) -> <a href="./src/opencode_sdk/types/skill_list_response.py">SkillListResponse</a></code>
