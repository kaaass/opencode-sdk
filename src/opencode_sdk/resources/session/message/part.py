# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Dict, cast
from typing_extensions import Literal, overload

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ...._utils import required_args, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.session.part import Part
from ....types.session.message import part_delete_params, part_update_params
from ....types.session.file_part_source_param import FilePartSourceParam
from ....types.session.message.part_delete_response import PartDeleteResponse

__all__ = ["PartResource", "AsyncPartResource"]


class PartResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PartResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kaaass/opencode-sdk#accessing-raw-response-data-eg-headers
        """
        return PartResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PartResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kaaass/opencode-sdk#with_streaming_response
        """
        return PartResourceWithStreamingResponse(self)

    @overload
    def update(
        self,
        part_id: str,
        *,
        path_session_id: str,
        path_message_id: str,
        id: str,
        body_message_id: str,
        body_session_id: str,
        text: str,
        type: Literal["text"],
        directory: str | Omit = omit,
        ignored: bool | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        synthetic: bool | Omit = omit,
        time: part_update_params.TextPartTime | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Part:
        """
        Update a part in a message

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        part_id: str,
        *,
        path_session_id: str,
        path_message_id: str,
        id: str,
        agent: str,
        description: str,
        body_message_id: str,
        prompt: str,
        body_session_id: str,
        type: Literal["subtask"],
        directory: str | Omit = omit,
        command: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Part:
        """
        Update a part in a message

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        part_id: str,
        *,
        path_session_id: str,
        path_message_id: str,
        id: str,
        body_message_id: str,
        body_session_id: str,
        text: str,
        time: part_update_params.ReasoningPartTime,
        type: Literal["reasoning"],
        directory: str | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Part:
        """
        Update a part in a message

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        part_id: str,
        *,
        path_session_id: str,
        path_message_id: str,
        id: str,
        body_message_id: str,
        mime: str,
        body_session_id: str,
        type: Literal["file"],
        url: str,
        directory: str | Omit = omit,
        filename: str | Omit = omit,
        source: FilePartSourceParam | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Part:
        """
        Update a part in a message

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        part_id: str,
        *,
        path_session_id: str,
        path_message_id: str,
        id: str,
        call_id: str,
        body_message_id: str,
        body_session_id: str,
        state: part_update_params.ToolPartState,
        tool: str,
        type: Literal["tool"],
        directory: str | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Part:
        """
        Update a part in a message

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        part_id: str,
        *,
        path_session_id: str,
        path_message_id: str,
        id: str,
        body_message_id: str,
        body_session_id: str,
        type: Literal["step-start"],
        directory: str | Omit = omit,
        snapshot: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Part:
        """
        Update a part in a message

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        part_id: str,
        *,
        path_session_id: str,
        path_message_id: str,
        id: str,
        cost: float,
        body_message_id: str,
        reason: str,
        body_session_id: str,
        tokens: part_update_params.StepFinishPartTokens,
        type: Literal["step-finish"],
        directory: str | Omit = omit,
        snapshot: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Part:
        """
        Update a part in a message

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        part_id: str,
        *,
        path_session_id: str,
        path_message_id: str,
        id: str,
        body_message_id: str,
        body_session_id: str,
        snapshot: str,
        type: Literal["snapshot"],
        directory: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Part:
        """
        Update a part in a message

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        part_id: str,
        *,
        path_session_id: str,
        path_message_id: str,
        id: str,
        files: SequenceNotStr[str],
        hash: str,
        body_message_id: str,
        body_session_id: str,
        type: Literal["patch"],
        directory: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Part:
        """
        Update a part in a message

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        part_id: str,
        *,
        path_session_id: str,
        path_message_id: str,
        id: str,
        body_message_id: str,
        name: str,
        body_session_id: str,
        type: Literal["agent"],
        directory: str | Omit = omit,
        source: part_update_params.AgentPartSource | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Part:
        """
        Update a part in a message

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        part_id: str,
        *,
        path_session_id: str,
        path_message_id: str,
        id: str,
        attempt: float,
        error: part_update_params.RetryPartError,
        body_message_id: str,
        body_session_id: str,
        time: part_update_params.RetryPartTime,
        type: Literal["retry"],
        directory: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Part:
        """
        Update a part in a message

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        part_id: str,
        *,
        path_session_id: str,
        path_message_id: str,
        id: str,
        auto: bool,
        body_message_id: str,
        body_session_id: str,
        type: Literal["compaction"],
        directory: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Part:
        """
        Update a part in a message

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        ["path_session_id", "path_message_id", "id", "body_message_id", "body_session_id", "text", "type"],
        [
            "path_session_id",
            "path_message_id",
            "id",
            "agent",
            "description",
            "body_message_id",
            "prompt",
            "body_session_id",
            "type",
        ],
        ["path_session_id", "path_message_id", "id", "body_message_id", "body_session_id", "text", "time", "type"],
        ["path_session_id", "path_message_id", "id", "body_message_id", "mime", "body_session_id", "type", "url"],
        [
            "path_session_id",
            "path_message_id",
            "id",
            "call_id",
            "body_message_id",
            "body_session_id",
            "state",
            "tool",
            "type",
        ],
        ["path_session_id", "path_message_id", "id", "body_message_id", "body_session_id", "type"],
        [
            "path_session_id",
            "path_message_id",
            "id",
            "cost",
            "body_message_id",
            "reason",
            "body_session_id",
            "tokens",
            "type",
        ],
        ["path_session_id", "path_message_id", "id", "body_message_id", "body_session_id", "snapshot", "type"],
        ["path_session_id", "path_message_id", "id", "files", "hash", "body_message_id", "body_session_id", "type"],
        ["path_session_id", "path_message_id", "id", "body_message_id", "name", "body_session_id", "type"],
        [
            "path_session_id",
            "path_message_id",
            "id",
            "attempt",
            "error",
            "body_message_id",
            "body_session_id",
            "time",
            "type",
        ],
        ["path_session_id", "path_message_id", "id", "auto", "body_message_id", "body_session_id", "type"],
    )
    def update(
        self,
        part_id: str,
        *,
        body_session_id: str,
        body_message_id: str,
        id: str,
        text: str | Omit = omit,
        type: Literal["text"]
        | Literal["subtask"]
        | Literal["reasoning"]
        | Literal["file"]
        | Literal["tool"]
        | Literal["step-start"]
        | Literal["step-finish"]
        | Literal["snapshot"]
        | Literal["patch"]
        | Literal["agent"]
        | Literal["retry"]
        | Literal["compaction"],
        directory: str | Omit = omit,
        ignored: bool | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        synthetic: bool | Omit = omit,
        time: part_update_params.TextPartTime
        | part_update_params.ReasoningPartTime
        | part_update_params.RetryPartTime
        | Omit = omit,
        agent: str | Omit = omit,
        description: str | Omit = omit,
        prompt: str | Omit = omit,
        command: str | Omit = omit,
        mime: str | Omit = omit,
        url: str | Omit = omit,
        filename: str | Omit = omit,
        source: FilePartSourceParam | part_update_params.AgentPartSource | Omit = omit,
        call_id: str | Omit = omit,
        state: part_update_params.ToolPartState | Omit = omit,
        tool: str | Omit = omit,
        snapshot: str | Omit = omit,
        cost: float | Omit = omit,
        reason: str | Omit = omit,
        tokens: part_update_params.StepFinishPartTokens | Omit = omit,
        files: SequenceNotStr[str] | Omit = omit,
        hash: str | Omit = omit,
        name: str | Omit = omit,
        attempt: float | Omit = omit,
        error: part_update_params.RetryPartError | Omit = omit,
        auto: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Part:
        if not path_session_id:
            raise ValueError(f"Expected a non-empty value for `path_session_id` but received {path_session_id!r}")
        if not path_message_id:
            raise ValueError(f"Expected a non-empty value for `path_message_id` but received {path_message_id!r}")
        if not part_id:
            raise ValueError(f"Expected a non-empty value for `part_id` but received {part_id!r}")
        return cast(
            Part,
            self._patch(
                f"/session/{path_session_id}/message/{path_message_id}/part/{part_id}",
                body=maybe_transform(
                    {
                        "id": id,
                        "body_message_id": body_message_id,
                        "body_session_id": body_session_id,
                        "text": text,
                        "type": type,
                        "ignored": ignored,
                        "metadata": metadata,
                        "synthetic": synthetic,
                        "time": time,
                        "agent": agent,
                        "description": description,
                        "prompt": prompt,
                        "command": command,
                        "mime": mime,
                        "url": url,
                        "filename": filename,
                        "source": source,
                        "call_id": call_id,
                        "state": state,
                        "tool": tool,
                        "snapshot": snapshot,
                        "cost": cost,
                        "reason": reason,
                        "tokens": tokens,
                        "files": files,
                        "hash": hash,
                        "name": name,
                        "attempt": attempt,
                        "error": error,
                        "auto": auto,
                    },
                    part_update_params.PartUpdateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=maybe_transform({"directory": directory}, part_update_params.PartUpdateParams),
                ),
                cast_to=cast(Any, Part),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def delete(
        self,
        part_id: str,
        *,
        session_id: str,
        message_id: str,
        directory: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PartDeleteResponse:
        """
        Delete a part from a message

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        if not part_id:
            raise ValueError(f"Expected a non-empty value for `part_id` but received {part_id!r}")
        return self._delete(
            f"/session/{session_id}/message/{message_id}/part/{part_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"directory": directory}, part_delete_params.PartDeleteParams),
            ),
            cast_to=PartDeleteResponse,
        )


class AsyncPartResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPartResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kaaass/opencode-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncPartResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPartResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kaaass/opencode-sdk#with_streaming_response
        """
        return AsyncPartResourceWithStreamingResponse(self)

    @overload
    async def update(
        self,
        part_id: str,
        *,
        path_session_id: str,
        path_message_id: str,
        id: str,
        body_message_id: str,
        body_session_id: str,
        text: str,
        type: Literal["text"],
        directory: str | Omit = omit,
        ignored: bool | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        synthetic: bool | Omit = omit,
        time: part_update_params.TextPartTime | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Part:
        """
        Update a part in a message

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        part_id: str,
        *,
        path_session_id: str,
        path_message_id: str,
        id: str,
        agent: str,
        description: str,
        body_message_id: str,
        prompt: str,
        body_session_id: str,
        type: Literal["subtask"],
        directory: str | Omit = omit,
        command: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Part:
        """
        Update a part in a message

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        part_id: str,
        *,
        path_session_id: str,
        path_message_id: str,
        id: str,
        body_message_id: str,
        body_session_id: str,
        text: str,
        time: part_update_params.ReasoningPartTime,
        type: Literal["reasoning"],
        directory: str | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Part:
        """
        Update a part in a message

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        part_id: str,
        *,
        path_session_id: str,
        path_message_id: str,
        id: str,
        body_message_id: str,
        mime: str,
        body_session_id: str,
        type: Literal["file"],
        url: str,
        directory: str | Omit = omit,
        filename: str | Omit = omit,
        source: FilePartSourceParam | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Part:
        """
        Update a part in a message

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        part_id: str,
        *,
        path_session_id: str,
        path_message_id: str,
        id: str,
        call_id: str,
        body_message_id: str,
        body_session_id: str,
        state: part_update_params.ToolPartState,
        tool: str,
        type: Literal["tool"],
        directory: str | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Part:
        """
        Update a part in a message

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        part_id: str,
        *,
        path_session_id: str,
        path_message_id: str,
        id: str,
        body_message_id: str,
        body_session_id: str,
        type: Literal["step-start"],
        directory: str | Omit = omit,
        snapshot: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Part:
        """
        Update a part in a message

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        part_id: str,
        *,
        path_session_id: str,
        path_message_id: str,
        id: str,
        cost: float,
        body_message_id: str,
        reason: str,
        body_session_id: str,
        tokens: part_update_params.StepFinishPartTokens,
        type: Literal["step-finish"],
        directory: str | Omit = omit,
        snapshot: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Part:
        """
        Update a part in a message

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        part_id: str,
        *,
        path_session_id: str,
        path_message_id: str,
        id: str,
        body_message_id: str,
        body_session_id: str,
        snapshot: str,
        type: Literal["snapshot"],
        directory: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Part:
        """
        Update a part in a message

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        part_id: str,
        *,
        path_session_id: str,
        path_message_id: str,
        id: str,
        files: SequenceNotStr[str],
        hash: str,
        body_message_id: str,
        body_session_id: str,
        type: Literal["patch"],
        directory: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Part:
        """
        Update a part in a message

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        part_id: str,
        *,
        path_session_id: str,
        path_message_id: str,
        id: str,
        body_message_id: str,
        name: str,
        body_session_id: str,
        type: Literal["agent"],
        directory: str | Omit = omit,
        source: part_update_params.AgentPartSource | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Part:
        """
        Update a part in a message

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        part_id: str,
        *,
        path_session_id: str,
        path_message_id: str,
        id: str,
        attempt: float,
        error: part_update_params.RetryPartError,
        body_message_id: str,
        body_session_id: str,
        time: part_update_params.RetryPartTime,
        type: Literal["retry"],
        directory: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Part:
        """
        Update a part in a message

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        part_id: str,
        *,
        path_session_id: str,
        path_message_id: str,
        id: str,
        auto: bool,
        body_message_id: str,
        body_session_id: str,
        type: Literal["compaction"],
        directory: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Part:
        """
        Update a part in a message

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        ["path_session_id", "path_message_id", "id", "body_message_id", "body_session_id", "text", "type"],
        [
            "path_session_id",
            "path_message_id",
            "id",
            "agent",
            "description",
            "body_message_id",
            "prompt",
            "body_session_id",
            "type",
        ],
        ["path_session_id", "path_message_id", "id", "body_message_id", "body_session_id", "text", "time", "type"],
        ["path_session_id", "path_message_id", "id", "body_message_id", "mime", "body_session_id", "type", "url"],
        [
            "path_session_id",
            "path_message_id",
            "id",
            "call_id",
            "body_message_id",
            "body_session_id",
            "state",
            "tool",
            "type",
        ],
        ["path_session_id", "path_message_id", "id", "body_message_id", "body_session_id", "type"],
        [
            "path_session_id",
            "path_message_id",
            "id",
            "cost",
            "body_message_id",
            "reason",
            "body_session_id",
            "tokens",
            "type",
        ],
        ["path_session_id", "path_message_id", "id", "body_message_id", "body_session_id", "snapshot", "type"],
        ["path_session_id", "path_message_id", "id", "files", "hash", "body_message_id", "body_session_id", "type"],
        ["path_session_id", "path_message_id", "id", "body_message_id", "name", "body_session_id", "type"],
        [
            "path_session_id",
            "path_message_id",
            "id",
            "attempt",
            "error",
            "body_message_id",
            "body_session_id",
            "time",
            "type",
        ],
        ["path_session_id", "path_message_id", "id", "auto", "body_message_id", "body_session_id", "type"],
    )
    async def update(
        self,
        part_id: str,
        *,
        body_session_id: str,
        body_message_id: str,
        id: str,
        text: str | Omit = omit,
        type: Literal["text"]
        | Literal["subtask"]
        | Literal["reasoning"]
        | Literal["file"]
        | Literal["tool"]
        | Literal["step-start"]
        | Literal["step-finish"]
        | Literal["snapshot"]
        | Literal["patch"]
        | Literal["agent"]
        | Literal["retry"]
        | Literal["compaction"],
        directory: str | Omit = omit,
        ignored: bool | Omit = omit,
        metadata: Dict[str, object] | Omit = omit,
        synthetic: bool | Omit = omit,
        time: part_update_params.TextPartTime
        | part_update_params.ReasoningPartTime
        | part_update_params.RetryPartTime
        | Omit = omit,
        agent: str | Omit = omit,
        description: str | Omit = omit,
        prompt: str | Omit = omit,
        command: str | Omit = omit,
        mime: str | Omit = omit,
        url: str | Omit = omit,
        filename: str | Omit = omit,
        source: FilePartSourceParam | part_update_params.AgentPartSource | Omit = omit,
        call_id: str | Omit = omit,
        state: part_update_params.ToolPartState | Omit = omit,
        tool: str | Omit = omit,
        snapshot: str | Omit = omit,
        cost: float | Omit = omit,
        reason: str | Omit = omit,
        tokens: part_update_params.StepFinishPartTokens | Omit = omit,
        files: SequenceNotStr[str] | Omit = omit,
        hash: str | Omit = omit,
        name: str | Omit = omit,
        attempt: float | Omit = omit,
        error: part_update_params.RetryPartError | Omit = omit,
        auto: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Part:
        if not path_session_id:
            raise ValueError(f"Expected a non-empty value for `path_session_id` but received {path_session_id!r}")
        if not path_message_id:
            raise ValueError(f"Expected a non-empty value for `path_message_id` but received {path_message_id!r}")
        if not part_id:
            raise ValueError(f"Expected a non-empty value for `part_id` but received {part_id!r}")
        return cast(
            Part,
            await self._patch(
                f"/session/{path_session_id}/message/{path_message_id}/part/{part_id}",
                body=await async_maybe_transform(
                    {
                        "id": id,
                        "body_message_id": body_message_id,
                        "body_session_id": body_session_id,
                        "text": text,
                        "type": type,
                        "ignored": ignored,
                        "metadata": metadata,
                        "synthetic": synthetic,
                        "time": time,
                        "agent": agent,
                        "description": description,
                        "prompt": prompt,
                        "command": command,
                        "mime": mime,
                        "url": url,
                        "filename": filename,
                        "source": source,
                        "call_id": call_id,
                        "state": state,
                        "tool": tool,
                        "snapshot": snapshot,
                        "cost": cost,
                        "reason": reason,
                        "tokens": tokens,
                        "files": files,
                        "hash": hash,
                        "name": name,
                        "attempt": attempt,
                        "error": error,
                        "auto": auto,
                    },
                    part_update_params.PartUpdateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=await async_maybe_transform({"directory": directory}, part_update_params.PartUpdateParams),
                ),
                cast_to=cast(Any, Part),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def delete(
        self,
        part_id: str,
        *,
        session_id: str,
        message_id: str,
        directory: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PartDeleteResponse:
        """
        Delete a part from a message

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        if not message_id:
            raise ValueError(f"Expected a non-empty value for `message_id` but received {message_id!r}")
        if not part_id:
            raise ValueError(f"Expected a non-empty value for `part_id` but received {part_id!r}")
        return await self._delete(
            f"/session/{session_id}/message/{message_id}/part/{part_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"directory": directory}, part_delete_params.PartDeleteParams),
            ),
            cast_to=PartDeleteResponse,
        )


class PartResourceWithRawResponse:
    def __init__(self, part: PartResource) -> None:
        self._part = part

        self.update = to_raw_response_wrapper(
            part.update,
        )
        self.delete = to_raw_response_wrapper(
            part.delete,
        )


class AsyncPartResourceWithRawResponse:
    def __init__(self, part: AsyncPartResource) -> None:
        self._part = part

        self.update = async_to_raw_response_wrapper(
            part.update,
        )
        self.delete = async_to_raw_response_wrapper(
            part.delete,
        )


class PartResourceWithStreamingResponse:
    def __init__(self, part: PartResource) -> None:
        self._part = part

        self.update = to_streamed_response_wrapper(
            part.update,
        )
        self.delete = to_streamed_response_wrapper(
            part.delete,
        )


class AsyncPartResourceWithStreamingResponse:
    def __init__(self, part: AsyncPartResource) -> None:
        self._part = part

        self.update = async_to_streamed_response_wrapper(
            part.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            part.delete,
        )
