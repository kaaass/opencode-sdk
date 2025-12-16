# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, cast

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
from ...types.mcp import auth_start_params, auth_remove_params, auth_complete_params, auth_authenticate_params
from ..._base_client import make_request_options
from ...types.mcp.auth_start_response import AuthStartResponse
from ...types.mcp.auth_remove_response import AuthRemoveResponse
from ...types.mcp.auth_complete_response import AuthCompleteResponse
from ...types.mcp.auth_authenticate_response import AuthAuthenticateResponse

__all__ = ["AuthResource", "AsyncAuthResource"]


class AuthResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AuthResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kaaass/opencode-sdk#accessing-raw-response-data-eg-headers
        """
        return AuthResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AuthResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kaaass/opencode-sdk#with_streaming_response
        """
        return AuthResourceWithStreamingResponse(self)

    def authenticate(
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
    ) -> AuthAuthenticateResponse:
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
            AuthAuthenticateResponse,
            self._post(
                f"/mcp/{name}/auth/authenticate",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=maybe_transform({"directory": directory}, auth_authenticate_params.AuthAuthenticateParams),
                ),
                cast_to=cast(
                    Any, AuthAuthenticateResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def complete(
        self,
        name: str,
        *,
        code: str,
        directory: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AuthCompleteResponse:
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
            AuthCompleteResponse,
            self._post(
                f"/mcp/{name}/auth/callback",
                body=maybe_transform({"code": code}, auth_complete_params.AuthCompleteParams),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=maybe_transform({"directory": directory}, auth_complete_params.AuthCompleteParams),
                ),
                cast_to=cast(
                    Any, AuthCompleteResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def remove(
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
    ) -> AuthRemoveResponse:
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
            f"/mcp/{name}/auth",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"directory": directory}, auth_remove_params.AuthRemoveParams),
            ),
            cast_to=AuthRemoveResponse,
        )

    def start(
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
    ) -> AuthStartResponse:
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
            f"/mcp/{name}/auth",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"directory": directory}, auth_start_params.AuthStartParams),
            ),
            cast_to=AuthStartResponse,
        )


class AsyncAuthResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAuthResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kaaass/opencode-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncAuthResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAuthResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kaaass/opencode-sdk#with_streaming_response
        """
        return AsyncAuthResourceWithStreamingResponse(self)

    async def authenticate(
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
    ) -> AuthAuthenticateResponse:
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
            AuthAuthenticateResponse,
            await self._post(
                f"/mcp/{name}/auth/authenticate",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=await async_maybe_transform(
                        {"directory": directory}, auth_authenticate_params.AuthAuthenticateParams
                    ),
                ),
                cast_to=cast(
                    Any, AuthAuthenticateResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def complete(
        self,
        name: str,
        *,
        code: str,
        directory: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AuthCompleteResponse:
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
            AuthCompleteResponse,
            await self._post(
                f"/mcp/{name}/auth/callback",
                body=await async_maybe_transform({"code": code}, auth_complete_params.AuthCompleteParams),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=await async_maybe_transform(
                        {"directory": directory}, auth_complete_params.AuthCompleteParams
                    ),
                ),
                cast_to=cast(
                    Any, AuthCompleteResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def remove(
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
    ) -> AuthRemoveResponse:
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
            f"/mcp/{name}/auth",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"directory": directory}, auth_remove_params.AuthRemoveParams),
            ),
            cast_to=AuthRemoveResponse,
        )

    async def start(
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
    ) -> AuthStartResponse:
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
            f"/mcp/{name}/auth",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"directory": directory}, auth_start_params.AuthStartParams),
            ),
            cast_to=AuthStartResponse,
        )


class AuthResourceWithRawResponse:
    def __init__(self, auth: AuthResource) -> None:
        self._auth = auth

        self.authenticate = to_raw_response_wrapper(
            auth.authenticate,
        )
        self.complete = to_raw_response_wrapper(
            auth.complete,
        )
        self.remove = to_raw_response_wrapper(
            auth.remove,
        )
        self.start = to_raw_response_wrapper(
            auth.start,
        )


class AsyncAuthResourceWithRawResponse:
    def __init__(self, auth: AsyncAuthResource) -> None:
        self._auth = auth

        self.authenticate = async_to_raw_response_wrapper(
            auth.authenticate,
        )
        self.complete = async_to_raw_response_wrapper(
            auth.complete,
        )
        self.remove = async_to_raw_response_wrapper(
            auth.remove,
        )
        self.start = async_to_raw_response_wrapper(
            auth.start,
        )


class AuthResourceWithStreamingResponse:
    def __init__(self, auth: AuthResource) -> None:
        self._auth = auth

        self.authenticate = to_streamed_response_wrapper(
            auth.authenticate,
        )
        self.complete = to_streamed_response_wrapper(
            auth.complete,
        )
        self.remove = to_streamed_response_wrapper(
            auth.remove,
        )
        self.start = to_streamed_response_wrapper(
            auth.start,
        )


class AsyncAuthResourceWithStreamingResponse:
    def __init__(self, auth: AsyncAuthResource) -> None:
        self._auth = auth

        self.authenticate = async_to_streamed_response_wrapper(
            auth.authenticate,
        )
        self.complete = async_to_streamed_response_wrapper(
            auth.complete,
        )
        self.remove = async_to_streamed_response_wrapper(
            auth.remove,
        )
        self.start = async_to_streamed_response_wrapper(
            auth.start,
        )
