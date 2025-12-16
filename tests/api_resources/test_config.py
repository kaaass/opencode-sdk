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
                    "color": "#E1CB97",
                    "description": "description",
                    "disable": True,
                    "max_steps": 1,
                    "mode": "subagent",
                    "model": "model",
                    "permission": {
                        "bash": "ask",
                        "doom_loop": "ask",
                        "edit": "ask",
                        "external_directory": "ask",
                        "webfetch": "ask",
                    },
                    "prompt": "prompt",
                    "temperature": 0,
                    "tools": {"foo": True},
                    "top_p": 0,
                },
                "compaction": {
                    "color": "#E1CB97",
                    "description": "description",
                    "disable": True,
                    "max_steps": 1,
                    "mode": "subagent",
                    "model": "model",
                    "permission": {
                        "bash": "ask",
                        "doom_loop": "ask",
                        "edit": "ask",
                        "external_directory": "ask",
                        "webfetch": "ask",
                    },
                    "prompt": "prompt",
                    "temperature": 0,
                    "tools": {"foo": True},
                    "top_p": 0,
                },
                "explore": {
                    "color": "#E1CB97",
                    "description": "description",
                    "disable": True,
                    "max_steps": 1,
                    "mode": "subagent",
                    "model": "model",
                    "permission": {
                        "bash": "ask",
                        "doom_loop": "ask",
                        "edit": "ask",
                        "external_directory": "ask",
                        "webfetch": "ask",
                    },
                    "prompt": "prompt",
                    "temperature": 0,
                    "tools": {"foo": True},
                    "top_p": 0,
                },
                "general": {
                    "color": "#E1CB97",
                    "description": "description",
                    "disable": True,
                    "max_steps": 1,
                    "mode": "subagent",
                    "model": "model",
                    "permission": {
                        "bash": "ask",
                        "doom_loop": "ask",
                        "edit": "ask",
                        "external_directory": "ask",
                        "webfetch": "ask",
                    },
                    "prompt": "prompt",
                    "temperature": 0,
                    "tools": {"foo": True},
                    "top_p": 0,
                },
                "plan": {
                    "color": "#E1CB97",
                    "description": "description",
                    "disable": True,
                    "max_steps": 1,
                    "mode": "subagent",
                    "model": "model",
                    "permission": {
                        "bash": "ask",
                        "doom_loop": "ask",
                        "edit": "ask",
                        "external_directory": "ask",
                        "webfetch": "ask",
                    },
                    "prompt": "prompt",
                    "temperature": 0,
                    "tools": {"foo": True},
                    "top_p": 0,
                },
                "summary": {
                    "color": "#E1CB97",
                    "description": "description",
                    "disable": True,
                    "max_steps": 1,
                    "mode": "subagent",
                    "model": "model",
                    "permission": {
                        "bash": "ask",
                        "doom_loop": "ask",
                        "edit": "ask",
                        "external_directory": "ask",
                        "webfetch": "ask",
                    },
                    "prompt": "prompt",
                    "temperature": 0,
                    "tools": {"foo": True},
                    "top_p": 0,
                },
                "title": {
                    "color": "#E1CB97",
                    "description": "description",
                    "disable": True,
                    "max_steps": 1,
                    "mode": "subagent",
                    "model": "model",
                    "permission": {
                        "bash": "ask",
                        "doom_loop": "ask",
                        "edit": "ask",
                        "external_directory": "ask",
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
            enabled_providers=["string"],
            enterprise={"url": "url"},
            experimental={
                "batch_tool": True,
                "chat_max_retries": 0,
                "continue_loop_on_deny": True,
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
                "open_telemetry": True,
                "primary_tools": ["string"],
            },
            formatter=True,
            instructions=["string"],
            keybinds={
                "agent_cycle": "agent_cycle",
                "agent_cycle_reverse": "agent_cycle_reverse",
                "agent_list": "agent_list",
                "app_exit": "app_exit",
                "command_list": "command_list",
                "editor_open": "editor_open",
                "history_next": "history_next",
                "history_previous": "history_previous",
                "input_backspace": "input_backspace",
                "input_buffer_end": "input_buffer_end",
                "input_buffer_home": "input_buffer_home",
                "input_clear": "input_clear",
                "input_delete": "input_delete",
                "input_delete_line": "input_delete_line",
                "input_delete_to_line_end": "input_delete_to_line_end",
                "input_delete_to_line_start": "input_delete_to_line_start",
                "input_delete_word_backward": "input_delete_word_backward",
                "input_delete_word_forward": "input_delete_word_forward",
                "input_line_end": "input_line_end",
                "input_line_home": "input_line_home",
                "input_move_down": "input_move_down",
                "input_move_left": "input_move_left",
                "input_move_right": "input_move_right",
                "input_move_up": "input_move_up",
                "input_newline": "input_newline",
                "input_paste": "input_paste",
                "input_redo": "input_redo",
                "input_select_buffer_end": "input_select_buffer_end",
                "input_select_buffer_home": "input_select_buffer_home",
                "input_select_down": "input_select_down",
                "input_select_left": "input_select_left",
                "input_select_line_end": "input_select_line_end",
                "input_select_line_home": "input_select_line_home",
                "input_select_right": "input_select_right",
                "input_select_up": "input_select_up",
                "input_select_visual_line_end": "input_select_visual_line_end",
                "input_select_visual_line_home": "input_select_visual_line_home",
                "input_select_word_backward": "input_select_word_backward",
                "input_select_word_forward": "input_select_word_forward",
                "input_submit": "input_submit",
                "input_undo": "input_undo",
                "input_visual_line_end": "input_visual_line_end",
                "input_visual_line_home": "input_visual_line_home",
                "input_word_backward": "input_word_backward",
                "input_word_forward": "input_word_forward",
                "leader": "leader",
                "messages_copy": "messages_copy",
                "messages_first": "messages_first",
                "messages_half_page_down": "messages_half_page_down",
                "messages_half_page_up": "messages_half_page_up",
                "messages_last": "messages_last",
                "messages_last_user": "messages_last_user",
                "messages_page_down": "messages_page_down",
                "messages_page_up": "messages_page_up",
                "messages_redo": "messages_redo",
                "messages_toggle_conceal": "messages_toggle_conceal",
                "messages_undo": "messages_undo",
                "model_cycle_favorite": "model_cycle_favorite",
                "model_cycle_favorite_reverse": "model_cycle_favorite_reverse",
                "model_cycle_recent": "model_cycle_recent",
                "model_cycle_recent_reverse": "model_cycle_recent_reverse",
                "model_list": "model_list",
                "scrollbar_toggle": "scrollbar_toggle",
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
                "sidebar_toggle": "sidebar_toggle",
                "status_view": "status_view",
                "terminal_suspend": "terminal_suspend",
                "theme_list": "theme_list",
                "tool_details": "tool_details",
                "username_toggle": "username_toggle",
            },
            layout="auto",
            lsp=True,
            mcp={
                "foo": {
                    "command": ["string"],
                    "type": "local",
                    "enabled": True,
                    "environment": {"foo": "string"},
                    "timeout": 1,
                }
            },
            mode={
                "build": {
                    "color": "#E1CB97",
                    "description": "description",
                    "disable": True,
                    "max_steps": 1,
                    "mode": "subagent",
                    "model": "model",
                    "permission": {
                        "bash": "ask",
                        "doom_loop": "ask",
                        "edit": "ask",
                        "external_directory": "ask",
                        "webfetch": "ask",
                    },
                    "prompt": "prompt",
                    "temperature": 0,
                    "tools": {"foo": True},
                    "top_p": 0,
                },
                "plan": {
                    "color": "#E1CB97",
                    "description": "description",
                    "disable": True,
                    "max_steps": 1,
                    "mode": "subagent",
                    "model": "model",
                    "permission": {
                        "bash": "ask",
                        "doom_loop": "ask",
                        "edit": "ask",
                        "external_directory": "ask",
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
                "doom_loop": "ask",
                "edit": "ask",
                "external_directory": "ask",
                "webfetch": "ask",
            },
            plugin=["string"],
            provider={
                "foo": {
                    "id": "id",
                    "api": "api",
                    "blacklist": ["string"],
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
                                "context_over_200k": {
                                    "input": 0,
                                    "output": 0,
                                    "cache_read": 0,
                                    "cache_write": 0,
                                },
                            },
                            "experimental": True,
                            "family": "family",
                            "headers": {"foo": "string"},
                            "interleaved": True,
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
                            "status": "alpha",
                            "temperature": True,
                            "tool_call": True,
                        }
                    },
                    "name": "name",
                    "npm": "npm",
                    "options": {
                        "api_key": "apiKey",
                        "base_url": "baseURL",
                        "enterprise_url": "enterpriseUrl",
                        "set_cache_key": True,
                        "timeout": 1,
                    },
                    "whitelist": ["string"],
                }
            },
            share="manual",
            small_model="small_model",
            snapshot=True,
            theme="theme",
            tools={"foo": True},
            tui={
                "diff_style": "auto",
                "scroll_acceleration": {"enabled": True},
                "scroll_speed": 0.001,
            },
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
                    "color": "#E1CB97",
                    "description": "description",
                    "disable": True,
                    "max_steps": 1,
                    "mode": "subagent",
                    "model": "model",
                    "permission": {
                        "bash": "ask",
                        "doom_loop": "ask",
                        "edit": "ask",
                        "external_directory": "ask",
                        "webfetch": "ask",
                    },
                    "prompt": "prompt",
                    "temperature": 0,
                    "tools": {"foo": True},
                    "top_p": 0,
                },
                "compaction": {
                    "color": "#E1CB97",
                    "description": "description",
                    "disable": True,
                    "max_steps": 1,
                    "mode": "subagent",
                    "model": "model",
                    "permission": {
                        "bash": "ask",
                        "doom_loop": "ask",
                        "edit": "ask",
                        "external_directory": "ask",
                        "webfetch": "ask",
                    },
                    "prompt": "prompt",
                    "temperature": 0,
                    "tools": {"foo": True},
                    "top_p": 0,
                },
                "explore": {
                    "color": "#E1CB97",
                    "description": "description",
                    "disable": True,
                    "max_steps": 1,
                    "mode": "subagent",
                    "model": "model",
                    "permission": {
                        "bash": "ask",
                        "doom_loop": "ask",
                        "edit": "ask",
                        "external_directory": "ask",
                        "webfetch": "ask",
                    },
                    "prompt": "prompt",
                    "temperature": 0,
                    "tools": {"foo": True},
                    "top_p": 0,
                },
                "general": {
                    "color": "#E1CB97",
                    "description": "description",
                    "disable": True,
                    "max_steps": 1,
                    "mode": "subagent",
                    "model": "model",
                    "permission": {
                        "bash": "ask",
                        "doom_loop": "ask",
                        "edit": "ask",
                        "external_directory": "ask",
                        "webfetch": "ask",
                    },
                    "prompt": "prompt",
                    "temperature": 0,
                    "tools": {"foo": True},
                    "top_p": 0,
                },
                "plan": {
                    "color": "#E1CB97",
                    "description": "description",
                    "disable": True,
                    "max_steps": 1,
                    "mode": "subagent",
                    "model": "model",
                    "permission": {
                        "bash": "ask",
                        "doom_loop": "ask",
                        "edit": "ask",
                        "external_directory": "ask",
                        "webfetch": "ask",
                    },
                    "prompt": "prompt",
                    "temperature": 0,
                    "tools": {"foo": True},
                    "top_p": 0,
                },
                "summary": {
                    "color": "#E1CB97",
                    "description": "description",
                    "disable": True,
                    "max_steps": 1,
                    "mode": "subagent",
                    "model": "model",
                    "permission": {
                        "bash": "ask",
                        "doom_loop": "ask",
                        "edit": "ask",
                        "external_directory": "ask",
                        "webfetch": "ask",
                    },
                    "prompt": "prompt",
                    "temperature": 0,
                    "tools": {"foo": True},
                    "top_p": 0,
                },
                "title": {
                    "color": "#E1CB97",
                    "description": "description",
                    "disable": True,
                    "max_steps": 1,
                    "mode": "subagent",
                    "model": "model",
                    "permission": {
                        "bash": "ask",
                        "doom_loop": "ask",
                        "edit": "ask",
                        "external_directory": "ask",
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
            enabled_providers=["string"],
            enterprise={"url": "url"},
            experimental={
                "batch_tool": True,
                "chat_max_retries": 0,
                "continue_loop_on_deny": True,
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
                "open_telemetry": True,
                "primary_tools": ["string"],
            },
            formatter=True,
            instructions=["string"],
            keybinds={
                "agent_cycle": "agent_cycle",
                "agent_cycle_reverse": "agent_cycle_reverse",
                "agent_list": "agent_list",
                "app_exit": "app_exit",
                "command_list": "command_list",
                "editor_open": "editor_open",
                "history_next": "history_next",
                "history_previous": "history_previous",
                "input_backspace": "input_backspace",
                "input_buffer_end": "input_buffer_end",
                "input_buffer_home": "input_buffer_home",
                "input_clear": "input_clear",
                "input_delete": "input_delete",
                "input_delete_line": "input_delete_line",
                "input_delete_to_line_end": "input_delete_to_line_end",
                "input_delete_to_line_start": "input_delete_to_line_start",
                "input_delete_word_backward": "input_delete_word_backward",
                "input_delete_word_forward": "input_delete_word_forward",
                "input_line_end": "input_line_end",
                "input_line_home": "input_line_home",
                "input_move_down": "input_move_down",
                "input_move_left": "input_move_left",
                "input_move_right": "input_move_right",
                "input_move_up": "input_move_up",
                "input_newline": "input_newline",
                "input_paste": "input_paste",
                "input_redo": "input_redo",
                "input_select_buffer_end": "input_select_buffer_end",
                "input_select_buffer_home": "input_select_buffer_home",
                "input_select_down": "input_select_down",
                "input_select_left": "input_select_left",
                "input_select_line_end": "input_select_line_end",
                "input_select_line_home": "input_select_line_home",
                "input_select_right": "input_select_right",
                "input_select_up": "input_select_up",
                "input_select_visual_line_end": "input_select_visual_line_end",
                "input_select_visual_line_home": "input_select_visual_line_home",
                "input_select_word_backward": "input_select_word_backward",
                "input_select_word_forward": "input_select_word_forward",
                "input_submit": "input_submit",
                "input_undo": "input_undo",
                "input_visual_line_end": "input_visual_line_end",
                "input_visual_line_home": "input_visual_line_home",
                "input_word_backward": "input_word_backward",
                "input_word_forward": "input_word_forward",
                "leader": "leader",
                "messages_copy": "messages_copy",
                "messages_first": "messages_first",
                "messages_half_page_down": "messages_half_page_down",
                "messages_half_page_up": "messages_half_page_up",
                "messages_last": "messages_last",
                "messages_last_user": "messages_last_user",
                "messages_page_down": "messages_page_down",
                "messages_page_up": "messages_page_up",
                "messages_redo": "messages_redo",
                "messages_toggle_conceal": "messages_toggle_conceal",
                "messages_undo": "messages_undo",
                "model_cycle_favorite": "model_cycle_favorite",
                "model_cycle_favorite_reverse": "model_cycle_favorite_reverse",
                "model_cycle_recent": "model_cycle_recent",
                "model_cycle_recent_reverse": "model_cycle_recent_reverse",
                "model_list": "model_list",
                "scrollbar_toggle": "scrollbar_toggle",
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
                "sidebar_toggle": "sidebar_toggle",
                "status_view": "status_view",
                "terminal_suspend": "terminal_suspend",
                "theme_list": "theme_list",
                "tool_details": "tool_details",
                "username_toggle": "username_toggle",
            },
            layout="auto",
            lsp=True,
            mcp={
                "foo": {
                    "command": ["string"],
                    "type": "local",
                    "enabled": True,
                    "environment": {"foo": "string"},
                    "timeout": 1,
                }
            },
            mode={
                "build": {
                    "color": "#E1CB97",
                    "description": "description",
                    "disable": True,
                    "max_steps": 1,
                    "mode": "subagent",
                    "model": "model",
                    "permission": {
                        "bash": "ask",
                        "doom_loop": "ask",
                        "edit": "ask",
                        "external_directory": "ask",
                        "webfetch": "ask",
                    },
                    "prompt": "prompt",
                    "temperature": 0,
                    "tools": {"foo": True},
                    "top_p": 0,
                },
                "plan": {
                    "color": "#E1CB97",
                    "description": "description",
                    "disable": True,
                    "max_steps": 1,
                    "mode": "subagent",
                    "model": "model",
                    "permission": {
                        "bash": "ask",
                        "doom_loop": "ask",
                        "edit": "ask",
                        "external_directory": "ask",
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
                "doom_loop": "ask",
                "edit": "ask",
                "external_directory": "ask",
                "webfetch": "ask",
            },
            plugin=["string"],
            provider={
                "foo": {
                    "id": "id",
                    "api": "api",
                    "blacklist": ["string"],
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
                                "context_over_200k": {
                                    "input": 0,
                                    "output": 0,
                                    "cache_read": 0,
                                    "cache_write": 0,
                                },
                            },
                            "experimental": True,
                            "family": "family",
                            "headers": {"foo": "string"},
                            "interleaved": True,
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
                            "status": "alpha",
                            "temperature": True,
                            "tool_call": True,
                        }
                    },
                    "name": "name",
                    "npm": "npm",
                    "options": {
                        "api_key": "apiKey",
                        "base_url": "baseURL",
                        "enterprise_url": "enterpriseUrl",
                        "set_cache_key": True,
                        "timeout": 1,
                    },
                    "whitelist": ["string"],
                }
            },
            share="manual",
            small_model="small_model",
            snapshot=True,
            theme="theme",
            tools={"foo": True},
            tui={
                "diff_style": "auto",
                "scroll_acceleration": {"enabled": True},
                "scroll_speed": 0.001,
            },
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
