# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import Body, Query, Headers, NotGiven, not_given
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._streaming import Stream, AsyncStream
from .._base_client import make_request_options
from ..types.global_get_health_response import GlobalGetHealthResponse
from ..types.global_get_version_response import GlobalGetVersionResponse
from ..types.global_retrieve_events_response import GlobalRetrieveEventsResponse
from ..types.global_dispose_instance_response import GlobalDisposeInstanceResponse

__all__ = ["GlobalResource", "AsyncGlobalResource"]


class GlobalResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> GlobalResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kaaass/opencode-sdk#accessing-raw-response-data-eg-headers
        """
        return GlobalResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GlobalResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kaaass/opencode-sdk#with_streaming_response
        """
        return GlobalResourceWithStreamingResponse(self)

    def dispose_instance(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GlobalDisposeInstanceResponse:
        """Clean up and dispose all OpenCode instances, releasing all resources."""
        return self._post(
            "/global/dispose",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GlobalDisposeInstanceResponse,
        )

    def get_health(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GlobalGetHealthResponse:
        """Get health information about the OpenCode server."""
        return self._get(
            "/global/health",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GlobalGetHealthResponse,
        )

    def get_version(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GlobalGetVersionResponse:
        """Get detailed version information including local, API, and upstream versions."""
        return self._get(
            "/global/version",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GlobalGetVersionResponse,
        )

    def retrieve_events(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Stream[GlobalRetrieveEventsResponse]:
        """Subscribe to global events from the OpenCode system using server-sent events."""
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        return self._get(
            "/global/event",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GlobalRetrieveEventsResponse,
            stream=True,
            stream_cls=Stream[GlobalRetrieveEventsResponse],
        )


class AsyncGlobalResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncGlobalResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kaaass/opencode-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncGlobalResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGlobalResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kaaass/opencode-sdk#with_streaming_response
        """
        return AsyncGlobalResourceWithStreamingResponse(self)

    async def dispose_instance(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GlobalDisposeInstanceResponse:
        """Clean up and dispose all OpenCode instances, releasing all resources."""
        return await self._post(
            "/global/dispose",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GlobalDisposeInstanceResponse,
        )

    async def get_health(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GlobalGetHealthResponse:
        """Get health information about the OpenCode server."""
        return await self._get(
            "/global/health",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GlobalGetHealthResponse,
        )

    async def get_version(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GlobalGetVersionResponse:
        """Get detailed version information including local, API, and upstream versions."""
        return await self._get(
            "/global/version",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GlobalGetVersionResponse,
        )

    async def retrieve_events(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncStream[GlobalRetrieveEventsResponse]:
        """Subscribe to global events from the OpenCode system using server-sent events."""
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        return await self._get(
            "/global/event",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GlobalRetrieveEventsResponse,
            stream=True,
            stream_cls=AsyncStream[GlobalRetrieveEventsResponse],
        )


class GlobalResourceWithRawResponse:
    def __init__(self, global_: GlobalResource) -> None:
        self._global_ = global_

        self.dispose_instance = to_raw_response_wrapper(
            global_.dispose_instance,
        )
        self.get_health = to_raw_response_wrapper(
            global_.get_health,
        )
        self.get_version = to_raw_response_wrapper(
            global_.get_version,
        )
        self.retrieve_events = to_raw_response_wrapper(
            global_.retrieve_events,
        )


class AsyncGlobalResourceWithRawResponse:
    def __init__(self, global_: AsyncGlobalResource) -> None:
        self._global_ = global_

        self.dispose_instance = async_to_raw_response_wrapper(
            global_.dispose_instance,
        )
        self.get_health = async_to_raw_response_wrapper(
            global_.get_health,
        )
        self.get_version = async_to_raw_response_wrapper(
            global_.get_version,
        )
        self.retrieve_events = async_to_raw_response_wrapper(
            global_.retrieve_events,
        )


class GlobalResourceWithStreamingResponse:
    def __init__(self, global_: GlobalResource) -> None:
        self._global_ = global_

        self.dispose_instance = to_streamed_response_wrapper(
            global_.dispose_instance,
        )
        self.get_health = to_streamed_response_wrapper(
            global_.get_health,
        )
        self.get_version = to_streamed_response_wrapper(
            global_.get_version,
        )
        self.retrieve_events = to_streamed_response_wrapper(
            global_.retrieve_events,
        )


class AsyncGlobalResourceWithStreamingResponse:
    def __init__(self, global_: AsyncGlobalResource) -> None:
        self._global_ = global_

        self.dispose_instance = async_to_streamed_response_wrapper(
            global_.dispose_instance,
        )
        self.get_health = async_to_streamed_response_wrapper(
            global_.get_health,
        )
        self.get_version = async_to_streamed_response_wrapper(
            global_.get_version,
        )
        self.retrieve_events = async_to_streamed_response_wrapper(
            global_.retrieve_events,
        )
