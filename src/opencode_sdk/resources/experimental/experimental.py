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
from ...types import experimental_get_resources_params, experimental_list_sessions_params
from .console import (
    ConsoleResource,
    AsyncConsoleResource,
    ConsoleResourceWithRawResponse,
    AsyncConsoleResourceWithRawResponse,
    ConsoleResourceWithStreamingResponse,
    AsyncConsoleResourceWithStreamingResponse,
)
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
from .workspace import (
    WorkspaceResource,
    AsyncWorkspaceResource,
    WorkspaceResourceWithRawResponse,
    AsyncWorkspaceResourceWithRawResponse,
    WorkspaceResourceWithStreamingResponse,
    AsyncWorkspaceResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.experimental_get_resources_response import ExperimentalGetResourcesResponse
from ...types.experimental_list_sessions_response import ExperimentalListSessionsResponse

__all__ = ["ExperimentalResource", "AsyncExperimentalResource"]


class ExperimentalResource(SyncAPIResource):
    @cached_property
    def tool(self) -> ToolResource:
        return ToolResource(self._client)

    @cached_property
    def worktree(self) -> WorktreeResource:
        return WorktreeResource(self._client)

    @cached_property
    def console(self) -> ConsoleResource:
        return ConsoleResource(self._client)

    @cached_property
    def workspace(self) -> WorkspaceResource:
        return WorkspaceResource(self._client)

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
        workspace: str | Omit = omit,
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
                    {
                        "directory": directory,
                        "workspace": workspace,
                    },
                    experimental_get_resources_params.ExperimentalGetResourcesParams,
                ),
            ),
            cast_to=ExperimentalGetResourcesResponse,
        )

    def list_sessions(
        self,
        *,
        archived: bool | Omit = omit,
        cursor: float | Omit = omit,
        directory: str | Omit = omit,
        limit: float | Omit = omit,
        roots: bool | Omit = omit,
        search: str | Omit = omit,
        start: float | Omit = omit,
        workspace: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExperimentalListSessionsResponse:
        """
        Get a list of all OpenCode sessions across projects, sorted by most recently
        updated. Archived sessions are excluded by default.

        Args:
          archived: Include archived sessions (default false)

          cursor: Return sessions updated before this timestamp (milliseconds since epoch)

          directory: Filter sessions by project directory

          limit: Maximum number of sessions to return

          roots: Only return root sessions (no parentID)

          search: Filter sessions by title (case-insensitive)

          start: Filter sessions updated on or after this timestamp (milliseconds since epoch)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/experimental/session",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "archived": archived,
                        "cursor": cursor,
                        "directory": directory,
                        "limit": limit,
                        "roots": roots,
                        "search": search,
                        "start": start,
                        "workspace": workspace,
                    },
                    experimental_list_sessions_params.ExperimentalListSessionsParams,
                ),
            ),
            cast_to=ExperimentalListSessionsResponse,
        )


class AsyncExperimentalResource(AsyncAPIResource):
    @cached_property
    def tool(self) -> AsyncToolResource:
        return AsyncToolResource(self._client)

    @cached_property
    def worktree(self) -> AsyncWorktreeResource:
        return AsyncWorktreeResource(self._client)

    @cached_property
    def console(self) -> AsyncConsoleResource:
        return AsyncConsoleResource(self._client)

    @cached_property
    def workspace(self) -> AsyncWorkspaceResource:
        return AsyncWorkspaceResource(self._client)

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
        workspace: str | Omit = omit,
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
                    {
                        "directory": directory,
                        "workspace": workspace,
                    },
                    experimental_get_resources_params.ExperimentalGetResourcesParams,
                ),
            ),
            cast_to=ExperimentalGetResourcesResponse,
        )

    async def list_sessions(
        self,
        *,
        archived: bool | Omit = omit,
        cursor: float | Omit = omit,
        directory: str | Omit = omit,
        limit: float | Omit = omit,
        roots: bool | Omit = omit,
        search: str | Omit = omit,
        start: float | Omit = omit,
        workspace: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExperimentalListSessionsResponse:
        """
        Get a list of all OpenCode sessions across projects, sorted by most recently
        updated. Archived sessions are excluded by default.

        Args:
          archived: Include archived sessions (default false)

          cursor: Return sessions updated before this timestamp (milliseconds since epoch)

          directory: Filter sessions by project directory

          limit: Maximum number of sessions to return

          roots: Only return root sessions (no parentID)

          search: Filter sessions by title (case-insensitive)

          start: Filter sessions updated on or after this timestamp (milliseconds since epoch)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/experimental/session",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "archived": archived,
                        "cursor": cursor,
                        "directory": directory,
                        "limit": limit,
                        "roots": roots,
                        "search": search,
                        "start": start,
                        "workspace": workspace,
                    },
                    experimental_list_sessions_params.ExperimentalListSessionsParams,
                ),
            ),
            cast_to=ExperimentalListSessionsResponse,
        )


class ExperimentalResourceWithRawResponse:
    def __init__(self, experimental: ExperimentalResource) -> None:
        self._experimental = experimental

        self.get_resources = to_raw_response_wrapper(
            experimental.get_resources,
        )
        self.list_sessions = to_raw_response_wrapper(
            experimental.list_sessions,
        )

    @cached_property
    def tool(self) -> ToolResourceWithRawResponse:
        return ToolResourceWithRawResponse(self._experimental.tool)

    @cached_property
    def worktree(self) -> WorktreeResourceWithRawResponse:
        return WorktreeResourceWithRawResponse(self._experimental.worktree)

    @cached_property
    def console(self) -> ConsoleResourceWithRawResponse:
        return ConsoleResourceWithRawResponse(self._experimental.console)

    @cached_property
    def workspace(self) -> WorkspaceResourceWithRawResponse:
        return WorkspaceResourceWithRawResponse(self._experimental.workspace)


class AsyncExperimentalResourceWithRawResponse:
    def __init__(self, experimental: AsyncExperimentalResource) -> None:
        self._experimental = experimental

        self.get_resources = async_to_raw_response_wrapper(
            experimental.get_resources,
        )
        self.list_sessions = async_to_raw_response_wrapper(
            experimental.list_sessions,
        )

    @cached_property
    def tool(self) -> AsyncToolResourceWithRawResponse:
        return AsyncToolResourceWithRawResponse(self._experimental.tool)

    @cached_property
    def worktree(self) -> AsyncWorktreeResourceWithRawResponse:
        return AsyncWorktreeResourceWithRawResponse(self._experimental.worktree)

    @cached_property
    def console(self) -> AsyncConsoleResourceWithRawResponse:
        return AsyncConsoleResourceWithRawResponse(self._experimental.console)

    @cached_property
    def workspace(self) -> AsyncWorkspaceResourceWithRawResponse:
        return AsyncWorkspaceResourceWithRawResponse(self._experimental.workspace)


class ExperimentalResourceWithStreamingResponse:
    def __init__(self, experimental: ExperimentalResource) -> None:
        self._experimental = experimental

        self.get_resources = to_streamed_response_wrapper(
            experimental.get_resources,
        )
        self.list_sessions = to_streamed_response_wrapper(
            experimental.list_sessions,
        )

    @cached_property
    def tool(self) -> ToolResourceWithStreamingResponse:
        return ToolResourceWithStreamingResponse(self._experimental.tool)

    @cached_property
    def worktree(self) -> WorktreeResourceWithStreamingResponse:
        return WorktreeResourceWithStreamingResponse(self._experimental.worktree)

    @cached_property
    def console(self) -> ConsoleResourceWithStreamingResponse:
        return ConsoleResourceWithStreamingResponse(self._experimental.console)

    @cached_property
    def workspace(self) -> WorkspaceResourceWithStreamingResponse:
        return WorkspaceResourceWithStreamingResponse(self._experimental.workspace)


class AsyncExperimentalResourceWithStreamingResponse:
    def __init__(self, experimental: AsyncExperimentalResource) -> None:
        self._experimental = experimental

        self.get_resources = async_to_streamed_response_wrapper(
            experimental.get_resources,
        )
        self.list_sessions = async_to_streamed_response_wrapper(
            experimental.list_sessions,
        )

    @cached_property
    def tool(self) -> AsyncToolResourceWithStreamingResponse:
        return AsyncToolResourceWithStreamingResponse(self._experimental.tool)

    @cached_property
    def worktree(self) -> AsyncWorktreeResourceWithStreamingResponse:
        return AsyncWorktreeResourceWithStreamingResponse(self._experimental.worktree)

    @cached_property
    def console(self) -> AsyncConsoleResourceWithStreamingResponse:
        return AsyncConsoleResourceWithStreamingResponse(self._experimental.console)

    @cached_property
    def workspace(self) -> AsyncWorkspaceResourceWithStreamingResponse:
        return AsyncWorkspaceResourceWithStreamingResponse(self._experimental.workspace)
