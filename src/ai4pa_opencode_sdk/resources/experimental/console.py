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
from ...types.experimental import console_retrieve_params, console_list_orgs_params, console_switch_org_params
from ...types.experimental.console_retrieve_response import ConsoleRetrieveResponse
from ...types.experimental.console_list_orgs_response import ConsoleListOrgsResponse
from ...types.experimental.console_switch_org_response import ConsoleSwitchOrgResponse

__all__ = ["ConsoleResource", "AsyncConsoleResource"]


class ConsoleResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ConsoleResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kaaass/opencode-sdk#accessing-raw-response-data-eg-headers
        """
        return ConsoleResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConsoleResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kaaass/opencode-sdk#with_streaming_response
        """
        return ConsoleResourceWithStreamingResponse(self)

    def retrieve(
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
    ) -> ConsoleRetrieveResponse:
        """
        Get the active Console org name and the set of provider IDs managed by that
        Console org.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/experimental/console",
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
                    console_retrieve_params.ConsoleRetrieveParams,
                ),
            ),
            cast_to=ConsoleRetrieveResponse,
        )

    def list_orgs(
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
    ) -> ConsoleListOrgsResponse:
        """
        Get the available Console orgs across logged-in accounts, including the current
        active org.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/experimental/console/orgs",
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
                    console_list_orgs_params.ConsoleListOrgsParams,
                ),
            ),
            cast_to=ConsoleListOrgsResponse,
        )

    def switch_org(
        self,
        *,
        account_id: str,
        org_id: str,
        directory: str | Omit = omit,
        workspace: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConsoleSwitchOrgResponse:
        """
        Persist a new active Console account/org selection for the current local
        OpenCode state.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/experimental/console/switch",
            body=maybe_transform(
                {
                    "account_id": account_id,
                    "org_id": org_id,
                },
                console_switch_org_params.ConsoleSwitchOrgParams,
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
                    console_switch_org_params.ConsoleSwitchOrgParams,
                ),
            ),
            cast_to=ConsoleSwitchOrgResponse,
        )


class AsyncConsoleResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncConsoleResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kaaass/opencode-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncConsoleResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConsoleResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kaaass/opencode-sdk#with_streaming_response
        """
        return AsyncConsoleResourceWithStreamingResponse(self)

    async def retrieve(
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
    ) -> ConsoleRetrieveResponse:
        """
        Get the active Console org name and the set of provider IDs managed by that
        Console org.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/experimental/console",
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
                    console_retrieve_params.ConsoleRetrieveParams,
                ),
            ),
            cast_to=ConsoleRetrieveResponse,
        )

    async def list_orgs(
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
    ) -> ConsoleListOrgsResponse:
        """
        Get the available Console orgs across logged-in accounts, including the current
        active org.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/experimental/console/orgs",
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
                    console_list_orgs_params.ConsoleListOrgsParams,
                ),
            ),
            cast_to=ConsoleListOrgsResponse,
        )

    async def switch_org(
        self,
        *,
        account_id: str,
        org_id: str,
        directory: str | Omit = omit,
        workspace: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConsoleSwitchOrgResponse:
        """
        Persist a new active Console account/org selection for the current local
        OpenCode state.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/experimental/console/switch",
            body=await async_maybe_transform(
                {
                    "account_id": account_id,
                    "org_id": org_id,
                },
                console_switch_org_params.ConsoleSwitchOrgParams,
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
                    console_switch_org_params.ConsoleSwitchOrgParams,
                ),
            ),
            cast_to=ConsoleSwitchOrgResponse,
        )


class ConsoleResourceWithRawResponse:
    def __init__(self, console: ConsoleResource) -> None:
        self._console = console

        self.retrieve = to_raw_response_wrapper(
            console.retrieve,
        )
        self.list_orgs = to_raw_response_wrapper(
            console.list_orgs,
        )
        self.switch_org = to_raw_response_wrapper(
            console.switch_org,
        )


class AsyncConsoleResourceWithRawResponse:
    def __init__(self, console: AsyncConsoleResource) -> None:
        self._console = console

        self.retrieve = async_to_raw_response_wrapper(
            console.retrieve,
        )
        self.list_orgs = async_to_raw_response_wrapper(
            console.list_orgs,
        )
        self.switch_org = async_to_raw_response_wrapper(
            console.switch_org,
        )


class ConsoleResourceWithStreamingResponse:
    def __init__(self, console: ConsoleResource) -> None:
        self._console = console

        self.retrieve = to_streamed_response_wrapper(
            console.retrieve,
        )
        self.list_orgs = to_streamed_response_wrapper(
            console.list_orgs,
        )
        self.switch_org = to_streamed_response_wrapper(
            console.switch_org,
        )


class AsyncConsoleResourceWithStreamingResponse:
    def __init__(self, console: AsyncConsoleResource) -> None:
        self._console = console

        self.retrieve = async_to_streamed_response_wrapper(
            console.retrieve,
        )
        self.list_orgs = async_to_streamed_response_wrapper(
            console.list_orgs,
        )
        self.switch_org = async_to_streamed_response_wrapper(
            console.switch_org,
        )
