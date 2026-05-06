# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from ai4pa_opencode_sdk import OpencodeSDK, AsyncOpencodeSDK
from ai4pa_opencode_sdk.types import (
    McpAddServerResponse,
    McpConnectServerResponse,
    McpRetrieveStatusResponse,
    McpDisconnectServerResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMcp:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_add_server(self, client: OpencodeSDK) -> None:
        mcp = client.mcp.add_server(
            config={
                "command": ["string"],
                "type": "local",
            },
            name="name",
        )
        assert_matches_type(McpAddServerResponse, mcp, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_add_server_with_all_params(self, client: OpencodeSDK) -> None:
        mcp = client.mcp.add_server(
            config={
                "command": ["string"],
                "type": "local",
                "enabled": True,
                "environment": {"foo": "string"},
                "timeout": 0,
            },
            name="name",
            directory="directory",
            workspace="workspace",
        )
        assert_matches_type(McpAddServerResponse, mcp, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_add_server(self, client: OpencodeSDK) -> None:
        response = client.mcp.with_raw_response.add_server(
            config={
                "command": ["string"],
                "type": "local",
            },
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp = response.parse()
        assert_matches_type(McpAddServerResponse, mcp, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_add_server(self, client: OpencodeSDK) -> None:
        with client.mcp.with_streaming_response.add_server(
            config={
                "command": ["string"],
                "type": "local",
            },
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp = response.parse()
            assert_matches_type(McpAddServerResponse, mcp, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_connect_server(self, client: OpencodeSDK) -> None:
        mcp = client.mcp.connect_server(
            name="name",
        )
        assert_matches_type(McpConnectServerResponse, mcp, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_connect_server_with_all_params(self, client: OpencodeSDK) -> None:
        mcp = client.mcp.connect_server(
            name="name",
            directory="directory",
            workspace="workspace",
        )
        assert_matches_type(McpConnectServerResponse, mcp, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_connect_server(self, client: OpencodeSDK) -> None:
        response = client.mcp.with_raw_response.connect_server(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp = response.parse()
        assert_matches_type(McpConnectServerResponse, mcp, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_connect_server(self, client: OpencodeSDK) -> None:
        with client.mcp.with_streaming_response.connect_server(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp = response.parse()
            assert_matches_type(McpConnectServerResponse, mcp, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_connect_server(self, client: OpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            client.mcp.with_raw_response.connect_server(
                name="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_disconnect_server(self, client: OpencodeSDK) -> None:
        mcp = client.mcp.disconnect_server(
            name="name",
        )
        assert_matches_type(McpDisconnectServerResponse, mcp, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_disconnect_server_with_all_params(self, client: OpencodeSDK) -> None:
        mcp = client.mcp.disconnect_server(
            name="name",
            directory="directory",
            workspace="workspace",
        )
        assert_matches_type(McpDisconnectServerResponse, mcp, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_disconnect_server(self, client: OpencodeSDK) -> None:
        response = client.mcp.with_raw_response.disconnect_server(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp = response.parse()
        assert_matches_type(McpDisconnectServerResponse, mcp, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_disconnect_server(self, client: OpencodeSDK) -> None:
        with client.mcp.with_streaming_response.disconnect_server(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp = response.parse()
            assert_matches_type(McpDisconnectServerResponse, mcp, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_disconnect_server(self, client: OpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            client.mcp.with_raw_response.disconnect_server(
                name="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_status(self, client: OpencodeSDK) -> None:
        mcp = client.mcp.retrieve_status()
        assert_matches_type(McpRetrieveStatusResponse, mcp, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_status_with_all_params(self, client: OpencodeSDK) -> None:
        mcp = client.mcp.retrieve_status(
            directory="directory",
            workspace="workspace",
        )
        assert_matches_type(McpRetrieveStatusResponse, mcp, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_status(self, client: OpencodeSDK) -> None:
        response = client.mcp.with_raw_response.retrieve_status()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp = response.parse()
        assert_matches_type(McpRetrieveStatusResponse, mcp, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_status(self, client: OpencodeSDK) -> None:
        with client.mcp.with_streaming_response.retrieve_status() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp = response.parse()
            assert_matches_type(McpRetrieveStatusResponse, mcp, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncMcp:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_add_server(self, async_client: AsyncOpencodeSDK) -> None:
        mcp = await async_client.mcp.add_server(
            config={
                "command": ["string"],
                "type": "local",
            },
            name="name",
        )
        assert_matches_type(McpAddServerResponse, mcp, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_add_server_with_all_params(self, async_client: AsyncOpencodeSDK) -> None:
        mcp = await async_client.mcp.add_server(
            config={
                "command": ["string"],
                "type": "local",
                "enabled": True,
                "environment": {"foo": "string"},
                "timeout": 0,
            },
            name="name",
            directory="directory",
            workspace="workspace",
        )
        assert_matches_type(McpAddServerResponse, mcp, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_add_server(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.mcp.with_raw_response.add_server(
            config={
                "command": ["string"],
                "type": "local",
            },
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp = await response.parse()
        assert_matches_type(McpAddServerResponse, mcp, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_add_server(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.mcp.with_streaming_response.add_server(
            config={
                "command": ["string"],
                "type": "local",
            },
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp = await response.parse()
            assert_matches_type(McpAddServerResponse, mcp, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_connect_server(self, async_client: AsyncOpencodeSDK) -> None:
        mcp = await async_client.mcp.connect_server(
            name="name",
        )
        assert_matches_type(McpConnectServerResponse, mcp, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_connect_server_with_all_params(self, async_client: AsyncOpencodeSDK) -> None:
        mcp = await async_client.mcp.connect_server(
            name="name",
            directory="directory",
            workspace="workspace",
        )
        assert_matches_type(McpConnectServerResponse, mcp, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_connect_server(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.mcp.with_raw_response.connect_server(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp = await response.parse()
        assert_matches_type(McpConnectServerResponse, mcp, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_connect_server(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.mcp.with_streaming_response.connect_server(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp = await response.parse()
            assert_matches_type(McpConnectServerResponse, mcp, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_connect_server(self, async_client: AsyncOpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            await async_client.mcp.with_raw_response.connect_server(
                name="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_disconnect_server(self, async_client: AsyncOpencodeSDK) -> None:
        mcp = await async_client.mcp.disconnect_server(
            name="name",
        )
        assert_matches_type(McpDisconnectServerResponse, mcp, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_disconnect_server_with_all_params(self, async_client: AsyncOpencodeSDK) -> None:
        mcp = await async_client.mcp.disconnect_server(
            name="name",
            directory="directory",
            workspace="workspace",
        )
        assert_matches_type(McpDisconnectServerResponse, mcp, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_disconnect_server(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.mcp.with_raw_response.disconnect_server(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp = await response.parse()
        assert_matches_type(McpDisconnectServerResponse, mcp, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_disconnect_server(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.mcp.with_streaming_response.disconnect_server(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp = await response.parse()
            assert_matches_type(McpDisconnectServerResponse, mcp, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_disconnect_server(self, async_client: AsyncOpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            await async_client.mcp.with_raw_response.disconnect_server(
                name="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_status(self, async_client: AsyncOpencodeSDK) -> None:
        mcp = await async_client.mcp.retrieve_status()
        assert_matches_type(McpRetrieveStatusResponse, mcp, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_status_with_all_params(self, async_client: AsyncOpencodeSDK) -> None:
        mcp = await async_client.mcp.retrieve_status(
            directory="directory",
            workspace="workspace",
        )
        assert_matches_type(McpRetrieveStatusResponse, mcp, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_status(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.mcp.with_raw_response.retrieve_status()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp = await response.parse()
        assert_matches_type(McpRetrieveStatusResponse, mcp, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_status(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.mcp.with_streaming_response.retrieve_status() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp = await response.parse()
            assert_matches_type(McpRetrieveStatusResponse, mcp, path=["response"])

        assert cast(Any, response.is_closed) is True
