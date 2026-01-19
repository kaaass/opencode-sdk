# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import artifact_delete_params, artifact_download_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    to_custom_raw_response_wrapper,
    async_to_streamed_response_wrapper,
    to_custom_streamed_response_wrapper,
    async_to_custom_raw_response_wrapper,
    async_to_custom_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.artifact_delete_response import ArtifactDeleteResponse

__all__ = ["ArtifactResource", "AsyncArtifactResource"]


class ArtifactResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ArtifactResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kaaass/opencode-sdk#accessing-raw-response-data-eg-headers
        """
        return ArtifactResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ArtifactResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kaaass/opencode-sdk#with_streaming_response
        """
        return ArtifactResourceWithStreamingResponse(self)

    def delete(
        self,
        artifact_id: str,
        *,
        session_id: str,
        directory: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ArtifactDeleteResponse:
        """
        Delete an artifact

        Args:
          session_id: Session ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not artifact_id:
            raise ValueError(f"Expected a non-empty value for `artifact_id` but received {artifact_id!r}")
        return self._delete(
            f"/artifact/{artifact_id}",
            body=maybe_transform({"session_id": session_id}, artifact_delete_params.ArtifactDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"directory": directory}, artifact_delete_params.ArtifactDeleteParams),
            ),
            cast_to=ArtifactDeleteResponse,
        )

    def download(
        self,
        artifact_id: str,
        *,
        session_id: str,
        directory: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BinaryAPIResponse:
        """
        Download an artifact file

        Args:
          session_id: Session ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not artifact_id:
            raise ValueError(f"Expected a non-empty value for `artifact_id` but received {artifact_id!r}")
        extra_headers = {"Accept": "application/octet-stream", **(extra_headers or {})}
        return self._get(
            f"/artifact/{artifact_id}/download",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "session_id": session_id,
                        "directory": directory,
                    },
                    artifact_download_params.ArtifactDownloadParams,
                ),
            ),
            cast_to=BinaryAPIResponse,
        )


class AsyncArtifactResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncArtifactResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kaaass/opencode-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncArtifactResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncArtifactResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kaaass/opencode-sdk#with_streaming_response
        """
        return AsyncArtifactResourceWithStreamingResponse(self)

    async def delete(
        self,
        artifact_id: str,
        *,
        session_id: str,
        directory: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ArtifactDeleteResponse:
        """
        Delete an artifact

        Args:
          session_id: Session ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not artifact_id:
            raise ValueError(f"Expected a non-empty value for `artifact_id` but received {artifact_id!r}")
        return await self._delete(
            f"/artifact/{artifact_id}",
            body=await async_maybe_transform({"session_id": session_id}, artifact_delete_params.ArtifactDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"directory": directory}, artifact_delete_params.ArtifactDeleteParams
                ),
            ),
            cast_to=ArtifactDeleteResponse,
        )

    async def download(
        self,
        artifact_id: str,
        *,
        session_id: str,
        directory: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncBinaryAPIResponse:
        """
        Download an artifact file

        Args:
          session_id: Session ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not artifact_id:
            raise ValueError(f"Expected a non-empty value for `artifact_id` but received {artifact_id!r}")
        extra_headers = {"Accept": "application/octet-stream", **(extra_headers or {})}
        return await self._get(
            f"/artifact/{artifact_id}/download",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "session_id": session_id,
                        "directory": directory,
                    },
                    artifact_download_params.ArtifactDownloadParams,
                ),
            ),
            cast_to=AsyncBinaryAPIResponse,
        )


class ArtifactResourceWithRawResponse:
    def __init__(self, artifact: ArtifactResource) -> None:
        self._artifact = artifact

        self.delete = to_raw_response_wrapper(
            artifact.delete,
        )
        self.download = to_custom_raw_response_wrapper(
            artifact.download,
            BinaryAPIResponse,
        )


class AsyncArtifactResourceWithRawResponse:
    def __init__(self, artifact: AsyncArtifactResource) -> None:
        self._artifact = artifact

        self.delete = async_to_raw_response_wrapper(
            artifact.delete,
        )
        self.download = async_to_custom_raw_response_wrapper(
            artifact.download,
            AsyncBinaryAPIResponse,
        )


class ArtifactResourceWithStreamingResponse:
    def __init__(self, artifact: ArtifactResource) -> None:
        self._artifact = artifact

        self.delete = to_streamed_response_wrapper(
            artifact.delete,
        )
        self.download = to_custom_streamed_response_wrapper(
            artifact.download,
            StreamedBinaryAPIResponse,
        )


class AsyncArtifactResourceWithStreamingResponse:
    def __init__(self, artifact: AsyncArtifactResource) -> None:
        self._artifact = artifact

        self.delete = async_to_streamed_response_wrapper(
            artifact.delete,
        )
        self.download = async_to_custom_streamed_response_wrapper(
            artifact.download,
            AsyncStreamedBinaryAPIResponse,
        )
