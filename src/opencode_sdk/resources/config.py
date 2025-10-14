# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal

import httpx

from ..types import config_update_params, config_retrieve_params, config_list_providers_params
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
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
from ..types.config import Config
from ..types.config_list_providers_response import ConfigListProvidersResponse

__all__ = ["ConfigResource", "AsyncConfigResource"]


class ConfigResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ConfigResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/opencode-sdk-python#accessing-raw-response-data-eg-headers
        """
        return ConfigResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConfigResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/opencode-sdk-python#with_streaming_response
        """
        return ConfigResourceWithStreamingResponse(self)

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
    ) -> Config:
        """
        Get config info

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/config",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"directory": directory}, config_retrieve_params.ConfigRetrieveParams),
            ),
            cast_to=Config,
        )

    def update(
        self,
        *,
        directory: str | Omit = omit,
        schema: str | Omit = omit,
        agent: config_update_params.Agent | Omit = omit,
        autoshare: bool | Omit = omit,
        autoupdate: bool | Omit = omit,
        command: Dict[str, config_update_params.Command] | Omit = omit,
        disabled_providers: SequenceNotStr[str] | Omit = omit,
        experimental: config_update_params.Experimental | Omit = omit,
        formatter: Dict[str, config_update_params.Formatter] | Omit = omit,
        instructions: SequenceNotStr[str] | Omit = omit,
        keybinds: config_update_params.Keybinds | Omit = omit,
        layout: Literal["auto", "stretch"] | Omit = omit,
        lsp: Dict[str, config_update_params.Lsp] | Omit = omit,
        mcp: Dict[str, config_update_params.Mcp] | Omit = omit,
        mode: config_update_params.Mode | Omit = omit,
        model: str | Omit = omit,
        permission: config_update_params.Permission | Omit = omit,
        plugin: SequenceNotStr[str] | Omit = omit,
        provider: Dict[str, config_update_params.Provider] | Omit = omit,
        share: Literal["manual", "auto", "disabled"] | Omit = omit,
        small_model: str | Omit = omit,
        snapshot: bool | Omit = omit,
        theme: str | Omit = omit,
        tools: Dict[str, bool] | Omit = omit,
        tui: config_update_params.Tui | Omit = omit,
        username: str | Omit = omit,
        watcher: config_update_params.Watcher | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Config:
        """
        Update config

        Args:
          schema: JSON schema reference for configuration validation

          agent: Agent configuration, see https://opencode.ai/docs/agent

          autoshare: @deprecated Use 'share' field instead. Share newly created sessions
              automatically

          autoupdate: Automatically update to the latest version

          command: Command configuration, see https://opencode.ai/docs/commands

          disabled_providers: Disable providers that are loaded automatically

          instructions: Additional instruction files or patterns to include

          keybinds: Custom keybind configurations

          layout: @deprecated Always uses stretch layout.

          mcp: MCP (Model Context Protocol) server configurations

          mode: @deprecated Use `agent` field instead.

          model: Model to use in the format of provider/model, eg anthropic/claude-2

          provider: Custom provider configurations and model overrides

          share: Control sharing behavior:'manual' allows manual sharing via commands, 'auto'
              enables automatic sharing, 'disabled' disables all sharing

          small_model: Small model to use for tasks like title generation in the format of
              provider/model

          theme: Theme name to use for the interface

          tui: TUI specific settings

          username: Custom username to display in conversations instead of system username

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            "/config",
            body=maybe_transform(
                {
                    "schema": schema,
                    "agent": agent,
                    "autoshare": autoshare,
                    "autoupdate": autoupdate,
                    "command": command,
                    "disabled_providers": disabled_providers,
                    "experimental": experimental,
                    "formatter": formatter,
                    "instructions": instructions,
                    "keybinds": keybinds,
                    "layout": layout,
                    "lsp": lsp,
                    "mcp": mcp,
                    "mode": mode,
                    "model": model,
                    "permission": permission,
                    "plugin": plugin,
                    "provider": provider,
                    "share": share,
                    "small_model": small_model,
                    "snapshot": snapshot,
                    "theme": theme,
                    "tools": tools,
                    "tui": tui,
                    "username": username,
                    "watcher": watcher,
                },
                config_update_params.ConfigUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"directory": directory}, config_update_params.ConfigUpdateParams),
            ),
            cast_to=Config,
        )

    def list_providers(
        self,
        *,
        directory: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConfigListProvidersResponse:
        """
        List all providers

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/config/providers",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"directory": directory}, config_list_providers_params.ConfigListProvidersParams),
            ),
            cast_to=ConfigListProvidersResponse,
        )


class AsyncConfigResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncConfigResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/opencode-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncConfigResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConfigResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/opencode-sdk-python#with_streaming_response
        """
        return AsyncConfigResourceWithStreamingResponse(self)

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
    ) -> Config:
        """
        Get config info

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/config",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"directory": directory}, config_retrieve_params.ConfigRetrieveParams
                ),
            ),
            cast_to=Config,
        )

    async def update(
        self,
        *,
        directory: str | Omit = omit,
        schema: str | Omit = omit,
        agent: config_update_params.Agent | Omit = omit,
        autoshare: bool | Omit = omit,
        autoupdate: bool | Omit = omit,
        command: Dict[str, config_update_params.Command] | Omit = omit,
        disabled_providers: SequenceNotStr[str] | Omit = omit,
        experimental: config_update_params.Experimental | Omit = omit,
        formatter: Dict[str, config_update_params.Formatter] | Omit = omit,
        instructions: SequenceNotStr[str] | Omit = omit,
        keybinds: config_update_params.Keybinds | Omit = omit,
        layout: Literal["auto", "stretch"] | Omit = omit,
        lsp: Dict[str, config_update_params.Lsp] | Omit = omit,
        mcp: Dict[str, config_update_params.Mcp] | Omit = omit,
        mode: config_update_params.Mode | Omit = omit,
        model: str | Omit = omit,
        permission: config_update_params.Permission | Omit = omit,
        plugin: SequenceNotStr[str] | Omit = omit,
        provider: Dict[str, config_update_params.Provider] | Omit = omit,
        share: Literal["manual", "auto", "disabled"] | Omit = omit,
        small_model: str | Omit = omit,
        snapshot: bool | Omit = omit,
        theme: str | Omit = omit,
        tools: Dict[str, bool] | Omit = omit,
        tui: config_update_params.Tui | Omit = omit,
        username: str | Omit = omit,
        watcher: config_update_params.Watcher | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Config:
        """
        Update config

        Args:
          schema: JSON schema reference for configuration validation

          agent: Agent configuration, see https://opencode.ai/docs/agent

          autoshare: @deprecated Use 'share' field instead. Share newly created sessions
              automatically

          autoupdate: Automatically update to the latest version

          command: Command configuration, see https://opencode.ai/docs/commands

          disabled_providers: Disable providers that are loaded automatically

          instructions: Additional instruction files or patterns to include

          keybinds: Custom keybind configurations

          layout: @deprecated Always uses stretch layout.

          mcp: MCP (Model Context Protocol) server configurations

          mode: @deprecated Use `agent` field instead.

          model: Model to use in the format of provider/model, eg anthropic/claude-2

          provider: Custom provider configurations and model overrides

          share: Control sharing behavior:'manual' allows manual sharing via commands, 'auto'
              enables automatic sharing, 'disabled' disables all sharing

          small_model: Small model to use for tasks like title generation in the format of
              provider/model

          theme: Theme name to use for the interface

          tui: TUI specific settings

          username: Custom username to display in conversations instead of system username

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            "/config",
            body=await async_maybe_transform(
                {
                    "schema": schema,
                    "agent": agent,
                    "autoshare": autoshare,
                    "autoupdate": autoupdate,
                    "command": command,
                    "disabled_providers": disabled_providers,
                    "experimental": experimental,
                    "formatter": formatter,
                    "instructions": instructions,
                    "keybinds": keybinds,
                    "layout": layout,
                    "lsp": lsp,
                    "mcp": mcp,
                    "mode": mode,
                    "model": model,
                    "permission": permission,
                    "plugin": plugin,
                    "provider": provider,
                    "share": share,
                    "small_model": small_model,
                    "snapshot": snapshot,
                    "theme": theme,
                    "tools": tools,
                    "tui": tui,
                    "username": username,
                    "watcher": watcher,
                },
                config_update_params.ConfigUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"directory": directory}, config_update_params.ConfigUpdateParams),
            ),
            cast_to=Config,
        )

    async def list_providers(
        self,
        *,
        directory: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConfigListProvidersResponse:
        """
        List all providers

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/config/providers",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"directory": directory}, config_list_providers_params.ConfigListProvidersParams
                ),
            ),
            cast_to=ConfigListProvidersResponse,
        )


class ConfigResourceWithRawResponse:
    def __init__(self, config: ConfigResource) -> None:
        self._config = config

        self.retrieve = to_raw_response_wrapper(
            config.retrieve,
        )
        self.update = to_raw_response_wrapper(
            config.update,
        )
        self.list_providers = to_raw_response_wrapper(
            config.list_providers,
        )


class AsyncConfigResourceWithRawResponse:
    def __init__(self, config: AsyncConfigResource) -> None:
        self._config = config

        self.retrieve = async_to_raw_response_wrapper(
            config.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            config.update,
        )
        self.list_providers = async_to_raw_response_wrapper(
            config.list_providers,
        )


class ConfigResourceWithStreamingResponse:
    def __init__(self, config: ConfigResource) -> None:
        self._config = config

        self.retrieve = to_streamed_response_wrapper(
            config.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            config.update,
        )
        self.list_providers = to_streamed_response_wrapper(
            config.list_providers,
        )


class AsyncConfigResourceWithStreamingResponse:
    def __init__(self, config: AsyncConfigResource) -> None:
        self._config = config

        self.retrieve = async_to_streamed_response_wrapper(
            config.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            config.update,
        )
        self.list_providers = async_to_streamed_response_wrapper(
            config.list_providers,
        )
