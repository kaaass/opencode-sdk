# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import path_retrieve_params
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
from ..types.path_retrieve_response import PathRetrieveResponse

__all__ = ["PathResource", "AsyncPathResource"]


class PathResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PathResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/opencode-sdk-python#accessing-raw-response-data-eg-headers
        """
        return PathResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PathResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/opencode-sdk-python#with_streaming_response
        """
        return PathResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        directory: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PathRetrieveResponse:
        """
        Get the current path

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/path",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"directory": directory}, path_retrieve_params.PathRetrieveParams),
            ),
            cast_to=PathRetrieveResponse,
        )


class AsyncPathResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPathResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/opencode-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPathResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPathResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/opencode-sdk-python#with_streaming_response
        """
        return AsyncPathResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        directory: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PathRetrieveResponse:
        """
        Get the current path

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/path",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"directory": directory}, path_retrieve_params.PathRetrieveParams),
            ),
            cast_to=PathRetrieveResponse,
        )


class PathResourceWithRawResponse:
    def __init__(self, path: PathResource) -> None:
        self._path = path

        self.retrieve = to_raw_response_wrapper(
            path.retrieve,
        )


class AsyncPathResourceWithRawResponse:
    def __init__(self, path: AsyncPathResource) -> None:
        self._path = path

        self.retrieve = async_to_raw_response_wrapper(
            path.retrieve,
        )


class PathResourceWithStreamingResponse:
    def __init__(self, path: PathResource) -> None:
        self._path = path

        self.retrieve = to_streamed_response_wrapper(
            path.retrieve,
        )


class AsyncPathResourceWithStreamingResponse:
    def __init__(self, path: AsyncPathResource) -> None:
        self._path = path

        self.retrieve = async_to_streamed_response_wrapper(
            path.retrieve,
        )
