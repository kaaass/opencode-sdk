# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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
    session_revert_params,
    session_update_params,
    session_analyze_params,
    session_get_todo_params,
    session_retrieve_params,
    session_run_shell_params,
    session_summarize_params,
    session_get_children_params,
    session_send_command_params,
    session_restore_reverted_params,
    session_respond_to_permission_params,
)
from .message import (
    MessageResource,
    AsyncMessageResource,
    MessageResourceWithRawResponse,
    AsyncMessageResourceWithRawResponse,
    MessageResourceWithStreamingResponse,
    AsyncMessageResourceWithStreamingResponse,
)
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ...types.session.session import Session
from ...types.assistant_message import AssistantMessage
from ...types.session_list_response import SessionListResponse
from ...types.session_abort_response import SessionAbortResponse
from ...types.session_delete_response import SessionDeleteResponse
from ...types.session_analyze_response import SessionAnalyzeResponse
from ...types.session_get_todo_response import SessionGetTodoResponse
from ...types.session_summarize_response import SessionSummarizeResponse
from ...types.session_get_children_response import SessionGetChildrenResponse
from ...types.session_send_command_response import SessionSendCommandResponse
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

        For more information, see https://www.github.com/stainless-sdks/opencode-sdk-python#accessing-raw-response-data-eg-headers
        """
        return SessionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SessionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/opencode-sdk-python#with_streaming_response
        """
        return SessionResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        directory: str | Omit = omit,
        parent_id: str | Omit = omit,
        title: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Session:
        """
        Create a new session

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
        id: str,
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
        Get session

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/session/{id}",
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
        id: str,
        *,
        directory: str | Omit = omit,
        title: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Session:
        """
        Update session properties

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/session/{id}",
            body=maybe_transform({"title": title}, session_update_params.SessionUpdateParams),
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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionListResponse:
        """
        List all sessions

        Args:
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
                query=maybe_transform({"directory": directory}, session_list_params.SessionListParams),
            ),
            cast_to=SessionListResponse,
        )

    def delete(
        self,
        id: str,
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
        Delete a session and all its data

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/session/{id}",
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
        id: str,
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
        Abort a session

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/session/{id}/abort",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"directory": directory}, session_abort_params.SessionAbortParams),
            ),
            cast_to=SessionAbortResponse,
        )

    def analyze(
        self,
        id: str,
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
    ) -> SessionAnalyzeResponse:
        """
        Analyze the app and create an AGENTS.md file

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/session/{id}/init",
            body=maybe_transform(
                {
                    "message_id": message_id,
                    "model_id": model_id,
                    "provider_id": provider_id,
                },
                session_analyze_params.SessionAnalyzeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"directory": directory}, session_analyze_params.SessionAnalyzeParams),
            ),
            cast_to=SessionAnalyzeResponse,
        )

    def fork(
        self,
        id: str,
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
        Fork an existing session at a specific message

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/session/{id}/fork",
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
        id: str,
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
        Get a session's children

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/session/{id}/children",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"directory": directory}, session_get_children_params.SessionGetChildrenParams),
            ),
            cast_to=SessionGetChildrenResponse,
        )

    def get_todo(
        self,
        id: str,
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
        Get the todo list for a session

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/session/{id}/todo",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"directory": directory}, session_get_todo_params.SessionGetTodoParams),
            ),
            cast_to=SessionGetTodoResponse,
        )

    def respond_to_permission(
        self,
        permission_id: str,
        *,
        id: str,
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
        Respond to a permission request

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not permission_id:
            raise ValueError(f"Expected a non-empty value for `permission_id` but received {permission_id!r}")
        return self._post(
            f"/session/{id}/permissions/{permission_id}",
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

    def restore_reverted(
        self,
        id: str,
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
        Restore all reverted messages

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/session/{id}/unrevert",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"directory": directory}, session_restore_reverted_params.SessionRestoreRevertedParams
                ),
            ),
            cast_to=Session,
        )

    def revert(
        self,
        id: str,
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
        Revert a message

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/session/{id}/revert",
            body=maybe_transform(
                {
                    "message_id": message_id,
                    "part_id": part_id,
                },
                session_revert_params.SessionRevertParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"directory": directory}, session_revert_params.SessionRevertParams),
            ),
            cast_to=Session,
        )

    def run_shell(
        self,
        id: str,
        *,
        agent: str,
        command: str,
        directory: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AssistantMessage:
        """
        Run a shell command

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/session/{id}/shell",
            body=maybe_transform(
                {
                    "agent": agent,
                    "command": command,
                },
                session_run_shell_params.SessionRunShellParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"directory": directory}, session_run_shell_params.SessionRunShellParams),
            ),
            cast_to=AssistantMessage,
        )

    def send_command(
        self,
        id: str,
        *,
        arguments: str,
        command: str,
        directory: str | Omit = omit,
        agent: str | Omit = omit,
        message_id: str | Omit = omit,
        model: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionSendCommandResponse:
        """
        Send a new command to a session

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/session/{id}/command",
            body=maybe_transform(
                {
                    "arguments": arguments,
                    "command": command,
                    "agent": agent,
                    "message_id": message_id,
                    "model": model,
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

    def summarize(
        self,
        id: str,
        *,
        model_id: str,
        provider_id: str,
        directory: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionSummarizeResponse:
        """
        Summarize the session

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/session/{id}/summarize",
            body=maybe_transform(
                {
                    "model_id": model_id,
                    "provider_id": provider_id,
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

        For more information, see https://www.github.com/stainless-sdks/opencode-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSessionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSessionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/opencode-sdk-python#with_streaming_response
        """
        return AsyncSessionResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        directory: str | Omit = omit,
        parent_id: str | Omit = omit,
        title: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Session:
        """
        Create a new session

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
        id: str,
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
        Get session

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/session/{id}",
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
        id: str,
        *,
        directory: str | Omit = omit,
        title: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Session:
        """
        Update session properties

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/session/{id}",
            body=await async_maybe_transform({"title": title}, session_update_params.SessionUpdateParams),
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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionListResponse:
        """
        List all sessions

        Args:
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
                query=await async_maybe_transform({"directory": directory}, session_list_params.SessionListParams),
            ),
            cast_to=SessionListResponse,
        )

    async def delete(
        self,
        id: str,
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
        Delete a session and all its data

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/session/{id}",
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
        id: str,
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
        Abort a session

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/session/{id}/abort",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"directory": directory}, session_abort_params.SessionAbortParams),
            ),
            cast_to=SessionAbortResponse,
        )

    async def analyze(
        self,
        id: str,
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
    ) -> SessionAnalyzeResponse:
        """
        Analyze the app and create an AGENTS.md file

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/session/{id}/init",
            body=await async_maybe_transform(
                {
                    "message_id": message_id,
                    "model_id": model_id,
                    "provider_id": provider_id,
                },
                session_analyze_params.SessionAnalyzeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"directory": directory}, session_analyze_params.SessionAnalyzeParams
                ),
            ),
            cast_to=SessionAnalyzeResponse,
        )

    async def fork(
        self,
        id: str,
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
        Fork an existing session at a specific message

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/session/{id}/fork",
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
        id: str,
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
        Get a session's children

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/session/{id}/children",
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

    async def get_todo(
        self,
        id: str,
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
        Get the todo list for a session

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/session/{id}/todo",
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

    async def respond_to_permission(
        self,
        permission_id: str,
        *,
        id: str,
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
        Respond to a permission request

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not permission_id:
            raise ValueError(f"Expected a non-empty value for `permission_id` but received {permission_id!r}")
        return await self._post(
            f"/session/{id}/permissions/{permission_id}",
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

    async def restore_reverted(
        self,
        id: str,
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
        Restore all reverted messages

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/session/{id}/unrevert",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"directory": directory}, session_restore_reverted_params.SessionRestoreRevertedParams
                ),
            ),
            cast_to=Session,
        )

    async def revert(
        self,
        id: str,
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
        Revert a message

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/session/{id}/revert",
            body=await async_maybe_transform(
                {
                    "message_id": message_id,
                    "part_id": part_id,
                },
                session_revert_params.SessionRevertParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"directory": directory}, session_revert_params.SessionRevertParams),
            ),
            cast_to=Session,
        )

    async def run_shell(
        self,
        id: str,
        *,
        agent: str,
        command: str,
        directory: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AssistantMessage:
        """
        Run a shell command

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/session/{id}/shell",
            body=await async_maybe_transform(
                {
                    "agent": agent,
                    "command": command,
                },
                session_run_shell_params.SessionRunShellParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"directory": directory}, session_run_shell_params.SessionRunShellParams
                ),
            ),
            cast_to=AssistantMessage,
        )

    async def send_command(
        self,
        id: str,
        *,
        arguments: str,
        command: str,
        directory: str | Omit = omit,
        agent: str | Omit = omit,
        message_id: str | Omit = omit,
        model: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionSendCommandResponse:
        """
        Send a new command to a session

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/session/{id}/command",
            body=await async_maybe_transform(
                {
                    "arguments": arguments,
                    "command": command,
                    "agent": agent,
                    "message_id": message_id,
                    "model": model,
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

    async def summarize(
        self,
        id: str,
        *,
        model_id: str,
        provider_id: str,
        directory: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SessionSummarizeResponse:
        """
        Summarize the session

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/session/{id}/summarize",
            body=await async_maybe_transform(
                {
                    "model_id": model_id,
                    "provider_id": provider_id,
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
        self.analyze = to_raw_response_wrapper(
            session.analyze,
        )
        self.fork = to_raw_response_wrapper(
            session.fork,
        )
        self.get_children = to_raw_response_wrapper(
            session.get_children,
        )
        self.get_todo = to_raw_response_wrapper(
            session.get_todo,
        )
        self.respond_to_permission = to_raw_response_wrapper(
            session.respond_to_permission,
        )
        self.restore_reverted = to_raw_response_wrapper(
            session.restore_reverted,
        )
        self.revert = to_raw_response_wrapper(
            session.revert,
        )
        self.run_shell = to_raw_response_wrapper(
            session.run_shell,
        )
        self.send_command = to_raw_response_wrapper(
            session.send_command,
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
        self.analyze = async_to_raw_response_wrapper(
            session.analyze,
        )
        self.fork = async_to_raw_response_wrapper(
            session.fork,
        )
        self.get_children = async_to_raw_response_wrapper(
            session.get_children,
        )
        self.get_todo = async_to_raw_response_wrapper(
            session.get_todo,
        )
        self.respond_to_permission = async_to_raw_response_wrapper(
            session.respond_to_permission,
        )
        self.restore_reverted = async_to_raw_response_wrapper(
            session.restore_reverted,
        )
        self.revert = async_to_raw_response_wrapper(
            session.revert,
        )
        self.run_shell = async_to_raw_response_wrapper(
            session.run_shell,
        )
        self.send_command = async_to_raw_response_wrapper(
            session.send_command,
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
        self.analyze = to_streamed_response_wrapper(
            session.analyze,
        )
        self.fork = to_streamed_response_wrapper(
            session.fork,
        )
        self.get_children = to_streamed_response_wrapper(
            session.get_children,
        )
        self.get_todo = to_streamed_response_wrapper(
            session.get_todo,
        )
        self.respond_to_permission = to_streamed_response_wrapper(
            session.respond_to_permission,
        )
        self.restore_reverted = to_streamed_response_wrapper(
            session.restore_reverted,
        )
        self.revert = to_streamed_response_wrapper(
            session.revert,
        )
        self.run_shell = to_streamed_response_wrapper(
            session.run_shell,
        )
        self.send_command = to_streamed_response_wrapper(
            session.send_command,
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
        self.analyze = async_to_streamed_response_wrapper(
            session.analyze,
        )
        self.fork = async_to_streamed_response_wrapper(
            session.fork,
        )
        self.get_children = async_to_streamed_response_wrapper(
            session.get_children,
        )
        self.get_todo = async_to_streamed_response_wrapper(
            session.get_todo,
        )
        self.respond_to_permission = async_to_streamed_response_wrapper(
            session.respond_to_permission,
        )
        self.restore_reverted = async_to_streamed_response_wrapper(
            session.restore_reverted,
        )
        self.revert = async_to_streamed_response_wrapper(
            session.revert,
        )
        self.run_shell = async_to_streamed_response_wrapper(
            session.run_shell,
        )
        self.send_command = async_to_streamed_response_wrapper(
            session.send_command,
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
