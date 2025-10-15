# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import find_retrieve_params, find_retrieve_file_params, find_retrieve_symbol_params
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
from ..types.find_retrieve_response import FindRetrieveResponse
from ..types.find_retrieve_file_response import FindRetrieveFileResponse
from ..types.find_retrieve_symbol_response import FindRetrieveSymbolResponse

__all__ = ["FindResource", "AsyncFindResource"]


class FindResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FindResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kaaass/opencode-sdk#accessing-raw-response-data-eg-headers
        """
        return FindResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FindResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kaaass/opencode-sdk#with_streaming_response
        """
        return FindResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        pattern: str,
        directory: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FindRetrieveResponse:
        """
        Find text in files

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
                    },
                    find_retrieve_params.FindRetrieveParams,
                ),
            ),
            cast_to=FindRetrieveResponse,
        )

    def retrieve_file(
        self,
        *,
        query: str,
        directory: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FindRetrieveFileResponse:
        """
        Find files

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
                    },
                    find_retrieve_file_params.FindRetrieveFileParams,
                ),
            ),
            cast_to=FindRetrieveFileResponse,
        )

    def retrieve_symbol(
        self,
        *,
        query: str,
        directory: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FindRetrieveSymbolResponse:
        """
        Find workspace symbols

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
                    },
                    find_retrieve_symbol_params.FindRetrieveSymbolParams,
                ),
            ),
            cast_to=FindRetrieveSymbolResponse,
        )


class AsyncFindResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFindResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kaaass/opencode-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncFindResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFindResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kaaass/opencode-sdk#with_streaming_response
        """
        return AsyncFindResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        pattern: str,
        directory: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FindRetrieveResponse:
        """
        Find text in files

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
                    },
                    find_retrieve_params.FindRetrieveParams,
                ),
            ),
            cast_to=FindRetrieveResponse,
        )

    async def retrieve_file(
        self,
        *,
        query: str,
        directory: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FindRetrieveFileResponse:
        """
        Find files

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
                    },
                    find_retrieve_file_params.FindRetrieveFileParams,
                ),
            ),
            cast_to=FindRetrieveFileResponse,
        )

    async def retrieve_symbol(
        self,
        *,
        query: str,
        directory: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FindRetrieveSymbolResponse:
        """
        Find workspace symbols

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
                    },
                    find_retrieve_symbol_params.FindRetrieveSymbolParams,
                ),
            ),
            cast_to=FindRetrieveSymbolResponse,
        )


class FindResourceWithRawResponse:
    def __init__(self, find: FindResource) -> None:
        self._find = find

        self.retrieve = to_raw_response_wrapper(
            find.retrieve,
        )
        self.retrieve_file = to_raw_response_wrapper(
            find.retrieve_file,
        )
        self.retrieve_symbol = to_raw_response_wrapper(
            find.retrieve_symbol,
        )


class AsyncFindResourceWithRawResponse:
    def __init__(self, find: AsyncFindResource) -> None:
        self._find = find

        self.retrieve = async_to_raw_response_wrapper(
            find.retrieve,
        )
        self.retrieve_file = async_to_raw_response_wrapper(
            find.retrieve_file,
        )
        self.retrieve_symbol = async_to_raw_response_wrapper(
            find.retrieve_symbol,
        )


class FindResourceWithStreamingResponse:
    def __init__(self, find: FindResource) -> None:
        self._find = find

        self.retrieve = to_streamed_response_wrapper(
            find.retrieve,
        )
        self.retrieve_file = to_streamed_response_wrapper(
            find.retrieve_file,
        )
        self.retrieve_symbol = to_streamed_response_wrapper(
            find.retrieve_symbol,
        )


class AsyncFindResourceWithStreamingResponse:
    def __init__(self, find: AsyncFindResource) -> None:
        self._find = find

        self.retrieve = async_to_streamed_response_wrapper(
            find.retrieve,
        )
        self.retrieve_file = async_to_streamed_response_wrapper(
            find.retrieve_file,
        )
        self.retrieve_symbol = async_to_streamed_response_wrapper(
            find.retrieve_symbol,
        )
