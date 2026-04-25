# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, cast

import httpx

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
from ...types.mcp import (
    auth_start_oauth_params,
    auth_remove_oauth_params,
    auth_complete_oauth_params,
    auth_authenticate_oauth_params,
)
from ..._base_client import make_request_options
from ...types.mcp.mcp_status import McpStatus
from ...types.mcp.auth_start_oauth_response import AuthStartOAuthResponse
from ...types.mcp.auth_remove_oauth_response import AuthRemoveOAuthResponse

__all__ = ["AuthResource", "AsyncAuthResource"]


class AuthResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AuthResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/opencode-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AuthResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AuthResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/opencode-sdk-python#with_streaming_response
        """
        return AuthResourceWithStreamingResponse(self)

    def authenticate_oauth(
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
    ) -> McpStatus:
        """
        Start OAuth flow and wait for callback (opens browser)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return cast(
            McpStatus,
            self._post(
                path_template("/mcp/{name}/auth/authenticate", name=name),
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
                        auth_authenticate_oauth_params.AuthAuthenticateOAuthParams,
                    ),
                ),
                cast_to=cast(Any, McpStatus),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def complete_oauth(
        self,
        name: str,
        *,
        code: str,
        directory: str | Omit = omit,
        workspace: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> McpStatus:
        """
        Complete OAuth authentication for a Model Context Protocol (MCP) server using
        the authorization code.

        Args:
          code: Authorization code from OAuth callback

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return cast(
            McpStatus,
            self._post(
                path_template("/mcp/{name}/auth/callback", name=name),
                body=maybe_transform({"code": code}, auth_complete_oauth_params.AuthCompleteOAuthParams),
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
                        auth_complete_oauth_params.AuthCompleteOAuthParams,
                    ),
                ),
                cast_to=cast(Any, McpStatus),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def remove_oauth(
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
    ) -> AuthRemoveOAuthResponse:
        """
        Remove OAuth credentials for an MCP server

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return self._delete(
            path_template("/mcp/{name}/auth", name=name),
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
                    auth_remove_oauth_params.AuthRemoveOAuthParams,
                ),
            ),
            cast_to=AuthRemoveOAuthResponse,
        )

    def start_oauth(
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
    ) -> AuthStartOAuthResponse:
        """
        Start OAuth authentication flow for a Model Context Protocol (MCP) server.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return self._post(
            path_template("/mcp/{name}/auth", name=name),
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
                    auth_start_oauth_params.AuthStartOAuthParams,
                ),
            ),
            cast_to=AuthStartOAuthResponse,
        )


class AsyncAuthResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAuthResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/opencode-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAuthResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAuthResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/opencode-sdk-python#with_streaming_response
        """
        return AsyncAuthResourceWithStreamingResponse(self)

    async def authenticate_oauth(
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
    ) -> McpStatus:
        """
        Start OAuth flow and wait for callback (opens browser)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return cast(
            McpStatus,
            await self._post(
                path_template("/mcp/{name}/auth/authenticate", name=name),
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
                        auth_authenticate_oauth_params.AuthAuthenticateOAuthParams,
                    ),
                ),
                cast_to=cast(Any, McpStatus),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def complete_oauth(
        self,
        name: str,
        *,
        code: str,
        directory: str | Omit = omit,
        workspace: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> McpStatus:
        """
        Complete OAuth authentication for a Model Context Protocol (MCP) server using
        the authorization code.

        Args:
          code: Authorization code from OAuth callback

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return cast(
            McpStatus,
            await self._post(
                path_template("/mcp/{name}/auth/callback", name=name),
                body=await async_maybe_transform({"code": code}, auth_complete_oauth_params.AuthCompleteOAuthParams),
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
                        auth_complete_oauth_params.AuthCompleteOAuthParams,
                    ),
                ),
                cast_to=cast(Any, McpStatus),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def remove_oauth(
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
    ) -> AuthRemoveOAuthResponse:
        """
        Remove OAuth credentials for an MCP server

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return await self._delete(
            path_template("/mcp/{name}/auth", name=name),
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
                    auth_remove_oauth_params.AuthRemoveOAuthParams,
                ),
            ),
            cast_to=AuthRemoveOAuthResponse,
        )

    async def start_oauth(
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
    ) -> AuthStartOAuthResponse:
        """
        Start OAuth authentication flow for a Model Context Protocol (MCP) server.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return await self._post(
            path_template("/mcp/{name}/auth", name=name),
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
                    auth_start_oauth_params.AuthStartOAuthParams,
                ),
            ),
            cast_to=AuthStartOAuthResponse,
        )


class AuthResourceWithRawResponse:
    def __init__(self, auth: AuthResource) -> None:
        self._auth = auth

        self.authenticate_oauth = to_raw_response_wrapper(
            auth.authenticate_oauth,
        )
        self.complete_oauth = to_raw_response_wrapper(
            auth.complete_oauth,
        )
        self.remove_oauth = to_raw_response_wrapper(
            auth.remove_oauth,
        )
        self.start_oauth = to_raw_response_wrapper(
            auth.start_oauth,
        )


class AsyncAuthResourceWithRawResponse:
    def __init__(self, auth: AsyncAuthResource) -> None:
        self._auth = auth

        self.authenticate_oauth = async_to_raw_response_wrapper(
            auth.authenticate_oauth,
        )
        self.complete_oauth = async_to_raw_response_wrapper(
            auth.complete_oauth,
        )
        self.remove_oauth = async_to_raw_response_wrapper(
            auth.remove_oauth,
        )
        self.start_oauth = async_to_raw_response_wrapper(
            auth.start_oauth,
        )


class AuthResourceWithStreamingResponse:
    def __init__(self, auth: AuthResource) -> None:
        self._auth = auth

        self.authenticate_oauth = to_streamed_response_wrapper(
            auth.authenticate_oauth,
        )
        self.complete_oauth = to_streamed_response_wrapper(
            auth.complete_oauth,
        )
        self.remove_oauth = to_streamed_response_wrapper(
            auth.remove_oauth,
        )
        self.start_oauth = to_streamed_response_wrapper(
            auth.start_oauth,
        )


class AsyncAuthResourceWithStreamingResponse:
    def __init__(self, auth: AsyncAuthResource) -> None:
        self._auth = auth

        self.authenticate_oauth = async_to_streamed_response_wrapper(
            auth.authenticate_oauth,
        )
        self.complete_oauth = async_to_streamed_response_wrapper(
            auth.complete_oauth,
        )
        self.remove_oauth = async_to_streamed_response_wrapper(
            auth.remove_oauth,
        )
        self.start_oauth = async_to_streamed_response_wrapper(
            auth.start_oauth,
        )
