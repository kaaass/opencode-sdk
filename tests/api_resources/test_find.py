# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from opencode_sdk import OpencodeSDK, AsyncOpencodeSDK
from opencode_sdk.types import (
    FindRetrieveResponse,
    FindRetrieveFileResponse,
    FindRetrieveSymbolResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFind:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: OpencodeSDK) -> None:
        find = client.find.retrieve(
            pattern="pattern",
        )
        assert_matches_type(FindRetrieveResponse, find, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: OpencodeSDK) -> None:
        find = client.find.retrieve(
            pattern="pattern",
            directory="directory",
        )
        assert_matches_type(FindRetrieveResponse, find, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: OpencodeSDK) -> None:
        response = client.find.with_raw_response.retrieve(
            pattern="pattern",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        find = response.parse()
        assert_matches_type(FindRetrieveResponse, find, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: OpencodeSDK) -> None:
        with client.find.with_streaming_response.retrieve(
            pattern="pattern",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            find = response.parse()
            assert_matches_type(FindRetrieveResponse, find, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_file(self, client: OpencodeSDK) -> None:
        find = client.find.retrieve_file(
            query="query",
        )
        assert_matches_type(FindRetrieveFileResponse, find, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_file_with_all_params(self, client: OpencodeSDK) -> None:
        find = client.find.retrieve_file(
            query="query",
            directory="directory",
            dirs="true",
        )
        assert_matches_type(FindRetrieveFileResponse, find, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_file(self, client: OpencodeSDK) -> None:
        response = client.find.with_raw_response.retrieve_file(
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        find = response.parse()
        assert_matches_type(FindRetrieveFileResponse, find, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_file(self, client: OpencodeSDK) -> None:
        with client.find.with_streaming_response.retrieve_file(
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            find = response.parse()
            assert_matches_type(FindRetrieveFileResponse, find, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_symbol(self, client: OpencodeSDK) -> None:
        find = client.find.retrieve_symbol(
            query="query",
        )
        assert_matches_type(FindRetrieveSymbolResponse, find, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_symbol_with_all_params(self, client: OpencodeSDK) -> None:
        find = client.find.retrieve_symbol(
            query="query",
            directory="directory",
        )
        assert_matches_type(FindRetrieveSymbolResponse, find, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_symbol(self, client: OpencodeSDK) -> None:
        response = client.find.with_raw_response.retrieve_symbol(
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        find = response.parse()
        assert_matches_type(FindRetrieveSymbolResponse, find, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_symbol(self, client: OpencodeSDK) -> None:
        with client.find.with_streaming_response.retrieve_symbol(
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            find = response.parse()
            assert_matches_type(FindRetrieveSymbolResponse, find, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncFind:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncOpencodeSDK) -> None:
        find = await async_client.find.retrieve(
            pattern="pattern",
        )
        assert_matches_type(FindRetrieveResponse, find, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncOpencodeSDK) -> None:
        find = await async_client.find.retrieve(
            pattern="pattern",
            directory="directory",
        )
        assert_matches_type(FindRetrieveResponse, find, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.find.with_raw_response.retrieve(
            pattern="pattern",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        find = await response.parse()
        assert_matches_type(FindRetrieveResponse, find, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.find.with_streaming_response.retrieve(
            pattern="pattern",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            find = await response.parse()
            assert_matches_type(FindRetrieveResponse, find, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_file(self, async_client: AsyncOpencodeSDK) -> None:
        find = await async_client.find.retrieve_file(
            query="query",
        )
        assert_matches_type(FindRetrieveFileResponse, find, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_file_with_all_params(self, async_client: AsyncOpencodeSDK) -> None:
        find = await async_client.find.retrieve_file(
            query="query",
            directory="directory",
            dirs="true",
        )
        assert_matches_type(FindRetrieveFileResponse, find, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_file(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.find.with_raw_response.retrieve_file(
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        find = await response.parse()
        assert_matches_type(FindRetrieveFileResponse, find, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_file(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.find.with_streaming_response.retrieve_file(
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            find = await response.parse()
            assert_matches_type(FindRetrieveFileResponse, find, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_symbol(self, async_client: AsyncOpencodeSDK) -> None:
        find = await async_client.find.retrieve_symbol(
            query="query",
        )
        assert_matches_type(FindRetrieveSymbolResponse, find, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_symbol_with_all_params(self, async_client: AsyncOpencodeSDK) -> None:
        find = await async_client.find.retrieve_symbol(
            query="query",
            directory="directory",
        )
        assert_matches_type(FindRetrieveSymbolResponse, find, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_symbol(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.find.with_raw_response.retrieve_symbol(
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        find = await response.parse()
        assert_matches_type(FindRetrieveSymbolResponse, find, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_symbol(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.find.with_streaming_response.retrieve_symbol(
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            find = await response.parse()
            assert_matches_type(FindRetrieveSymbolResponse, find, path=["response"])

        assert cast(Any, response.is_closed) is True
