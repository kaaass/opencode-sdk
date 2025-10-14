# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal

import httpx

from ..types import log_write_params
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
from ..types.log_write_response import LogWriteResponse

__all__ = ["LogResource", "AsyncLogResource"]


class LogResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LogResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/opencode-sdk-python#accessing-raw-response-data-eg-headers
        """
        return LogResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LogResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/opencode-sdk-python#with_streaming_response
        """
        return LogResourceWithStreamingResponse(self)

    def write(
        self,
        *,
        level: Literal["debug", "info", "error", "warn"],
        message: str,
        service: str,
        directory: str | Omit = omit,
        extra: Dict[str, object] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LogWriteResponse:
        """
        Write a log entry to the server logs

        Args:
          level: Log level

          message: Log message

          service: Service name for the log entry

          extra: Additional metadata for the log entry

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/log",
            body=maybe_transform(
                {
                    "level": level,
                    "message": message,
                    "service": service,
                    "extra": extra,
                },
                log_write_params.LogWriteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"directory": directory}, log_write_params.LogWriteParams),
            ),
            cast_to=LogWriteResponse,
        )


class AsyncLogResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLogResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/opencode-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLogResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLogResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/opencode-sdk-python#with_streaming_response
        """
        return AsyncLogResourceWithStreamingResponse(self)

    async def write(
        self,
        *,
        level: Literal["debug", "info", "error", "warn"],
        message: str,
        service: str,
        directory: str | Omit = omit,
        extra: Dict[str, object] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LogWriteResponse:
        """
        Write a log entry to the server logs

        Args:
          level: Log level

          message: Log message

          service: Service name for the log entry

          extra: Additional metadata for the log entry

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/log",
            body=await async_maybe_transform(
                {
                    "level": level,
                    "message": message,
                    "service": service,
                    "extra": extra,
                },
                log_write_params.LogWriteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"directory": directory}, log_write_params.LogWriteParams),
            ),
            cast_to=LogWriteResponse,
        )


class LogResourceWithRawResponse:
    def __init__(self, log: LogResource) -> None:
        self._log = log

        self.write = to_raw_response_wrapper(
            log.write,
        )


class AsyncLogResourceWithRawResponse:
    def __init__(self, log: AsyncLogResource) -> None:
        self._log = log

        self.write = async_to_raw_response_wrapper(
            log.write,
        )


class LogResourceWithStreamingResponse:
    def __init__(self, log: LogResource) -> None:
        self._log = log

        self.write = to_streamed_response_wrapper(
            log.write,
        )


class AsyncLogResourceWithStreamingResponse:
    def __init__(self, log: AsyncLogResource) -> None:
        self._log = log

        self.write = async_to_streamed_response_wrapper(
            log.write,
        )
