# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from opencode_sdk import OpencodeSDK, AsyncOpencodeSDK
from opencode_sdk.types import (
    Config,
    ConfigListProvidersResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestConfig:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: OpencodeSDK) -> None:
        config = client.config.retrieve()
        assert_matches_type(Config, config, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: OpencodeSDK) -> None:
        config = client.config.retrieve(
            directory="directory",
        )
        assert_matches_type(Config, config, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: OpencodeSDK) -> None:
        response = client.config.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = response.parse()
        assert_matches_type(Config, config, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: OpencodeSDK) -> None:
        with client.config.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = response.parse()
            assert_matches_type(Config, config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: OpencodeSDK) -> None:
        config = client.config.update()
        assert_matches_type(Config, config, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: OpencodeSDK) -> None:
        config = client.config.update(
            directory="directory",
            schema="$schema",
            agent={
                "build": {
                    "description": "description",
                    "disable": True,
                    "mode": "subagent",
                    "model": "model",
                    "permission": {
                        "bash": "ask",
                        "edit": "ask",
                        "webfetch": "ask",
                    },
                    "prompt": "prompt",
                    "temperature": 0,
                    "tools": {"foo": True},
                    "top_p": 0,
                },
                "general": {
                    "description": "description",
                    "disable": True,
                    "mode": "subagent",
                    "model": "model",
                    "permission": {
                        "bash": "ask",
                        "edit": "ask",
                        "webfetch": "ask",
                    },
                    "prompt": "prompt",
                    "temperature": 0,
                    "tools": {"foo": True},
                    "top_p": 0,
                },
                "plan": {
                    "description": "description",
                    "disable": True,
                    "mode": "subagent",
                    "model": "model",
                    "permission": {
                        "bash": "ask",
                        "edit": "ask",
                        "webfetch": "ask",
                    },
                    "prompt": "prompt",
                    "temperature": 0,
                    "tools": {"foo": True},
                    "top_p": 0,
                },
            },
            autoshare=True,
            autoupdate=True,
            command={
                "foo": {
                    "template": "template",
                    "agent": "agent",
                    "description": "description",
                    "model": "model",
                    "subtask": True,
                }
            },
            disabled_providers=["string"],
            experimental={
                "disable_paste_summary": True,
                "hook": {
                    "file_edited": {
                        "foo": [
                            {
                                "command": ["string"],
                                "environment": {"foo": "string"},
                            }
                        ]
                    },
                    "session_completed": [
                        {
                            "command": ["string"],
                            "environment": {"foo": "string"},
                        }
                    ],
                },
            },
            formatter={
                "foo": {
                    "command": ["string"],
                    "disabled": True,
                    "environment": {"foo": "string"},
                    "extensions": ["string"],
                }
            },
            instructions=["string"],
            keybinds={
                "agent_cycle": "agent_cycle",
                "agent_cycle_reverse": "agent_cycle_reverse",
                "agent_list": "agent_list",
                "app_exit": "app_exit",
                "app_help": "app_help",
                "editor_open": "editor_open",
                "file_close": "file_close",
                "file_diff_toggle": "file_diff_toggle",
                "file_list": "file_list",
                "file_search": "file_search",
                "input_clear": "input_clear",
                "input_newline": "input_newline",
                "input_paste": "input_paste",
                "input_submit": "input_submit",
                "leader": "leader",
                "messages_copy": "messages_copy",
                "messages_first": "messages_first",
                "messages_half_page_down": "messages_half_page_down",
                "messages_half_page_up": "messages_half_page_up",
                "messages_last": "messages_last",
                "messages_layout_toggle": "messages_layout_toggle",
                "messages_next": "messages_next",
                "messages_page_down": "messages_page_down",
                "messages_page_up": "messages_page_up",
                "messages_previous": "messages_previous",
                "messages_redo": "messages_redo",
                "messages_revert": "messages_revert",
                "messages_undo": "messages_undo",
                "model_cycle_recent": "model_cycle_recent",
                "model_cycle_recent_reverse": "model_cycle_recent_reverse",
                "model_list": "model_list",
                "project_init": "project_init",
                "session_child_cycle": "session_child_cycle",
                "session_child_cycle_reverse": "session_child_cycle_reverse",
                "session_compact": "session_compact",
                "session_export": "session_export",
                "session_interrupt": "session_interrupt",
                "session_list": "session_list",
                "session_new": "session_new",
                "session_share": "session_share",
                "session_timeline": "session_timeline",
                "session_unshare": "session_unshare",
                "switch_agent": "switch_agent",
                "switch_agent_reverse": "switch_agent_reverse",
                "switch_mode": "switch_mode",
                "switch_mode_reverse": "switch_mode_reverse",
                "theme_list": "theme_list",
                "thinking_blocks": "thinking_blocks",
                "tool_details": "tool_details",
            },
            layout="auto",
            lsp={"foo": {"disabled": True}},
            mcp={
                "foo": {
                    "command": ["string"],
                    "type": "local",
                    "enabled": True,
                    "environment": {"foo": "string"},
                }
            },
            mode={
                "build": {
                    "description": "description",
                    "disable": True,
                    "mode": "subagent",
                    "model": "model",
                    "permission": {
                        "bash": "ask",
                        "edit": "ask",
                        "webfetch": "ask",
                    },
                    "prompt": "prompt",
                    "temperature": 0,
                    "tools": {"foo": True},
                    "top_p": 0,
                },
                "plan": {
                    "description": "description",
                    "disable": True,
                    "mode": "subagent",
                    "model": "model",
                    "permission": {
                        "bash": "ask",
                        "edit": "ask",
                        "webfetch": "ask",
                    },
                    "prompt": "prompt",
                    "temperature": 0,
                    "tools": {"foo": True},
                    "top_p": 0,
                },
            },
            model="model",
            permission={
                "bash": "ask",
                "edit": "ask",
                "webfetch": "ask",
            },
            plugin=["string"],
            provider={
                "foo": {
                    "id": "id",
                    "api": "api",
                    "env": ["string"],
                    "models": {
                        "foo": {
                            "id": "id",
                            "attachment": True,
                            "cost": {
                                "input": 0,
                                "output": 0,
                                "cache_read": 0,
                                "cache_write": 0,
                            },
                            "experimental": True,
                            "limit": {
                                "context": 0,
                                "output": 0,
                            },
                            "modalities": {
                                "input": ["text"],
                                "output": ["text"],
                            },
                            "name": "name",
                            "options": {"foo": "bar"},
                            "provider": {"npm": "npm"},
                            "reasoning": True,
                            "release_date": "release_date",
                            "temperature": True,
                            "tool_call": True,
                        }
                    },
                    "name": "name",
                    "npm": "npm",
                    "options": {
                        "api_key": "apiKey",
                        "base_url": "baseURL",
                        "timeout": 1,
                    },
                }
            },
            share="manual",
            small_model="small_model",
            snapshot=True,
            theme="theme",
            tools={"foo": True},
            tui={"scroll_speed": 1},
            username="username",
            watcher={"ignore": ["string"]},
        )
        assert_matches_type(Config, config, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: OpencodeSDK) -> None:
        response = client.config.with_raw_response.update()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = response.parse()
        assert_matches_type(Config, config, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: OpencodeSDK) -> None:
        with client.config.with_streaming_response.update() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = response.parse()
            assert_matches_type(Config, config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_providers(self, client: OpencodeSDK) -> None:
        config = client.config.list_providers()
        assert_matches_type(ConfigListProvidersResponse, config, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_providers_with_all_params(self, client: OpencodeSDK) -> None:
        config = client.config.list_providers(
            directory="directory",
        )
        assert_matches_type(ConfigListProvidersResponse, config, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_providers(self, client: OpencodeSDK) -> None:
        response = client.config.with_raw_response.list_providers()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = response.parse()
        assert_matches_type(ConfigListProvidersResponse, config, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_providers(self, client: OpencodeSDK) -> None:
        with client.config.with_streaming_response.list_providers() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = response.parse()
            assert_matches_type(ConfigListProvidersResponse, config, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncConfig:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncOpencodeSDK) -> None:
        config = await async_client.config.retrieve()
        assert_matches_type(Config, config, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncOpencodeSDK) -> None:
        config = await async_client.config.retrieve(
            directory="directory",
        )
        assert_matches_type(Config, config, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.config.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = await response.parse()
        assert_matches_type(Config, config, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.config.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = await response.parse()
            assert_matches_type(Config, config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncOpencodeSDK) -> None:
        config = await async_client.config.update()
        assert_matches_type(Config, config, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncOpencodeSDK) -> None:
        config = await async_client.config.update(
            directory="directory",
            schema="$schema",
            agent={
                "build": {
                    "description": "description",
                    "disable": True,
                    "mode": "subagent",
                    "model": "model",
                    "permission": {
                        "bash": "ask",
                        "edit": "ask",
                        "webfetch": "ask",
                    },
                    "prompt": "prompt",
                    "temperature": 0,
                    "tools": {"foo": True},
                    "top_p": 0,
                },
                "general": {
                    "description": "description",
                    "disable": True,
                    "mode": "subagent",
                    "model": "model",
                    "permission": {
                        "bash": "ask",
                        "edit": "ask",
                        "webfetch": "ask",
                    },
                    "prompt": "prompt",
                    "temperature": 0,
                    "tools": {"foo": True},
                    "top_p": 0,
                },
                "plan": {
                    "description": "description",
                    "disable": True,
                    "mode": "subagent",
                    "model": "model",
                    "permission": {
                        "bash": "ask",
                        "edit": "ask",
                        "webfetch": "ask",
                    },
                    "prompt": "prompt",
                    "temperature": 0,
                    "tools": {"foo": True},
                    "top_p": 0,
                },
            },
            autoshare=True,
            autoupdate=True,
            command={
                "foo": {
                    "template": "template",
                    "agent": "agent",
                    "description": "description",
                    "model": "model",
                    "subtask": True,
                }
            },
            disabled_providers=["string"],
            experimental={
                "disable_paste_summary": True,
                "hook": {
                    "file_edited": {
                        "foo": [
                            {
                                "command": ["string"],
                                "environment": {"foo": "string"},
                            }
                        ]
                    },
                    "session_completed": [
                        {
                            "command": ["string"],
                            "environment": {"foo": "string"},
                        }
                    ],
                },
            },
            formatter={
                "foo": {
                    "command": ["string"],
                    "disabled": True,
                    "environment": {"foo": "string"},
                    "extensions": ["string"],
                }
            },
            instructions=["string"],
            keybinds={
                "agent_cycle": "agent_cycle",
                "agent_cycle_reverse": "agent_cycle_reverse",
                "agent_list": "agent_list",
                "app_exit": "app_exit",
                "app_help": "app_help",
                "editor_open": "editor_open",
                "file_close": "file_close",
                "file_diff_toggle": "file_diff_toggle",
                "file_list": "file_list",
                "file_search": "file_search",
                "input_clear": "input_clear",
                "input_newline": "input_newline",
                "input_paste": "input_paste",
                "input_submit": "input_submit",
                "leader": "leader",
                "messages_copy": "messages_copy",
                "messages_first": "messages_first",
                "messages_half_page_down": "messages_half_page_down",
                "messages_half_page_up": "messages_half_page_up",
                "messages_last": "messages_last",
                "messages_layout_toggle": "messages_layout_toggle",
                "messages_next": "messages_next",
                "messages_page_down": "messages_page_down",
                "messages_page_up": "messages_page_up",
                "messages_previous": "messages_previous",
                "messages_redo": "messages_redo",
                "messages_revert": "messages_revert",
                "messages_undo": "messages_undo",
                "model_cycle_recent": "model_cycle_recent",
                "model_cycle_recent_reverse": "model_cycle_recent_reverse",
                "model_list": "model_list",
                "project_init": "project_init",
                "session_child_cycle": "session_child_cycle",
                "session_child_cycle_reverse": "session_child_cycle_reverse",
                "session_compact": "session_compact",
                "session_export": "session_export",
                "session_interrupt": "session_interrupt",
                "session_list": "session_list",
                "session_new": "session_new",
                "session_share": "session_share",
                "session_timeline": "session_timeline",
                "session_unshare": "session_unshare",
                "switch_agent": "switch_agent",
                "switch_agent_reverse": "switch_agent_reverse",
                "switch_mode": "switch_mode",
                "switch_mode_reverse": "switch_mode_reverse",
                "theme_list": "theme_list",
                "thinking_blocks": "thinking_blocks",
                "tool_details": "tool_details",
            },
            layout="auto",
            lsp={"foo": {"disabled": True}},
            mcp={
                "foo": {
                    "command": ["string"],
                    "type": "local",
                    "enabled": True,
                    "environment": {"foo": "string"},
                }
            },
            mode={
                "build": {
                    "description": "description",
                    "disable": True,
                    "mode": "subagent",
                    "model": "model",
                    "permission": {
                        "bash": "ask",
                        "edit": "ask",
                        "webfetch": "ask",
                    },
                    "prompt": "prompt",
                    "temperature": 0,
                    "tools": {"foo": True},
                    "top_p": 0,
                },
                "plan": {
                    "description": "description",
                    "disable": True,
                    "mode": "subagent",
                    "model": "model",
                    "permission": {
                        "bash": "ask",
                        "edit": "ask",
                        "webfetch": "ask",
                    },
                    "prompt": "prompt",
                    "temperature": 0,
                    "tools": {"foo": True},
                    "top_p": 0,
                },
            },
            model="model",
            permission={
                "bash": "ask",
                "edit": "ask",
                "webfetch": "ask",
            },
            plugin=["string"],
            provider={
                "foo": {
                    "id": "id",
                    "api": "api",
                    "env": ["string"],
                    "models": {
                        "foo": {
                            "id": "id",
                            "attachment": True,
                            "cost": {
                                "input": 0,
                                "output": 0,
                                "cache_read": 0,
                                "cache_write": 0,
                            },
                            "experimental": True,
                            "limit": {
                                "context": 0,
                                "output": 0,
                            },
                            "modalities": {
                                "input": ["text"],
                                "output": ["text"],
                            },
                            "name": "name",
                            "options": {"foo": "bar"},
                            "provider": {"npm": "npm"},
                            "reasoning": True,
                            "release_date": "release_date",
                            "temperature": True,
                            "tool_call": True,
                        }
                    },
                    "name": "name",
                    "npm": "npm",
                    "options": {
                        "api_key": "apiKey",
                        "base_url": "baseURL",
                        "timeout": 1,
                    },
                }
            },
            share="manual",
            small_model="small_model",
            snapshot=True,
            theme="theme",
            tools={"foo": True},
            tui={"scroll_speed": 1},
            username="username",
            watcher={"ignore": ["string"]},
        )
        assert_matches_type(Config, config, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.config.with_raw_response.update()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = await response.parse()
        assert_matches_type(Config, config, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.config.with_streaming_response.update() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = await response.parse()
            assert_matches_type(Config, config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_providers(self, async_client: AsyncOpencodeSDK) -> None:
        config = await async_client.config.list_providers()
        assert_matches_type(ConfigListProvidersResponse, config, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_providers_with_all_params(self, async_client: AsyncOpencodeSDK) -> None:
        config = await async_client.config.list_providers(
            directory="directory",
        )
        assert_matches_type(ConfigListProvidersResponse, config, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_providers(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.config.with_raw_response.list_providers()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = await response.parse()
        assert_matches_type(ConfigListProvidersResponse, config, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_providers(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.config.with_streaming_response.list_providers() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = await response.parse()
            assert_matches_type(ConfigListProvidersResponse, config, path=["response"])

        assert cast(Any, response.is_closed) is True
