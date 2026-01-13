# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict

import httpx

from ..types import client_tool_list_params, client_tool_create_params, client_tool_delete_params
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
from ..types.client_tool_list_response import ClientToolListResponse
from ..types.client_tool_create_response import ClientToolCreateResponse
from ..types.client_tool_delete_response import ClientToolDeleteResponse

__all__ = ["ClientToolResource", "AsyncClientToolResource"]


class ClientToolResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ClientToolResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kaaass/opencode-sdk#accessing-raw-response-data-eg-headers
        """
        return ClientToolResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ClientToolResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kaaass/opencode-sdk#with_streaming_response
        """
        return ClientToolResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        id: str,
        description: str,
        parameters: Dict[str, object],
        directory: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ClientToolCreateResponse:
        """
        Register a new client tool that requires external execution.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/client-tool",
            body=maybe_transform(
                {
                    "id": id,
                    "description": description,
                    "parameters": parameters,
                },
                client_tool_create_params.ClientToolCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"directory": directory}, client_tool_create_params.ClientToolCreateParams),
            ),
            cast_to=ClientToolCreateResponse,
        )

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
    ) -> ClientToolListResponse:
        """
        Get a list of all registered client tools.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/client-tool",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"directory": directory}, client_tool_list_params.ClientToolListParams),
            ),
            cast_to=ClientToolListResponse,
        )

    def delete(
        self,
        id: str,
        *,
        directory: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ClientToolDeleteResponse:
        """
        Remove a registered client tool.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/client-tool/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"directory": directory}, client_tool_delete_params.ClientToolDeleteParams),
            ),
            cast_to=ClientToolDeleteResponse,
        )


class AsyncClientToolResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncClientToolResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kaaass/opencode-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncClientToolResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncClientToolResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kaaass/opencode-sdk#with_streaming_response
        """
        return AsyncClientToolResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        id: str,
        description: str,
        parameters: Dict[str, object],
        directory: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ClientToolCreateResponse:
        """
        Register a new client tool that requires external execution.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/client-tool",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "description": description,
                    "parameters": parameters,
                },
                client_tool_create_params.ClientToolCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"directory": directory}, client_tool_create_params.ClientToolCreateParams
                ),
            ),
            cast_to=ClientToolCreateResponse,
        )

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
    ) -> ClientToolListResponse:
        """
        Get a list of all registered client tools.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/client-tool",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"directory": directory}, client_tool_list_params.ClientToolListParams
                ),
            ),
            cast_to=ClientToolListResponse,
        )

    async def delete(
        self,
        id: str,
        *,
        directory: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ClientToolDeleteResponse:
        """
        Remove a registered client tool.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/client-tool/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"directory": directory}, client_tool_delete_params.ClientToolDeleteParams
                ),
            ),
            cast_to=ClientToolDeleteResponse,
        )


class ClientToolResourceWithRawResponse:
    def __init__(self, client_tool: ClientToolResource) -> None:
        self._client_tool = client_tool

        self.create = to_raw_response_wrapper(
            client_tool.create,
        )
        self.list = to_raw_response_wrapper(
            client_tool.list,
        )
        self.delete = to_raw_response_wrapper(
            client_tool.delete,
        )


class AsyncClientToolResourceWithRawResponse:
    def __init__(self, client_tool: AsyncClientToolResource) -> None:
        self._client_tool = client_tool

        self.create = async_to_raw_response_wrapper(
            client_tool.create,
        )
        self.list = async_to_raw_response_wrapper(
            client_tool.list,
        )
        self.delete = async_to_raw_response_wrapper(
            client_tool.delete,
        )


class ClientToolResourceWithStreamingResponse:
    def __init__(self, client_tool: ClientToolResource) -> None:
        self._client_tool = client_tool

        self.create = to_streamed_response_wrapper(
            client_tool.create,
        )
        self.list = to_streamed_response_wrapper(
            client_tool.list,
        )
        self.delete = to_streamed_response_wrapper(
            client_tool.delete,
        )


class AsyncClientToolResourceWithStreamingResponse:
    def __init__(self, client_tool: AsyncClientToolResource) -> None:
        self._client_tool = client_tool

        self.create = async_to_streamed_response_wrapper(
            client_tool.create,
        )
        self.list = async_to_streamed_response_wrapper(
            client_tool.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            client_tool.delete,
        )
