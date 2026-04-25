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
    mcp_add_server_params,
    mcp_connect_server_params,
    mcp_retrieve_status_params,
    mcp_disconnect_server_params,
)
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.mcp_add_server_response import McpAddServerResponse
from ...types.mcp_connect_server_response import McpConnectServerResponse
from ...types.mcp_retrieve_status_response import McpRetrieveStatusResponse
from ...types.mcp_disconnect_server_response import McpDisconnectServerResponse

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

    def add_server(
        self,
        *,
        config: mcp_add_server_params.Config,
        name: str,
        directory: str | Omit = omit,
        workspace: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> McpAddServerResponse:
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
                mcp_add_server_params.McpAddServerParams,
            ),
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
                    mcp_add_server_params.McpAddServerParams,
                ),
            ),
            cast_to=McpAddServerResponse,
        )

    def connect_server(
        self,
        name: str,
        *,
        directory: str | Omit = omit,
        workspace: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> McpConnectServerResponse:
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
            path_template("/mcp/{name}/connect", name=name),
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
                    mcp_connect_server_params.McpConnectServerParams,
                ),
            ),
            cast_to=McpConnectServerResponse,
        )

    def disconnect_server(
        self,
        name: str,
        *,
        directory: str | Omit = omit,
        workspace: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> McpDisconnectServerResponse:
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
            path_template("/mcp/{name}/disconnect", name=name),
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
                    mcp_disconnect_server_params.McpDisconnectServerParams,
                ),
            ),
            cast_to=McpDisconnectServerResponse,
        )

    def retrieve_status(
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
    ) -> McpRetrieveStatusResponse:
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
                query=maybe_transform(
                    {
                        "directory": directory,
                        "workspace": workspace,
                    },
                    mcp_retrieve_status_params.McpRetrieveStatusParams,
                ),
            ),
            cast_to=McpRetrieveStatusResponse,
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

    async def add_server(
        self,
        *,
        config: mcp_add_server_params.Config,
        name: str,
        directory: str | Omit = omit,
        workspace: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> McpAddServerResponse:
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
                mcp_add_server_params.McpAddServerParams,
            ),
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
                    mcp_add_server_params.McpAddServerParams,
                ),
            ),
            cast_to=McpAddServerResponse,
        )

    async def connect_server(
        self,
        name: str,
        *,
        directory: str | Omit = omit,
        workspace: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> McpConnectServerResponse:
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
            path_template("/mcp/{name}/connect", name=name),
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
                    mcp_connect_server_params.McpConnectServerParams,
                ),
            ),
            cast_to=McpConnectServerResponse,
        )

    async def disconnect_server(
        self,
        name: str,
        *,
        directory: str | Omit = omit,
        workspace: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> McpDisconnectServerResponse:
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
            path_template("/mcp/{name}/disconnect", name=name),
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
                    mcp_disconnect_server_params.McpDisconnectServerParams,
                ),
            ),
            cast_to=McpDisconnectServerResponse,
        )

    async def retrieve_status(
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
    ) -> McpRetrieveStatusResponse:
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
                query=await async_maybe_transform(
                    {
                        "directory": directory,
                        "workspace": workspace,
                    },
                    mcp_retrieve_status_params.McpRetrieveStatusParams,
                ),
            ),
            cast_to=McpRetrieveStatusResponse,
        )


class McpResourceWithRawResponse:
    def __init__(self, mcp: McpResource) -> None:
        self._mcp = mcp

        self.add_server = to_raw_response_wrapper(
            mcp.add_server,
        )
        self.connect_server = to_raw_response_wrapper(
            mcp.connect_server,
        )
        self.disconnect_server = to_raw_response_wrapper(
            mcp.disconnect_server,
        )
        self.retrieve_status = to_raw_response_wrapper(
            mcp.retrieve_status,
        )

    @cached_property
    def auth(self) -> AuthResourceWithRawResponse:
        return AuthResourceWithRawResponse(self._mcp.auth)


class AsyncMcpResourceWithRawResponse:
    def __init__(self, mcp: AsyncMcpResource) -> None:
        self._mcp = mcp

        self.add_server = async_to_raw_response_wrapper(
            mcp.add_server,
        )
        self.connect_server = async_to_raw_response_wrapper(
            mcp.connect_server,
        )
        self.disconnect_server = async_to_raw_response_wrapper(
            mcp.disconnect_server,
        )
        self.retrieve_status = async_to_raw_response_wrapper(
            mcp.retrieve_status,
        )

    @cached_property
    def auth(self) -> AsyncAuthResourceWithRawResponse:
        return AsyncAuthResourceWithRawResponse(self._mcp.auth)


class McpResourceWithStreamingResponse:
    def __init__(self, mcp: McpResource) -> None:
        self._mcp = mcp

        self.add_server = to_streamed_response_wrapper(
            mcp.add_server,
        )
        self.connect_server = to_streamed_response_wrapper(
            mcp.connect_server,
        )
        self.disconnect_server = to_streamed_response_wrapper(
            mcp.disconnect_server,
        )
        self.retrieve_status = to_streamed_response_wrapper(
            mcp.retrieve_status,
        )

    @cached_property
    def auth(self) -> AuthResourceWithStreamingResponse:
        return AuthResourceWithStreamingResponse(self._mcp.auth)


class AsyncMcpResourceWithStreamingResponse:
    def __init__(self, mcp: AsyncMcpResource) -> None:
        self._mcp = mcp

        self.add_server = async_to_streamed_response_wrapper(
            mcp.add_server,
        )
        self.connect_server = async_to_streamed_response_wrapper(
            mcp.connect_server,
        )
        self.disconnect_server = async_to_streamed_response_wrapper(
            mcp.disconnect_server,
        )
        self.retrieve_status = async_to_streamed_response_wrapper(
            mcp.retrieve_status,
        )

    @cached_property
    def auth(self) -> AsyncAuthResourceWithStreamingResponse:
        return AsyncAuthResourceWithStreamingResponse(self._mcp.auth)
