# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from ai4pa_opencode_sdk import OpencodeSDK, AsyncOpencodeSDK
from ai4pa_opencode_sdk.types import ClientConnectionCloseResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestClientConnection:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_close(self, client: OpencodeSDK) -> None:
        client_connection = client.client_connection.close()
        assert_matches_type(ClientConnectionCloseResponse, client_connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_close_with_all_params(self, client: OpencodeSDK) -> None:
        client_connection = client.client_connection.close(
            directory="directory",
            workspace="workspace",
        )
        assert_matches_type(ClientConnectionCloseResponse, client_connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_close(self, client: OpencodeSDK) -> None:
        response = client.client_connection.with_raw_response.close()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client_connection = response.parse()
        assert_matches_type(ClientConnectionCloseResponse, client_connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_close(self, client: OpencodeSDK) -> None:
        with client.client_connection.with_streaming_response.close() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client_connection = response.parse()
            assert_matches_type(ClientConnectionCloseResponse, client_connection, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncClientConnection:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_close(self, async_client: AsyncOpencodeSDK) -> None:
        client_connection = await async_client.client_connection.close()
        assert_matches_type(ClientConnectionCloseResponse, client_connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_close_with_all_params(self, async_client: AsyncOpencodeSDK) -> None:
        client_connection = await async_client.client_connection.close(
            directory="directory",
            workspace="workspace",
        )
        assert_matches_type(ClientConnectionCloseResponse, client_connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_close(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.client_connection.with_raw_response.close()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client_connection = await response.parse()
        assert_matches_type(ClientConnectionCloseResponse, client_connection, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_close(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.client_connection.with_streaming_response.close() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client_connection = await response.parse()
            assert_matches_type(ClientConnectionCloseResponse, client_connection, path=["response"])

        assert cast(Any, response.is_closed) is True
