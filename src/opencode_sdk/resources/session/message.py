# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable

import httpx

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
from ...types.session import message_send_params, message_get_all_params, message_retrieve_params
from ...types.session.message_send_response import MessageSendResponse
from ...types.session.message_get_all_response import MessageGetAllResponse
from ...types.session.message_retrieve_response import MessageRetrieveResponse

__all__ = ["MessageResource", "AsyncMessageResource"]


class MessageResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MessageResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kaaass/opencode-sdk#accessing-raw-response-data-eg-headers
        """
        return MessageResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MessageResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kaaass/opencode-sdk#with_streaming_response
        """
        return MessageResourceWithStreamingResponse(self)

    def retrieve(
        self,
        message_id: str,
        *,
        session_id: str,
        directory: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageRetrieveResponse:
        """
        Retrieve a specific message from a session by its message ID.

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
        return self._get(
            f"/session/{session_id}/message/{message_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"directory": directory}, message_retrieve_params.MessageRetrieveParams),
            ),
            cast_to=MessageRetrieveResponse,
        )

    def get_all(
        self,
        session_id: str,
        *,
        directory: str | Omit = omit,
        limit: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageGetAllResponse:
        """
        Retrieve all messages in a session, including user prompts and AI responses.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._get(
            f"/session/{session_id}/message",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "directory": directory,
                        "limit": limit,
                    },
                    message_get_all_params.MessageGetAllParams,
                ),
            ),
            cast_to=MessageGetAllResponse,
        )

    def send(
        self,
        session_id: str,
        *,
        parts: Iterable[message_send_params.Part],
        directory: str | Omit = omit,
        agent: str | Omit = omit,
        message_id: str | Omit = omit,
        model: message_send_params.Model | Omit = omit,
        no_reply: bool | Omit = omit,
        system: str | Omit = omit,
        tools: Dict[str, bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageSendResponse:
        """
        Create and send a new message to a session, streaming the AI response.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._post(
            f"/session/{session_id}/message",
            body=maybe_transform(
                {
                    "parts": parts,
                    "agent": agent,
                    "message_id": message_id,
                    "model": model,
                    "no_reply": no_reply,
                    "system": system,
                    "tools": tools,
                },
                message_send_params.MessageSendParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"directory": directory}, message_send_params.MessageSendParams),
            ),
            cast_to=MessageSendResponse,
        )


class AsyncMessageResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMessageResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kaaass/opencode-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncMessageResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMessageResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kaaass/opencode-sdk#with_streaming_response
        """
        return AsyncMessageResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        message_id: str,
        *,
        session_id: str,
        directory: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageRetrieveResponse:
        """
        Retrieve a specific message from a session by its message ID.

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
        return await self._get(
            f"/session/{session_id}/message/{message_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"directory": directory}, message_retrieve_params.MessageRetrieveParams
                ),
            ),
            cast_to=MessageRetrieveResponse,
        )

    async def get_all(
        self,
        session_id: str,
        *,
        directory: str | Omit = omit,
        limit: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageGetAllResponse:
        """
        Retrieve all messages in a session, including user prompts and AI responses.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._get(
            f"/session/{session_id}/message",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "directory": directory,
                        "limit": limit,
                    },
                    message_get_all_params.MessageGetAllParams,
                ),
            ),
            cast_to=MessageGetAllResponse,
        )

    async def send(
        self,
        session_id: str,
        *,
        parts: Iterable[message_send_params.Part],
        directory: str | Omit = omit,
        agent: str | Omit = omit,
        message_id: str | Omit = omit,
        model: message_send_params.Model | Omit = omit,
        no_reply: bool | Omit = omit,
        system: str | Omit = omit,
        tools: Dict[str, bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MessageSendResponse:
        """
        Create and send a new message to a session, streaming the AI response.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._post(
            f"/session/{session_id}/message",
            body=await async_maybe_transform(
                {
                    "parts": parts,
                    "agent": agent,
                    "message_id": message_id,
                    "model": model,
                    "no_reply": no_reply,
                    "system": system,
                    "tools": tools,
                },
                message_send_params.MessageSendParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"directory": directory}, message_send_params.MessageSendParams),
            ),
            cast_to=MessageSendResponse,
        )


class MessageResourceWithRawResponse:
    def __init__(self, message: MessageResource) -> None:
        self._message = message

        self.retrieve = to_raw_response_wrapper(
            message.retrieve,
        )
        self.get_all = to_raw_response_wrapper(
            message.get_all,
        )
        self.send = to_raw_response_wrapper(
            message.send,
        )


class AsyncMessageResourceWithRawResponse:
    def __init__(self, message: AsyncMessageResource) -> None:
        self._message = message

        self.retrieve = async_to_raw_response_wrapper(
            message.retrieve,
        )
        self.get_all = async_to_raw_response_wrapper(
            message.get_all,
        )
        self.send = async_to_raw_response_wrapper(
            message.send,
        )


class MessageResourceWithStreamingResponse:
    def __init__(self, message: MessageResource) -> None:
        self._message = message

        self.retrieve = to_streamed_response_wrapper(
            message.retrieve,
        )
        self.get_all = to_streamed_response_wrapper(
            message.get_all,
        )
        self.send = to_streamed_response_wrapper(
            message.send,
        )


class AsyncMessageResourceWithStreamingResponse:
    def __init__(self, message: AsyncMessageResource) -> None:
        self._message = message

        self.retrieve = async_to_streamed_response_wrapper(
            message.retrieve,
        )
        self.get_all = async_to_streamed_response_wrapper(
            message.get_all,
        )
        self.send = async_to_streamed_response_wrapper(
            message.send,
        )
