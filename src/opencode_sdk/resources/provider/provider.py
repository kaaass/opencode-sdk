# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .oauth import (
    OAuthResource,
    AsyncOAuthResource,
    OAuthResourceWithRawResponse,
    AsyncOAuthResourceWithRawResponse,
    OAuthResourceWithStreamingResponse,
    AsyncOAuthResourceWithStreamingResponse,
)
from ...types import provider_list_params, provider_get_auth_methods_params
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
from ...types.provider_list_response import ProviderListResponse
from ...types.provider_get_auth_methods_response import ProviderGetAuthMethodsResponse

__all__ = ["ProviderResource", "AsyncProviderResource"]


class ProviderResource(SyncAPIResource):
    @cached_property
    def oauth(self) -> OAuthResource:
        return OAuthResource(self._client)

    @cached_property
    def with_raw_response(self) -> ProviderResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kaaass/opencode-sdk#accessing-raw-response-data-eg-headers
        """
        return ProviderResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProviderResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kaaass/opencode-sdk#with_streaming_response
        """
        return ProviderResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        directory: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProviderListResponse:
        """
        Get a list of all available AI providers, including both available and connected
        ones.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/provider",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"directory": directory}, provider_list_params.ProviderListParams),
            ),
            cast_to=ProviderListResponse,
        )

    def get_auth_methods(
        self,
        *,
        directory: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProviderGetAuthMethodsResponse:
        """
        Retrieve available authentication methods for all AI providers.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/provider/auth",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"directory": directory}, provider_get_auth_methods_params.ProviderGetAuthMethodsParams
                ),
            ),
            cast_to=ProviderGetAuthMethodsResponse,
        )


class AsyncProviderResource(AsyncAPIResource):
    @cached_property
    def oauth(self) -> AsyncOAuthResource:
        return AsyncOAuthResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncProviderResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kaaass/opencode-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncProviderResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProviderResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kaaass/opencode-sdk#with_streaming_response
        """
        return AsyncProviderResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        directory: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProviderListResponse:
        """
        Get a list of all available AI providers, including both available and connected
        ones.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/provider",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"directory": directory}, provider_list_params.ProviderListParams),
            ),
            cast_to=ProviderListResponse,
        )

    async def get_auth_methods(
        self,
        *,
        directory: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProviderGetAuthMethodsResponse:
        """
        Retrieve available authentication methods for all AI providers.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/provider/auth",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"directory": directory}, provider_get_auth_methods_params.ProviderGetAuthMethodsParams
                ),
            ),
            cast_to=ProviderGetAuthMethodsResponse,
        )


class ProviderResourceWithRawResponse:
    def __init__(self, provider: ProviderResource) -> None:
        self._provider = provider

        self.list = to_raw_response_wrapper(
            provider.list,
        )
        self.get_auth_methods = to_raw_response_wrapper(
            provider.get_auth_methods,
        )

    @cached_property
    def oauth(self) -> OAuthResourceWithRawResponse:
        return OAuthResourceWithRawResponse(self._provider.oauth)


class AsyncProviderResourceWithRawResponse:
    def __init__(self, provider: AsyncProviderResource) -> None:
        self._provider = provider

        self.list = async_to_raw_response_wrapper(
            provider.list,
        )
        self.get_auth_methods = async_to_raw_response_wrapper(
            provider.get_auth_methods,
        )

    @cached_property
    def oauth(self) -> AsyncOAuthResourceWithRawResponse:
        return AsyncOAuthResourceWithRawResponse(self._provider.oauth)


class ProviderResourceWithStreamingResponse:
    def __init__(self, provider: ProviderResource) -> None:
        self._provider = provider

        self.list = to_streamed_response_wrapper(
            provider.list,
        )
        self.get_auth_methods = to_streamed_response_wrapper(
            provider.get_auth_methods,
        )

    @cached_property
    def oauth(self) -> OAuthResourceWithStreamingResponse:
        return OAuthResourceWithStreamingResponse(self._provider.oauth)


class AsyncProviderResourceWithStreamingResponse:
    def __init__(self, provider: AsyncProviderResource) -> None:
        self._provider = provider

        self.list = async_to_streamed_response_wrapper(
            provider.list,
        )
        self.get_auth_methods = async_to_streamed_response_wrapper(
            provider.get_auth_methods,
        )

    @cached_property
    def oauth(self) -> AsyncOAuthResourceWithStreamingResponse:
        return AsyncOAuthResourceWithStreamingResponse(self._provider.oauth)
