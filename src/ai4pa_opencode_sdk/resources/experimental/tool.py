# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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
from ...types.experimental import tool_list_params, tool_list_ids_params
from ...types.experimental.tool_list_response import ToolListResponse
from ...types.experimental.tool_list_ids_response import ToolListIDsResponse

__all__ = ["ToolResource", "AsyncToolResource"]


class ToolResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ToolResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/opencode-sdk-python#accessing-raw-response-data-eg-headers
        """
        return ToolResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ToolResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/opencode-sdk-python#with_streaming_response
        """
        return ToolResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        model: str,
        provider: str,
        directory: str | Omit = omit,
        workspace: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ToolListResponse:
        """
        Get a list of available tools with their JSON schema parameters for a specific
        provider and model combination.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/experimental/tool",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "model": model,
                        "provider": provider,
                        "directory": directory,
                        "workspace": workspace,
                    },
                    tool_list_params.ToolListParams,
                ),
            ),
            cast_to=ToolListResponse,
        )

    def list_ids(
        self,
        *,
        directory: str | Omit = omit,
        workspace: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ToolListIDsResponse:
        """
        Get a list of all available tool IDs, including both built-in tools and
        dynamically registered tools.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/experimental/tool/ids",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "directory": directory,
                        "workspace": workspace,
                    },
                    tool_list_ids_params.ToolListIDsParams,
                ),
            ),
            cast_to=ToolListIDsResponse,
        )


class AsyncToolResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncToolResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/opencode-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncToolResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncToolResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/opencode-sdk-python#with_streaming_response
        """
        return AsyncToolResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        model: str,
        provider: str,
        directory: str | Omit = omit,
        workspace: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ToolListResponse:
        """
        Get a list of available tools with their JSON schema parameters for a specific
        provider and model combination.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/experimental/tool",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "model": model,
                        "provider": provider,
                        "directory": directory,
                        "workspace": workspace,
                    },
                    tool_list_params.ToolListParams,
                ),
            ),
            cast_to=ToolListResponse,
        )

    async def list_ids(
        self,
        *,
        directory: str | Omit = omit,
        workspace: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ToolListIDsResponse:
        """
        Get a list of all available tool IDs, including both built-in tools and
        dynamically registered tools.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/experimental/tool/ids",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "directory": directory,
                        "workspace": workspace,
                    },
                    tool_list_ids_params.ToolListIDsParams,
                ),
            ),
            cast_to=ToolListIDsResponse,
        )


class ToolResourceWithRawResponse:
    def __init__(self, tool: ToolResource) -> None:
        self._tool = tool

        self.list = to_raw_response_wrapper(
            tool.list,
        )
        self.list_ids = to_raw_response_wrapper(
            tool.list_ids,
        )


class AsyncToolResourceWithRawResponse:
    def __init__(self, tool: AsyncToolResource) -> None:
        self._tool = tool

        self.list = async_to_raw_response_wrapper(
            tool.list,
        )
        self.list_ids = async_to_raw_response_wrapper(
            tool.list_ids,
        )


class ToolResourceWithStreamingResponse:
    def __init__(self, tool: ToolResource) -> None:
        self._tool = tool

        self.list = to_streamed_response_wrapper(
            tool.list,
        )
        self.list_ids = to_streamed_response_wrapper(
            tool.list_ids,
        )


class AsyncToolResourceWithStreamingResponse:
    def __init__(self, tool: AsyncToolResource) -> None:
        self._tool = tool

        self.list = async_to_streamed_response_wrapper(
            tool.list,
        )
        self.list_ids = async_to_streamed_response_wrapper(
            tool.list_ids,
        )
