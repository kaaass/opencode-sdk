# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from opencode_sdk import OpencodeSDK, AsyncOpencodeSDK
from opencode_sdk.types import (
    ClientToolListResponse,
    ClientToolCreateResponse,
    ClientToolDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestClientTool:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: OpencodeSDK) -> None:
        client_tool = client.client_tool.create(
            id="id",
            description="description",
            parameters={"foo": "bar"},
        )
        assert_matches_type(ClientToolCreateResponse, client_tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: OpencodeSDK) -> None:
        client_tool = client.client_tool.create(
            id="id",
            description="description",
            parameters={"foo": "bar"},
            directory="directory",
        )
        assert_matches_type(ClientToolCreateResponse, client_tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: OpencodeSDK) -> None:
        response = client.client_tool.with_raw_response.create(
            id="id",
            description="description",
            parameters={"foo": "bar"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client_tool = response.parse()
        assert_matches_type(ClientToolCreateResponse, client_tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: OpencodeSDK) -> None:
        with client.client_tool.with_streaming_response.create(
            id="id",
            description="description",
            parameters={"foo": "bar"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client_tool = response.parse()
            assert_matches_type(ClientToolCreateResponse, client_tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: OpencodeSDK) -> None:
        client_tool = client.client_tool.list()
        assert_matches_type(ClientToolListResponse, client_tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: OpencodeSDK) -> None:
        client_tool = client.client_tool.list(
            directory="directory",
        )
        assert_matches_type(ClientToolListResponse, client_tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: OpencodeSDK) -> None:
        response = client.client_tool.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client_tool = response.parse()
        assert_matches_type(ClientToolListResponse, client_tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: OpencodeSDK) -> None:
        with client.client_tool.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client_tool = response.parse()
            assert_matches_type(ClientToolListResponse, client_tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: OpencodeSDK) -> None:
        client_tool = client.client_tool.delete(
            id="id",
        )
        assert_matches_type(ClientToolDeleteResponse, client_tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete_with_all_params(self, client: OpencodeSDK) -> None:
        client_tool = client.client_tool.delete(
            id="id",
            directory="directory",
        )
        assert_matches_type(ClientToolDeleteResponse, client_tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: OpencodeSDK) -> None:
        response = client.client_tool.with_raw_response.delete(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client_tool = response.parse()
        assert_matches_type(ClientToolDeleteResponse, client_tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: OpencodeSDK) -> None:
        with client.client_tool.with_streaming_response.delete(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client_tool = response.parse()
            assert_matches_type(ClientToolDeleteResponse, client_tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: OpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.client_tool.with_raw_response.delete(
                id="",
            )


class TestAsyncClientTool:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncOpencodeSDK) -> None:
        client_tool = await async_client.client_tool.create(
            id="id",
            description="description",
            parameters={"foo": "bar"},
        )
        assert_matches_type(ClientToolCreateResponse, client_tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncOpencodeSDK) -> None:
        client_tool = await async_client.client_tool.create(
            id="id",
            description="description",
            parameters={"foo": "bar"},
            directory="directory",
        )
        assert_matches_type(ClientToolCreateResponse, client_tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.client_tool.with_raw_response.create(
            id="id",
            description="description",
            parameters={"foo": "bar"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client_tool = await response.parse()
        assert_matches_type(ClientToolCreateResponse, client_tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.client_tool.with_streaming_response.create(
            id="id",
            description="description",
            parameters={"foo": "bar"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client_tool = await response.parse()
            assert_matches_type(ClientToolCreateResponse, client_tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncOpencodeSDK) -> None:
        client_tool = await async_client.client_tool.list()
        assert_matches_type(ClientToolListResponse, client_tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncOpencodeSDK) -> None:
        client_tool = await async_client.client_tool.list(
            directory="directory",
        )
        assert_matches_type(ClientToolListResponse, client_tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.client_tool.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client_tool = await response.parse()
        assert_matches_type(ClientToolListResponse, client_tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.client_tool.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client_tool = await response.parse()
            assert_matches_type(ClientToolListResponse, client_tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncOpencodeSDK) -> None:
        client_tool = await async_client.client_tool.delete(
            id="id",
        )
        assert_matches_type(ClientToolDeleteResponse, client_tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncOpencodeSDK) -> None:
        client_tool = await async_client.client_tool.delete(
            id="id",
            directory="directory",
        )
        assert_matches_type(ClientToolDeleteResponse, client_tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.client_tool.with_raw_response.delete(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client_tool = await response.parse()
        assert_matches_type(ClientToolDeleteResponse, client_tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.client_tool.with_streaming_response.delete(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client_tool = await response.parse()
            assert_matches_type(ClientToolDeleteResponse, client_tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncOpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.client_tool.with_raw_response.delete(
                id="",
            )
