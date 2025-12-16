# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from opencode_sdk import OpencodeSDK, AsyncOpencodeSDK
from opencode_sdk.types import (
    RemoteToolListResponse,
    RemoteToolRegisterResponse,
    RemoteToolUnregisterResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRemoteTool:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: OpencodeSDK) -> None:
        remote_tool = client.remote_tool.list()
        assert_matches_type(RemoteToolListResponse, remote_tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: OpencodeSDK) -> None:
        remote_tool = client.remote_tool.list(
            directory="directory",
        )
        assert_matches_type(RemoteToolListResponse, remote_tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: OpencodeSDK) -> None:
        response = client.remote_tool.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        remote_tool = response.parse()
        assert_matches_type(RemoteToolListResponse, remote_tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: OpencodeSDK) -> None:
        with client.remote_tool.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            remote_tool = response.parse()
            assert_matches_type(RemoteToolListResponse, remote_tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_register(self, client: OpencodeSDK) -> None:
        remote_tool = client.remote_tool.register(
            id="id",
            description="description",
            parameters={"foo": "bar"},
        )
        assert_matches_type(RemoteToolRegisterResponse, remote_tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_register_with_all_params(self, client: OpencodeSDK) -> None:
        remote_tool = client.remote_tool.register(
            id="id",
            description="description",
            parameters={"foo": "bar"},
            directory="directory",
        )
        assert_matches_type(RemoteToolRegisterResponse, remote_tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_register(self, client: OpencodeSDK) -> None:
        response = client.remote_tool.with_raw_response.register(
            id="id",
            description="description",
            parameters={"foo": "bar"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        remote_tool = response.parse()
        assert_matches_type(RemoteToolRegisterResponse, remote_tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_register(self, client: OpencodeSDK) -> None:
        with client.remote_tool.with_streaming_response.register(
            id="id",
            description="description",
            parameters={"foo": "bar"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            remote_tool = response.parse()
            assert_matches_type(RemoteToolRegisterResponse, remote_tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_unregister(self, client: OpencodeSDK) -> None:
        remote_tool = client.remote_tool.unregister(
            id="id",
        )
        assert_matches_type(RemoteToolUnregisterResponse, remote_tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_unregister_with_all_params(self, client: OpencodeSDK) -> None:
        remote_tool = client.remote_tool.unregister(
            id="id",
            directory="directory",
        )
        assert_matches_type(RemoteToolUnregisterResponse, remote_tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_unregister(self, client: OpencodeSDK) -> None:
        response = client.remote_tool.with_raw_response.unregister(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        remote_tool = response.parse()
        assert_matches_type(RemoteToolUnregisterResponse, remote_tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_unregister(self, client: OpencodeSDK) -> None:
        with client.remote_tool.with_streaming_response.unregister(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            remote_tool = response.parse()
            assert_matches_type(RemoteToolUnregisterResponse, remote_tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_unregister(self, client: OpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.remote_tool.with_raw_response.unregister(
                id="",
            )


class TestAsyncRemoteTool:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncOpencodeSDK) -> None:
        remote_tool = await async_client.remote_tool.list()
        assert_matches_type(RemoteToolListResponse, remote_tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncOpencodeSDK) -> None:
        remote_tool = await async_client.remote_tool.list(
            directory="directory",
        )
        assert_matches_type(RemoteToolListResponse, remote_tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.remote_tool.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        remote_tool = await response.parse()
        assert_matches_type(RemoteToolListResponse, remote_tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.remote_tool.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            remote_tool = await response.parse()
            assert_matches_type(RemoteToolListResponse, remote_tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_register(self, async_client: AsyncOpencodeSDK) -> None:
        remote_tool = await async_client.remote_tool.register(
            id="id",
            description="description",
            parameters={"foo": "bar"},
        )
        assert_matches_type(RemoteToolRegisterResponse, remote_tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_register_with_all_params(self, async_client: AsyncOpencodeSDK) -> None:
        remote_tool = await async_client.remote_tool.register(
            id="id",
            description="description",
            parameters={"foo": "bar"},
            directory="directory",
        )
        assert_matches_type(RemoteToolRegisterResponse, remote_tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_register(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.remote_tool.with_raw_response.register(
            id="id",
            description="description",
            parameters={"foo": "bar"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        remote_tool = await response.parse()
        assert_matches_type(RemoteToolRegisterResponse, remote_tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_register(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.remote_tool.with_streaming_response.register(
            id="id",
            description="description",
            parameters={"foo": "bar"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            remote_tool = await response.parse()
            assert_matches_type(RemoteToolRegisterResponse, remote_tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_unregister(self, async_client: AsyncOpencodeSDK) -> None:
        remote_tool = await async_client.remote_tool.unregister(
            id="id",
        )
        assert_matches_type(RemoteToolUnregisterResponse, remote_tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_unregister_with_all_params(self, async_client: AsyncOpencodeSDK) -> None:
        remote_tool = await async_client.remote_tool.unregister(
            id="id",
            directory="directory",
        )
        assert_matches_type(RemoteToolUnregisterResponse, remote_tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_unregister(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.remote_tool.with_raw_response.unregister(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        remote_tool = await response.parse()
        assert_matches_type(RemoteToolUnregisterResponse, remote_tool, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_unregister(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.remote_tool.with_streaming_response.unregister(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            remote_tool = await response.parse()
            assert_matches_type(RemoteToolUnregisterResponse, remote_tool, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_unregister(self, async_client: AsyncOpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.remote_tool.with_raw_response.unregister(
                id="",
            )
