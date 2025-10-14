# Project

Types:

```python
from opencode_sdk.types import Project, ProjectListResponse
```

Methods:

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

## Tool

Types:

```python
from opencode_sdk.types.experimental import ToolListIDsResponse, ToolListToolsResponse
```

Methods:

- <code title="get /experimental/tool/ids">client.experimental.tool.<a href="./src/opencode_sdk/resources/experimental/tool.py">list_ids</a>(\*\*<a href="src/opencode_sdk/types/experimental/tool_list_ids_params.py">params</a>) -> <a href="./src/opencode_sdk/types/experimental/tool_list_ids_response.py">ToolListIDsResponse</a></code>
- <code title="get /experimental/tool">client.experimental.tool.<a href="./src/opencode_sdk/resources/experimental/tool.py">list_tools</a>(\*\*<a href="src/opencode_sdk/types/experimental/tool_list_tools_params.py">params</a>) -> <a href="./src/opencode_sdk/types/experimental/tool_list_tools_response.py">ToolListToolsResponse</a></code>

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
    SessionAnalyzeResponse,
    SessionGetChildrenResponse,
    SessionGetTodoResponse,
    SessionRespondToPermissionResponse,
    SessionSendCommandResponse,
    SessionSummarizeResponse,
)
```

Methods:

- <code title="post /session">client.session.<a href="./src/opencode_sdk/resources/session/session.py">create</a>(\*\*<a href="src/opencode_sdk/types/session_create_params.py">params</a>) -> <a href="./src/opencode_sdk/types/session/session.py">Session</a></code>
- <code title="get /session/{id}">client.session.<a href="./src/opencode_sdk/resources/session/session.py">retrieve</a>(id, \*\*<a href="src/opencode_sdk/types/session_retrieve_params.py">params</a>) -> <a href="./src/opencode_sdk/types/session/session.py">Session</a></code>
- <code title="patch /session/{id}">client.session.<a href="./src/opencode_sdk/resources/session/session.py">update</a>(id, \*\*<a href="src/opencode_sdk/types/session_update_params.py">params</a>) -> <a href="./src/opencode_sdk/types/session/session.py">Session</a></code>
- <code title="get /session">client.session.<a href="./src/opencode_sdk/resources/session/session.py">list</a>(\*\*<a href="src/opencode_sdk/types/session_list_params.py">params</a>) -> <a href="./src/opencode_sdk/types/session_list_response.py">SessionListResponse</a></code>
- <code title="delete /session/{id}">client.session.<a href="./src/opencode_sdk/resources/session/session.py">delete</a>(id, \*\*<a href="src/opencode_sdk/types/session_delete_params.py">params</a>) -> <a href="./src/opencode_sdk/types/session_delete_response.py">SessionDeleteResponse</a></code>
- <code title="post /session/{id}/abort">client.session.<a href="./src/opencode_sdk/resources/session/session.py">abort</a>(id, \*\*<a href="src/opencode_sdk/types/session_abort_params.py">params</a>) -> <a href="./src/opencode_sdk/types/session_abort_response.py">SessionAbortResponse</a></code>
- <code title="post /session/{id}/init">client.session.<a href="./src/opencode_sdk/resources/session/session.py">analyze</a>(id, \*\*<a href="src/opencode_sdk/types/session_analyze_params.py">params</a>) -> <a href="./src/opencode_sdk/types/session_analyze_response.py">SessionAnalyzeResponse</a></code>
- <code title="post /session/{id}/fork">client.session.<a href="./src/opencode_sdk/resources/session/session.py">fork</a>(id, \*\*<a href="src/opencode_sdk/types/session_fork_params.py">params</a>) -> <a href="./src/opencode_sdk/types/session/session.py">Session</a></code>
- <code title="get /session/{id}/children">client.session.<a href="./src/opencode_sdk/resources/session/session.py">get_children</a>(id, \*\*<a href="src/opencode_sdk/types/session_get_children_params.py">params</a>) -> <a href="./src/opencode_sdk/types/session_get_children_response.py">SessionGetChildrenResponse</a></code>
- <code title="get /session/{id}/todo">client.session.<a href="./src/opencode_sdk/resources/session/session.py">get_todo</a>(id, \*\*<a href="src/opencode_sdk/types/session_get_todo_params.py">params</a>) -> <a href="./src/opencode_sdk/types/session_get_todo_response.py">SessionGetTodoResponse</a></code>
- <code title="post /session/{id}/permissions/{permissionID}">client.session.<a href="./src/opencode_sdk/resources/session/session.py">respond_to_permission</a>(permission_id, \*, id, \*\*<a href="src/opencode_sdk/types/session_respond_to_permission_params.py">params</a>) -> <a href="./src/opencode_sdk/types/session_respond_to_permission_response.py">SessionRespondToPermissionResponse</a></code>
- <code title="post /session/{id}/unrevert">client.session.<a href="./src/opencode_sdk/resources/session/session.py">restore_reverted</a>(id, \*\*<a href="src/opencode_sdk/types/session_restore_reverted_params.py">params</a>) -> <a href="./src/opencode_sdk/types/session/session.py">Session</a></code>
- <code title="post /session/{id}/revert">client.session.<a href="./src/opencode_sdk/resources/session/session.py">revert</a>(id, \*\*<a href="src/opencode_sdk/types/session_revert_params.py">params</a>) -> <a href="./src/opencode_sdk/types/session/session.py">Session</a></code>
- <code title="post /session/{id}/shell">client.session.<a href="./src/opencode_sdk/resources/session/session.py">run_shell</a>(id, \*\*<a href="src/opencode_sdk/types/session_run_shell_params.py">params</a>) -> <a href="./src/opencode_sdk/types/assistant_message.py">AssistantMessage</a></code>
- <code title="post /session/{id}/command">client.session.<a href="./src/opencode_sdk/resources/session/session.py">send_command</a>(id, \*\*<a href="src/opencode_sdk/types/session_send_command_params.py">params</a>) -> <a href="./src/opencode_sdk/types/session_send_command_response.py">SessionSendCommandResponse</a></code>
- <code title="post /session/{id}/summarize">client.session.<a href="./src/opencode_sdk/resources/session/session.py">summarize</a>(id, \*\*<a href="src/opencode_sdk/types/session_summarize_params.py">params</a>) -> <a href="./src/opencode_sdk/types/session_summarize_response.py">SessionSummarizeResponse</a></code>

## Share

Methods:

- <code title="post /session/{id}/share">client.session.share.<a href="./src/opencode_sdk/resources/session/share.py">create</a>(id, \*\*<a href="src/opencode_sdk/types/session/share_create_params.py">params</a>) -> <a href="./src/opencode_sdk/types/session/session.py">Session</a></code>
- <code title="delete /session/{id}/share">client.session.share.<a href="./src/opencode_sdk/resources/session/share.py">delete</a>(id, \*\*<a href="src/opencode_sdk/types/session/share_delete_params.py">params</a>) -> <a href="./src/opencode_sdk/types/session/session.py">Session</a></code>

## Message

Types:

```python
from opencode_sdk.types.session import (
    FilePart,
    FilePartSource,
    FilePartSourceText,
    Message,
    Part,
    MessageCreateResponse,
    MessageRetrieveResponse,
    MessageListResponse,
)
```

Methods:

- <code title="post /session/{id}/message">client.session.message.<a href="./src/opencode_sdk/resources/session/message.py">create</a>(id, \*\*<a href="src/opencode_sdk/types/session/message_create_params.py">params</a>) -> <a href="./src/opencode_sdk/types/session/message_create_response.py">MessageCreateResponse</a></code>
- <code title="get /session/{id}/message/{messageID}">client.session.message.<a href="./src/opencode_sdk/resources/session/message.py">retrieve</a>(message_id, \*, id, \*\*<a href="src/opencode_sdk/types/session/message_retrieve_params.py">params</a>) -> <a href="./src/opencode_sdk/types/session/message_retrieve_response.py">MessageRetrieveResponse</a></code>
- <code title="get /session/{id}/message">client.session.message.<a href="./src/opencode_sdk/resources/session/message.py">list</a>(id, \*\*<a href="src/opencode_sdk/types/session/message_list_params.py">params</a>) -> <a href="./src/opencode_sdk/types/session/message_list_response.py">MessageListResponse</a></code>

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
from opencode_sdk.types import AgentListResponse
```

Methods:

- <code title="get /agent">client.agent.<a href="./src/opencode_sdk/resources/agent.py">list</a>(\*\*<a href="src/opencode_sdk/types/agent_list_params.py">params</a>) -> <a href="./src/opencode_sdk/types/agent_list_response.py">AgentListResponse</a></code>

# Mcp

Methods:

- <code title="get /mcp">client.mcp.<a href="./src/opencode_sdk/resources/mcp.py">retrieve</a>(\*\*<a href="src/opencode_sdk/types/mcp_retrieve_params.py">params</a>) -> object</code>

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
    TuiShowToastResponse,
    TuiSubmitPromptResponse,
)
```

Methods:

- <code title="post /tui/append-prompt">client.tui.<a href="./src/opencode_sdk/resources/tui.py">append_prompt</a>(\*\*<a href="src/opencode_sdk/types/tui_append_prompt_params.py">params</a>) -> <a href="./src/opencode_sdk/types/tui_append_prompt_response.py">TuiAppendPromptResponse</a></code>
- <code title="post /tui/clear-prompt">client.tui.<a href="./src/opencode_sdk/resources/tui.py">clear_prompt</a>(\*\*<a href="src/opencode_sdk/types/tui_clear_prompt_params.py">params</a>) -> <a href="./src/opencode_sdk/types/tui_clear_prompt_response.py">TuiClearPromptResponse</a></code>
- <code title="post /tui/execute-command">client.tui.<a href="./src/opencode_sdk/resources/tui.py">execute_command</a>(\*\*<a href="src/opencode_sdk/types/tui_execute_command_params.py">params</a>) -> <a href="./src/opencode_sdk/types/tui_execute_command_response.py">TuiExecuteCommandResponse</a></code>
- <code title="post /tui/open-help">client.tui.<a href="./src/opencode_sdk/resources/tui.py">open_help</a>(\*\*<a href="src/opencode_sdk/types/tui_open_help_params.py">params</a>) -> <a href="./src/opencode_sdk/types/tui_open_help_response.py">TuiOpenHelpResponse</a></code>
- <code title="post /tui/open-models">client.tui.<a href="./src/opencode_sdk/resources/tui.py">open_models</a>(\*\*<a href="src/opencode_sdk/types/tui_open_models_params.py">params</a>) -> <a href="./src/opencode_sdk/types/tui_open_models_response.py">TuiOpenModelsResponse</a></code>
- <code title="post /tui/open-sessions">client.tui.<a href="./src/opencode_sdk/resources/tui.py">open_sessions</a>(\*\*<a href="src/opencode_sdk/types/tui_open_sessions_params.py">params</a>) -> <a href="./src/opencode_sdk/types/tui_open_sessions_response.py">TuiOpenSessionsResponse</a></code>
- <code title="post /tui/open-themes">client.tui.<a href="./src/opencode_sdk/resources/tui.py">open_themes</a>(\*\*<a href="src/opencode_sdk/types/tui_open_themes_params.py">params</a>) -> <a href="./src/opencode_sdk/types/tui_open_themes_response.py">TuiOpenThemesResponse</a></code>
- <code title="post /tui/show-toast">client.tui.<a href="./src/opencode_sdk/resources/tui.py">show_toast</a>(\*\*<a href="src/opencode_sdk/types/tui_show_toast_params.py">params</a>) -> <a href="./src/opencode_sdk/types/tui_show_toast_response.py">TuiShowToastResponse</a></code>
- <code title="post /tui/submit-prompt">client.tui.<a href="./src/opencode_sdk/resources/tui.py">submit_prompt</a>(\*\*<a href="src/opencode_sdk/types/tui_submit_prompt_params.py">params</a>) -> <a href="./src/opencode_sdk/types/tui_submit_prompt_response.py">TuiSubmitPromptResponse</a></code>

# Auth

Types:

```python
from opencode_sdk.types import AuthUpdateCredentialsResponse
```

Methods:

- <code title="put /auth/{id}">client.auth.<a href="./src/opencode_sdk/resources/auth.py">update_credentials</a>(id, \*\*<a href="src/opencode_sdk/types/auth_update_credentials_params.py">params</a>) -> <a href="./src/opencode_sdk/types/auth_update_credentials_response.py">AuthUpdateCredentialsResponse</a></code>

# Event

Types:

```python
from opencode_sdk.types import EventListResponse
```

Methods:

- <code title="get /event">client.event.<a href="./src/opencode_sdk/resources/event.py">list</a>(\*\*<a href="src/opencode_sdk/types/event_list_params.py">params</a>) -> <a href="./src/opencode_sdk/types/event_list_response.py">EventListResponse</a></code>
