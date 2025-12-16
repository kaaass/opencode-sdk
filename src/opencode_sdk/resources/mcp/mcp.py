# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .auth import (
    AuthResource,
    AsyncAuthResource,
    AuthResourceWithRawResponse,
    AsyncAuthResourceWithRawResponse,
    AuthResourceWithStreamingResponse,
    AsyncAuthResourceWithStreamingResponse,
)
from ...types import (
    mcp_create_params,
    mcp_reload_params,
    mcp_connect_params,
    mcp_retrieve_params,
    mcp_disconnect_params,
)
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
from ..._base_client import make_request_options
from ...types.mcp_create_response import McpCreateResponse
from ...types.mcp_reload_response import McpReloadResponse
from ...types.mcp_connect_response import McpConnectResponse
from ...types.mcp_retrieve_response import McpRetrieveResponse
from ...types.mcp_disconnect_response import McpDisconnectResponse

__all__ = ["McpResource", "AsyncMcpResource"]


class McpResource(SyncAPIResource):
    @cached_property
    def auth(self) -> AuthResource:
        return AuthResource(self._client)

    @cached_property
    def with_raw_response(self) -> McpResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kaaass/opencode-sdk#accessing-raw-response-data-eg-headers
        """
        return McpResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> McpResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kaaass/opencode-sdk#with_streaming_response
        """
        return McpResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        config: mcp_create_params.Config,
        name: str,
        directory: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> McpCreateResponse:
        """
        Dynamically add a new Model Context Protocol (MCP) server to the system.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/mcp",
            body=maybe_transform(
                {
                    "config": config,
                    "name": name,
                },
                mcp_create_params.McpCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"directory": directory}, mcp_create_params.McpCreateParams),
            ),
            cast_to=McpCreateResponse,
        )

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
    ) -> McpRetrieveResponse:
        """
        Get the status of all Model Context Protocol (MCP) servers.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/mcp",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"directory": directory}, mcp_retrieve_params.McpRetrieveParams),
            ),
            cast_to=McpRetrieveResponse,
        )

    def connect(
        self,
        name: str,
        *,
        directory: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> McpConnectResponse:
        """
        Connect an MCP server

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return self._post(
            f"/mcp/{name}/connect",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"directory": directory}, mcp_connect_params.McpConnectParams),
            ),
            cast_to=McpConnectResponse,
        )

    def disconnect(
        self,
        name: str,
        *,
        directory: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> McpDisconnectResponse:
        """
        Disconnect an MCP server

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return self._post(
            f"/mcp/{name}/disconnect",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"directory": directory}, mcp_disconnect_params.McpDisconnectParams),
            ),
            cast_to=McpDisconnectResponse,
        )

    def reload(
        self,
        *,
        directory: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> McpReloadResponse:
        """
        Reload all MCP servers

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/mcp/reload",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"directory": directory}, mcp_reload_params.McpReloadParams),
            ),
            cast_to=McpReloadResponse,
        )


class AsyncMcpResource(AsyncAPIResource):
    @cached_property
    def auth(self) -> AsyncAuthResource:
        return AsyncAuthResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncMcpResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kaaass/opencode-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncMcpResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMcpResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kaaass/opencode-sdk#with_streaming_response
        """
        return AsyncMcpResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        config: mcp_create_params.Config,
        name: str,
        directory: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> McpCreateResponse:
        """
        Dynamically add a new Model Context Protocol (MCP) server to the system.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/mcp",
            body=await async_maybe_transform(
                {
                    "config": config,
                    "name": name,
                },
                mcp_create_params.McpCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"directory": directory}, mcp_create_params.McpCreateParams),
            ),
            cast_to=McpCreateResponse,
        )

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
    ) -> McpRetrieveResponse:
        """
        Get the status of all Model Context Protocol (MCP) servers.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/mcp",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"directory": directory}, mcp_retrieve_params.McpRetrieveParams),
            ),
            cast_to=McpRetrieveResponse,
        )

    async def connect(
        self,
        name: str,
        *,
        directory: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> McpConnectResponse:
        """
        Connect an MCP server

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return await self._post(
            f"/mcp/{name}/connect",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"directory": directory}, mcp_connect_params.McpConnectParams),
            ),
            cast_to=McpConnectResponse,
        )

    async def disconnect(
        self,
        name: str,
        *,
        directory: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> McpDisconnectResponse:
        """
        Disconnect an MCP server

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return await self._post(
            f"/mcp/{name}/disconnect",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"directory": directory}, mcp_disconnect_params.McpDisconnectParams),
            ),
            cast_to=McpDisconnectResponse,
        )

    async def reload(
        self,
        *,
        directory: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> McpReloadResponse:
        """
        Reload all MCP servers

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/mcp/reload",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"directory": directory}, mcp_reload_params.McpReloadParams),
            ),
            cast_to=McpReloadResponse,
        )


class McpResourceWithRawResponse:
    def __init__(self, mcp: McpResource) -> None:
        self._mcp = mcp

        self.create = to_raw_response_wrapper(
            mcp.create,
        )
        self.retrieve = to_raw_response_wrapper(
            mcp.retrieve,
        )
        self.connect = to_raw_response_wrapper(
            mcp.connect,
        )
        self.disconnect = to_raw_response_wrapper(
            mcp.disconnect,
        )
        self.reload = to_raw_response_wrapper(
            mcp.reload,
        )

    @cached_property
    def auth(self) -> AuthResourceWithRawResponse:
        return AuthResourceWithRawResponse(self._mcp.auth)


class AsyncMcpResourceWithRawResponse:
    def __init__(self, mcp: AsyncMcpResource) -> None:
        self._mcp = mcp

        self.create = async_to_raw_response_wrapper(
            mcp.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            mcp.retrieve,
        )
        self.connect = async_to_raw_response_wrapper(
            mcp.connect,
        )
        self.disconnect = async_to_raw_response_wrapper(
            mcp.disconnect,
        )
        self.reload = async_to_raw_response_wrapper(
            mcp.reload,
        )

    @cached_property
    def auth(self) -> AsyncAuthResourceWithRawResponse:
        return AsyncAuthResourceWithRawResponse(self._mcp.auth)


class McpResourceWithStreamingResponse:
    def __init__(self, mcp: McpResource) -> None:
        self._mcp = mcp

        self.create = to_streamed_response_wrapper(
            mcp.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            mcp.retrieve,
        )
        self.connect = to_streamed_response_wrapper(
            mcp.connect,
        )
        self.disconnect = to_streamed_response_wrapper(
            mcp.disconnect,
        )
        self.reload = to_streamed_response_wrapper(
            mcp.reload,
        )

    @cached_property
    def auth(self) -> AuthResourceWithStreamingResponse:
        return AuthResourceWithStreamingResponse(self._mcp.auth)


class AsyncMcpResourceWithStreamingResponse:
    def __init__(self, mcp: AsyncMcpResource) -> None:
        self._mcp = mcp

        self.create = async_to_streamed_response_wrapper(
            mcp.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            mcp.retrieve,
        )
        self.connect = async_to_streamed_response_wrapper(
            mcp.connect,
        )
        self.disconnect = async_to_streamed_response_wrapper(
            mcp.disconnect,
        )
        self.reload = async_to_streamed_response_wrapper(
            mcp.reload,
        )

    @cached_property
    def auth(self) -> AsyncAuthResourceWithStreamingResponse:
        return AsyncAuthResourceWithStreamingResponse(self._mcp.auth)
