# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .tool import (
    ToolResource,
    AsyncToolResource,
    ToolResourceWithRawResponse,
    AsyncToolResourceWithRawResponse,
    ToolResourceWithStreamingResponse,
    AsyncToolResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["ExperimentalResource", "AsyncExperimentalResource"]


class ExperimentalResource(SyncAPIResource):
    @cached_property
    def tool(self) -> ToolResource:
        return ToolResource(self._client)

    @cached_property
    def with_raw_response(self) -> ExperimentalResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/opencode-sdk-python#accessing-raw-response-data-eg-headers
        """
        return ExperimentalResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExperimentalResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/opencode-sdk-python#with_streaming_response
        """
        return ExperimentalResourceWithStreamingResponse(self)


class AsyncExperimentalResource(AsyncAPIResource):
    @cached_property
    def tool(self) -> AsyncToolResource:
        return AsyncToolResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncExperimentalResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/opencode-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncExperimentalResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExperimentalResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/opencode-sdk-python#with_streaming_response
        """
        return AsyncExperimentalResourceWithStreamingResponse(self)


class ExperimentalResourceWithRawResponse:
    def __init__(self, experimental: ExperimentalResource) -> None:
        self._experimental = experimental

    @cached_property
    def tool(self) -> ToolResourceWithRawResponse:
        return ToolResourceWithRawResponse(self._experimental.tool)


class AsyncExperimentalResourceWithRawResponse:
    def __init__(self, experimental: AsyncExperimentalResource) -> None:
        self._experimental = experimental

    @cached_property
    def tool(self) -> AsyncToolResourceWithRawResponse:
        return AsyncToolResourceWithRawResponse(self._experimental.tool)


class ExperimentalResourceWithStreamingResponse:
    def __init__(self, experimental: ExperimentalResource) -> None:
        self._experimental = experimental

    @cached_property
    def tool(self) -> ToolResourceWithStreamingResponse:
        return ToolResourceWithStreamingResponse(self._experimental.tool)


class AsyncExperimentalResourceWithStreamingResponse:
    def __init__(self, experimental: AsyncExperimentalResource) -> None:
        self._experimental = experimental

    @cached_property
    def tool(self) -> AsyncToolResourceWithStreamingResponse:
        return AsyncToolResourceWithStreamingResponse(self._experimental.tool)
