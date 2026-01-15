# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, overload

import httpx

from ..types import auth_set_credentials_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import required_args, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.auth_set_credentials_response import AuthSetCredentialsResponse

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

    @overload
    def set_credentials(
        self,
        provider_id: str,
        *,
        access: str,
        expires: float,
        refresh: str,
        type: Literal["oauth"],
        directory: str | Omit = omit,
        account_id: str | Omit = omit,
        enterprise_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AuthSetCredentialsResponse:
        """
        Set authentication credentials

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def set_credentials(
        self,
        provider_id: str,
        *,
        key: str,
        type: Literal["api"],
        directory: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AuthSetCredentialsResponse:
        """
        Set authentication credentials

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def set_credentials(
        self,
        provider_id: str,
        *,
        token: str,
        key: str,
        type: Literal["wellknown"],
        directory: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AuthSetCredentialsResponse:
        """
        Set authentication credentials

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["access", "expires", "refresh", "type"], ["key", "type"], ["token", "key", "type"])
    def set_credentials(
        self,
        provider_id: str,
        *,
        access: str | Omit = omit,
        expires: float | Omit = omit,
        refresh: str | Omit = omit,
        type: Literal["oauth"] | Literal["api"] | Literal["wellknown"],
        directory: str | Omit = omit,
        account_id: str | Omit = omit,
        enterprise_url: str | Omit = omit,
        key: str | Omit = omit,
        token: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AuthSetCredentialsResponse:
        if not provider_id:
            raise ValueError(f"Expected a non-empty value for `provider_id` but received {provider_id!r}")
        return self._put(
            f"/auth/{provider_id}",
            body=maybe_transform(
                {
                    "access": access,
                    "expires": expires,
                    "refresh": refresh,
                    "type": type,
                    "account_id": account_id,
                    "enterprise_url": enterprise_url,
                    "key": key,
                    "token": token,
                },
                auth_set_credentials_params.AuthSetCredentialsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"directory": directory}, auth_set_credentials_params.AuthSetCredentialsParams),
            ),
            cast_to=AuthSetCredentialsResponse,
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

    @overload
    async def set_credentials(
        self,
        provider_id: str,
        *,
        access: str,
        expires: float,
        refresh: str,
        type: Literal["oauth"],
        directory: str | Omit = omit,
        account_id: str | Omit = omit,
        enterprise_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AuthSetCredentialsResponse:
        """
        Set authentication credentials

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def set_credentials(
        self,
        provider_id: str,
        *,
        key: str,
        type: Literal["api"],
        directory: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AuthSetCredentialsResponse:
        """
        Set authentication credentials

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def set_credentials(
        self,
        provider_id: str,
        *,
        token: str,
        key: str,
        type: Literal["wellknown"],
        directory: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AuthSetCredentialsResponse:
        """
        Set authentication credentials

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["access", "expires", "refresh", "type"], ["key", "type"], ["token", "key", "type"])
    async def set_credentials(
        self,
        provider_id: str,
        *,
        access: str | Omit = omit,
        expires: float | Omit = omit,
        refresh: str | Omit = omit,
        type: Literal["oauth"] | Literal["api"] | Literal["wellknown"],
        directory: str | Omit = omit,
        account_id: str | Omit = omit,
        enterprise_url: str | Omit = omit,
        key: str | Omit = omit,
        token: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AuthSetCredentialsResponse:
        if not provider_id:
            raise ValueError(f"Expected a non-empty value for `provider_id` but received {provider_id!r}")
        return await self._put(
            f"/auth/{provider_id}",
            body=await async_maybe_transform(
                {
                    "access": access,
                    "expires": expires,
                    "refresh": refresh,
                    "type": type,
                    "account_id": account_id,
                    "enterprise_url": enterprise_url,
                    "key": key,
                    "token": token,
                },
                auth_set_credentials_params.AuthSetCredentialsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"directory": directory}, auth_set_credentials_params.AuthSetCredentialsParams
                ),
            ),
            cast_to=AuthSetCredentialsResponse,
        )


class AuthResourceWithRawResponse:
    def __init__(self, auth: AuthResource) -> None:
        self._auth = auth

        self.set_credentials = to_raw_response_wrapper(
            auth.set_credentials,
        )


class AsyncAuthResourceWithRawResponse:
    def __init__(self, auth: AsyncAuthResource) -> None:
        self._auth = auth

        self.set_credentials = async_to_raw_response_wrapper(
            auth.set_credentials,
        )


class AuthResourceWithStreamingResponse:
    def __init__(self, auth: AuthResource) -> None:
        self._auth = auth

        self.set_credentials = to_streamed_response_wrapper(
            auth.set_credentials,
        )


class AsyncAuthResourceWithStreamingResponse:
    def __init__(self, auth: AsyncAuthResource) -> None:
        self._auth = auth

        self.set_credentials = async_to_streamed_response_wrapper(
            auth.set_credentials,
        )
