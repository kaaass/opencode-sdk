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
from ...types.experimental import (
    worktree_list_params,
    worktree_reset_params,
    worktree_create_params,
    worktree_remove_params,
)
from ...types.experimental.worktree_list_response import WorktreeListResponse
from ...types.experimental.worktree_reset_response import WorktreeResetResponse
from ...types.experimental.worktree_create_response import WorktreeCreateResponse
from ...types.experimental.worktree_remove_response import WorktreeRemoveResponse

__all__ = ["WorktreeResource", "AsyncWorktreeResource"]


class WorktreeResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> WorktreeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kaaass/opencode-sdk#accessing-raw-response-data-eg-headers
        """
        return WorktreeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WorktreeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kaaass/opencode-sdk#with_streaming_response
        """
        return WorktreeResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        directory: str | Omit = omit,
        workspace: str | Omit = omit,
        name: str | Omit = omit,
        start_command: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorktreeCreateResponse:
        """
        Create a new git worktree for the current project and run any configured startup
        scripts.

        Args:
          start_command: Additional startup script to run after the project's start command

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/experimental/worktree",
            body=maybe_transform(
                {
                    "name": name,
                    "start_command": start_command,
                },
                worktree_create_params.WorktreeCreateParams,
            ),
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
                    worktree_create_params.WorktreeCreateParams,
                ),
            ),
            cast_to=WorktreeCreateResponse,
        )

    def list(
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
    ) -> WorktreeListResponse:
        """
        List all sandbox worktrees for the current project.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/experimental/worktree",
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
                    worktree_list_params.WorktreeListParams,
                ),
            ),
            cast_to=WorktreeListResponse,
        )

    def remove(
        self,
        *,
        body_directory: str,
        query_directory: str | Omit = omit,
        workspace: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorktreeRemoveResponse:
        """
        Remove a git worktree and delete its branch.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._delete(
            "/experimental/worktree",
            body=maybe_transform({"body_directory": body_directory}, worktree_remove_params.WorktreeRemoveParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "query_directory": query_directory,
                        "workspace": workspace,
                    },
                    worktree_remove_params.WorktreeRemoveParams,
                ),
            ),
            cast_to=WorktreeRemoveResponse,
        )

    def reset(
        self,
        *,
        body_directory: str,
        query_directory: str | Omit = omit,
        workspace: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorktreeResetResponse:
        """
        Reset a worktree branch to the primary default branch.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/experimental/worktree/reset",
            body=maybe_transform({"body_directory": body_directory}, worktree_reset_params.WorktreeResetParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "query_directory": query_directory,
                        "workspace": workspace,
                    },
                    worktree_reset_params.WorktreeResetParams,
                ),
            ),
            cast_to=WorktreeResetResponse,
        )


class AsyncWorktreeResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncWorktreeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kaaass/opencode-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncWorktreeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWorktreeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kaaass/opencode-sdk#with_streaming_response
        """
        return AsyncWorktreeResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        directory: str | Omit = omit,
        workspace: str | Omit = omit,
        name: str | Omit = omit,
        start_command: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorktreeCreateResponse:
        """
        Create a new git worktree for the current project and run any configured startup
        scripts.

        Args:
          start_command: Additional startup script to run after the project's start command

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/experimental/worktree",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "start_command": start_command,
                },
                worktree_create_params.WorktreeCreateParams,
            ),
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
                    worktree_create_params.WorktreeCreateParams,
                ),
            ),
            cast_to=WorktreeCreateResponse,
        )

    async def list(
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
    ) -> WorktreeListResponse:
        """
        List all sandbox worktrees for the current project.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/experimental/worktree",
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
                    worktree_list_params.WorktreeListParams,
                ),
            ),
            cast_to=WorktreeListResponse,
        )

    async def remove(
        self,
        *,
        body_directory: str,
        query_directory: str | Omit = omit,
        workspace: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorktreeRemoveResponse:
        """
        Remove a git worktree and delete its branch.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._delete(
            "/experimental/worktree",
            body=await async_maybe_transform(
                {"body_directory": body_directory}, worktree_remove_params.WorktreeRemoveParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "query_directory": query_directory,
                        "workspace": workspace,
                    },
                    worktree_remove_params.WorktreeRemoveParams,
                ),
            ),
            cast_to=WorktreeRemoveResponse,
        )

    async def reset(
        self,
        *,
        body_directory: str,
        query_directory: str | Omit = omit,
        workspace: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorktreeResetResponse:
        """
        Reset a worktree branch to the primary default branch.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/experimental/worktree/reset",
            body=await async_maybe_transform(
                {"body_directory": body_directory}, worktree_reset_params.WorktreeResetParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "query_directory": query_directory,
                        "workspace": workspace,
                    },
                    worktree_reset_params.WorktreeResetParams,
                ),
            ),
            cast_to=WorktreeResetResponse,
        )


class WorktreeResourceWithRawResponse:
    def __init__(self, worktree: WorktreeResource) -> None:
        self._worktree = worktree

        self.create = to_raw_response_wrapper(
            worktree.create,
        )
        self.list = to_raw_response_wrapper(
            worktree.list,
        )
        self.remove = to_raw_response_wrapper(
            worktree.remove,
        )
        self.reset = to_raw_response_wrapper(
            worktree.reset,
        )


class AsyncWorktreeResourceWithRawResponse:
    def __init__(self, worktree: AsyncWorktreeResource) -> None:
        self._worktree = worktree

        self.create = async_to_raw_response_wrapper(
            worktree.create,
        )
        self.list = async_to_raw_response_wrapper(
            worktree.list,
        )
        self.remove = async_to_raw_response_wrapper(
            worktree.remove,
        )
        self.reset = async_to_raw_response_wrapper(
            worktree.reset,
        )


class WorktreeResourceWithStreamingResponse:
    def __init__(self, worktree: WorktreeResource) -> None:
        self._worktree = worktree

        self.create = to_streamed_response_wrapper(
            worktree.create,
        )
        self.list = to_streamed_response_wrapper(
            worktree.list,
        )
        self.remove = to_streamed_response_wrapper(
            worktree.remove,
        )
        self.reset = to_streamed_response_wrapper(
            worktree.reset,
        )


class AsyncWorktreeResourceWithStreamingResponse:
    def __init__(self, worktree: AsyncWorktreeResource) -> None:
        self._worktree = worktree

        self.create = async_to_streamed_response_wrapper(
            worktree.create,
        )
        self.list = async_to_streamed_response_wrapper(
            worktree.list,
        )
        self.remove = async_to_streamed_response_wrapper(
            worktree.remove,
        )
        self.reset = async_to_streamed_response_wrapper(
            worktree.reset,
        )
