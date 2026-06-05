# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
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
from ...types.session import attach_attach_params, attach_detach_params

__all__ = ["AttachResource", "AsyncAttachResource"]


class AttachResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AttachResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kaaass/opencode-sdk#accessing-raw-response-data-eg-headers
        """
        return AttachResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AttachResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kaaass/opencode-sdk#with_streaming_response
        """
        return AttachResourceWithStreamingResponse(self)

    def attach(
        self,
        session_id: str,
        *,
        directory: str | Omit = omit,
        workspace: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Explicitly attach the current connection to a session (1:1 exclusive).

        Already
        attached by self is a no-op; attached by another connection returns 409.
        Header-less (global) callers are a no-op.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            path_template("/session/{session_id}/attach", session_id=session_id),
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
                    attach_attach_params.AttachAttachParams,
                ),
            ),
            cast_to=NoneType,
        )

    def detach(
        self,
        session_id: str,
        *,
        directory: str | Omit = omit,
        workspace: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Detach the current connection from a session, aborting any running prompt.

        Only
        the owner connection may detach.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/session/{session_id}/attach", session_id=session_id),
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
                    attach_detach_params.AttachDetachParams,
                ),
            ),
            cast_to=NoneType,
        )


class AsyncAttachResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAttachResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kaaass/opencode-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncAttachResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAttachResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kaaass/opencode-sdk#with_streaming_response
        """
        return AsyncAttachResourceWithStreamingResponse(self)

    async def attach(
        self,
        session_id: str,
        *,
        directory: str | Omit = omit,
        workspace: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Explicitly attach the current connection to a session (1:1 exclusive).

        Already
        attached by self is a no-op; attached by another connection returns 409.
        Header-less (global) callers are a no-op.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            path_template("/session/{session_id}/attach", session_id=session_id),
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
                    attach_attach_params.AttachAttachParams,
                ),
            ),
            cast_to=NoneType,
        )

    async def detach(
        self,
        session_id: str,
        *,
        directory: str | Omit = omit,
        workspace: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Detach the current connection from a session, aborting any running prompt.

        Only
        the owner connection may detach.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/session/{session_id}/attach", session_id=session_id),
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
                    attach_detach_params.AttachDetachParams,
                ),
            ),
            cast_to=NoneType,
        )


class AttachResourceWithRawResponse:
    def __init__(self, attach: AttachResource) -> None:
        self._attach = attach

        self.attach = to_raw_response_wrapper(
            attach.attach,
        )
        self.detach = to_raw_response_wrapper(
            attach.detach,
        )


class AsyncAttachResourceWithRawResponse:
    def __init__(self, attach: AsyncAttachResource) -> None:
        self._attach = attach

        self.attach = async_to_raw_response_wrapper(
            attach.attach,
        )
        self.detach = async_to_raw_response_wrapper(
            attach.detach,
        )


class AttachResourceWithStreamingResponse:
    def __init__(self, attach: AttachResource) -> None:
        self._attach = attach

        self.attach = to_streamed_response_wrapper(
            attach.attach,
        )
        self.detach = to_streamed_response_wrapper(
            attach.detach,
        )


class AsyncAttachResourceWithStreamingResponse:
    def __init__(self, attach: AsyncAttachResource) -> None:
        self._attach = attach

        self.attach = async_to_streamed_response_wrapper(
            attach.attach,
        )
        self.detach = async_to_streamed_response_wrapper(
            attach.detach,
        )
