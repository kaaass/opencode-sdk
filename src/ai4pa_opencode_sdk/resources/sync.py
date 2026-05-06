# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable

import httpx

from ..types import sync_start_params, sync_replay_params, sync_list_events_params
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
from ..types.sync_start_response import SyncStartResponse
from ..types.sync_replay_response import SyncReplayResponse
from ..types.sync_list_events_response import SyncListEventsResponse

__all__ = ["SyncResource", "AsyncSyncResource"]


class SyncResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SyncResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kaaass/opencode-sdk#accessing-raw-response-data-eg-headers
        """
        return SyncResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SyncResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kaaass/opencode-sdk#with_streaming_response
        """
        return SyncResourceWithStreamingResponse(self)

    def list_events(
        self,
        *,
        directory: str | Omit = omit,
        workspace: str | Omit = omit,
        body: Dict[str, int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncListEventsResponse:
        """List sync events for all aggregates.

        Keys are aggregate IDs the client already
        knows about, values are the last known sequence ID. Events with seq > value are
        returned for those aggregates. Aggregates not listed in the input get their full
        history.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/sync/history",
            body=maybe_transform(body, sync_list_events_params.SyncListEventsParams),
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
                    sync_list_events_params.SyncListEventsParams,
                ),
            ),
            cast_to=SyncListEventsResponse,
        )

    def replay(
        self,
        *,
        body_directory: str,
        events: Iterable[sync_replay_params.Event],
        query_directory: str | Omit = omit,
        workspace: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncReplayResponse:
        """
        Validate and replay a complete sync event history.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/sync/replay",
            body=maybe_transform(
                {
                    "body_directory": body_directory,
                    "events": events,
                },
                sync_replay_params.SyncReplayParams,
            ),
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
                    sync_replay_params.SyncReplayParams,
                ),
            ),
            cast_to=SyncReplayResponse,
        )

    def start(
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
    ) -> SyncStartResponse:
        """
        Start sync loops for workspaces in the current project that have active
        sessions.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/sync/start",
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
                    sync_start_params.SyncStartParams,
                ),
            ),
            cast_to=SyncStartResponse,
        )


class AsyncSyncResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSyncResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kaaass/opencode-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncSyncResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSyncResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kaaass/opencode-sdk#with_streaming_response
        """
        return AsyncSyncResourceWithStreamingResponse(self)

    async def list_events(
        self,
        *,
        directory: str | Omit = omit,
        workspace: str | Omit = omit,
        body: Dict[str, int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncListEventsResponse:
        """List sync events for all aggregates.

        Keys are aggregate IDs the client already
        knows about, values are the last known sequence ID. Events with seq > value are
        returned for those aggregates. Aggregates not listed in the input get their full
        history.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/sync/history",
            body=await async_maybe_transform(body, sync_list_events_params.SyncListEventsParams),
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
                    sync_list_events_params.SyncListEventsParams,
                ),
            ),
            cast_to=SyncListEventsResponse,
        )

    async def replay(
        self,
        *,
        body_directory: str,
        events: Iterable[sync_replay_params.Event],
        query_directory: str | Omit = omit,
        workspace: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncReplayResponse:
        """
        Validate and replay a complete sync event history.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/sync/replay",
            body=await async_maybe_transform(
                {
                    "body_directory": body_directory,
                    "events": events,
                },
                sync_replay_params.SyncReplayParams,
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
                    sync_replay_params.SyncReplayParams,
                ),
            ),
            cast_to=SyncReplayResponse,
        )

    async def start(
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
    ) -> SyncStartResponse:
        """
        Start sync loops for workspaces in the current project that have active
        sessions.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/sync/start",
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
                    sync_start_params.SyncStartParams,
                ),
            ),
            cast_to=SyncStartResponse,
        )


class SyncResourceWithRawResponse:
    def __init__(self, sync: SyncResource) -> None:
        self._sync = sync

        self.list_events = to_raw_response_wrapper(
            sync.list_events,
        )
        self.replay = to_raw_response_wrapper(
            sync.replay,
        )
        self.start = to_raw_response_wrapper(
            sync.start,
        )


class AsyncSyncResourceWithRawResponse:
    def __init__(self, sync: AsyncSyncResource) -> None:
        self._sync = sync

        self.list_events = async_to_raw_response_wrapper(
            sync.list_events,
        )
        self.replay = async_to_raw_response_wrapper(
            sync.replay,
        )
        self.start = async_to_raw_response_wrapper(
            sync.start,
        )


class SyncResourceWithStreamingResponse:
    def __init__(self, sync: SyncResource) -> None:
        self._sync = sync

        self.list_events = to_streamed_response_wrapper(
            sync.list_events,
        )
        self.replay = to_streamed_response_wrapper(
            sync.replay,
        )
        self.start = to_streamed_response_wrapper(
            sync.start,
        )


class AsyncSyncResourceWithStreamingResponse:
    def __init__(self, sync: AsyncSyncResource) -> None:
        self._sync = sync

        self.list_events = async_to_streamed_response_wrapper(
            sync.list_events,
        )
        self.replay = async_to_streamed_response_wrapper(
            sync.replay,
        )
        self.start = async_to_streamed_response_wrapper(
            sync.start,
        )
