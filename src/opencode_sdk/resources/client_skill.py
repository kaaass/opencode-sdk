# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Mapping, cast

import httpx

from ..types import client_skill_list_params, client_skill_delete_params, client_skill_upload_params
from .._types import Body, Omit, Query, Headers, NotGiven, FileTypes, omit, not_given
from .._utils import extract_files, maybe_transform, deepcopy_minimal, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.client_skill_list_response import ClientSkillListResponse
from ..types.client_skill_delete_response import ClientSkillDeleteResponse
from ..types.client_skill_upload_response import ClientSkillUploadResponse

__all__ = ["ClientSkillResource", "AsyncClientSkillResource"]


class ClientSkillResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ClientSkillResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kaaass/opencode-sdk#accessing-raw-response-data-eg-headers
        """
        return ClientSkillResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ClientSkillResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kaaass/opencode-sdk#with_streaming_response
        """
        return ClientSkillResourceWithStreamingResponse(self)

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
    ) -> ClientSkillListResponse:
        """
        Get all registered client skills.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/client-skill",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"directory": directory}, client_skill_list_params.ClientSkillListParams),
            ),
            cast_to=ClientSkillListResponse,
        )

    def delete(
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
    ) -> ClientSkillDeleteResponse:
        """
        Remove a client skill and its files.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return self._delete(
            f"/client-skill/{name}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"directory": directory}, client_skill_delete_params.ClientSkillDeleteParams),
            ),
            cast_to=ClientSkillDeleteResponse,
        )

    def upload(
        self,
        *,
        file: FileTypes,
        directory: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ClientSkillUploadResponse:
        """
        Upload a skill package (tar.gz) to be loaded at runtime.

        Args:
          file: Skill package file (tar.gz format)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal({"file": file})
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            "/client-skill",
            body=maybe_transform(body, client_skill_upload_params.ClientSkillUploadParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"directory": directory}, client_skill_upload_params.ClientSkillUploadParams),
            ),
            cast_to=ClientSkillUploadResponse,
        )


class AsyncClientSkillResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncClientSkillResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/kaaass/opencode-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncClientSkillResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncClientSkillResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kaaass/opencode-sdk#with_streaming_response
        """
        return AsyncClientSkillResourceWithStreamingResponse(self)

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
    ) -> ClientSkillListResponse:
        """
        Get all registered client skills.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/client-skill",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"directory": directory}, client_skill_list_params.ClientSkillListParams
                ),
            ),
            cast_to=ClientSkillListResponse,
        )

    async def delete(
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
    ) -> ClientSkillDeleteResponse:
        """
        Remove a client skill and its files.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return await self._delete(
            f"/client-skill/{name}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"directory": directory}, client_skill_delete_params.ClientSkillDeleteParams
                ),
            ),
            cast_to=ClientSkillDeleteResponse,
        )

    async def upload(
        self,
        *,
        file: FileTypes,
        directory: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ClientSkillUploadResponse:
        """
        Upload a skill package (tar.gz) to be loaded at runtime.

        Args:
          file: Skill package file (tar.gz format)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal({"file": file})
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            "/client-skill",
            body=await async_maybe_transform(body, client_skill_upload_params.ClientSkillUploadParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"directory": directory}, client_skill_upload_params.ClientSkillUploadParams
                ),
            ),
            cast_to=ClientSkillUploadResponse,
        )


class ClientSkillResourceWithRawResponse:
    def __init__(self, client_skill: ClientSkillResource) -> None:
        self._client_skill = client_skill

        self.list = to_raw_response_wrapper(
            client_skill.list,
        )
        self.delete = to_raw_response_wrapper(
            client_skill.delete,
        )
        self.upload = to_raw_response_wrapper(
            client_skill.upload,
        )


class AsyncClientSkillResourceWithRawResponse:
    def __init__(self, client_skill: AsyncClientSkillResource) -> None:
        self._client_skill = client_skill

        self.list = async_to_raw_response_wrapper(
            client_skill.list,
        )
        self.delete = async_to_raw_response_wrapper(
            client_skill.delete,
        )
        self.upload = async_to_raw_response_wrapper(
            client_skill.upload,
        )


class ClientSkillResourceWithStreamingResponse:
    def __init__(self, client_skill: ClientSkillResource) -> None:
        self._client_skill = client_skill

        self.list = to_streamed_response_wrapper(
            client_skill.list,
        )
        self.delete = to_streamed_response_wrapper(
            client_skill.delete,
        )
        self.upload = to_streamed_response_wrapper(
            client_skill.upload,
        )


class AsyncClientSkillResourceWithStreamingResponse:
    def __init__(self, client_skill: AsyncClientSkillResource) -> None:
        self._client_skill = client_skill

        self.list = async_to_streamed_response_wrapper(
            client_skill.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            client_skill.delete,
        )
        self.upload = async_to_streamed_response_wrapper(
            client_skill.upload,
        )
