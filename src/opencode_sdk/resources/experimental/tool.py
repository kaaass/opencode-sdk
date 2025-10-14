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
from ...types.experimental import tool_list_ids_params, tool_list_tools_params
from ...types.experimental.tool_list_ids_response import ToolListIDsResponse
from ...types.experimental.tool_list_tools_response import ToolListToolsResponse

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

    def list_ids(
        self,
        *,
        directory: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ToolListIDsResponse:
        """
        List all tool IDs (including built-in and dynamically registered)

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
                query=maybe_transform({"directory": directory}, tool_list_ids_params.ToolListIDsParams),
            ),
            cast_to=ToolListIDsResponse,
        )

    def list_tools(
        self,
        *,
        model: str,
        provider: str,
        directory: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ToolListToolsResponse:
        """
        List tools with JSON schema parameters for a provider/model

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
                    },
                    tool_list_tools_params.ToolListToolsParams,
                ),
            ),
            cast_to=ToolListToolsResponse,
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

    async def list_ids(
        self,
        *,
        directory: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ToolListIDsResponse:
        """
        List all tool IDs (including built-in and dynamically registered)

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
                query=await async_maybe_transform({"directory": directory}, tool_list_ids_params.ToolListIDsParams),
            ),
            cast_to=ToolListIDsResponse,
        )

    async def list_tools(
        self,
        *,
        model: str,
        provider: str,
        directory: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ToolListToolsResponse:
        """
        List tools with JSON schema parameters for a provider/model

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
                    },
                    tool_list_tools_params.ToolListToolsParams,
                ),
            ),
            cast_to=ToolListToolsResponse,
        )


class ToolResourceWithRawResponse:
    def __init__(self, tool: ToolResource) -> None:
        self._tool = tool

        self.list_ids = to_raw_response_wrapper(
            tool.list_ids,
        )
        self.list_tools = to_raw_response_wrapper(
            tool.list_tools,
        )


class AsyncToolResourceWithRawResponse:
    def __init__(self, tool: AsyncToolResource) -> None:
        self._tool = tool

        self.list_ids = async_to_raw_response_wrapper(
            tool.list_ids,
        )
        self.list_tools = async_to_raw_response_wrapper(
            tool.list_tools,
        )


class ToolResourceWithStreamingResponse:
    def __init__(self, tool: ToolResource) -> None:
        self._tool = tool

        self.list_ids = to_streamed_response_wrapper(
            tool.list_ids,
        )
        self.list_tools = to_streamed_response_wrapper(
            tool.list_tools,
        )


class AsyncToolResourceWithStreamingResponse:
    def __init__(self, tool: AsyncToolResource) -> None:
        self._tool = tool

        self.list_ids = async_to_streamed_response_wrapper(
            tool.list_ids,
        )
        self.list_tools = async_to_streamed_response_wrapper(
            tool.list_tools,
        )
