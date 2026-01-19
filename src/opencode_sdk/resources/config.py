# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
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

        For more information, see https://www.github.com/kaaass/opencode-sdk#accessing-raw-response-data-eg-headers
        """
        return ConfigResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConfigResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kaaass/opencode-sdk#with_streaming_response
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
        Retrieve the current OpenCode configuration settings and preferences.

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
        artifact_allowed_paths: SequenceNotStr[str] | Omit = omit,
        autoshare: bool | Omit = omit,
        autoupdate: Union[bool, Literal["notify"]] | Omit = omit,
        command: Dict[str, config_update_params.Command] | Omit = omit,
        compaction: config_update_params.Compaction | Omit = omit,
        custom_provider_npm_whitelist: SequenceNotStr[str] | Omit = omit,
        default_agent: str | Omit = omit,
        disabled_providers: SequenceNotStr[str] | Omit = omit,
        enabled_providers: SequenceNotStr[str] | Omit = omit,
        enterprise: config_update_params.Enterprise | Omit = omit,
        experimental: config_update_params.Experimental | Omit = omit,
        formatter: Union[bool, Dict[str, config_update_params.FormatterUnionMember1FormatterUnionMember1Item]]
        | Omit = omit,
        instructions: SequenceNotStr[str] | Omit = omit,
        keybinds: config_update_params.Keybinds | Omit = omit,
        layout: Literal["auto", "stretch"] | Omit = omit,
        log_level: Literal["DEBUG", "INFO", "WARN", "ERROR"] | Omit = omit,
        lsp: Union[bool, Dict[str, config_update_params.LspUnionMember1LspUnionMember1Item]] | Omit = omit,
        mcp: Dict[str, config_update_params.Mcp] | Omit = omit,
        mode: config_update_params.Mode | Omit = omit,
        model: str | Omit = omit,
        permission: config_update_params.Permission | Omit = omit,
        plugin: SequenceNotStr[str] | Omit = omit,
        provider: Dict[str, config_update_params.Provider] | Omit = omit,
        server: config_update_params.Server | Omit = omit,
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
        Update OpenCode configuration settings and preferences.

        Args:
          schema: JSON schema reference for configuration validation

          agent: Agent configuration, see https://opencode.ai/docs/agent

          artifact_allowed_paths: 允许创建 artifact 的文件路径前缀白名单。路径将被 resolve 为绝对路径后进行前缀匹
              配。默认允许 /tmp 路径。

          autoshare: @deprecated Use 'share' field instead. Share newly created sessions
              automatically

          autoupdate: Automatically update to the latest version. Set to true to auto-update, false to
              disable, or 'notify' to show update notifications

          command: Command configuration, see https://opencode.ai/docs/commands

          custom_provider_npm_whitelist: 允许用于 custom provider 的 npm 包白名单

          default_agent: Default agent to use when none is specified. Must be a primary agent. Falls back
              to 'build' if not set or if the specified agent is invalid.

          disabled_providers: Disable providers that are loaded automatically

          enabled_providers: When set, ONLY these providers will be enabled. All other providers will be
              ignored

          instructions: Additional instruction files or patterns to include

          keybinds: Custom keybind configurations

          layout: @deprecated Always uses stretch layout.

          log_level: Log level

          mcp: MCP (Model Context Protocol) server configurations

          mode: @deprecated Use `agent` field instead.

          model: Model to use in the format of provider/model, eg anthropic/claude-2

          provider: Custom provider configurations and model overrides

          server: Server configuration for opencode serve and web commands

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
                    "artifact_allowed_paths": artifact_allowed_paths,
                    "autoshare": autoshare,
                    "autoupdate": autoupdate,
                    "command": command,
                    "compaction": compaction,
                    "custom_provider_npm_whitelist": custom_provider_npm_whitelist,
                    "default_agent": default_agent,
                    "disabled_providers": disabled_providers,
                    "enabled_providers": enabled_providers,
                    "enterprise": enterprise,
                    "experimental": experimental,
                    "formatter": formatter,
                    "instructions": instructions,
                    "keybinds": keybinds,
                    "layout": layout,
                    "log_level": log_level,
                    "lsp": lsp,
                    "mcp": mcp,
                    "mode": mode,
                    "model": model,
                    "permission": permission,
                    "plugin": plugin,
                    "provider": provider,
                    "server": server,
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
        Get a list of all configured AI providers and their default models.

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

        For more information, see https://www.github.com/kaaass/opencode-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncConfigResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConfigResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/kaaass/opencode-sdk#with_streaming_response
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
        Retrieve the current OpenCode configuration settings and preferences.

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
        artifact_allowed_paths: SequenceNotStr[str] | Omit = omit,
        autoshare: bool | Omit = omit,
        autoupdate: Union[bool, Literal["notify"]] | Omit = omit,
        command: Dict[str, config_update_params.Command] | Omit = omit,
        compaction: config_update_params.Compaction | Omit = omit,
        custom_provider_npm_whitelist: SequenceNotStr[str] | Omit = omit,
        default_agent: str | Omit = omit,
        disabled_providers: SequenceNotStr[str] | Omit = omit,
        enabled_providers: SequenceNotStr[str] | Omit = omit,
        enterprise: config_update_params.Enterprise | Omit = omit,
        experimental: config_update_params.Experimental | Omit = omit,
        formatter: Union[bool, Dict[str, config_update_params.FormatterUnionMember1FormatterUnionMember1Item]]
        | Omit = omit,
        instructions: SequenceNotStr[str] | Omit = omit,
        keybinds: config_update_params.Keybinds | Omit = omit,
        layout: Literal["auto", "stretch"] | Omit = omit,
        log_level: Literal["DEBUG", "INFO", "WARN", "ERROR"] | Omit = omit,
        lsp: Union[bool, Dict[str, config_update_params.LspUnionMember1LspUnionMember1Item]] | Omit = omit,
        mcp: Dict[str, config_update_params.Mcp] | Omit = omit,
        mode: config_update_params.Mode | Omit = omit,
        model: str | Omit = omit,
        permission: config_update_params.Permission | Omit = omit,
        plugin: SequenceNotStr[str] | Omit = omit,
        provider: Dict[str, config_update_params.Provider] | Omit = omit,
        server: config_update_params.Server | Omit = omit,
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
        Update OpenCode configuration settings and preferences.

        Args:
          schema: JSON schema reference for configuration validation

          agent: Agent configuration, see https://opencode.ai/docs/agent

          artifact_allowed_paths: 允许创建 artifact 的文件路径前缀白名单。路径将被 resolve 为绝对路径后进行前缀匹
              配。默认允许 /tmp 路径。

          autoshare: @deprecated Use 'share' field instead. Share newly created sessions
              automatically

          autoupdate: Automatically update to the latest version. Set to true to auto-update, false to
              disable, or 'notify' to show update notifications

          command: Command configuration, see https://opencode.ai/docs/commands

          custom_provider_npm_whitelist: 允许用于 custom provider 的 npm 包白名单

          default_agent: Default agent to use when none is specified. Must be a primary agent. Falls back
              to 'build' if not set or if the specified agent is invalid.

          disabled_providers: Disable providers that are loaded automatically

          enabled_providers: When set, ONLY these providers will be enabled. All other providers will be
              ignored

          instructions: Additional instruction files or patterns to include

          keybinds: Custom keybind configurations

          layout: @deprecated Always uses stretch layout.

          log_level: Log level

          mcp: MCP (Model Context Protocol) server configurations

          mode: @deprecated Use `agent` field instead.

          model: Model to use in the format of provider/model, eg anthropic/claude-2

          provider: Custom provider configurations and model overrides

          server: Server configuration for opencode serve and web commands

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
                    "artifact_allowed_paths": artifact_allowed_paths,
                    "autoshare": autoshare,
                    "autoupdate": autoupdate,
                    "command": command,
                    "compaction": compaction,
                    "custom_provider_npm_whitelist": custom_provider_npm_whitelist,
                    "default_agent": default_agent,
                    "disabled_providers": disabled_providers,
                    "enabled_providers": enabled_providers,
                    "enterprise": enterprise,
                    "experimental": experimental,
                    "formatter": formatter,
                    "instructions": instructions,
                    "keybinds": keybinds,
                    "layout": layout,
                    "log_level": log_level,
                    "lsp": lsp,
                    "mcp": mcp,
                    "mode": mode,
                    "model": model,
                    "permission": permission,
                    "plugin": plugin,
                    "provider": provider,
                    "server": server,
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
        Get a list of all configured AI providers and their default models.

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
