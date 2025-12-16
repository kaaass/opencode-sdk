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
from ...types.tui import control_submit_response_params, control_get_next_request_params
from ..._base_client import make_request_options
from ...types.tui.control_submit_response_response import ControlSubmitResponseResponse
from ...types.tui.control_get_next_request_response import ControlGetNextRequestResponse

__all__ = ["ControlResource", "AsyncControlResource"]


class ControlResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ControlResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kaaass/opencode-sdk#accessing-raw-response-data-eg-headers
        """
        return ControlResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ControlResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kaaass/opencode-sdk#with_streaming_response
        """
        return ControlResourceWithStreamingResponse(self)

    def get_next_request(
        self,
        *,
        directory: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ControlGetNextRequestResponse:
        """
        Retrieve the next TUI (Terminal User Interface) request from the queue for
        processing.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/tui/control/next",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"directory": directory}, control_get_next_request_params.ControlGetNextRequestParams
                ),
            ),
            cast_to=ControlGetNextRequestResponse,
        )

    def submit_response(
        self,
        *,
        directory: str | Omit = omit,
        body: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ControlSubmitResponseResponse:
        """
        Submit a response to the TUI request queue to complete a pending request.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/tui/control/response",
            body=maybe_transform(body, control_submit_response_params.ControlSubmitResponseParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"directory": directory}, control_submit_response_params.ControlSubmitResponseParams
                ),
            ),
            cast_to=ControlSubmitResponseResponse,
        )


class AsyncControlResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncControlResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kaaass/opencode-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncControlResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncControlResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kaaass/opencode-sdk#with_streaming_response
        """
        return AsyncControlResourceWithStreamingResponse(self)

    async def get_next_request(
        self,
        *,
        directory: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ControlGetNextRequestResponse:
        """
        Retrieve the next TUI (Terminal User Interface) request from the queue for
        processing.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/tui/control/next",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"directory": directory}, control_get_next_request_params.ControlGetNextRequestParams
                ),
            ),
            cast_to=ControlGetNextRequestResponse,
        )

    async def submit_response(
        self,
        *,
        directory: str | Omit = omit,
        body: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ControlSubmitResponseResponse:
        """
        Submit a response to the TUI request queue to complete a pending request.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/tui/control/response",
            body=await async_maybe_transform(body, control_submit_response_params.ControlSubmitResponseParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"directory": directory}, control_submit_response_params.ControlSubmitResponseParams
                ),
            ),
            cast_to=ControlSubmitResponseResponse,
        )


class ControlResourceWithRawResponse:
    def __init__(self, control: ControlResource) -> None:
        self._control = control

        self.get_next_request = to_raw_response_wrapper(
            control.get_next_request,
        )
        self.submit_response = to_raw_response_wrapper(
            control.submit_response,
        )


class AsyncControlResourceWithRawResponse:
    def __init__(self, control: AsyncControlResource) -> None:
        self._control = control

        self.get_next_request = async_to_raw_response_wrapper(
            control.get_next_request,
        )
        self.submit_response = async_to_raw_response_wrapper(
            control.submit_response,
        )


class ControlResourceWithStreamingResponse:
    def __init__(self, control: ControlResource) -> None:
        self._control = control

        self.get_next_request = to_streamed_response_wrapper(
            control.get_next_request,
        )
        self.submit_response = to_streamed_response_wrapper(
            control.submit_response,
        )


class AsyncControlResourceWithStreamingResponse:
    def __init__(self, control: AsyncControlResource) -> None:
        self._control = control

        self.get_next_request = async_to_streamed_response_wrapper(
            control.get_next_request,
        )
        self.submit_response = async_to_streamed_response_wrapper(
            control.submit_response,
        )
