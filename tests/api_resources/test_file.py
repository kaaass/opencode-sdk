# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from opencode_sdk import OpencodeSDK, AsyncOpencodeSDK
from opencode_sdk.types import (
    FileListResponse,
    FileReadResponse,
    FileGetStatusResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFile:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: OpencodeSDK) -> None:
        file = client.file.list(
            path="path",
        )
        assert_matches_type(FileListResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: OpencodeSDK) -> None:
        file = client.file.list(
            path="path",
            directory="directory",
        )
        assert_matches_type(FileListResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: OpencodeSDK) -> None:
        response = client.file.with_raw_response.list(
            path="path",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(FileListResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: OpencodeSDK) -> None:
        with client.file.with_streaming_response.list(
            path="path",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(FileListResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_status(self, client: OpencodeSDK) -> None:
        file = client.file.get_status()
        assert_matches_type(FileGetStatusResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_status_with_all_params(self, client: OpencodeSDK) -> None:
        file = client.file.get_status(
            directory="directory",
        )
        assert_matches_type(FileGetStatusResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_status(self, client: OpencodeSDK) -> None:
        response = client.file.with_raw_response.get_status()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(FileGetStatusResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_status(self, client: OpencodeSDK) -> None:
        with client.file.with_streaming_response.get_status() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(FileGetStatusResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_read(self, client: OpencodeSDK) -> None:
        file = client.file.read(
            path="path",
        )
        assert_matches_type(FileReadResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_read_with_all_params(self, client: OpencodeSDK) -> None:
        file = client.file.read(
            path="path",
            directory="directory",
        )
        assert_matches_type(FileReadResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_read(self, client: OpencodeSDK) -> None:
        response = client.file.with_raw_response.read(
            path="path",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(FileReadResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_read(self, client: OpencodeSDK) -> None:
        with client.file.with_streaming_response.read(
            path="path",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(FileReadResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncFile:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncOpencodeSDK) -> None:
        file = await async_client.file.list(
            path="path",
        )
        assert_matches_type(FileListResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncOpencodeSDK) -> None:
        file = await async_client.file.list(
            path="path",
            directory="directory",
        )
        assert_matches_type(FileListResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.file.with_raw_response.list(
            path="path",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(FileListResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.file.with_streaming_response.list(
            path="path",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(FileListResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_status(self, async_client: AsyncOpencodeSDK) -> None:
        file = await async_client.file.get_status()
        assert_matches_type(FileGetStatusResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_status_with_all_params(self, async_client: AsyncOpencodeSDK) -> None:
        file = await async_client.file.get_status(
            directory="directory",
        )
        assert_matches_type(FileGetStatusResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_status(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.file.with_raw_response.get_status()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(FileGetStatusResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_status(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.file.with_streaming_response.get_status() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(FileGetStatusResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_read(self, async_client: AsyncOpencodeSDK) -> None:
        file = await async_client.file.read(
            path="path",
        )
        assert_matches_type(FileReadResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_read_with_all_params(self, async_client: AsyncOpencodeSDK) -> None:
        file = await async_client.file.read(
            path="path",
            directory="directory",
        )
        assert_matches_type(FileReadResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_read(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.file.with_raw_response.read(
            path="path",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(FileReadResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_read(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.file.with_streaming_response.read(
            path="path",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(FileReadResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True
