# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import vc_retrieve_params
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
from ..types.vc_retrieve_response import VcRetrieveResponse

__all__ = ["VcsResource", "AsyncVcsResource"]


class VcsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> VcsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kaaass/opencode-sdk#accessing-raw-response-data-eg-headers
        """
        return VcsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VcsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kaaass/opencode-sdk#with_streaming_response
        """
        return VcsResourceWithStreamingResponse(self)

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
    ) -> VcRetrieveResponse:
        """
        Retrieve version control system (VCS) information for the current project, such
        as git branch.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/vcs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"directory": directory}, vc_retrieve_params.VcRetrieveParams),
            ),
            cast_to=VcRetrieveResponse,
        )


class AsyncVcsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncVcsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kaaass/opencode-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncVcsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVcsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kaaass/opencode-sdk#with_streaming_response
        """
        return AsyncVcsResourceWithStreamingResponse(self)

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
    ) -> VcRetrieveResponse:
        """
        Retrieve version control system (VCS) information for the current project, such
        as git branch.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/vcs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"directory": directory}, vc_retrieve_params.VcRetrieveParams),
            ),
            cast_to=VcRetrieveResponse,
        )


class VcsResourceWithRawResponse:
    def __init__(self, vcs: VcsResource) -> None:
        self._vcs = vcs

        self.retrieve = to_raw_response_wrapper(
            vcs.retrieve,
        )


class AsyncVcsResourceWithRawResponse:
    def __init__(self, vcs: AsyncVcsResource) -> None:
        self._vcs = vcs

        self.retrieve = async_to_raw_response_wrapper(
            vcs.retrieve,
        )


class VcsResourceWithStreamingResponse:
    def __init__(self, vcs: VcsResource) -> None:
        self._vcs = vcs

        self.retrieve = to_streamed_response_wrapper(
            vcs.retrieve,
        )


class AsyncVcsResourceWithStreamingResponse:
    def __init__(self, vcs: AsyncVcsResource) -> None:
        self._vcs = vcs

        self.retrieve = async_to_streamed_response_wrapper(
            vcs.retrieve,
        )
