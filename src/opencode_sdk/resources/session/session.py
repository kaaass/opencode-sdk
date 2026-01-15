# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import typing_extensions
from typing import Any, Dict, Iterable, cast
from typing_extensions import Literal

import httpx

from .share import (
    ShareResource,
    AsyncShareResource,
    ShareResourceWithRawResponse,
    AsyncShareResourceWithRawResponse,
    ShareResourceWithStreamingResponse,
    AsyncShareResourceWithStreamingResponse,
)
from ...types import (
    session_fork_params,
    session_list_params,
    session_abort_params,
    session_create_params,
    session_delete_params,
    session_update_params,
    session_get_diff_params,
    session_get_todo_params,
    session_retrieve_params,
    session_summarize_params,
    session_get_status_params,
    session_initialize_params,
    session_get_children_params,
    session_send_command_params,
    session_revert_message_params,
    session_retrieve_status_params,
    session_run_shell_command_params,
    session_send_async_message_params,
    session_submit_tool_results_params,
    session_respond_to_permission_params,
    session_restore_reverted_messages_params,
)
from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from .message.message import (
    MessageResource,
    AsyncMessageResource,
    MessageResourceWithRawResponse,
    AsyncMessageResourceWithRawResponse,
    MessageResourceWithStreamingResponse,
    AsyncMessageResourceWithStreamingResponse,
)
from ...types.session.session import Session
from ...types.assistant_message import AssistantMessage
from ...types.session_list_response import SessionListResponse
from ...types.session_abort_response import SessionAbortResponse
from ...types.session_delete_response import SessionDeleteResponse
from ...types.session_get_diff_response import SessionGetDiffResponse
from ...types.session_get_todo_response import SessionGetTodoResponse
from ...types.session_summarize_response import SessionSummarizeResponse
from ...types.session_get_status_response import SessionGetStatusResponse
from ...types.session_initialize_response import SessionInitializeResponse
from ...types.session_get_children_response import SessionGetChildrenResponse
from ...types.session_send_command_response import SessionSendCommandResponse
from ...types.session_retrieve_status_response import SessionRetrieveStatusResponse
from ...types.session_submit_tool_results_response import SessionSubmitToolResultsResponse
from ...types.session_respond_to_permission_response import SessionRespondToPermissionResponse

__all__ = ["SessionResource", "AsyncSessionResource"]


class SessionResource(SyncAPIResource):
    @cached_property
    def share(self) -> ShareResource:
        return ShareResource(self._client)

    @cached_property
    def message(self) -> MessageResource:
        return MessageResource(self._client)

    @cached_property
    def with_raw_response(self) -> SessionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kaaass/opencode-sdk#accessing-raw-response-data-eg-headers
        """
        return SessionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SessionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kaaass/opencode-sdk#with_streaming_response
        """
        return SessionResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        directory: str | Omit = omit,
        parent_id: str | Omit = omit,
        permission: Iterable[session_create_params.Permission] | Omit = omit,
        title: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Session:
        """
        Create a new OpenCode session for interacting with AI assistants and managing
        conversations.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/session",
            body=maybe_transform(
                {
                    "parent_id": parent_id,
                    "permission": permission,
                    "title": title,
                },
                session_create_params.SessionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"directory": directory}, session_create_params.SessionCreateParams),
            ),
            cast_to=Session,
        )

    def retrieve(
        self,
        session_id: str,
        *,
        directory: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Session:
        """
        Retrieve detailed information about a specific OpenCode session.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._get(
            f"/session/{session_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"directory": directory}, session_retrieve_params.SessionRetrieveParams),
            ),
            cast_to=Session,
        )

    def update(
        self,
        session_id: str,
        *,
        directory: str | Omit = omit,
        time: session_update_params.Time | Omit = omit,
        title: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Session:
        """
        Update properties of an existing session, such as title or other metadata.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._patch(
            f"/session/{session_id}",
            body=maybe_transform(
                {
                    "time": time,
                    "title": title,
                },
                session_update_params.SessionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"directory": directory}, session_update_params.SessionUpdateParams),
            ),
            cast_to=Session,
        )

    def list(
        self,
        *,
        directory: str | Omit = omit,
        limit: float | Omit = omit,
        search: str | Omit = omit,
        start: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionListResponse:
        """
        Get a list of all OpenCode sessions, sorted by most recently updated.

        Args:
          limit: Maximum number of sessions to return

          search: Filter sessions by title (case-insensitive)

          start: Filter sessions updated on or after this timestamp (milliseconds since epoch)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/session",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "directory": directory,
                        "limit": limit,
                        "search": search,
                        "start": start,
                    },
                    session_list_params.SessionListParams,
                ),
            ),
            cast_to=SessionListResponse,
        )

    def delete(
        self,
        session_id: str,
        *,
        directory: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionDeleteResponse:
        """
        Delete a session and permanently remove all associated data, including messages
        and history.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._delete(
            f"/session/{session_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"directory": directory}, session_delete_params.SessionDeleteParams),
            ),
            cast_to=SessionDeleteResponse,
        )

    def abort(
        self,
        session_id: str,
        *,
        directory: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionAbortResponse:
        """
        Abort an active session and stop any ongoing AI processing or command execution.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._post(
            f"/session/{session_id}/abort",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"directory": directory}, session_abort_params.SessionAbortParams),
            ),
            cast_to=SessionAbortResponse,
        )

    def fork(
        self,
        session_id: str,
        *,
        directory: str | Omit = omit,
        message_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Session:
        """
        Create a new session by forking an existing session at a specific message point.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._post(
            f"/session/{session_id}/fork",
            body=maybe_transform({"message_id": message_id}, session_fork_params.SessionForkParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"directory": directory}, session_fork_params.SessionForkParams),
            ),
            cast_to=Session,
        )

    def get_children(
        self,
        session_id: str,
        *,
        directory: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionGetChildrenResponse:
        """
        Retrieve all child sessions that were forked from the specified parent session.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._get(
            f"/session/{session_id}/children",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"directory": directory}, session_get_children_params.SessionGetChildrenParams),
            ),
            cast_to=SessionGetChildrenResponse,
        )

    def get_diff(
        self,
        session_id: str,
        *,
        directory: str | Omit = omit,
        message_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionGetDiffResponse:
        """
        Get all file changes (diffs) made during this session.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._get(
            f"/session/{session_id}/diff",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "directory": directory,
                        "message_id": message_id,
                    },
                    session_get_diff_params.SessionGetDiffParams,
                ),
            ),
            cast_to=SessionGetDiffResponse,
        )

    def get_status(
        self,
        *,
        directory: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionGetStatusResponse:
        """
        Retrieve the current status of all sessions, including active, idle, and
        completed states.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/session/status",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"directory": directory}, session_get_status_params.SessionGetStatusParams),
            ),
            cast_to=SessionGetStatusResponse,
        )

    def get_todo(
        self,
        session_id: str,
        *,
        directory: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionGetTodoResponse:
        """
        Retrieve the todo list associated with a specific session, showing tasks and
        action items.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._get(
            f"/session/{session_id}/todo",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"directory": directory}, session_get_todo_params.SessionGetTodoParams),
            ),
            cast_to=SessionGetTodoResponse,
        )

    def initialize(
        self,
        session_id: str,
        *,
        message_id: str,
        model_id: str,
        provider_id: str,
        directory: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionInitializeResponse:
        """
        Analyze the current application and create an AGENTS.md file with
        project-specific agent configurations.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._post(
            f"/session/{session_id}/init",
            body=maybe_transform(
                {
                    "message_id": message_id,
                    "model_id": model_id,
                    "provider_id": provider_id,
                },
                session_initialize_params.SessionInitializeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"directory": directory}, session_initialize_params.SessionInitializeParams),
            ),
            cast_to=SessionInitializeResponse,
        )

    @typing_extensions.deprecated("deprecated")
    def respond_to_permission(
        self,
        permission_id: str,
        *,
        session_id: str,
        response: Literal["once", "always", "reject"],
        directory: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionRespondToPermissionResponse:
        """
        Approve or deny a permission request from the AI assistant.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        if not permission_id:
            raise ValueError(f"Expected a non-empty value for `permission_id` but received {permission_id!r}")
        return self._post(
            f"/session/{session_id}/permissions/{permission_id}",
            body=maybe_transform(
                {"response": response}, session_respond_to_permission_params.SessionRespondToPermissionParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"directory": directory}, session_respond_to_permission_params.SessionRespondToPermissionParams
                ),
            ),
            cast_to=SessionRespondToPermissionResponse,
        )

    def restore_reverted_messages(
        self,
        session_id: str,
        *,
        directory: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Session:
        """
        Restore all previously reverted messages in a session.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._post(
            f"/session/{session_id}/unrevert",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"directory": directory},
                    session_restore_reverted_messages_params.SessionRestoreRevertedMessagesParams,
                ),
            ),
            cast_to=Session,
        )

    def retrieve_status(
        self,
        session_id: str,
        *,
        directory: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionRetrieveStatusResponse:
        """
        Retrieve the current status of a specific session (idle, busy, retry, or
        wait-tool-result).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return cast(
            SessionRetrieveStatusResponse,
            self._get(
                f"/session/{session_id}/status",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=maybe_transform(
                        {"directory": directory}, session_retrieve_status_params.SessionRetrieveStatusParams
                    ),
                ),
                cast_to=cast(
                    Any, SessionRetrieveStatusResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def revert_message(
        self,
        session_id: str,
        *,
        message_id: str,
        directory: str | Omit = omit,
        part_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Session:
        """
        Revert a specific message in a session, undoing its effects and restoring the
        previous state.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._post(
            f"/session/{session_id}/revert",
            body=maybe_transform(
                {
                    "message_id": message_id,
                    "part_id": part_id,
                },
                session_revert_message_params.SessionRevertMessageParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"directory": directory}, session_revert_message_params.SessionRevertMessageParams
                ),
            ),
            cast_to=Session,
        )

    def run_shell_command(
        self,
        session_id: str,
        *,
        agent: str,
        command: str,
        directory: str | Omit = omit,
        model: session_run_shell_command_params.Model | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AssistantMessage:
        """
        Execute a shell command within the session context and return the AI's response.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._post(
            f"/session/{session_id}/shell",
            body=maybe_transform(
                {
                    "agent": agent,
                    "command": command,
                    "model": model,
                },
                session_run_shell_command_params.SessionRunShellCommandParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"directory": directory}, session_run_shell_command_params.SessionRunShellCommandParams
                ),
            ),
            cast_to=AssistantMessage,
        )

    def send_async_message(
        self,
        session_id: str,
        *,
        parts: Iterable[session_send_async_message_params.Part],
        directory: str | Omit = omit,
        agent: str | Omit = omit,
        message_id: str | Omit = omit,
        model: session_send_async_message_params.Model | Omit = omit,
        no_reply: bool | Omit = omit,
        system: str | Omit = omit,
        tools: Dict[str, bool] | Omit = omit,
        variant: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Create and send a new message to a session asynchronously, starting the session
        if needed and returning immediately.

        Args:
          tools: @deprecated tools and permissions have been merged, you can set permissions on
              the session itself now

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/session/{session_id}/prompt_async",
            body=maybe_transform(
                {
                    "parts": parts,
                    "agent": agent,
                    "message_id": message_id,
                    "model": model,
                    "no_reply": no_reply,
                    "system": system,
                    "tools": tools,
                    "variant": variant,
                },
                session_send_async_message_params.SessionSendAsyncMessageParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"directory": directory}, session_send_async_message_params.SessionSendAsyncMessageParams
                ),
            ),
            cast_to=NoneType,
        )

    def send_command(
        self,
        session_id: str,
        *,
        arguments: str,
        command: str,
        directory: str | Omit = omit,
        agent: str | Omit = omit,
        message_id: str | Omit = omit,
        model: str | Omit = omit,
        parts: Iterable[session_send_command_params.Part] | Omit = omit,
        variant: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionSendCommandResponse:
        """
        Send a new command to a session for execution by the AI assistant.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._post(
            f"/session/{session_id}/command",
            body=maybe_transform(
                {
                    "arguments": arguments,
                    "command": command,
                    "agent": agent,
                    "message_id": message_id,
                    "model": model,
                    "parts": parts,
                    "variant": variant,
                },
                session_send_command_params.SessionSendCommandParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"directory": directory}, session_send_command_params.SessionSendCommandParams),
            ),
            cast_to=SessionSendCommandResponse,
        )

    def submit_tool_results(
        self,
        session_id: str,
        *,
        results: Iterable[session_submit_tool_results_params.Result],
        directory: str | Omit = omit,
        async_: bool | Omit = omit,
        continue_loop: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionSubmitToolResultsResponse:
        """
        Submit results for remote tools that are waiting for external execution, and
        optionally continue the inference loop.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._post(
            f"/session/{session_id}/tool-results",
            body=maybe_transform(
                {
                    "results": results,
                    "async_": async_,
                    "continue_loop": continue_loop,
                },
                session_submit_tool_results_params.SessionSubmitToolResultsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"directory": directory}, session_submit_tool_results_params.SessionSubmitToolResultsParams
                ),
            ),
            cast_to=SessionSubmitToolResultsResponse,
        )

    def summarize(
        self,
        session_id: str,
        *,
        model_id: str,
        provider_id: str,
        directory: str | Omit = omit,
        auto: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionSummarizeResponse:
        """
        Generate a concise summary of the session using AI compaction to preserve key
        information.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._post(
            f"/session/{session_id}/summarize",
            body=maybe_transform(
                {
                    "model_id": model_id,
                    "provider_id": provider_id,
                    "auto": auto,
                },
                session_summarize_params.SessionSummarizeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"directory": directory}, session_summarize_params.SessionSummarizeParams),
            ),
            cast_to=SessionSummarizeResponse,
        )


class AsyncSessionResource(AsyncAPIResource):
    @cached_property
    def share(self) -> AsyncShareResource:
        return AsyncShareResource(self._client)

    @cached_property
    def message(self) -> AsyncMessageResource:
        return AsyncMessageResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSessionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kaaass/opencode-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncSessionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSessionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kaaass/opencode-sdk#with_streaming_response
        """
        return AsyncSessionResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        directory: str | Omit = omit,
        parent_id: str | Omit = omit,
        permission: Iterable[session_create_params.Permission] | Omit = omit,
        title: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Session:
        """
        Create a new OpenCode session for interacting with AI assistants and managing
        conversations.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/session",
            body=await async_maybe_transform(
                {
                    "parent_id": parent_id,
                    "permission": permission,
                    "title": title,
                },
                session_create_params.SessionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"directory": directory}, session_create_params.SessionCreateParams),
            ),
            cast_to=Session,
        )

    async def retrieve(
        self,
        session_id: str,
        *,
        directory: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Session:
        """
        Retrieve detailed information about a specific OpenCode session.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._get(
            f"/session/{session_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"directory": directory}, session_retrieve_params.SessionRetrieveParams
                ),
            ),
            cast_to=Session,
        )

    async def update(
        self,
        session_id: str,
        *,
        directory: str | Omit = omit,
        time: session_update_params.Time | Omit = omit,
        title: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Session:
        """
        Update properties of an existing session, such as title or other metadata.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._patch(
            f"/session/{session_id}",
            body=await async_maybe_transform(
                {
                    "time": time,
                    "title": title,
                },
                session_update_params.SessionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"directory": directory}, session_update_params.SessionUpdateParams),
            ),
            cast_to=Session,
        )

    async def list(
        self,
        *,
        directory: str | Omit = omit,
        limit: float | Omit = omit,
        search: str | Omit = omit,
        start: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionListResponse:
        """
        Get a list of all OpenCode sessions, sorted by most recently updated.

        Args:
          limit: Maximum number of sessions to return

          search: Filter sessions by title (case-insensitive)

          start: Filter sessions updated on or after this timestamp (milliseconds since epoch)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/session",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "directory": directory,
                        "limit": limit,
                        "search": search,
                        "start": start,
                    },
                    session_list_params.SessionListParams,
                ),
            ),
            cast_to=SessionListResponse,
        )

    async def delete(
        self,
        session_id: str,
        *,
        directory: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionDeleteResponse:
        """
        Delete a session and permanently remove all associated data, including messages
        and history.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._delete(
            f"/session/{session_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"directory": directory}, session_delete_params.SessionDeleteParams),
            ),
            cast_to=SessionDeleteResponse,
        )

    async def abort(
        self,
        session_id: str,
        *,
        directory: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionAbortResponse:
        """
        Abort an active session and stop any ongoing AI processing or command execution.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._post(
            f"/session/{session_id}/abort",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"directory": directory}, session_abort_params.SessionAbortParams),
            ),
            cast_to=SessionAbortResponse,
        )

    async def fork(
        self,
        session_id: str,
        *,
        directory: str | Omit = omit,
        message_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Session:
        """
        Create a new session by forking an existing session at a specific message point.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._post(
            f"/session/{session_id}/fork",
            body=await async_maybe_transform({"message_id": message_id}, session_fork_params.SessionForkParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"directory": directory}, session_fork_params.SessionForkParams),
            ),
            cast_to=Session,
        )

    async def get_children(
        self,
        session_id: str,
        *,
        directory: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionGetChildrenResponse:
        """
        Retrieve all child sessions that were forked from the specified parent session.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._get(
            f"/session/{session_id}/children",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"directory": directory}, session_get_children_params.SessionGetChildrenParams
                ),
            ),
            cast_to=SessionGetChildrenResponse,
        )

    async def get_diff(
        self,
        session_id: str,
        *,
        directory: str | Omit = omit,
        message_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionGetDiffResponse:
        """
        Get all file changes (diffs) made during this session.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._get(
            f"/session/{session_id}/diff",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "directory": directory,
                        "message_id": message_id,
                    },
                    session_get_diff_params.SessionGetDiffParams,
                ),
            ),
            cast_to=SessionGetDiffResponse,
        )

    async def get_status(
        self,
        *,
        directory: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionGetStatusResponse:
        """
        Retrieve the current status of all sessions, including active, idle, and
        completed states.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/session/status",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"directory": directory}, session_get_status_params.SessionGetStatusParams
                ),
            ),
            cast_to=SessionGetStatusResponse,
        )

    async def get_todo(
        self,
        session_id: str,
        *,
        directory: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionGetTodoResponse:
        """
        Retrieve the todo list associated with a specific session, showing tasks and
        action items.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._get(
            f"/session/{session_id}/todo",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"directory": directory}, session_get_todo_params.SessionGetTodoParams
                ),
            ),
            cast_to=SessionGetTodoResponse,
        )

    async def initialize(
        self,
        session_id: str,
        *,
        message_id: str,
        model_id: str,
        provider_id: str,
        directory: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionInitializeResponse:
        """
        Analyze the current application and create an AGENTS.md file with
        project-specific agent configurations.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._post(
            f"/session/{session_id}/init",
            body=await async_maybe_transform(
                {
                    "message_id": message_id,
                    "model_id": model_id,
                    "provider_id": provider_id,
                },
                session_initialize_params.SessionInitializeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"directory": directory}, session_initialize_params.SessionInitializeParams
                ),
            ),
            cast_to=SessionInitializeResponse,
        )

    @typing_extensions.deprecated("deprecated")
    async def respond_to_permission(
        self,
        permission_id: str,
        *,
        session_id: str,
        response: Literal["once", "always", "reject"],
        directory: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionRespondToPermissionResponse:
        """
        Approve or deny a permission request from the AI assistant.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        if not permission_id:
            raise ValueError(f"Expected a non-empty value for `permission_id` but received {permission_id!r}")
        return await self._post(
            f"/session/{session_id}/permissions/{permission_id}",
            body=await async_maybe_transform(
                {"response": response}, session_respond_to_permission_params.SessionRespondToPermissionParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"directory": directory}, session_respond_to_permission_params.SessionRespondToPermissionParams
                ),
            ),
            cast_to=SessionRespondToPermissionResponse,
        )

    async def restore_reverted_messages(
        self,
        session_id: str,
        *,
        directory: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Session:
        """
        Restore all previously reverted messages in a session.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._post(
            f"/session/{session_id}/unrevert",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"directory": directory},
                    session_restore_reverted_messages_params.SessionRestoreRevertedMessagesParams,
                ),
            ),
            cast_to=Session,
        )

    async def retrieve_status(
        self,
        session_id: str,
        *,
        directory: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionRetrieveStatusResponse:
        """
        Retrieve the current status of a specific session (idle, busy, retry, or
        wait-tool-result).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return cast(
            SessionRetrieveStatusResponse,
            await self._get(
                f"/session/{session_id}/status",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=await async_maybe_transform(
                        {"directory": directory}, session_retrieve_status_params.SessionRetrieveStatusParams
                    ),
                ),
                cast_to=cast(
                    Any, SessionRetrieveStatusResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def revert_message(
        self,
        session_id: str,
        *,
        message_id: str,
        directory: str | Omit = omit,
        part_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Session:
        """
        Revert a specific message in a session, undoing its effects and restoring the
        previous state.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._post(
            f"/session/{session_id}/revert",
            body=await async_maybe_transform(
                {
                    "message_id": message_id,
                    "part_id": part_id,
                },
                session_revert_message_params.SessionRevertMessageParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"directory": directory}, session_revert_message_params.SessionRevertMessageParams
                ),
            ),
            cast_to=Session,
        )

    async def run_shell_command(
        self,
        session_id: str,
        *,
        agent: str,
        command: str,
        directory: str | Omit = omit,
        model: session_run_shell_command_params.Model | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AssistantMessage:
        """
        Execute a shell command within the session context and return the AI's response.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._post(
            f"/session/{session_id}/shell",
            body=await async_maybe_transform(
                {
                    "agent": agent,
                    "command": command,
                    "model": model,
                },
                session_run_shell_command_params.SessionRunShellCommandParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"directory": directory}, session_run_shell_command_params.SessionRunShellCommandParams
                ),
            ),
            cast_to=AssistantMessage,
        )

    async def send_async_message(
        self,
        session_id: str,
        *,
        parts: Iterable[session_send_async_message_params.Part],
        directory: str | Omit = omit,
        agent: str | Omit = omit,
        message_id: str | Omit = omit,
        model: session_send_async_message_params.Model | Omit = omit,
        no_reply: bool | Omit = omit,
        system: str | Omit = omit,
        tools: Dict[str, bool] | Omit = omit,
        variant: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Create and send a new message to a session asynchronously, starting the session
        if needed and returning immediately.

        Args:
          tools: @deprecated tools and permissions have been merged, you can set permissions on
              the session itself now

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/session/{session_id}/prompt_async",
            body=await async_maybe_transform(
                {
                    "parts": parts,
                    "agent": agent,
                    "message_id": message_id,
                    "model": model,
                    "no_reply": no_reply,
                    "system": system,
                    "tools": tools,
                    "variant": variant,
                },
                session_send_async_message_params.SessionSendAsyncMessageParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"directory": directory}, session_send_async_message_params.SessionSendAsyncMessageParams
                ),
            ),
            cast_to=NoneType,
        )

    async def send_command(
        self,
        session_id: str,
        *,
        arguments: str,
        command: str,
        directory: str | Omit = omit,
        agent: str | Omit = omit,
        message_id: str | Omit = omit,
        model: str | Omit = omit,
        parts: Iterable[session_send_command_params.Part] | Omit = omit,
        variant: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionSendCommandResponse:
        """
        Send a new command to a session for execution by the AI assistant.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._post(
            f"/session/{session_id}/command",
            body=await async_maybe_transform(
                {
                    "arguments": arguments,
                    "command": command,
                    "agent": agent,
                    "message_id": message_id,
                    "model": model,
                    "parts": parts,
                    "variant": variant,
                },
                session_send_command_params.SessionSendCommandParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"directory": directory}, session_send_command_params.SessionSendCommandParams
                ),
            ),
            cast_to=SessionSendCommandResponse,
        )

    async def submit_tool_results(
        self,
        session_id: str,
        *,
        results: Iterable[session_submit_tool_results_params.Result],
        directory: str | Omit = omit,
        async_: bool | Omit = omit,
        continue_loop: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionSubmitToolResultsResponse:
        """
        Submit results for remote tools that are waiting for external execution, and
        optionally continue the inference loop.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._post(
            f"/session/{session_id}/tool-results",
            body=await async_maybe_transform(
                {
                    "results": results,
                    "async_": async_,
                    "continue_loop": continue_loop,
                },
                session_submit_tool_results_params.SessionSubmitToolResultsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"directory": directory}, session_submit_tool_results_params.SessionSubmitToolResultsParams
                ),
            ),
            cast_to=SessionSubmitToolResultsResponse,
        )

    async def summarize(
        self,
        session_id: str,
        *,
        model_id: str,
        provider_id: str,
        directory: str | Omit = omit,
        auto: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionSummarizeResponse:
        """
        Generate a concise summary of the session using AI compaction to preserve key
        information.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._post(
            f"/session/{session_id}/summarize",
            body=await async_maybe_transform(
                {
                    "model_id": model_id,
                    "provider_id": provider_id,
                    "auto": auto,
                },
                session_summarize_params.SessionSummarizeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"directory": directory}, session_summarize_params.SessionSummarizeParams
                ),
            ),
            cast_to=SessionSummarizeResponse,
        )


class SessionResourceWithRawResponse:
    def __init__(self, session: SessionResource) -> None:
        self._session = session

        self.create = to_raw_response_wrapper(
            session.create,
        )
        self.retrieve = to_raw_response_wrapper(
            session.retrieve,
        )
        self.update = to_raw_response_wrapper(
            session.update,
        )
        self.list = to_raw_response_wrapper(
            session.list,
        )
        self.delete = to_raw_response_wrapper(
            session.delete,
        )
        self.abort = to_raw_response_wrapper(
            session.abort,
        )
        self.fork = to_raw_response_wrapper(
            session.fork,
        )
        self.get_children = to_raw_response_wrapper(
            session.get_children,
        )
        self.get_diff = to_raw_response_wrapper(
            session.get_diff,
        )
        self.get_status = to_raw_response_wrapper(
            session.get_status,
        )
        self.get_todo = to_raw_response_wrapper(
            session.get_todo,
        )
        self.initialize = to_raw_response_wrapper(
            session.initialize,
        )
        self.respond_to_permission = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                session.respond_to_permission,  # pyright: ignore[reportDeprecated],
            )
        )
        self.restore_reverted_messages = to_raw_response_wrapper(
            session.restore_reverted_messages,
        )
        self.retrieve_status = to_raw_response_wrapper(
            session.retrieve_status,
        )
        self.revert_message = to_raw_response_wrapper(
            session.revert_message,
        )
        self.run_shell_command = to_raw_response_wrapper(
            session.run_shell_command,
        )
        self.send_async_message = to_raw_response_wrapper(
            session.send_async_message,
        )
        self.send_command = to_raw_response_wrapper(
            session.send_command,
        )
        self.submit_tool_results = to_raw_response_wrapper(
            session.submit_tool_results,
        )
        self.summarize = to_raw_response_wrapper(
            session.summarize,
        )

    @cached_property
    def share(self) -> ShareResourceWithRawResponse:
        return ShareResourceWithRawResponse(self._session.share)

    @cached_property
    def message(self) -> MessageResourceWithRawResponse:
        return MessageResourceWithRawResponse(self._session.message)


class AsyncSessionResourceWithRawResponse:
    def __init__(self, session: AsyncSessionResource) -> None:
        self._session = session

        self.create = async_to_raw_response_wrapper(
            session.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            session.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            session.update,
        )
        self.list = async_to_raw_response_wrapper(
            session.list,
        )
        self.delete = async_to_raw_response_wrapper(
            session.delete,
        )
        self.abort = async_to_raw_response_wrapper(
            session.abort,
        )
        self.fork = async_to_raw_response_wrapper(
            session.fork,
        )
        self.get_children = async_to_raw_response_wrapper(
            session.get_children,
        )
        self.get_diff = async_to_raw_response_wrapper(
            session.get_diff,
        )
        self.get_status = async_to_raw_response_wrapper(
            session.get_status,
        )
        self.get_todo = async_to_raw_response_wrapper(
            session.get_todo,
        )
        self.initialize = async_to_raw_response_wrapper(
            session.initialize,
        )
        self.respond_to_permission = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                session.respond_to_permission,  # pyright: ignore[reportDeprecated],
            )
        )
        self.restore_reverted_messages = async_to_raw_response_wrapper(
            session.restore_reverted_messages,
        )
        self.retrieve_status = async_to_raw_response_wrapper(
            session.retrieve_status,
        )
        self.revert_message = async_to_raw_response_wrapper(
            session.revert_message,
        )
        self.run_shell_command = async_to_raw_response_wrapper(
            session.run_shell_command,
        )
        self.send_async_message = async_to_raw_response_wrapper(
            session.send_async_message,
        )
        self.send_command = async_to_raw_response_wrapper(
            session.send_command,
        )
        self.submit_tool_results = async_to_raw_response_wrapper(
            session.submit_tool_results,
        )
        self.summarize = async_to_raw_response_wrapper(
            session.summarize,
        )

    @cached_property
    def share(self) -> AsyncShareResourceWithRawResponse:
        return AsyncShareResourceWithRawResponse(self._session.share)

    @cached_property
    def message(self) -> AsyncMessageResourceWithRawResponse:
        return AsyncMessageResourceWithRawResponse(self._session.message)


class SessionResourceWithStreamingResponse:
    def __init__(self, session: SessionResource) -> None:
        self._session = session

        self.create = to_streamed_response_wrapper(
            session.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            session.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            session.update,
        )
        self.list = to_streamed_response_wrapper(
            session.list,
        )
        self.delete = to_streamed_response_wrapper(
            session.delete,
        )
        self.abort = to_streamed_response_wrapper(
            session.abort,
        )
        self.fork = to_streamed_response_wrapper(
            session.fork,
        )
        self.get_children = to_streamed_response_wrapper(
            session.get_children,
        )
        self.get_diff = to_streamed_response_wrapper(
            session.get_diff,
        )
        self.get_status = to_streamed_response_wrapper(
            session.get_status,
        )
        self.get_todo = to_streamed_response_wrapper(
            session.get_todo,
        )
        self.initialize = to_streamed_response_wrapper(
            session.initialize,
        )
        self.respond_to_permission = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                session.respond_to_permission,  # pyright: ignore[reportDeprecated],
            )
        )
        self.restore_reverted_messages = to_streamed_response_wrapper(
            session.restore_reverted_messages,
        )
        self.retrieve_status = to_streamed_response_wrapper(
            session.retrieve_status,
        )
        self.revert_message = to_streamed_response_wrapper(
            session.revert_message,
        )
        self.run_shell_command = to_streamed_response_wrapper(
            session.run_shell_command,
        )
        self.send_async_message = to_streamed_response_wrapper(
            session.send_async_message,
        )
        self.send_command = to_streamed_response_wrapper(
            session.send_command,
        )
        self.submit_tool_results = to_streamed_response_wrapper(
            session.submit_tool_results,
        )
        self.summarize = to_streamed_response_wrapper(
            session.summarize,
        )

    @cached_property
    def share(self) -> ShareResourceWithStreamingResponse:
        return ShareResourceWithStreamingResponse(self._session.share)

    @cached_property
    def message(self) -> MessageResourceWithStreamingResponse:
        return MessageResourceWithStreamingResponse(self._session.message)


class AsyncSessionResourceWithStreamingResponse:
    def __init__(self, session: AsyncSessionResource) -> None:
        self._session = session

        self.create = async_to_streamed_response_wrapper(
            session.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            session.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            session.update,
        )
        self.list = async_to_streamed_response_wrapper(
            session.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            session.delete,
        )
        self.abort = async_to_streamed_response_wrapper(
            session.abort,
        )
        self.fork = async_to_streamed_response_wrapper(
            session.fork,
        )
        self.get_children = async_to_streamed_response_wrapper(
            session.get_children,
        )
        self.get_diff = async_to_streamed_response_wrapper(
            session.get_diff,
        )
        self.get_status = async_to_streamed_response_wrapper(
            session.get_status,
        )
        self.get_todo = async_to_streamed_response_wrapper(
            session.get_todo,
        )
        self.initialize = async_to_streamed_response_wrapper(
            session.initialize,
        )
        self.respond_to_permission = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                session.respond_to_permission,  # pyright: ignore[reportDeprecated],
            )
        )
        self.restore_reverted_messages = async_to_streamed_response_wrapper(
            session.restore_reverted_messages,
        )
        self.retrieve_status = async_to_streamed_response_wrapper(
            session.retrieve_status,
        )
        self.revert_message = async_to_streamed_response_wrapper(
            session.revert_message,
        )
        self.run_shell_command = async_to_streamed_response_wrapper(
            session.run_shell_command,
        )
        self.send_async_message = async_to_streamed_response_wrapper(
            session.send_async_message,
        )
        self.send_command = async_to_streamed_response_wrapper(
            session.send_command,
        )
        self.submit_tool_results = async_to_streamed_response_wrapper(
            session.submit_tool_results,
        )
        self.summarize = async_to_streamed_response_wrapper(
            session.summarize,
        )

    @cached_property
    def share(self) -> AsyncShareResourceWithStreamingResponse:
        return AsyncShareResourceWithStreamingResponse(self._session.share)

    @cached_property
    def message(self) -> AsyncMessageResourceWithStreamingResponse:
        return AsyncMessageResourceWithStreamingResponse(self._session.message)
