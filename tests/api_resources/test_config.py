# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from ai4pa_opencode_sdk import OpencodeSDK, AsyncOpencodeSDK
from ai4pa_opencode_sdk.types import (
    ConfigListProvidersResponse,
)
from ai4pa_opencode_sdk.types.global_ import Config

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestConfig:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: OpencodeSDK) -> None:
        config = client.config.retrieve()
        assert_matches_type(Config, config, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: OpencodeSDK) -> None:
        config = client.config.retrieve(
            directory="directory",
            workspace="workspace",
        )
        assert_matches_type(Config, config, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: OpencodeSDK) -> None:
        response = client.config.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = response.parse()
        assert_matches_type(Config, config, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: OpencodeSDK) -> None:
        with client.config.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = response.parse()
            assert_matches_type(Config, config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: OpencodeSDK) -> None:
        config = client.config.update()
        assert_matches_type(Config, config, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: OpencodeSDK) -> None:
        config = client.config.update(
            directory="directory",
            workspace="workspace",
            schema="$schema",
            agent={
                "build": {
                    "color": "primary",
                    "description": "description",
                    "disable": True,
                    "hidden": True,
                    "max_steps": 1,
                    "mode": "subagent",
                    "model": "model",
                    "options": {"foo": "bar"},
                    "permission": "ask",
                    "prompt": "prompt",
                    "skills": ["string"],
                    "steps": 1,
                    "sub_agents": ["string"],
                    "temperature": 0,
                    "tools": {"foo": True},
                    "top_p": 0,
                    "variant": "variant",
                },
                "compaction": {
                    "color": "primary",
                    "description": "description",
                    "disable": True,
                    "hidden": True,
                    "max_steps": 1,
                    "mode": "subagent",
                    "model": "model",
                    "options": {"foo": "bar"},
                    "permission": "ask",
                    "prompt": "prompt",
                    "skills": ["string"],
                    "steps": 1,
                    "sub_agents": ["string"],
                    "temperature": 0,
                    "tools": {"foo": True},
                    "top_p": 0,
                    "variant": "variant",
                },
                "explore": {
                    "color": "primary",
                    "description": "description",
                    "disable": True,
                    "hidden": True,
                    "max_steps": 1,
                    "mode": "subagent",
                    "model": "model",
                    "options": {"foo": "bar"},
                    "permission": "ask",
                    "prompt": "prompt",
                    "skills": ["string"],
                    "steps": 1,
                    "sub_agents": ["string"],
                    "temperature": 0,
                    "tools": {"foo": True},
                    "top_p": 0,
                    "variant": "variant",
                },
                "general": {
                    "color": "primary",
                    "description": "description",
                    "disable": True,
                    "hidden": True,
                    "max_steps": 1,
                    "mode": "subagent",
                    "model": "model",
                    "options": {"foo": "bar"},
                    "permission": "ask",
                    "prompt": "prompt",
                    "skills": ["string"],
                    "steps": 1,
                    "sub_agents": ["string"],
                    "temperature": 0,
                    "tools": {"foo": True},
                    "top_p": 0,
                    "variant": "variant",
                },
                "plan": {
                    "color": "primary",
                    "description": "description",
                    "disable": True,
                    "hidden": True,
                    "max_steps": 1,
                    "mode": "subagent",
                    "model": "model",
                    "options": {"foo": "bar"},
                    "permission": "ask",
                    "prompt": "prompt",
                    "skills": ["string"],
                    "steps": 1,
                    "sub_agents": ["string"],
                    "temperature": 0,
                    "tools": {"foo": True},
                    "top_p": 0,
                    "variant": "variant",
                },
                "summary": {
                    "color": "primary",
                    "description": "description",
                    "disable": True,
                    "hidden": True,
                    "max_steps": 1,
                    "mode": "subagent",
                    "model": "model",
                    "options": {"foo": "bar"},
                    "permission": "ask",
                    "prompt": "prompt",
                    "skills": ["string"],
                    "steps": 1,
                    "sub_agents": ["string"],
                    "temperature": 0,
                    "tools": {"foo": True},
                    "top_p": 0,
                    "variant": "variant",
                },
                "title": {
                    "color": "primary",
                    "description": "description",
                    "disable": True,
                    "hidden": True,
                    "max_steps": 1,
                    "mode": "subagent",
                    "model": "model",
                    "options": {"foo": "bar"},
                    "permission": "ask",
                    "prompt": "prompt",
                    "skills": ["string"],
                    "steps": 1,
                    "sub_agents": ["string"],
                    "temperature": 0,
                    "tools": {"foo": True},
                    "top_p": 0,
                    "variant": "variant",
                },
            },
            artifact_allowed_paths=["string"],
            autoshare=True,
            autoupdate="notify",
            command={
                "foo": {
                    "template": "template",
                    "agent": "agent",
                    "description": "description",
                    "model": "model",
                    "subtask": True,
                }
            },
            compaction={
                "auto": True,
                "preserve_recent_tokens": 0,
                "prune": True,
                "reserved": 0,
                "tail_turns": 0,
            },
            custom_provider_npm_whitelist=["string"],
            default_agent="default_agent",
            disabled_providers=["string"],
            enabled_providers=["string"],
            enterprise={"url": "url"},
            experimental={
                "batch_tool": True,
                "continue_loop_on_deny": True,
                "disable_paste_summary": True,
                "mcp_timeout": 1,
                "open_telemetry": True,
                "primary_tools": ["string"],
            },
            formatter=True,
            instructions=["string"],
            layout="auto",
            log_level="DEBUG",
            lsp=True,
            mcp={
                "foo": {
                    "command": ["string"],
                    "type": "local",
                    "enabled": True,
                    "environment": {"foo": "string"},
                    "timeout": 0,
                }
            },
            mode={
                "build": {
                    "color": "primary",
                    "description": "description",
                    "disable": True,
                    "hidden": True,
                    "max_steps": 1,
                    "mode": "subagent",
                    "model": "model",
                    "options": {"foo": "bar"},
                    "permission": "ask",
                    "prompt": "prompt",
                    "skills": ["string"],
                    "steps": 1,
                    "sub_agents": ["string"],
                    "temperature": 0,
                    "tools": {"foo": True},
                    "top_p": 0,
                    "variant": "variant",
                },
                "plan": {
                    "color": "primary",
                    "description": "description",
                    "disable": True,
                    "hidden": True,
                    "max_steps": 1,
                    "mode": "subagent",
                    "model": "model",
                    "options": {"foo": "bar"},
                    "permission": "ask",
                    "prompt": "prompt",
                    "skills": ["string"],
                    "steps": 1,
                    "sub_agents": ["string"],
                    "temperature": 0,
                    "tools": {"foo": True},
                    "top_p": 0,
                    "variant": "variant",
                },
            },
            model="model",
            permission="ask",
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
                                "input": 0,
                            },
                            "modalities": {
                                "input": ["text"],
                                "output": ["text"],
                            },
                            "name": "name",
                            "options": {"foo": "bar"},
                            "provider": {
                                "api": "api",
                                "npm": "npm",
                            },
                            "reasoning": True,
                            "release_date": "release_date",
                            "status": "alpha",
                            "temperature": True,
                            "tool_call": True,
                            "variants": {"foo": {"disabled": True}},
                        }
                    },
                    "name": "name",
                    "npm": "npm",
                    "options": {
                        "api_key": "apiKey",
                        "base_url": "baseURL",
                        "chunk_timeout": 1,
                        "enterprise_url": "enterpriseUrl",
                        "set_cache_key": True,
                        "timeout": False,
                    },
                    "whitelist": ["string"],
                }
            },
            server={
                "cors": ["string"],
                "hostname": "hostname",
                "mdns": True,
                "mdns_domain": "mdnsDomain",
                "port": 1,
            },
            share="manual",
            shell="shell",
            skills={
                "paths": ["string"],
                "urls": ["string"],
            },
            small_model="small_model",
            snapshot=True,
            tool_output={
                "max_bytes": 1,
                "max_lines": 1,
            },
            tools={"foo": True},
            username="username",
            watcher={"ignore": ["string"]},
        )
        assert_matches_type(Config, config, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: OpencodeSDK) -> None:
        response = client.config.with_raw_response.update()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = response.parse()
        assert_matches_type(Config, config, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: OpencodeSDK) -> None:
        with client.config.with_streaming_response.update() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = response.parse()
            assert_matches_type(Config, config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_providers(self, client: OpencodeSDK) -> None:
        config = client.config.list_providers()
        assert_matches_type(ConfigListProvidersResponse, config, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_providers_with_all_params(self, client: OpencodeSDK) -> None:
        config = client.config.list_providers(
            directory="directory",
            workspace="workspace",
        )
        assert_matches_type(ConfigListProvidersResponse, config, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_providers(self, client: OpencodeSDK) -> None:
        response = client.config.with_raw_response.list_providers()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = response.parse()
        assert_matches_type(ConfigListProvidersResponse, config, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
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

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncOpencodeSDK) -> None:
        config = await async_client.config.retrieve()
        assert_matches_type(Config, config, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncOpencodeSDK) -> None:
        config = await async_client.config.retrieve(
            directory="directory",
            workspace="workspace",
        )
        assert_matches_type(Config, config, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.config.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = await response.parse()
        assert_matches_type(Config, config, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.config.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = await response.parse()
            assert_matches_type(Config, config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncOpencodeSDK) -> None:
        config = await async_client.config.update()
        assert_matches_type(Config, config, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncOpencodeSDK) -> None:
        config = await async_client.config.update(
            directory="directory",
            workspace="workspace",
            schema="$schema",
            agent={
                "build": {
                    "color": "primary",
                    "description": "description",
                    "disable": True,
                    "hidden": True,
                    "max_steps": 1,
                    "mode": "subagent",
                    "model": "model",
                    "options": {"foo": "bar"},
                    "permission": "ask",
                    "prompt": "prompt",
                    "skills": ["string"],
                    "steps": 1,
                    "sub_agents": ["string"],
                    "temperature": 0,
                    "tools": {"foo": True},
                    "top_p": 0,
                    "variant": "variant",
                },
                "compaction": {
                    "color": "primary",
                    "description": "description",
                    "disable": True,
                    "hidden": True,
                    "max_steps": 1,
                    "mode": "subagent",
                    "model": "model",
                    "options": {"foo": "bar"},
                    "permission": "ask",
                    "prompt": "prompt",
                    "skills": ["string"],
                    "steps": 1,
                    "sub_agents": ["string"],
                    "temperature": 0,
                    "tools": {"foo": True},
                    "top_p": 0,
                    "variant": "variant",
                },
                "explore": {
                    "color": "primary",
                    "description": "description",
                    "disable": True,
                    "hidden": True,
                    "max_steps": 1,
                    "mode": "subagent",
                    "model": "model",
                    "options": {"foo": "bar"},
                    "permission": "ask",
                    "prompt": "prompt",
                    "skills": ["string"],
                    "steps": 1,
                    "sub_agents": ["string"],
                    "temperature": 0,
                    "tools": {"foo": True},
                    "top_p": 0,
                    "variant": "variant",
                },
                "general": {
                    "color": "primary",
                    "description": "description",
                    "disable": True,
                    "hidden": True,
                    "max_steps": 1,
                    "mode": "subagent",
                    "model": "model",
                    "options": {"foo": "bar"},
                    "permission": "ask",
                    "prompt": "prompt",
                    "skills": ["string"],
                    "steps": 1,
                    "sub_agents": ["string"],
                    "temperature": 0,
                    "tools": {"foo": True},
                    "top_p": 0,
                    "variant": "variant",
                },
                "plan": {
                    "color": "primary",
                    "description": "description",
                    "disable": True,
                    "hidden": True,
                    "max_steps": 1,
                    "mode": "subagent",
                    "model": "model",
                    "options": {"foo": "bar"},
                    "permission": "ask",
                    "prompt": "prompt",
                    "skills": ["string"],
                    "steps": 1,
                    "sub_agents": ["string"],
                    "temperature": 0,
                    "tools": {"foo": True},
                    "top_p": 0,
                    "variant": "variant",
                },
                "summary": {
                    "color": "primary",
                    "description": "description",
                    "disable": True,
                    "hidden": True,
                    "max_steps": 1,
                    "mode": "subagent",
                    "model": "model",
                    "options": {"foo": "bar"},
                    "permission": "ask",
                    "prompt": "prompt",
                    "skills": ["string"],
                    "steps": 1,
                    "sub_agents": ["string"],
                    "temperature": 0,
                    "tools": {"foo": True},
                    "top_p": 0,
                    "variant": "variant",
                },
                "title": {
                    "color": "primary",
                    "description": "description",
                    "disable": True,
                    "hidden": True,
                    "max_steps": 1,
                    "mode": "subagent",
                    "model": "model",
                    "options": {"foo": "bar"},
                    "permission": "ask",
                    "prompt": "prompt",
                    "skills": ["string"],
                    "steps": 1,
                    "sub_agents": ["string"],
                    "temperature": 0,
                    "tools": {"foo": True},
                    "top_p": 0,
                    "variant": "variant",
                },
            },
            artifact_allowed_paths=["string"],
            autoshare=True,
            autoupdate="notify",
            command={
                "foo": {
                    "template": "template",
                    "agent": "agent",
                    "description": "description",
                    "model": "model",
                    "subtask": True,
                }
            },
            compaction={
                "auto": True,
                "preserve_recent_tokens": 0,
                "prune": True,
                "reserved": 0,
                "tail_turns": 0,
            },
            custom_provider_npm_whitelist=["string"],
            default_agent="default_agent",
            disabled_providers=["string"],
            enabled_providers=["string"],
            enterprise={"url": "url"},
            experimental={
                "batch_tool": True,
                "continue_loop_on_deny": True,
                "disable_paste_summary": True,
                "mcp_timeout": 1,
                "open_telemetry": True,
                "primary_tools": ["string"],
            },
            formatter=True,
            instructions=["string"],
            layout="auto",
            log_level="DEBUG",
            lsp=True,
            mcp={
                "foo": {
                    "command": ["string"],
                    "type": "local",
                    "enabled": True,
                    "environment": {"foo": "string"},
                    "timeout": 0,
                }
            },
            mode={
                "build": {
                    "color": "primary",
                    "description": "description",
                    "disable": True,
                    "hidden": True,
                    "max_steps": 1,
                    "mode": "subagent",
                    "model": "model",
                    "options": {"foo": "bar"},
                    "permission": "ask",
                    "prompt": "prompt",
                    "skills": ["string"],
                    "steps": 1,
                    "sub_agents": ["string"],
                    "temperature": 0,
                    "tools": {"foo": True},
                    "top_p": 0,
                    "variant": "variant",
                },
                "plan": {
                    "color": "primary",
                    "description": "description",
                    "disable": True,
                    "hidden": True,
                    "max_steps": 1,
                    "mode": "subagent",
                    "model": "model",
                    "options": {"foo": "bar"},
                    "permission": "ask",
                    "prompt": "prompt",
                    "skills": ["string"],
                    "steps": 1,
                    "sub_agents": ["string"],
                    "temperature": 0,
                    "tools": {"foo": True},
                    "top_p": 0,
                    "variant": "variant",
                },
            },
            model="model",
            permission="ask",
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
                                "input": 0,
                            },
                            "modalities": {
                                "input": ["text"],
                                "output": ["text"],
                            },
                            "name": "name",
                            "options": {"foo": "bar"},
                            "provider": {
                                "api": "api",
                                "npm": "npm",
                            },
                            "reasoning": True,
                            "release_date": "release_date",
                            "status": "alpha",
                            "temperature": True,
                            "tool_call": True,
                            "variants": {"foo": {"disabled": True}},
                        }
                    },
                    "name": "name",
                    "npm": "npm",
                    "options": {
                        "api_key": "apiKey",
                        "base_url": "baseURL",
                        "chunk_timeout": 1,
                        "enterprise_url": "enterpriseUrl",
                        "set_cache_key": True,
                        "timeout": False,
                    },
                    "whitelist": ["string"],
                }
            },
            server={
                "cors": ["string"],
                "hostname": "hostname",
                "mdns": True,
                "mdns_domain": "mdnsDomain",
                "port": 1,
            },
            share="manual",
            shell="shell",
            skills={
                "paths": ["string"],
                "urls": ["string"],
            },
            small_model="small_model",
            snapshot=True,
            tool_output={
                "max_bytes": 1,
                "max_lines": 1,
            },
            tools={"foo": True},
            username="username",
            watcher={"ignore": ["string"]},
        )
        assert_matches_type(Config, config, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.config.with_raw_response.update()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = await response.parse()
        assert_matches_type(Config, config, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.config.with_streaming_response.update() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = await response.parse()
            assert_matches_type(Config, config, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_providers(self, async_client: AsyncOpencodeSDK) -> None:
        config = await async_client.config.list_providers()
        assert_matches_type(ConfigListProvidersResponse, config, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_providers_with_all_params(self, async_client: AsyncOpencodeSDK) -> None:
        config = await async_client.config.list_providers(
            directory="directory",
            workspace="workspace",
        )
        assert_matches_type(ConfigListProvidersResponse, config, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_providers(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.config.with_raw_response.list_providers()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = await response.parse()
        assert_matches_type(ConfigListProvidersResponse, config, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_providers(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.config.with_streaming_response.list_providers() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = await response.parse()
            assert_matches_type(ConfigListProvidersResponse, config, path=["response"])

        assert cast(Any, response.is_closed) is True
