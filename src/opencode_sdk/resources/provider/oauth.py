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
from ..._base_client import make_request_options
from ...types.provider import oauth_authorize_params, oauth_handle_callback_params
from ...types.provider.oauth_authorize_response import OAuthAuthorizeResponse
from ...types.provider.oauth_handle_callback_response import OAuthHandleCallbackResponse

__all__ = ["OAuthResource", "AsyncOAuthResource"]


class OAuthResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OAuthResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kaaass/opencode-sdk#accessing-raw-response-data-eg-headers
        """
        return OAuthResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OAuthResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kaaass/opencode-sdk#with_streaming_response
        """
        return OAuthResourceWithStreamingResponse(self)

    def authorize(
        self,
        provider_id: str,
        *,
        method: float,
        directory: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OAuthAuthorizeResponse:
        """
        Initiate OAuth authorization for a specific AI provider to get an authorization
        URL.

        Args:
          method: Auth method index

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not provider_id:
            raise ValueError(f"Expected a non-empty value for `provider_id` but received {provider_id!r}")
        return self._post(
            f"/provider/{provider_id}/oauth/authorize",
            body=maybe_transform({"method": method}, oauth_authorize_params.OAuthAuthorizeParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"directory": directory}, oauth_authorize_params.OAuthAuthorizeParams),
            ),
            cast_to=OAuthAuthorizeResponse,
        )

    def handle_callback(
        self,
        provider_id: str,
        *,
        method: float,
        directory: str | Omit = omit,
        code: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OAuthHandleCallbackResponse:
        """
        Handle the OAuth callback from a provider after user authorization.

        Args:
          method: Auth method index

          code: OAuth authorization code

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not provider_id:
            raise ValueError(f"Expected a non-empty value for `provider_id` but received {provider_id!r}")
        return self._post(
            f"/provider/{provider_id}/oauth/callback",
            body=maybe_transform(
                {
                    "method": method,
                    "code": code,
                },
                oauth_handle_callback_params.OAuthHandleCallbackParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"directory": directory}, oauth_handle_callback_params.OAuthHandleCallbackParams),
            ),
            cast_to=OAuthHandleCallbackResponse,
        )


class AsyncOAuthResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOAuthResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kaaass/opencode-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncOAuthResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOAuthResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kaaass/opencode-sdk#with_streaming_response
        """
        return AsyncOAuthResourceWithStreamingResponse(self)

    async def authorize(
        self,
        provider_id: str,
        *,
        method: float,
        directory: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OAuthAuthorizeResponse:
        """
        Initiate OAuth authorization for a specific AI provider to get an authorization
        URL.

        Args:
          method: Auth method index

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not provider_id:
            raise ValueError(f"Expected a non-empty value for `provider_id` but received {provider_id!r}")
        return await self._post(
            f"/provider/{provider_id}/oauth/authorize",
            body=await async_maybe_transform({"method": method}, oauth_authorize_params.OAuthAuthorizeParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"directory": directory}, oauth_authorize_params.OAuthAuthorizeParams
                ),
            ),
            cast_to=OAuthAuthorizeResponse,
        )

    async def handle_callback(
        self,
        provider_id: str,
        *,
        method: float,
        directory: str | Omit = omit,
        code: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OAuthHandleCallbackResponse:
        """
        Handle the OAuth callback from a provider after user authorization.

        Args:
          method: Auth method index

          code: OAuth authorization code

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not provider_id:
            raise ValueError(f"Expected a non-empty value for `provider_id` but received {provider_id!r}")
        return await self._post(
            f"/provider/{provider_id}/oauth/callback",
            body=await async_maybe_transform(
                {
                    "method": method,
                    "code": code,
                },
                oauth_handle_callback_params.OAuthHandleCallbackParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"directory": directory}, oauth_handle_callback_params.OAuthHandleCallbackParams
                ),
            ),
            cast_to=OAuthHandleCallbackResponse,
        )


class OAuthResourceWithRawResponse:
    def __init__(self, oauth: OAuthResource) -> None:
        self._oauth = oauth

        self.authorize = to_raw_response_wrapper(
            oauth.authorize,
        )
        self.handle_callback = to_raw_response_wrapper(
            oauth.handle_callback,
        )


class AsyncOAuthResourceWithRawResponse:
    def __init__(self, oauth: AsyncOAuthResource) -> None:
        self._oauth = oauth

        self.authorize = async_to_raw_response_wrapper(
            oauth.authorize,
        )
        self.handle_callback = async_to_raw_response_wrapper(
            oauth.handle_callback,
        )


class OAuthResourceWithStreamingResponse:
    def __init__(self, oauth: OAuthResource) -> None:
        self._oauth = oauth

        self.authorize = to_streamed_response_wrapper(
            oauth.authorize,
        )
        self.handle_callback = to_streamed_response_wrapper(
            oauth.handle_callback,
        )


class AsyncOAuthResourceWithStreamingResponse:
    def __init__(self, oauth: AsyncOAuthResource) -> None:
        self._oauth = oauth

        self.authorize = async_to_streamed_response_wrapper(
            oauth.authorize,
        )
        self.handle_callback = async_to_streamed_response_wrapper(
            oauth.handle_callback,
        )
