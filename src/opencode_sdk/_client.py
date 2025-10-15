# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import is_given, get_async_library
from ._version import __version__
from .resources import log, mcp, tui, auth, file, find, path, agent, event, config, command, project
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)
from .resources.session import session
from .resources.experimental import experimental

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "OpencodeSDK",
    "AsyncOpencodeSDK",
    "Client",
    "AsyncClient",
]


class OpencodeSDK(SyncAPIClient):
    project: project.ProjectResource
    config: config.ConfigResource
    experimental: experimental.ExperimentalResource
    path: path.PathResource
    session: session.SessionResource
    command: command.CommandResource
    find: find.FindResource
    file: file.FileResource
    log: log.LogResource
    agent: agent.AgentResource
    mcp: mcp.McpResource
    tui: tui.TuiResource
    auth: auth.AuthResource
    event: event.EventResource
    with_raw_response: OpencodeSDKWithRawResponse
    with_streaming_response: OpencodeSDKWithStreamedResponse

    # client options

    def __init__(
        self,
        *,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous OpencodeSDK client instance."""
        if base_url is None:
            base_url = os.environ.get("OPENCODE_SDK_BASE_URL")
        if base_url is None:
            base_url = f"https://api.example.com"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self._default_stream_cls = Stream

        self.project = project.ProjectResource(self)
        self.config = config.ConfigResource(self)
        self.experimental = experimental.ExperimentalResource(self)
        self.path = path.PathResource(self)
        self.session = session.SessionResource(self)
        self.command = command.CommandResource(self)
        self.find = find.FindResource(self)
        self.file = file.FileResource(self)
        self.log = log.LogResource(self)
        self.agent = agent.AgentResource(self)
        self.mcp = mcp.McpResource(self)
        self.tui = tui.TuiResource(self)
        self.auth = auth.AuthResource(self)
        self.event = event.EventResource(self)
        self.with_raw_response = OpencodeSDKWithRawResponse(self)
        self.with_streaming_response = OpencodeSDKWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncOpencodeSDK(AsyncAPIClient):
    project: project.AsyncProjectResource
    config: config.AsyncConfigResource
    experimental: experimental.AsyncExperimentalResource
    path: path.AsyncPathResource
    session: session.AsyncSessionResource
    command: command.AsyncCommandResource
    find: find.AsyncFindResource
    file: file.AsyncFileResource
    log: log.AsyncLogResource
    agent: agent.AsyncAgentResource
    mcp: mcp.AsyncMcpResource
    tui: tui.AsyncTuiResource
    auth: auth.AsyncAuthResource
    event: event.AsyncEventResource
    with_raw_response: AsyncOpencodeSDKWithRawResponse
    with_streaming_response: AsyncOpencodeSDKWithStreamedResponse

    # client options

    def __init__(
        self,
        *,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncOpencodeSDK client instance."""
        if base_url is None:
            base_url = os.environ.get("OPENCODE_SDK_BASE_URL")
        if base_url is None:
            base_url = f"https://api.example.com"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self._default_stream_cls = AsyncStream

        self.project = project.AsyncProjectResource(self)
        self.config = config.AsyncConfigResource(self)
        self.experimental = experimental.AsyncExperimentalResource(self)
        self.path = path.AsyncPathResource(self)
        self.session = session.AsyncSessionResource(self)
        self.command = command.AsyncCommandResource(self)
        self.find = find.AsyncFindResource(self)
        self.file = file.AsyncFileResource(self)
        self.log = log.AsyncLogResource(self)
        self.agent = agent.AsyncAgentResource(self)
        self.mcp = mcp.AsyncMcpResource(self)
        self.tui = tui.AsyncTuiResource(self)
        self.auth = auth.AsyncAuthResource(self)
        self.event = event.AsyncEventResource(self)
        self.with_raw_response = AsyncOpencodeSDKWithRawResponse(self)
        self.with_streaming_response = AsyncOpencodeSDKWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class OpencodeSDKWithRawResponse:
    def __init__(self, client: OpencodeSDK) -> None:
        self.project = project.ProjectResourceWithRawResponse(client.project)
        self.config = config.ConfigResourceWithRawResponse(client.config)
        self.experimental = experimental.ExperimentalResourceWithRawResponse(client.experimental)
        self.path = path.PathResourceWithRawResponse(client.path)
        self.session = session.SessionResourceWithRawResponse(client.session)
        self.command = command.CommandResourceWithRawResponse(client.command)
        self.find = find.FindResourceWithRawResponse(client.find)
        self.file = file.FileResourceWithRawResponse(client.file)
        self.log = log.LogResourceWithRawResponse(client.log)
        self.agent = agent.AgentResourceWithRawResponse(client.agent)
        self.mcp = mcp.McpResourceWithRawResponse(client.mcp)
        self.tui = tui.TuiResourceWithRawResponse(client.tui)
        self.auth = auth.AuthResourceWithRawResponse(client.auth)
        self.event = event.EventResourceWithRawResponse(client.event)


class AsyncOpencodeSDKWithRawResponse:
    def __init__(self, client: AsyncOpencodeSDK) -> None:
        self.project = project.AsyncProjectResourceWithRawResponse(client.project)
        self.config = config.AsyncConfigResourceWithRawResponse(client.config)
        self.experimental = experimental.AsyncExperimentalResourceWithRawResponse(client.experimental)
        self.path = path.AsyncPathResourceWithRawResponse(client.path)
        self.session = session.AsyncSessionResourceWithRawResponse(client.session)
        self.command = command.AsyncCommandResourceWithRawResponse(client.command)
        self.find = find.AsyncFindResourceWithRawResponse(client.find)
        self.file = file.AsyncFileResourceWithRawResponse(client.file)
        self.log = log.AsyncLogResourceWithRawResponse(client.log)
        self.agent = agent.AsyncAgentResourceWithRawResponse(client.agent)
        self.mcp = mcp.AsyncMcpResourceWithRawResponse(client.mcp)
        self.tui = tui.AsyncTuiResourceWithRawResponse(client.tui)
        self.auth = auth.AsyncAuthResourceWithRawResponse(client.auth)
        self.event = event.AsyncEventResourceWithRawResponse(client.event)


class OpencodeSDKWithStreamedResponse:
    def __init__(self, client: OpencodeSDK) -> None:
        self.project = project.ProjectResourceWithStreamingResponse(client.project)
        self.config = config.ConfigResourceWithStreamingResponse(client.config)
        self.experimental = experimental.ExperimentalResourceWithStreamingResponse(client.experimental)
        self.path = path.PathResourceWithStreamingResponse(client.path)
        self.session = session.SessionResourceWithStreamingResponse(client.session)
        self.command = command.CommandResourceWithStreamingResponse(client.command)
        self.find = find.FindResourceWithStreamingResponse(client.find)
        self.file = file.FileResourceWithStreamingResponse(client.file)
        self.log = log.LogResourceWithStreamingResponse(client.log)
        self.agent = agent.AgentResourceWithStreamingResponse(client.agent)
        self.mcp = mcp.McpResourceWithStreamingResponse(client.mcp)
        self.tui = tui.TuiResourceWithStreamingResponse(client.tui)
        self.auth = auth.AuthResourceWithStreamingResponse(client.auth)
        self.event = event.EventResourceWithStreamingResponse(client.event)


class AsyncOpencodeSDKWithStreamedResponse:
    def __init__(self, client: AsyncOpencodeSDK) -> None:
        self.project = project.AsyncProjectResourceWithStreamingResponse(client.project)
        self.config = config.AsyncConfigResourceWithStreamingResponse(client.config)
        self.experimental = experimental.AsyncExperimentalResourceWithStreamingResponse(client.experimental)
        self.path = path.AsyncPathResourceWithStreamingResponse(client.path)
        self.session = session.AsyncSessionResourceWithStreamingResponse(client.session)
        self.command = command.AsyncCommandResourceWithStreamingResponse(client.command)
        self.find = find.AsyncFindResourceWithStreamingResponse(client.find)
        self.file = file.AsyncFileResourceWithStreamingResponse(client.file)
        self.log = log.AsyncLogResourceWithStreamingResponse(client.log)
        self.agent = agent.AsyncAgentResourceWithStreamingResponse(client.agent)
        self.mcp = mcp.AsyncMcpResourceWithStreamingResponse(client.mcp)
        self.tui = tui.AsyncTuiResourceWithStreamingResponse(client.tui)
        self.auth = auth.AsyncAuthResourceWithStreamingResponse(client.auth)
        self.event = event.AsyncEventResourceWithStreamingResponse(client.event)


Client = OpencodeSDK

AsyncClient = AsyncOpencodeSDK
