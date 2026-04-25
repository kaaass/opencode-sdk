# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import find_search_params, find_search_files_params, find_search_symbols_params
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
from ..types.find_search_response import FindSearchResponse
from ..types.find_search_files_response import FindSearchFilesResponse
from ..types.find_search_symbols_response import FindSearchSymbolsResponse

__all__ = ["FindResource", "AsyncFindResource"]


class FindResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FindResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/opencode-sdk-python#accessing-raw-response-data-eg-headers
        """
        return FindResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FindResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/opencode-sdk-python#with_streaming_response
        """
        return FindResourceWithStreamingResponse(self)

    def search(
        self,
        *,
        pattern: str,
        directory: str | Omit = omit,
        workspace: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FindSearchResponse:
        """
        Search for text patterns across files in the project using ripgrep.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/find",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "pattern": pattern,
                        "directory": directory,
                        "workspace": workspace,
                    },
                    find_search_params.FindSearchParams,
                ),
            ),
            cast_to=FindSearchResponse,
        )

    def search_files(
        self,
        *,
        query: str,
        directory: str | Omit = omit,
        dirs: Literal["true", "false"] | Omit = omit,
        limit: int | Omit = omit,
        type: Literal["file", "directory"] | Omit = omit,
        workspace: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FindSearchFilesResponse:
        """
        Search for files or directories by name or pattern in the project directory.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/find/file",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "query": query,
                        "directory": directory,
                        "dirs": dirs,
                        "limit": limit,
                        "type": type,
                        "workspace": workspace,
                    },
                    find_search_files_params.FindSearchFilesParams,
                ),
            ),
            cast_to=FindSearchFilesResponse,
        )

    def search_symbols(
        self,
        *,
        query: str,
        directory: str | Omit = omit,
        workspace: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FindSearchSymbolsResponse:
        """
        Search for workspace symbols like functions, classes, and variables using LSP.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/find/symbol",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "query": query,
                        "directory": directory,
                        "workspace": workspace,
                    },
                    find_search_symbols_params.FindSearchSymbolsParams,
                ),
            ),
            cast_to=FindSearchSymbolsResponse,
        )


class AsyncFindResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFindResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/opencode-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFindResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFindResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/opencode-sdk-python#with_streaming_response
        """
        return AsyncFindResourceWithStreamingResponse(self)

    async def search(
        self,
        *,
        pattern: str,
        directory: str | Omit = omit,
        workspace: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FindSearchResponse:
        """
        Search for text patterns across files in the project using ripgrep.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/find",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "pattern": pattern,
                        "directory": directory,
                        "workspace": workspace,
                    },
                    find_search_params.FindSearchParams,
                ),
            ),
            cast_to=FindSearchResponse,
        )

    async def search_files(
        self,
        *,
        query: str,
        directory: str | Omit = omit,
        dirs: Literal["true", "false"] | Omit = omit,
        limit: int | Omit = omit,
        type: Literal["file", "directory"] | Omit = omit,
        workspace: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FindSearchFilesResponse:
        """
        Search for files or directories by name or pattern in the project directory.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/find/file",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "query": query,
                        "directory": directory,
                        "dirs": dirs,
                        "limit": limit,
                        "type": type,
                        "workspace": workspace,
                    },
                    find_search_files_params.FindSearchFilesParams,
                ),
            ),
            cast_to=FindSearchFilesResponse,
        )

    async def search_symbols(
        self,
        *,
        query: str,
        directory: str | Omit = omit,
        workspace: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FindSearchSymbolsResponse:
        """
        Search for workspace symbols like functions, classes, and variables using LSP.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/find/symbol",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "query": query,
                        "directory": directory,
                        "workspace": workspace,
                    },
                    find_search_symbols_params.FindSearchSymbolsParams,
                ),
            ),
            cast_to=FindSearchSymbolsResponse,
        )


class FindResourceWithRawResponse:
    def __init__(self, find: FindResource) -> None:
        self._find = find

        self.search = to_raw_response_wrapper(
            find.search,
        )
        self.search_files = to_raw_response_wrapper(
            find.search_files,
        )
        self.search_symbols = to_raw_response_wrapper(
            find.search_symbols,
        )


class AsyncFindResourceWithRawResponse:
    def __init__(self, find: AsyncFindResource) -> None:
        self._find = find

        self.search = async_to_raw_response_wrapper(
            find.search,
        )
        self.search_files = async_to_raw_response_wrapper(
            find.search_files,
        )
        self.search_symbols = async_to_raw_response_wrapper(
            find.search_symbols,
        )


class FindResourceWithStreamingResponse:
    def __init__(self, find: FindResource) -> None:
        self._find = find

        self.search = to_streamed_response_wrapper(
            find.search,
        )
        self.search_files = to_streamed_response_wrapper(
            find.search_files,
        )
        self.search_symbols = to_streamed_response_wrapper(
            find.search_symbols,
        )


class AsyncFindResourceWithStreamingResponse:
    def __init__(self, find: AsyncFindResource) -> None:
        self._find = find

        self.search = async_to_streamed_response_wrapper(
            find.search,
        )
        self.search_files = async_to_streamed_response_wrapper(
            find.search_files,
        )
        self.search_symbols = async_to_streamed_response_wrapper(
            find.search_symbols,
        )
