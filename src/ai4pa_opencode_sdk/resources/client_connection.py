# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import client_connection_close_params
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
from ..types.client_connection_close_response import ClientConnectionCloseResponse

__all__ = ["ClientConnectionResource", "AsyncClientConnectionResource"]


class ClientConnectionResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ClientConnectionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kaaass/opencode-sdk#accessing-raw-response-data-eg-headers
        """
        return ClientConnectionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ClientConnectionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kaaass/opencode-sdk#with_streaming_response
        """
        return ClientConnectionResourceWithStreamingResponse(self)

    def close(
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
    ) -> ClientConnectionCloseResponse:
        """
        Close the ClientConnectionContext (within the current Instance) keyed by
        X-Connection-ID header.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._delete(
            "/client-connection",
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
                    client_connection_close_params.ClientConnectionCloseParams,
                ),
            ),
            cast_to=ClientConnectionCloseResponse,
        )


class AsyncClientConnectionResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncClientConnectionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kaaass/opencode-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncClientConnectionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncClientConnectionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kaaass/opencode-sdk#with_streaming_response
        """
        return AsyncClientConnectionResourceWithStreamingResponse(self)

    async def close(
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
    ) -> ClientConnectionCloseResponse:
        """
        Close the ClientConnectionContext (within the current Instance) keyed by
        X-Connection-ID header.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._delete(
            "/client-connection",
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
                    client_connection_close_params.ClientConnectionCloseParams,
                ),
            ),
            cast_to=ClientConnectionCloseResponse,
        )


class ClientConnectionResourceWithRawResponse:
    def __init__(self, client_connection: ClientConnectionResource) -> None:
        self._client_connection = client_connection

        self.close = to_raw_response_wrapper(
            client_connection.close,
        )


class AsyncClientConnectionResourceWithRawResponse:
    def __init__(self, client_connection: AsyncClientConnectionResource) -> None:
        self._client_connection = client_connection

        self.close = async_to_raw_response_wrapper(
            client_connection.close,
        )


class ClientConnectionResourceWithStreamingResponse:
    def __init__(self, client_connection: ClientConnectionResource) -> None:
        self._client_connection = client_connection

        self.close = to_streamed_response_wrapper(
            client_connection.close,
        )


class AsyncClientConnectionResourceWithStreamingResponse:
    def __init__(self, client_connection: AsyncClientConnectionResource) -> None:
        self._client_connection = client_connection

        self.close = async_to_streamed_response_wrapper(
            client_connection.close,
        )
