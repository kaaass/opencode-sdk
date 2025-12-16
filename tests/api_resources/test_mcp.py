# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from opencode_sdk import OpencodeSDK, AsyncOpencodeSDK
from opencode_sdk.types import (
    McpCreateResponse,
    McpReloadResponse,
    McpConnectResponse,
    McpRetrieveResponse,
    McpDisconnectResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMcp:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: OpencodeSDK) -> None:
        mcp = client.mcp.create(
            config={
                "command": ["string"],
                "type": "local",
            },
            name="name",
        )
        assert_matches_type(McpCreateResponse, mcp, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: OpencodeSDK) -> None:
        mcp = client.mcp.create(
            config={
                "command": ["string"],
                "type": "local",
                "enabled": True,
                "environment": {"foo": "string"},
                "timeout": 1,
            },
            name="name",
            directory="directory",
        )
        assert_matches_type(McpCreateResponse, mcp, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: OpencodeSDK) -> None:
        response = client.mcp.with_raw_response.create(
            config={
                "command": ["string"],
                "type": "local",
            },
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp = response.parse()
        assert_matches_type(McpCreateResponse, mcp, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: OpencodeSDK) -> None:
        with client.mcp.with_streaming_response.create(
            config={
                "command": ["string"],
                "type": "local",
            },
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp = response.parse()
            assert_matches_type(McpCreateResponse, mcp, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: OpencodeSDK) -> None:
        mcp = client.mcp.retrieve()
        assert_matches_type(McpRetrieveResponse, mcp, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: OpencodeSDK) -> None:
        mcp = client.mcp.retrieve(
            directory="directory",
        )
        assert_matches_type(McpRetrieveResponse, mcp, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: OpencodeSDK) -> None:
        response = client.mcp.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp = response.parse()
        assert_matches_type(McpRetrieveResponse, mcp, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: OpencodeSDK) -> None:
        with client.mcp.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp = response.parse()
            assert_matches_type(McpRetrieveResponse, mcp, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_connect(self, client: OpencodeSDK) -> None:
        mcp = client.mcp.connect(
            name="name",
        )
        assert_matches_type(McpConnectResponse, mcp, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_connect_with_all_params(self, client: OpencodeSDK) -> None:
        mcp = client.mcp.connect(
            name="name",
            directory="directory",
        )
        assert_matches_type(McpConnectResponse, mcp, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_connect(self, client: OpencodeSDK) -> None:
        response = client.mcp.with_raw_response.connect(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp = response.parse()
        assert_matches_type(McpConnectResponse, mcp, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_connect(self, client: OpencodeSDK) -> None:
        with client.mcp.with_streaming_response.connect(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp = response.parse()
            assert_matches_type(McpConnectResponse, mcp, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_connect(self, client: OpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            client.mcp.with_raw_response.connect(
                name="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_disconnect(self, client: OpencodeSDK) -> None:
        mcp = client.mcp.disconnect(
            name="name",
        )
        assert_matches_type(McpDisconnectResponse, mcp, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_disconnect_with_all_params(self, client: OpencodeSDK) -> None:
        mcp = client.mcp.disconnect(
            name="name",
            directory="directory",
        )
        assert_matches_type(McpDisconnectResponse, mcp, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_disconnect(self, client: OpencodeSDK) -> None:
        response = client.mcp.with_raw_response.disconnect(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp = response.parse()
        assert_matches_type(McpDisconnectResponse, mcp, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_disconnect(self, client: OpencodeSDK) -> None:
        with client.mcp.with_streaming_response.disconnect(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp = response.parse()
            assert_matches_type(McpDisconnectResponse, mcp, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_disconnect(self, client: OpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            client.mcp.with_raw_response.disconnect(
                name="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_reload(self, client: OpencodeSDK) -> None:
        mcp = client.mcp.reload()
        assert_matches_type(McpReloadResponse, mcp, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_reload_with_all_params(self, client: OpencodeSDK) -> None:
        mcp = client.mcp.reload(
            directory="directory",
        )
        assert_matches_type(McpReloadResponse, mcp, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_reload(self, client: OpencodeSDK) -> None:
        response = client.mcp.with_raw_response.reload()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp = response.parse()
        assert_matches_type(McpReloadResponse, mcp, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_reload(self, client: OpencodeSDK) -> None:
        with client.mcp.with_streaming_response.reload() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp = response.parse()
            assert_matches_type(McpReloadResponse, mcp, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncMcp:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncOpencodeSDK) -> None:
        mcp = await async_client.mcp.create(
            config={
                "command": ["string"],
                "type": "local",
            },
            name="name",
        )
        assert_matches_type(McpCreateResponse, mcp, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncOpencodeSDK) -> None:
        mcp = await async_client.mcp.create(
            config={
                "command": ["string"],
                "type": "local",
                "enabled": True,
                "environment": {"foo": "string"},
                "timeout": 1,
            },
            name="name",
            directory="directory",
        )
        assert_matches_type(McpCreateResponse, mcp, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.mcp.with_raw_response.create(
            config={
                "command": ["string"],
                "type": "local",
            },
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp = await response.parse()
        assert_matches_type(McpCreateResponse, mcp, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.mcp.with_streaming_response.create(
            config={
                "command": ["string"],
                "type": "local",
            },
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp = await response.parse()
            assert_matches_type(McpCreateResponse, mcp, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncOpencodeSDK) -> None:
        mcp = await async_client.mcp.retrieve()
        assert_matches_type(McpRetrieveResponse, mcp, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncOpencodeSDK) -> None:
        mcp = await async_client.mcp.retrieve(
            directory="directory",
        )
        assert_matches_type(McpRetrieveResponse, mcp, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.mcp.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp = await response.parse()
        assert_matches_type(McpRetrieveResponse, mcp, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.mcp.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp = await response.parse()
            assert_matches_type(McpRetrieveResponse, mcp, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_connect(self, async_client: AsyncOpencodeSDK) -> None:
        mcp = await async_client.mcp.connect(
            name="name",
        )
        assert_matches_type(McpConnectResponse, mcp, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_connect_with_all_params(self, async_client: AsyncOpencodeSDK) -> None:
        mcp = await async_client.mcp.connect(
            name="name",
            directory="directory",
        )
        assert_matches_type(McpConnectResponse, mcp, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_connect(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.mcp.with_raw_response.connect(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp = await response.parse()
        assert_matches_type(McpConnectResponse, mcp, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_connect(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.mcp.with_streaming_response.connect(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp = await response.parse()
            assert_matches_type(McpConnectResponse, mcp, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_connect(self, async_client: AsyncOpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            await async_client.mcp.with_raw_response.connect(
                name="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_disconnect(self, async_client: AsyncOpencodeSDK) -> None:
        mcp = await async_client.mcp.disconnect(
            name="name",
        )
        assert_matches_type(McpDisconnectResponse, mcp, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_disconnect_with_all_params(self, async_client: AsyncOpencodeSDK) -> None:
        mcp = await async_client.mcp.disconnect(
            name="name",
            directory="directory",
        )
        assert_matches_type(McpDisconnectResponse, mcp, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_disconnect(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.mcp.with_raw_response.disconnect(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp = await response.parse()
        assert_matches_type(McpDisconnectResponse, mcp, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_disconnect(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.mcp.with_streaming_response.disconnect(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp = await response.parse()
            assert_matches_type(McpDisconnectResponse, mcp, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_disconnect(self, async_client: AsyncOpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            await async_client.mcp.with_raw_response.disconnect(
                name="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_reload(self, async_client: AsyncOpencodeSDK) -> None:
        mcp = await async_client.mcp.reload()
        assert_matches_type(McpReloadResponse, mcp, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_reload_with_all_params(self, async_client: AsyncOpencodeSDK) -> None:
        mcp = await async_client.mcp.reload(
            directory="directory",
        )
        assert_matches_type(McpReloadResponse, mcp, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_reload(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.mcp.with_raw_response.reload()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mcp = await response.parse()
        assert_matches_type(McpReloadResponse, mcp, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_reload(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.mcp.with_streaming_response.reload() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mcp = await response.parse()
            assert_matches_type(McpReloadResponse, mcp, path=["response"])

        assert cast(Any, response.is_closed) is True
