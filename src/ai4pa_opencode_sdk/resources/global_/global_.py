# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, cast

import httpx

from .config import (
    ConfigResource,
    AsyncConfigResource,
    ConfigResourceWithRawResponse,
    AsyncConfigResourceWithRawResponse,
    ConfigResourceWithStreamingResponse,
    AsyncConfigResourceWithStreamingResponse,
)
from ...types import global_upgrade_opencode_params
from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._streaming import Stream, AsyncStream
from ..._base_client import make_request_options
from ...types.global_get_events_response import GlobalGetEventsResponse
from ...types.global_get_health_response import GlobalGetHealthResponse
from ...types.global_get_version_response import GlobalGetVersionResponse
from ...types.global_dispose_instance_response import GlobalDisposeInstanceResponse
from ...types.global_upgrade_opencode_response import GlobalUpgradeOpencodeResponse

__all__ = ["GlobalResource", "AsyncGlobalResource"]


class GlobalResource(SyncAPIResource):
    @cached_property
    def config(self) -> ConfigResource:
        return ConfigResource(self._client)

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

    def exit_server(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Exit server"""
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/global/exit",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get_events(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Stream[GlobalGetEventsResponse]:
        """Subscribe to global events from the OpenCode system using server-sent events."""
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        return self._get(
            "/global/event",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GlobalGetEventsResponse,
            stream=True,
            stream_cls=Stream[GlobalGetEventsResponse],
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
        """Get version info"""
        return self._get(
            "/global/version",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GlobalGetVersionResponse,
        )

    def upgrade_opencode(
        self,
        *,
        target: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GlobalUpgradeOpencodeResponse:
        """
        Upgrade opencode to the specified version or latest if not specified.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            GlobalUpgradeOpencodeResponse,
            self._post(
                "/global/upgrade",
                body=maybe_transform({"target": target}, global_upgrade_opencode_params.GlobalUpgradeOpencodeParams),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, GlobalUpgradeOpencodeResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncGlobalResource(AsyncAPIResource):
    @cached_property
    def config(self) -> AsyncConfigResource:
        return AsyncConfigResource(self._client)

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

    async def exit_server(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Exit server"""
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/global/exit",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get_events(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncStream[GlobalGetEventsResponse]:
        """Subscribe to global events from the OpenCode system using server-sent events."""
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        return await self._get(
            "/global/event",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GlobalGetEventsResponse,
            stream=True,
            stream_cls=AsyncStream[GlobalGetEventsResponse],
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
        """Get version info"""
        return await self._get(
            "/global/version",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GlobalGetVersionResponse,
        )

    async def upgrade_opencode(
        self,
        *,
        target: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GlobalUpgradeOpencodeResponse:
        """
        Upgrade opencode to the specified version or latest if not specified.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            GlobalUpgradeOpencodeResponse,
            await self._post(
                "/global/upgrade",
                body=await async_maybe_transform(
                    {"target": target}, global_upgrade_opencode_params.GlobalUpgradeOpencodeParams
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, GlobalUpgradeOpencodeResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class GlobalResourceWithRawResponse:
    def __init__(self, global_: GlobalResource) -> None:
        self._global_ = global_

        self.dispose_instance = to_raw_response_wrapper(
            global_.dispose_instance,
        )
        self.exit_server = to_raw_response_wrapper(
            global_.exit_server,
        )
        self.get_events = to_raw_response_wrapper(
            global_.get_events,
        )
        self.get_health = to_raw_response_wrapper(
            global_.get_health,
        )
        self.get_version = to_raw_response_wrapper(
            global_.get_version,
        )
        self.upgrade_opencode = to_raw_response_wrapper(
            global_.upgrade_opencode,
        )

    @cached_property
    def config(self) -> ConfigResourceWithRawResponse:
        return ConfigResourceWithRawResponse(self._global_.config)


class AsyncGlobalResourceWithRawResponse:
    def __init__(self, global_: AsyncGlobalResource) -> None:
        self._global_ = global_

        self.dispose_instance = async_to_raw_response_wrapper(
            global_.dispose_instance,
        )
        self.exit_server = async_to_raw_response_wrapper(
            global_.exit_server,
        )
        self.get_events = async_to_raw_response_wrapper(
            global_.get_events,
        )
        self.get_health = async_to_raw_response_wrapper(
            global_.get_health,
        )
        self.get_version = async_to_raw_response_wrapper(
            global_.get_version,
        )
        self.upgrade_opencode = async_to_raw_response_wrapper(
            global_.upgrade_opencode,
        )

    @cached_property
    def config(self) -> AsyncConfigResourceWithRawResponse:
        return AsyncConfigResourceWithRawResponse(self._global_.config)


class GlobalResourceWithStreamingResponse:
    def __init__(self, global_: GlobalResource) -> None:
        self._global_ = global_

        self.dispose_instance = to_streamed_response_wrapper(
            global_.dispose_instance,
        )
        self.exit_server = to_streamed_response_wrapper(
            global_.exit_server,
        )
        self.get_events = to_streamed_response_wrapper(
            global_.get_events,
        )
        self.get_health = to_streamed_response_wrapper(
            global_.get_health,
        )
        self.get_version = to_streamed_response_wrapper(
            global_.get_version,
        )
        self.upgrade_opencode = to_streamed_response_wrapper(
            global_.upgrade_opencode,
        )

    @cached_property
    def config(self) -> ConfigResourceWithStreamingResponse:
        return ConfigResourceWithStreamingResponse(self._global_.config)


class AsyncGlobalResourceWithStreamingResponse:
    def __init__(self, global_: AsyncGlobalResource) -> None:
        self._global_ = global_

        self.dispose_instance = async_to_streamed_response_wrapper(
            global_.dispose_instance,
        )
        self.exit_server = async_to_streamed_response_wrapper(
            global_.exit_server,
        )
        self.get_events = async_to_streamed_response_wrapper(
            global_.get_events,
        )
        self.get_health = async_to_streamed_response_wrapper(
            global_.get_health,
        )
        self.get_version = async_to_streamed_response_wrapper(
            global_.get_version,
        )
        self.upgrade_opencode = async_to_streamed_response_wrapper(
            global_.upgrade_opencode,
        )

    @cached_property
    def config(self) -> AsyncConfigResourceWithStreamingResponse:
        return AsyncConfigResourceWithStreamingResponse(self._global_.config)
