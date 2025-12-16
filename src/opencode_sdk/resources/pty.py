# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict

import httpx

from ..types import (
    pty_list_params,
    pty_create_params,
    pty_delete_params,
    pty_update_params,
    pty_connect_params,
    pty_retrieve_params,
)
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.pty_list_response import PtyListResponse
from ..types.pty_create_response import PtyCreateResponse
from ..types.pty_delete_response import PtyDeleteResponse
from ..types.pty_update_response import PtyUpdateResponse
from ..types.pty_connect_response import PtyConnectResponse
from ..types.pty_retrieve_response import PtyRetrieveResponse

__all__ = ["PtyResource", "AsyncPtyResource"]


class PtyResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PtyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kaaass/opencode-sdk#accessing-raw-response-data-eg-headers
        """
        return PtyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PtyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kaaass/opencode-sdk#with_streaming_response
        """
        return PtyResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        directory: str | Omit = omit,
        args: SequenceNotStr[str] | Omit = omit,
        command: str | Omit = omit,
        cwd: str | Omit = omit,
        env: Dict[str, str] | Omit = omit,
        title: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PtyCreateResponse:
        """
        Create a new pseudo-terminal (PTY) session for running shell commands and
        processes.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/pty",
            body=maybe_transform(
                {
                    "args": args,
                    "command": command,
                    "cwd": cwd,
                    "env": env,
                    "title": title,
                },
                pty_create_params.PtyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"directory": directory}, pty_create_params.PtyCreateParams),
            ),
            cast_to=PtyCreateResponse,
        )

    def retrieve(
        self,
        pty_id: str,
        *,
        directory: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PtyRetrieveResponse:
        """
        Retrieve detailed information about a specific pseudo-terminal (PTY) session.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not pty_id:
            raise ValueError(f"Expected a non-empty value for `pty_id` but received {pty_id!r}")
        return self._get(
            f"/pty/{pty_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"directory": directory}, pty_retrieve_params.PtyRetrieveParams),
            ),
            cast_to=PtyRetrieveResponse,
        )

    def update(
        self,
        pty_id: str,
        *,
        directory: str | Omit = omit,
        size: pty_update_params.Size | Omit = omit,
        title: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PtyUpdateResponse:
        """
        Update properties of an existing pseudo-terminal (PTY) session.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not pty_id:
            raise ValueError(f"Expected a non-empty value for `pty_id` but received {pty_id!r}")
        return self._put(
            f"/pty/{pty_id}",
            body=maybe_transform(
                {
                    "size": size,
                    "title": title,
                },
                pty_update_params.PtyUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"directory": directory}, pty_update_params.PtyUpdateParams),
            ),
            cast_to=PtyUpdateResponse,
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
    ) -> PtyListResponse:
        """
        Get a list of all active pseudo-terminal (PTY) sessions managed by OpenCode.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/pty",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"directory": directory}, pty_list_params.PtyListParams),
            ),
            cast_to=PtyListResponse,
        )

    def delete(
        self,
        pty_id: str,
        *,
        directory: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PtyDeleteResponse:
        """
        Remove and terminate a specific pseudo-terminal (PTY) session.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not pty_id:
            raise ValueError(f"Expected a non-empty value for `pty_id` but received {pty_id!r}")
        return self._delete(
            f"/pty/{pty_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"directory": directory}, pty_delete_params.PtyDeleteParams),
            ),
            cast_to=PtyDeleteResponse,
        )

    def connect(
        self,
        pty_id: str,
        *,
        directory: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PtyConnectResponse:
        """
        Establish a WebSocket connection to interact with a pseudo-terminal (PTY)
        session in real-time.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not pty_id:
            raise ValueError(f"Expected a non-empty value for `pty_id` but received {pty_id!r}")
        return self._get(
            f"/pty/{pty_id}/connect",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"directory": directory}, pty_connect_params.PtyConnectParams),
            ),
            cast_to=PtyConnectResponse,
        )


class AsyncPtyResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPtyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kaaass/opencode-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncPtyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPtyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kaaass/opencode-sdk#with_streaming_response
        """
        return AsyncPtyResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        directory: str | Omit = omit,
        args: SequenceNotStr[str] | Omit = omit,
        command: str | Omit = omit,
        cwd: str | Omit = omit,
        env: Dict[str, str] | Omit = omit,
        title: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PtyCreateResponse:
        """
        Create a new pseudo-terminal (PTY) session for running shell commands and
        processes.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/pty",
            body=await async_maybe_transform(
                {
                    "args": args,
                    "command": command,
                    "cwd": cwd,
                    "env": env,
                    "title": title,
                },
                pty_create_params.PtyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"directory": directory}, pty_create_params.PtyCreateParams),
            ),
            cast_to=PtyCreateResponse,
        )

    async def retrieve(
        self,
        pty_id: str,
        *,
        directory: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PtyRetrieveResponse:
        """
        Retrieve detailed information about a specific pseudo-terminal (PTY) session.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not pty_id:
            raise ValueError(f"Expected a non-empty value for `pty_id` but received {pty_id!r}")
        return await self._get(
            f"/pty/{pty_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"directory": directory}, pty_retrieve_params.PtyRetrieveParams),
            ),
            cast_to=PtyRetrieveResponse,
        )

    async def update(
        self,
        pty_id: str,
        *,
        directory: str | Omit = omit,
        size: pty_update_params.Size | Omit = omit,
        title: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PtyUpdateResponse:
        """
        Update properties of an existing pseudo-terminal (PTY) session.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not pty_id:
            raise ValueError(f"Expected a non-empty value for `pty_id` but received {pty_id!r}")
        return await self._put(
            f"/pty/{pty_id}",
            body=await async_maybe_transform(
                {
                    "size": size,
                    "title": title,
                },
                pty_update_params.PtyUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"directory": directory}, pty_update_params.PtyUpdateParams),
            ),
            cast_to=PtyUpdateResponse,
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
    ) -> PtyListResponse:
        """
        Get a list of all active pseudo-terminal (PTY) sessions managed by OpenCode.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/pty",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"directory": directory}, pty_list_params.PtyListParams),
            ),
            cast_to=PtyListResponse,
        )

    async def delete(
        self,
        pty_id: str,
        *,
        directory: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PtyDeleteResponse:
        """
        Remove and terminate a specific pseudo-terminal (PTY) session.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not pty_id:
            raise ValueError(f"Expected a non-empty value for `pty_id` but received {pty_id!r}")
        return await self._delete(
            f"/pty/{pty_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"directory": directory}, pty_delete_params.PtyDeleteParams),
            ),
            cast_to=PtyDeleteResponse,
        )

    async def connect(
        self,
        pty_id: str,
        *,
        directory: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PtyConnectResponse:
        """
        Establish a WebSocket connection to interact with a pseudo-terminal (PTY)
        session in real-time.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not pty_id:
            raise ValueError(f"Expected a non-empty value for `pty_id` but received {pty_id!r}")
        return await self._get(
            f"/pty/{pty_id}/connect",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"directory": directory}, pty_connect_params.PtyConnectParams),
            ),
            cast_to=PtyConnectResponse,
        )


class PtyResourceWithRawResponse:
    def __init__(self, pty: PtyResource) -> None:
        self._pty = pty

        self.create = to_raw_response_wrapper(
            pty.create,
        )
        self.retrieve = to_raw_response_wrapper(
            pty.retrieve,
        )
        self.update = to_raw_response_wrapper(
            pty.update,
        )
        self.list = to_raw_response_wrapper(
            pty.list,
        )
        self.delete = to_raw_response_wrapper(
            pty.delete,
        )
        self.connect = to_raw_response_wrapper(
            pty.connect,
        )


class AsyncPtyResourceWithRawResponse:
    def __init__(self, pty: AsyncPtyResource) -> None:
        self._pty = pty

        self.create = async_to_raw_response_wrapper(
            pty.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            pty.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            pty.update,
        )
        self.list = async_to_raw_response_wrapper(
            pty.list,
        )
        self.delete = async_to_raw_response_wrapper(
            pty.delete,
        )
        self.connect = async_to_raw_response_wrapper(
            pty.connect,
        )


class PtyResourceWithStreamingResponse:
    def __init__(self, pty: PtyResource) -> None:
        self._pty = pty

        self.create = to_streamed_response_wrapper(
            pty.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            pty.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            pty.update,
        )
        self.list = to_streamed_response_wrapper(
            pty.list,
        )
        self.delete = to_streamed_response_wrapper(
            pty.delete,
        )
        self.connect = to_streamed_response_wrapper(
            pty.connect,
        )


class AsyncPtyResourceWithStreamingResponse:
    def __init__(self, pty: AsyncPtyResource) -> None:
        self._pty = pty

        self.create = async_to_streamed_response_wrapper(
            pty.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            pty.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            pty.update,
        )
        self.list = async_to_streamed_response_wrapper(
            pty.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            pty.delete,
        )
        self.connect = async_to_streamed_response_wrapper(
            pty.connect,
        )
