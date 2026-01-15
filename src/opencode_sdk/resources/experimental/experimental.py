# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .tool import (
    ToolResource,
    AsyncToolResource,
    ToolResourceWithRawResponse,
    AsyncToolResourceWithRawResponse,
    ToolResourceWithStreamingResponse,
    AsyncToolResourceWithStreamingResponse,
)
from ...types import experimental_get_resources_params
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from .worktree import (
    WorktreeResource,
    AsyncWorktreeResource,
    WorktreeResourceWithRawResponse,
    AsyncWorktreeResourceWithRawResponse,
    WorktreeResourceWithStreamingResponse,
    AsyncWorktreeResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.experimental_get_resources_response import ExperimentalGetResourcesResponse

__all__ = ["ExperimentalResource", "AsyncExperimentalResource"]


class ExperimentalResource(SyncAPIResource):
    @cached_property
    def tool(self) -> ToolResource:
        return ToolResource(self._client)

    @cached_property
    def worktree(self) -> WorktreeResource:
        return WorktreeResource(self._client)

    @cached_property
    def with_raw_response(self) -> ExperimentalResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kaaass/opencode-sdk#accessing-raw-response-data-eg-headers
        """
        return ExperimentalResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExperimentalResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kaaass/opencode-sdk#with_streaming_response
        """
        return ExperimentalResourceWithStreamingResponse(self)

    def get_resources(
        self,
        *,
        directory: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExperimentalGetResourcesResponse:
        """Get all available MCP resources from connected servers.

        Optionally filter by
        name.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/experimental/resource",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"directory": directory}, experimental_get_resources_params.ExperimentalGetResourcesParams
                ),
            ),
            cast_to=ExperimentalGetResourcesResponse,
        )


class AsyncExperimentalResource(AsyncAPIResource):
    @cached_property
    def tool(self) -> AsyncToolResource:
        return AsyncToolResource(self._client)

    @cached_property
    def worktree(self) -> AsyncWorktreeResource:
        return AsyncWorktreeResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncExperimentalResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kaaass/opencode-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncExperimentalResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExperimentalResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kaaass/opencode-sdk#with_streaming_response
        """
        return AsyncExperimentalResourceWithStreamingResponse(self)

    async def get_resources(
        self,
        *,
        directory: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExperimentalGetResourcesResponse:
        """Get all available MCP resources from connected servers.

        Optionally filter by
        name.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/experimental/resource",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"directory": directory}, experimental_get_resources_params.ExperimentalGetResourcesParams
                ),
            ),
            cast_to=ExperimentalGetResourcesResponse,
        )


class ExperimentalResourceWithRawResponse:
    def __init__(self, experimental: ExperimentalResource) -> None:
        self._experimental = experimental

        self.get_resources = to_raw_response_wrapper(
            experimental.get_resources,
        )

    @cached_property
    def tool(self) -> ToolResourceWithRawResponse:
        return ToolResourceWithRawResponse(self._experimental.tool)

    @cached_property
    def worktree(self) -> WorktreeResourceWithRawResponse:
        return WorktreeResourceWithRawResponse(self._experimental.worktree)


class AsyncExperimentalResourceWithRawResponse:
    def __init__(self, experimental: AsyncExperimentalResource) -> None:
        self._experimental = experimental

        self.get_resources = async_to_raw_response_wrapper(
            experimental.get_resources,
        )

    @cached_property
    def tool(self) -> AsyncToolResourceWithRawResponse:
        return AsyncToolResourceWithRawResponse(self._experimental.tool)

    @cached_property
    def worktree(self) -> AsyncWorktreeResourceWithRawResponse:
        return AsyncWorktreeResourceWithRawResponse(self._experimental.worktree)


class ExperimentalResourceWithStreamingResponse:
    def __init__(self, experimental: ExperimentalResource) -> None:
        self._experimental = experimental

        self.get_resources = to_streamed_response_wrapper(
            experimental.get_resources,
        )

    @cached_property
    def tool(self) -> ToolResourceWithStreamingResponse:
        return ToolResourceWithStreamingResponse(self._experimental.tool)

    @cached_property
    def worktree(self) -> WorktreeResourceWithStreamingResponse:
        return WorktreeResourceWithStreamingResponse(self._experimental.worktree)


class AsyncExperimentalResourceWithStreamingResponse:
    def __init__(self, experimental: AsyncExperimentalResource) -> None:
        self._experimental = experimental

        self.get_resources = async_to_streamed_response_wrapper(
            experimental.get_resources,
        )

    @cached_property
    def tool(self) -> AsyncToolResourceWithStreamingResponse:
        return AsyncToolResourceWithStreamingResponse(self._experimental.tool)

    @cached_property
    def worktree(self) -> AsyncWorktreeResourceWithStreamingResponse:
        return AsyncWorktreeResourceWithStreamingResponse(self._experimental.worktree)
