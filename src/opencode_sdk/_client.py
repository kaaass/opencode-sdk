# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Headers,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import is_given, get_async_library
from ._compat import cached_property
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import (
        log,
        lsp,
        mcp,
        pty,
        tui,
        vcs,
        auth,
        file,
        find,
        path,
        agent,
        event,
        config,
        command,
        global_,
        project,
        session,
        instance,
        provider,
        question,
        formatter,
        permission,
        client_tool,
        experimental,
    )
    from .resources.log import LogResource, AsyncLogResource
    from .resources.lsp import LspResource, AsyncLspResource
    from .resources.pty import PtyResource, AsyncPtyResource
    from .resources.vcs import VcsResource, AsyncVcsResource
    from .resources.auth import AuthResource, AsyncAuthResource
    from .resources.file import FileResource, AsyncFileResource
    from .resources.find import FindResource, AsyncFindResource
    from .resources.path import PathResource, AsyncPathResource
    from .resources.agent import AgentResource, AsyncAgentResource
    from .resources.event import EventResource, AsyncEventResource
    from .resources.config import ConfigResource, AsyncConfigResource
    from .resources.command import CommandResource, AsyncCommandResource
    from .resources.global_ import GlobalResource, AsyncGlobalResource
    from .resources.mcp.mcp import McpResource, AsyncMcpResource
    from .resources.project import ProjectResource, AsyncProjectResource
    from .resources.tui.tui import TuiResource, AsyncTuiResource
    from .resources.instance import InstanceResource, AsyncInstanceResource
    from .resources.question import QuestionResource, AsyncQuestionResource
    from .resources.formatter import FormatterResource, AsyncFormatterResource
    from .resources.permission import PermissionResource, AsyncPermissionResource
    from .resources.client_tool import ClientToolResource, AsyncClientToolResource
    from .resources.session.session import SessionResource, AsyncSessionResource
    from .resources.provider.provider import ProviderResource, AsyncProviderResource
    from .resources.experimental.experimental import ExperimentalResource, AsyncExperimentalResource

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
    # client options
    api_key: str | None

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable SSL certificate verification.
        # When set to False, SSL certificates will not be verified.
        # This is useful for development with self-signed certificates.
        # WARNING: Disabling SSL verification is insecure and should only be used in development.
        verify_ssl: bool = True,
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
        """Construct a new synchronous OpencodeSDK client instance.

        This automatically infers the `api_key` argument from the `OPENCODE_SDK_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("OPENCODE_SDK_API_KEY")
        self.api_key = api_key

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
            verify_ssl=verify_ssl,
        )

        self._default_stream_cls = Stream

    @cached_property
    def project(self) -> ProjectResource:
        from .resources.project import ProjectResource

        return ProjectResource(self)

    @cached_property
    def config(self) -> ConfigResource:
        from .resources.config import ConfigResource

        return ConfigResource(self)

    @cached_property
    def experimental(self) -> ExperimentalResource:
        from .resources.experimental import ExperimentalResource

        return ExperimentalResource(self)

    @cached_property
    def path(self) -> PathResource:
        from .resources.path import PathResource

        return PathResource(self)

    @cached_property
    def session(self) -> SessionResource:
        from .resources.session import SessionResource

        return SessionResource(self)

    @cached_property
    def command(self) -> CommandResource:
        from .resources.command import CommandResource

        return CommandResource(self)

    @cached_property
    def find(self) -> FindResource:
        from .resources.find import FindResource

        return FindResource(self)

    @cached_property
    def file(self) -> FileResource:
        from .resources.file import FileResource

        return FileResource(self)

    @cached_property
    def log(self) -> LogResource:
        from .resources.log import LogResource

        return LogResource(self)

    @cached_property
    def agent(self) -> AgentResource:
        from .resources.agent import AgentResource

        return AgentResource(self)

    @cached_property
    def mcp(self) -> McpResource:
        from .resources.mcp import McpResource

        return McpResource(self)

    @cached_property
    def tui(self) -> TuiResource:
        from .resources.tui import TuiResource

        return TuiResource(self)

    @cached_property
    def auth(self) -> AuthResource:
        from .resources.auth import AuthResource

        return AuthResource(self)

    @cached_property
    def event(self) -> EventResource:
        from .resources.event import EventResource

        return EventResource(self)

    @cached_property
    def global_(self) -> GlobalResource:
        from .resources.global_ import GlobalResource

        return GlobalResource(self)

    @cached_property
    def pty(self) -> PtyResource:
        from .resources.pty import PtyResource

        return PtyResource(self)

    @cached_property
    def instance(self) -> InstanceResource:
        from .resources.instance import InstanceResource

        return InstanceResource(self)

    @cached_property
    def vcs(self) -> VcsResource:
        from .resources.vcs import VcsResource

        return VcsResource(self)

    @cached_property
    def provider(self) -> ProviderResource:
        from .resources.provider import ProviderResource

        return ProviderResource(self)

    @cached_property
    def client_tool(self) -> ClientToolResource:
        from .resources.client_tool import ClientToolResource

        return ClientToolResource(self)

    @cached_property
    def lsp(self) -> LspResource:
        from .resources.lsp import LspResource

        return LspResource(self)

    @cached_property
    def formatter(self) -> FormatterResource:
        from .resources.formatter import FormatterResource

        return FormatterResource(self)

    @cached_property
    def permission(self) -> PermissionResource:
        from .resources.permission import PermissionResource

        return PermissionResource(self)

    @cached_property
    def question(self) -> QuestionResource:
        from .resources.question import QuestionResource

        return QuestionResource(self)

    @cached_property
    def with_raw_response(self) -> OpencodeSDKWithRawResponse:
        return OpencodeSDKWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OpencodeSDKWithStreamedResponse:
        return OpencodeSDKWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        if api_key is None:
            return {}
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    @override
    def _validate_headers(self, headers: Headers, custom_headers: Headers) -> None:
        if headers.get("Authorization") or isinstance(custom_headers.get("Authorization"), Omit):
            return

        raise TypeError(
            '"Could not resolve authentication method. Expected the api_key to be set. Or for the `Authorization` headers to be explicitly omitted"'
        )

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        verify_ssl: bool | NotGiven = not_given,
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
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            verify_ssl=verify_ssl if is_given(verify_ssl) else True,
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
    # client options
    api_key: str | None

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable SSL certificate verification.
        # When set to False, SSL certificates will not be verified.
        # This is useful for development with self-signed certificates.
        # WARNING: Disabling SSL verification is insecure and should only be used in development.
        verify_ssl: bool = True,
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
        """Construct a new async AsyncOpencodeSDK client instance.

        This automatically infers the `api_key` argument from the `OPENCODE_SDK_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("OPENCODE_SDK_API_KEY")
        self.api_key = api_key

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
            verify_ssl=verify_ssl,
        )

        self._default_stream_cls = AsyncStream

    @cached_property
    def project(self) -> AsyncProjectResource:
        from .resources.project import AsyncProjectResource

        return AsyncProjectResource(self)

    @cached_property
    def config(self) -> AsyncConfigResource:
        from .resources.config import AsyncConfigResource

        return AsyncConfigResource(self)

    @cached_property
    def experimental(self) -> AsyncExperimentalResource:
        from .resources.experimental import AsyncExperimentalResource

        return AsyncExperimentalResource(self)

    @cached_property
    def path(self) -> AsyncPathResource:
        from .resources.path import AsyncPathResource

        return AsyncPathResource(self)

    @cached_property
    def session(self) -> AsyncSessionResource:
        from .resources.session import AsyncSessionResource

        return AsyncSessionResource(self)

    @cached_property
    def command(self) -> AsyncCommandResource:
        from .resources.command import AsyncCommandResource

        return AsyncCommandResource(self)

    @cached_property
    def find(self) -> AsyncFindResource:
        from .resources.find import AsyncFindResource

        return AsyncFindResource(self)

    @cached_property
    def file(self) -> AsyncFileResource:
        from .resources.file import AsyncFileResource

        return AsyncFileResource(self)

    @cached_property
    def log(self) -> AsyncLogResource:
        from .resources.log import AsyncLogResource

        return AsyncLogResource(self)

    @cached_property
    def agent(self) -> AsyncAgentResource:
        from .resources.agent import AsyncAgentResource

        return AsyncAgentResource(self)

    @cached_property
    def mcp(self) -> AsyncMcpResource:
        from .resources.mcp import AsyncMcpResource

        return AsyncMcpResource(self)

    @cached_property
    def tui(self) -> AsyncTuiResource:
        from .resources.tui import AsyncTuiResource

        return AsyncTuiResource(self)

    @cached_property
    def auth(self) -> AsyncAuthResource:
        from .resources.auth import AsyncAuthResource

        return AsyncAuthResource(self)

    @cached_property
    def event(self) -> AsyncEventResource:
        from .resources.event import AsyncEventResource

        return AsyncEventResource(self)

    @cached_property
    def global_(self) -> AsyncGlobalResource:
        from .resources.global_ import AsyncGlobalResource

        return AsyncGlobalResource(self)

    @cached_property
    def pty(self) -> AsyncPtyResource:
        from .resources.pty import AsyncPtyResource

        return AsyncPtyResource(self)

    @cached_property
    def instance(self) -> AsyncInstanceResource:
        from .resources.instance import AsyncInstanceResource

        return AsyncInstanceResource(self)

    @cached_property
    def vcs(self) -> AsyncVcsResource:
        from .resources.vcs import AsyncVcsResource

        return AsyncVcsResource(self)

    @cached_property
    def provider(self) -> AsyncProviderResource:
        from .resources.provider import AsyncProviderResource

        return AsyncProviderResource(self)

    @cached_property
    def client_tool(self) -> AsyncClientToolResource:
        from .resources.client_tool import AsyncClientToolResource

        return AsyncClientToolResource(self)

    @cached_property
    def lsp(self) -> AsyncLspResource:
        from .resources.lsp import AsyncLspResource

        return AsyncLspResource(self)

    @cached_property
    def formatter(self) -> AsyncFormatterResource:
        from .resources.formatter import AsyncFormatterResource

        return AsyncFormatterResource(self)

    @cached_property
    def permission(self) -> AsyncPermissionResource:
        from .resources.permission import AsyncPermissionResource

        return AsyncPermissionResource(self)

    @cached_property
    def question(self) -> AsyncQuestionResource:
        from .resources.question import AsyncQuestionResource

        return AsyncQuestionResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncOpencodeSDKWithRawResponse:
        return AsyncOpencodeSDKWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOpencodeSDKWithStreamedResponse:
        return AsyncOpencodeSDKWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        if api_key is None:
            return {}
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    @override
    def _validate_headers(self, headers: Headers, custom_headers: Headers) -> None:
        if headers.get("Authorization") or isinstance(custom_headers.get("Authorization"), Omit):
            return

        raise TypeError(
            '"Could not resolve authentication method. Expected the api_key to be set. Or for the `Authorization` headers to be explicitly omitted"'
        )

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        verify_ssl: bool | NotGiven = not_given,
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
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            verify_ssl=verify_ssl if is_given(verify_ssl) else True,
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
    _client: OpencodeSDK

    def __init__(self, client: OpencodeSDK) -> None:
        self._client = client

    @cached_property
    def project(self) -> project.ProjectResourceWithRawResponse:
        from .resources.project import ProjectResourceWithRawResponse

        return ProjectResourceWithRawResponse(self._client.project)

    @cached_property
    def config(self) -> config.ConfigResourceWithRawResponse:
        from .resources.config import ConfigResourceWithRawResponse

        return ConfigResourceWithRawResponse(self._client.config)

    @cached_property
    def experimental(self) -> experimental.ExperimentalResourceWithRawResponse:
        from .resources.experimental import ExperimentalResourceWithRawResponse

        return ExperimentalResourceWithRawResponse(self._client.experimental)

    @cached_property
    def path(self) -> path.PathResourceWithRawResponse:
        from .resources.path import PathResourceWithRawResponse

        return PathResourceWithRawResponse(self._client.path)

    @cached_property
    def session(self) -> session.SessionResourceWithRawResponse:
        from .resources.session import SessionResourceWithRawResponse

        return SessionResourceWithRawResponse(self._client.session)

    @cached_property
    def command(self) -> command.CommandResourceWithRawResponse:
        from .resources.command import CommandResourceWithRawResponse

        return CommandResourceWithRawResponse(self._client.command)

    @cached_property
    def find(self) -> find.FindResourceWithRawResponse:
        from .resources.find import FindResourceWithRawResponse

        return FindResourceWithRawResponse(self._client.find)

    @cached_property
    def file(self) -> file.FileResourceWithRawResponse:
        from .resources.file import FileResourceWithRawResponse

        return FileResourceWithRawResponse(self._client.file)

    @cached_property
    def log(self) -> log.LogResourceWithRawResponse:
        from .resources.log import LogResourceWithRawResponse

        return LogResourceWithRawResponse(self._client.log)

    @cached_property
    def agent(self) -> agent.AgentResourceWithRawResponse:
        from .resources.agent import AgentResourceWithRawResponse

        return AgentResourceWithRawResponse(self._client.agent)

    @cached_property
    def mcp(self) -> mcp.McpResourceWithRawResponse:
        from .resources.mcp import McpResourceWithRawResponse

        return McpResourceWithRawResponse(self._client.mcp)

    @cached_property
    def tui(self) -> tui.TuiResourceWithRawResponse:
        from .resources.tui import TuiResourceWithRawResponse

        return TuiResourceWithRawResponse(self._client.tui)

    @cached_property
    def auth(self) -> auth.AuthResourceWithRawResponse:
        from .resources.auth import AuthResourceWithRawResponse

        return AuthResourceWithRawResponse(self._client.auth)

    @cached_property
    def event(self) -> event.EventResourceWithRawResponse:
        from .resources.event import EventResourceWithRawResponse

        return EventResourceWithRawResponse(self._client.event)

    @cached_property
    def global_(self) -> global_.GlobalResourceWithRawResponse:
        from .resources.global_ import GlobalResourceWithRawResponse

        return GlobalResourceWithRawResponse(self._client.global_)

    @cached_property
    def pty(self) -> pty.PtyResourceWithRawResponse:
        from .resources.pty import PtyResourceWithRawResponse

        return PtyResourceWithRawResponse(self._client.pty)

    @cached_property
    def instance(self) -> instance.InstanceResourceWithRawResponse:
        from .resources.instance import InstanceResourceWithRawResponse

        return InstanceResourceWithRawResponse(self._client.instance)

    @cached_property
    def vcs(self) -> vcs.VcsResourceWithRawResponse:
        from .resources.vcs import VcsResourceWithRawResponse

        return VcsResourceWithRawResponse(self._client.vcs)

    @cached_property
    def provider(self) -> provider.ProviderResourceWithRawResponse:
        from .resources.provider import ProviderResourceWithRawResponse

        return ProviderResourceWithRawResponse(self._client.provider)

    @cached_property
    def client_tool(self) -> client_tool.ClientToolResourceWithRawResponse:
        from .resources.client_tool import ClientToolResourceWithRawResponse

        return ClientToolResourceWithRawResponse(self._client.client_tool)

    @cached_property
    def lsp(self) -> lsp.LspResourceWithRawResponse:
        from .resources.lsp import LspResourceWithRawResponse

        return LspResourceWithRawResponse(self._client.lsp)

    @cached_property
    def formatter(self) -> formatter.FormatterResourceWithRawResponse:
        from .resources.formatter import FormatterResourceWithRawResponse

        return FormatterResourceWithRawResponse(self._client.formatter)

    @cached_property
    def permission(self) -> permission.PermissionResourceWithRawResponse:
        from .resources.permission import PermissionResourceWithRawResponse

        return PermissionResourceWithRawResponse(self._client.permission)

    @cached_property
    def question(self) -> question.QuestionResourceWithRawResponse:
        from .resources.question import QuestionResourceWithRawResponse

        return QuestionResourceWithRawResponse(self._client.question)


class AsyncOpencodeSDKWithRawResponse:
    _client: AsyncOpencodeSDK

    def __init__(self, client: AsyncOpencodeSDK) -> None:
        self._client = client

    @cached_property
    def project(self) -> project.AsyncProjectResourceWithRawResponse:
        from .resources.project import AsyncProjectResourceWithRawResponse

        return AsyncProjectResourceWithRawResponse(self._client.project)

    @cached_property
    def config(self) -> config.AsyncConfigResourceWithRawResponse:
        from .resources.config import AsyncConfigResourceWithRawResponse

        return AsyncConfigResourceWithRawResponse(self._client.config)

    @cached_property
    def experimental(self) -> experimental.AsyncExperimentalResourceWithRawResponse:
        from .resources.experimental import AsyncExperimentalResourceWithRawResponse

        return AsyncExperimentalResourceWithRawResponse(self._client.experimental)

    @cached_property
    def path(self) -> path.AsyncPathResourceWithRawResponse:
        from .resources.path import AsyncPathResourceWithRawResponse

        return AsyncPathResourceWithRawResponse(self._client.path)

    @cached_property
    def session(self) -> session.AsyncSessionResourceWithRawResponse:
        from .resources.session import AsyncSessionResourceWithRawResponse

        return AsyncSessionResourceWithRawResponse(self._client.session)

    @cached_property
    def command(self) -> command.AsyncCommandResourceWithRawResponse:
        from .resources.command import AsyncCommandResourceWithRawResponse

        return AsyncCommandResourceWithRawResponse(self._client.command)

    @cached_property
    def find(self) -> find.AsyncFindResourceWithRawResponse:
        from .resources.find import AsyncFindResourceWithRawResponse

        return AsyncFindResourceWithRawResponse(self._client.find)

    @cached_property
    def file(self) -> file.AsyncFileResourceWithRawResponse:
        from .resources.file import AsyncFileResourceWithRawResponse

        return AsyncFileResourceWithRawResponse(self._client.file)

    @cached_property
    def log(self) -> log.AsyncLogResourceWithRawResponse:
        from .resources.log import AsyncLogResourceWithRawResponse

        return AsyncLogResourceWithRawResponse(self._client.log)

    @cached_property
    def agent(self) -> agent.AsyncAgentResourceWithRawResponse:
        from .resources.agent import AsyncAgentResourceWithRawResponse

        return AsyncAgentResourceWithRawResponse(self._client.agent)

    @cached_property
    def mcp(self) -> mcp.AsyncMcpResourceWithRawResponse:
        from .resources.mcp import AsyncMcpResourceWithRawResponse

        return AsyncMcpResourceWithRawResponse(self._client.mcp)

    @cached_property
    def tui(self) -> tui.AsyncTuiResourceWithRawResponse:
        from .resources.tui import AsyncTuiResourceWithRawResponse

        return AsyncTuiResourceWithRawResponse(self._client.tui)

    @cached_property
    def auth(self) -> auth.AsyncAuthResourceWithRawResponse:
        from .resources.auth import AsyncAuthResourceWithRawResponse

        return AsyncAuthResourceWithRawResponse(self._client.auth)

    @cached_property
    def event(self) -> event.AsyncEventResourceWithRawResponse:
        from .resources.event import AsyncEventResourceWithRawResponse

        return AsyncEventResourceWithRawResponse(self._client.event)

    @cached_property
    def global_(self) -> global_.AsyncGlobalResourceWithRawResponse:
        from .resources.global_ import AsyncGlobalResourceWithRawResponse

        return AsyncGlobalResourceWithRawResponse(self._client.global_)

    @cached_property
    def pty(self) -> pty.AsyncPtyResourceWithRawResponse:
        from .resources.pty import AsyncPtyResourceWithRawResponse

        return AsyncPtyResourceWithRawResponse(self._client.pty)

    @cached_property
    def instance(self) -> instance.AsyncInstanceResourceWithRawResponse:
        from .resources.instance import AsyncInstanceResourceWithRawResponse

        return AsyncInstanceResourceWithRawResponse(self._client.instance)

    @cached_property
    def vcs(self) -> vcs.AsyncVcsResourceWithRawResponse:
        from .resources.vcs import AsyncVcsResourceWithRawResponse

        return AsyncVcsResourceWithRawResponse(self._client.vcs)

    @cached_property
    def provider(self) -> provider.AsyncProviderResourceWithRawResponse:
        from .resources.provider import AsyncProviderResourceWithRawResponse

        return AsyncProviderResourceWithRawResponse(self._client.provider)

    @cached_property
    def client_tool(self) -> client_tool.AsyncClientToolResourceWithRawResponse:
        from .resources.client_tool import AsyncClientToolResourceWithRawResponse

        return AsyncClientToolResourceWithRawResponse(self._client.client_tool)

    @cached_property
    def lsp(self) -> lsp.AsyncLspResourceWithRawResponse:
        from .resources.lsp import AsyncLspResourceWithRawResponse

        return AsyncLspResourceWithRawResponse(self._client.lsp)

    @cached_property
    def formatter(self) -> formatter.AsyncFormatterResourceWithRawResponse:
        from .resources.formatter import AsyncFormatterResourceWithRawResponse

        return AsyncFormatterResourceWithRawResponse(self._client.formatter)

    @cached_property
    def permission(self) -> permission.AsyncPermissionResourceWithRawResponse:
        from .resources.permission import AsyncPermissionResourceWithRawResponse

        return AsyncPermissionResourceWithRawResponse(self._client.permission)

    @cached_property
    def question(self) -> question.AsyncQuestionResourceWithRawResponse:
        from .resources.question import AsyncQuestionResourceWithRawResponse

        return AsyncQuestionResourceWithRawResponse(self._client.question)


class OpencodeSDKWithStreamedResponse:
    _client: OpencodeSDK

    def __init__(self, client: OpencodeSDK) -> None:
        self._client = client

    @cached_property
    def project(self) -> project.ProjectResourceWithStreamingResponse:
        from .resources.project import ProjectResourceWithStreamingResponse

        return ProjectResourceWithStreamingResponse(self._client.project)

    @cached_property
    def config(self) -> config.ConfigResourceWithStreamingResponse:
        from .resources.config import ConfigResourceWithStreamingResponse

        return ConfigResourceWithStreamingResponse(self._client.config)

    @cached_property
    def experimental(self) -> experimental.ExperimentalResourceWithStreamingResponse:
        from .resources.experimental import ExperimentalResourceWithStreamingResponse

        return ExperimentalResourceWithStreamingResponse(self._client.experimental)

    @cached_property
    def path(self) -> path.PathResourceWithStreamingResponse:
        from .resources.path import PathResourceWithStreamingResponse

        return PathResourceWithStreamingResponse(self._client.path)

    @cached_property
    def session(self) -> session.SessionResourceWithStreamingResponse:
        from .resources.session import SessionResourceWithStreamingResponse

        return SessionResourceWithStreamingResponse(self._client.session)

    @cached_property
    def command(self) -> command.CommandResourceWithStreamingResponse:
        from .resources.command import CommandResourceWithStreamingResponse

        return CommandResourceWithStreamingResponse(self._client.command)

    @cached_property
    def find(self) -> find.FindResourceWithStreamingResponse:
        from .resources.find import FindResourceWithStreamingResponse

        return FindResourceWithStreamingResponse(self._client.find)

    @cached_property
    def file(self) -> file.FileResourceWithStreamingResponse:
        from .resources.file import FileResourceWithStreamingResponse

        return FileResourceWithStreamingResponse(self._client.file)

    @cached_property
    def log(self) -> log.LogResourceWithStreamingResponse:
        from .resources.log import LogResourceWithStreamingResponse

        return LogResourceWithStreamingResponse(self._client.log)

    @cached_property
    def agent(self) -> agent.AgentResourceWithStreamingResponse:
        from .resources.agent import AgentResourceWithStreamingResponse

        return AgentResourceWithStreamingResponse(self._client.agent)

    @cached_property
    def mcp(self) -> mcp.McpResourceWithStreamingResponse:
        from .resources.mcp import McpResourceWithStreamingResponse

        return McpResourceWithStreamingResponse(self._client.mcp)

    @cached_property
    def tui(self) -> tui.TuiResourceWithStreamingResponse:
        from .resources.tui import TuiResourceWithStreamingResponse

        return TuiResourceWithStreamingResponse(self._client.tui)

    @cached_property
    def auth(self) -> auth.AuthResourceWithStreamingResponse:
        from .resources.auth import AuthResourceWithStreamingResponse

        return AuthResourceWithStreamingResponse(self._client.auth)

    @cached_property
    def event(self) -> event.EventResourceWithStreamingResponse:
        from .resources.event import EventResourceWithStreamingResponse

        return EventResourceWithStreamingResponse(self._client.event)

    @cached_property
    def global_(self) -> global_.GlobalResourceWithStreamingResponse:
        from .resources.global_ import GlobalResourceWithStreamingResponse

        return GlobalResourceWithStreamingResponse(self._client.global_)

    @cached_property
    def pty(self) -> pty.PtyResourceWithStreamingResponse:
        from .resources.pty import PtyResourceWithStreamingResponse

        return PtyResourceWithStreamingResponse(self._client.pty)

    @cached_property
    def instance(self) -> instance.InstanceResourceWithStreamingResponse:
        from .resources.instance import InstanceResourceWithStreamingResponse

        return InstanceResourceWithStreamingResponse(self._client.instance)

    @cached_property
    def vcs(self) -> vcs.VcsResourceWithStreamingResponse:
        from .resources.vcs import VcsResourceWithStreamingResponse

        return VcsResourceWithStreamingResponse(self._client.vcs)

    @cached_property
    def provider(self) -> provider.ProviderResourceWithStreamingResponse:
        from .resources.provider import ProviderResourceWithStreamingResponse

        return ProviderResourceWithStreamingResponse(self._client.provider)

    @cached_property
    def client_tool(self) -> client_tool.ClientToolResourceWithStreamingResponse:
        from .resources.client_tool import ClientToolResourceWithStreamingResponse

        return ClientToolResourceWithStreamingResponse(self._client.client_tool)

    @cached_property
    def lsp(self) -> lsp.LspResourceWithStreamingResponse:
        from .resources.lsp import LspResourceWithStreamingResponse

        return LspResourceWithStreamingResponse(self._client.lsp)

    @cached_property
    def formatter(self) -> formatter.FormatterResourceWithStreamingResponse:
        from .resources.formatter import FormatterResourceWithStreamingResponse

        return FormatterResourceWithStreamingResponse(self._client.formatter)

    @cached_property
    def permission(self) -> permission.PermissionResourceWithStreamingResponse:
        from .resources.permission import PermissionResourceWithStreamingResponse

        return PermissionResourceWithStreamingResponse(self._client.permission)

    @cached_property
    def question(self) -> question.QuestionResourceWithStreamingResponse:
        from .resources.question import QuestionResourceWithStreamingResponse

        return QuestionResourceWithStreamingResponse(self._client.question)


class AsyncOpencodeSDKWithStreamedResponse:
    _client: AsyncOpencodeSDK

    def __init__(self, client: AsyncOpencodeSDK) -> None:
        self._client = client

    @cached_property
    def project(self) -> project.AsyncProjectResourceWithStreamingResponse:
        from .resources.project import AsyncProjectResourceWithStreamingResponse

        return AsyncProjectResourceWithStreamingResponse(self._client.project)

    @cached_property
    def config(self) -> config.AsyncConfigResourceWithStreamingResponse:
        from .resources.config import AsyncConfigResourceWithStreamingResponse

        return AsyncConfigResourceWithStreamingResponse(self._client.config)

    @cached_property
    def experimental(self) -> experimental.AsyncExperimentalResourceWithStreamingResponse:
        from .resources.experimental import AsyncExperimentalResourceWithStreamingResponse

        return AsyncExperimentalResourceWithStreamingResponse(self._client.experimental)

    @cached_property
    def path(self) -> path.AsyncPathResourceWithStreamingResponse:
        from .resources.path import AsyncPathResourceWithStreamingResponse

        return AsyncPathResourceWithStreamingResponse(self._client.path)

    @cached_property
    def session(self) -> session.AsyncSessionResourceWithStreamingResponse:
        from .resources.session import AsyncSessionResourceWithStreamingResponse

        return AsyncSessionResourceWithStreamingResponse(self._client.session)

    @cached_property
    def command(self) -> command.AsyncCommandResourceWithStreamingResponse:
        from .resources.command import AsyncCommandResourceWithStreamingResponse

        return AsyncCommandResourceWithStreamingResponse(self._client.command)

    @cached_property
    def find(self) -> find.AsyncFindResourceWithStreamingResponse:
        from .resources.find import AsyncFindResourceWithStreamingResponse

        return AsyncFindResourceWithStreamingResponse(self._client.find)

    @cached_property
    def file(self) -> file.AsyncFileResourceWithStreamingResponse:
        from .resources.file import AsyncFileResourceWithStreamingResponse

        return AsyncFileResourceWithStreamingResponse(self._client.file)

    @cached_property
    def log(self) -> log.AsyncLogResourceWithStreamingResponse:
        from .resources.log import AsyncLogResourceWithStreamingResponse

        return AsyncLogResourceWithStreamingResponse(self._client.log)

    @cached_property
    def agent(self) -> agent.AsyncAgentResourceWithStreamingResponse:
        from .resources.agent import AsyncAgentResourceWithStreamingResponse

        return AsyncAgentResourceWithStreamingResponse(self._client.agent)

    @cached_property
    def mcp(self) -> mcp.AsyncMcpResourceWithStreamingResponse:
        from .resources.mcp import AsyncMcpResourceWithStreamingResponse

        return AsyncMcpResourceWithStreamingResponse(self._client.mcp)

    @cached_property
    def tui(self) -> tui.AsyncTuiResourceWithStreamingResponse:
        from .resources.tui import AsyncTuiResourceWithStreamingResponse

        return AsyncTuiResourceWithStreamingResponse(self._client.tui)

    @cached_property
    def auth(self) -> auth.AsyncAuthResourceWithStreamingResponse:
        from .resources.auth import AsyncAuthResourceWithStreamingResponse

        return AsyncAuthResourceWithStreamingResponse(self._client.auth)

    @cached_property
    def event(self) -> event.AsyncEventResourceWithStreamingResponse:
        from .resources.event import AsyncEventResourceWithStreamingResponse

        return AsyncEventResourceWithStreamingResponse(self._client.event)

    @cached_property
    def global_(self) -> global_.AsyncGlobalResourceWithStreamingResponse:
        from .resources.global_ import AsyncGlobalResourceWithStreamingResponse

        return AsyncGlobalResourceWithStreamingResponse(self._client.global_)

    @cached_property
    def pty(self) -> pty.AsyncPtyResourceWithStreamingResponse:
        from .resources.pty import AsyncPtyResourceWithStreamingResponse

        return AsyncPtyResourceWithStreamingResponse(self._client.pty)

    @cached_property
    def instance(self) -> instance.AsyncInstanceResourceWithStreamingResponse:
        from .resources.instance import AsyncInstanceResourceWithStreamingResponse

        return AsyncInstanceResourceWithStreamingResponse(self._client.instance)

    @cached_property
    def vcs(self) -> vcs.AsyncVcsResourceWithStreamingResponse:
        from .resources.vcs import AsyncVcsResourceWithStreamingResponse

        return AsyncVcsResourceWithStreamingResponse(self._client.vcs)

    @cached_property
    def provider(self) -> provider.AsyncProviderResourceWithStreamingResponse:
        from .resources.provider import AsyncProviderResourceWithStreamingResponse

        return AsyncProviderResourceWithStreamingResponse(self._client.provider)

    @cached_property
    def client_tool(self) -> client_tool.AsyncClientToolResourceWithStreamingResponse:
        from .resources.client_tool import AsyncClientToolResourceWithStreamingResponse

        return AsyncClientToolResourceWithStreamingResponse(self._client.client_tool)

    @cached_property
    def lsp(self) -> lsp.AsyncLspResourceWithStreamingResponse:
        from .resources.lsp import AsyncLspResourceWithStreamingResponse

        return AsyncLspResourceWithStreamingResponse(self._client.lsp)

    @cached_property
    def formatter(self) -> formatter.AsyncFormatterResourceWithStreamingResponse:
        from .resources.formatter import AsyncFormatterResourceWithStreamingResponse

        return AsyncFormatterResourceWithStreamingResponse(self._client.formatter)

    @cached_property
    def permission(self) -> permission.AsyncPermissionResourceWithStreamingResponse:
        from .resources.permission import AsyncPermissionResourceWithStreamingResponse

        return AsyncPermissionResourceWithStreamingResponse(self._client.permission)

    @cached_property
    def question(self) -> question.AsyncQuestionResourceWithStreamingResponse:
        from .resources.question import AsyncQuestionResourceWithStreamingResponse

        return AsyncQuestionResourceWithStreamingResponse(self._client.question)


Client = OpencodeSDK

AsyncClient = AsyncOpencodeSDK
