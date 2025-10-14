# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from opencode_sdk import OpencodeSDK, AsyncOpencodeSDK
from opencode_sdk.types.experimental import (
    ToolListIDsResponse,
    ToolListToolsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTool:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_ids(self, client: OpencodeSDK) -> None:
        tool = client.experimental.tool.list_ids()
        assert_matches_type(ToolListIDsResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_ids_with_all_params(self, client: OpencodeSDK) -> None:
        tool = client.experimental.tool.list_ids(
            directory="directory",
        )
        assert_matches_type(ToolListIDsResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_ids(self, client: OpencodeSDK) -> None:
        response = client.experimental.tool.with_raw_response.list_ids()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(ToolListIDsResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_ids(self, client: OpencodeSDK) -> None:
        with client.experimental.tool.with_streaming_response.list_ids() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = response.parse()
            assert_matches_type(ToolListIDsResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_tools(self, client: OpencodeSDK) -> None:
        tool = client.experimental.tool.list_tools(
            model="model",
            provider="provider",
        )
        assert_matches_type(ToolListToolsResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_tools_with_all_params(self, client: OpencodeSDK) -> None:
        tool = client.experimental.tool.list_tools(
            model="model",
            provider="provider",
            directory="directory",
        )
        assert_matches_type(ToolListToolsResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_tools(self, client: OpencodeSDK) -> None:
        response = client.experimental.tool.with_raw_response.list_tools(
            model="model",
            provider="provider",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = response.parse()
        assert_matches_type(ToolListToolsResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_tools(self, client: OpencodeSDK) -> None:
        with client.experimental.tool.with_streaming_response.list_tools(
            model="model",
            provider="provider",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = response.parse()
            assert_matches_type(ToolListToolsResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTool:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_ids(self, async_client: AsyncOpencodeSDK) -> None:
        tool = await async_client.experimental.tool.list_ids()
        assert_matches_type(ToolListIDsResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_ids_with_all_params(self, async_client: AsyncOpencodeSDK) -> None:
        tool = await async_client.experimental.tool.list_ids(
            directory="directory",
        )
        assert_matches_type(ToolListIDsResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_ids(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.experimental.tool.with_raw_response.list_ids()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(ToolListIDsResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_ids(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.experimental.tool.with_streaming_response.list_ids() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = await response.parse()
            assert_matches_type(ToolListIDsResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_tools(self, async_client: AsyncOpencodeSDK) -> None:
        tool = await async_client.experimental.tool.list_tools(
            model="model",
            provider="provider",
        )
        assert_matches_type(ToolListToolsResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_tools_with_all_params(self, async_client: AsyncOpencodeSDK) -> None:
        tool = await async_client.experimental.tool.list_tools(
            model="model",
            provider="provider",
            directory="directory",
        )
        assert_matches_type(ToolListToolsResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_tools(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.experimental.tool.with_raw_response.list_tools(
            model="model",
            provider="provider",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tool = await response.parse()
        assert_matches_type(ToolListToolsResponse, tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_tools(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.experimental.tool.with_streaming_response.list_tools(
            model="model",
            provider="provider",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tool = await response.parse()
            assert_matches_type(ToolListToolsResponse, tool, path=["response"])

        assert cast(Any, response.is_closed) is True
