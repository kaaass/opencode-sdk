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
from ...types.project import git_initialize_params
from ...types.project.project import Project

__all__ = ["GitResource", "AsyncGitResource"]


class GitResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> GitResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kaaass/opencode-sdk#accessing-raw-response-data-eg-headers
        """
        return GitResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GitResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kaaass/opencode-sdk#with_streaming_response
        """
        return GitResourceWithStreamingResponse(self)

    def initialize(
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
    ) -> Project:
        """
        Create a git repository for the current project and return the refreshed project
        info.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/project/git/init",
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
                    git_initialize_params.GitInitializeParams,
                ),
            ),
            cast_to=Project,
        )


class AsyncGitResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncGitResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kaaass/opencode-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncGitResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGitResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kaaass/opencode-sdk#with_streaming_response
        """
        return AsyncGitResourceWithStreamingResponse(self)

    async def initialize(
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
    ) -> Project:
        """
        Create a git repository for the current project and return the refreshed project
        info.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/project/git/init",
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
                    git_initialize_params.GitInitializeParams,
                ),
            ),
            cast_to=Project,
        )


class GitResourceWithRawResponse:
    def __init__(self, git: GitResource) -> None:
        self._git = git

        self.initialize = to_raw_response_wrapper(
            git.initialize,
        )


class AsyncGitResourceWithRawResponse:
    def __init__(self, git: AsyncGitResource) -> None:
        self._git = git

        self.initialize = async_to_raw_response_wrapper(
            git.initialize,
        )


class GitResourceWithStreamingResponse:
    def __init__(self, git: GitResource) -> None:
        self._git = git

        self.initialize = to_streamed_response_wrapper(
            git.initialize,
        )


class AsyncGitResourceWithStreamingResponse:
    def __init__(self, git: AsyncGitResource) -> None:
        self._git = git

        self.initialize = async_to_streamed_response_wrapper(
            git.initialize,
        )
