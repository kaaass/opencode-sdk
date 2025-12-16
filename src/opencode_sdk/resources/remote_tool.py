# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict

import httpx

from ..types import remote_tool_list_params, remote_tool_register_params, remote_tool_unregister_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ..types.remote_tool_list_response import RemoteToolListResponse
from ..types.remote_tool_register_response import RemoteToolRegisterResponse
from ..types.remote_tool_unregister_response import RemoteToolUnregisterResponse

__all__ = ["RemoteToolResource", "AsyncRemoteToolResource"]


class RemoteToolResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RemoteToolResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kaaass/opencode-sdk#accessing-raw-response-data-eg-headers
        """
        return RemoteToolResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RemoteToolResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kaaass/opencode-sdk#with_streaming_response
        """
        return RemoteToolResourceWithStreamingResponse(self)

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
    ) -> RemoteToolListResponse:
        """
        Get a list of all registered remote tools.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/remote-tool",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"directory": directory}, remote_tool_list_params.RemoteToolListParams),
            ),
            cast_to=RemoteToolListResponse,
        )

    def register(
        self,
        *,
        id: str,
        description: str,
        parameters: Dict[str, object],
        directory: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RemoteToolRegisterResponse:
        """
        Register a new remote tool that requires external execution.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/remote-tool",
            body=maybe_transform(
                {
                    "id": id,
                    "description": description,
                    "parameters": parameters,
                },
                remote_tool_register_params.RemoteToolRegisterParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"directory": directory}, remote_tool_register_params.RemoteToolRegisterParams),
            ),
            cast_to=RemoteToolRegisterResponse,
        )

    def unregister(
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
    ) -> RemoteToolUnregisterResponse:
        """
        Remove a registered remote tool.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/remote-tool/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"directory": directory}, remote_tool_unregister_params.RemoteToolUnregisterParams
                ),
            ),
            cast_to=RemoteToolUnregisterResponse,
        )


class AsyncRemoteToolResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRemoteToolResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kaaass/opencode-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncRemoteToolResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRemoteToolResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kaaass/opencode-sdk#with_streaming_response
        """
        return AsyncRemoteToolResourceWithStreamingResponse(self)

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
    ) -> RemoteToolListResponse:
        """
        Get a list of all registered remote tools.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/remote-tool",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"directory": directory}, remote_tool_list_params.RemoteToolListParams
                ),
            ),
            cast_to=RemoteToolListResponse,
        )

    async def register(
        self,
        *,
        id: str,
        description: str,
        parameters: Dict[str, object],
        directory: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RemoteToolRegisterResponse:
        """
        Register a new remote tool that requires external execution.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/remote-tool",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "description": description,
                    "parameters": parameters,
                },
                remote_tool_register_params.RemoteToolRegisterParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"directory": directory}, remote_tool_register_params.RemoteToolRegisterParams
                ),
            ),
            cast_to=RemoteToolRegisterResponse,
        )

    async def unregister(
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
    ) -> RemoteToolUnregisterResponse:
        """
        Remove a registered remote tool.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/remote-tool/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"directory": directory}, remote_tool_unregister_params.RemoteToolUnregisterParams
                ),
            ),
            cast_to=RemoteToolUnregisterResponse,
        )


class RemoteToolResourceWithRawResponse:
    def __init__(self, remote_tool: RemoteToolResource) -> None:
        self._remote_tool = remote_tool

        self.list = to_raw_response_wrapper(
            remote_tool.list,
        )
        self.register = to_raw_response_wrapper(
            remote_tool.register,
        )
        self.unregister = to_raw_response_wrapper(
            remote_tool.unregister,
        )


class AsyncRemoteToolResourceWithRawResponse:
    def __init__(self, remote_tool: AsyncRemoteToolResource) -> None:
        self._remote_tool = remote_tool

        self.list = async_to_raw_response_wrapper(
            remote_tool.list,
        )
        self.register = async_to_raw_response_wrapper(
            remote_tool.register,
        )
        self.unregister = async_to_raw_response_wrapper(
            remote_tool.unregister,
        )


class RemoteToolResourceWithStreamingResponse:
    def __init__(self, remote_tool: RemoteToolResource) -> None:
        self._remote_tool = remote_tool

        self.list = to_streamed_response_wrapper(
            remote_tool.list,
        )
        self.register = to_streamed_response_wrapper(
            remote_tool.register,
        )
        self.unregister = to_streamed_response_wrapper(
            remote_tool.unregister,
        )


class AsyncRemoteToolResourceWithStreamingResponse:
    def __init__(self, remote_tool: AsyncRemoteToolResource) -> None:
        self._remote_tool = remote_tool

        self.list = async_to_streamed_response_wrapper(
            remote_tool.list,
        )
        self.register = async_to_streamed_response_wrapper(
            remote_tool.register,
        )
        self.unregister = async_to_streamed_response_wrapper(
            remote_tool.unregister,
        )
