# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from opencode_sdk import OpencodeSDK, AsyncOpencodeSDK
from opencode_sdk.types import LspRetrieveStatusResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLsp:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_status(self, client: OpencodeSDK) -> None:
        lsp = client.lsp.retrieve_status()
        assert_matches_type(LspRetrieveStatusResponse, lsp, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_status_with_all_params(self, client: OpencodeSDK) -> None:
        lsp = client.lsp.retrieve_status(
            directory="directory",
        )
        assert_matches_type(LspRetrieveStatusResponse, lsp, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_status(self, client: OpencodeSDK) -> None:
        response = client.lsp.with_raw_response.retrieve_status()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lsp = response.parse()
        assert_matches_type(LspRetrieveStatusResponse, lsp, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_status(self, client: OpencodeSDK) -> None:
        with client.lsp.with_streaming_response.retrieve_status() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lsp = response.parse()
            assert_matches_type(LspRetrieveStatusResponse, lsp, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncLsp:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_status(self, async_client: AsyncOpencodeSDK) -> None:
        lsp = await async_client.lsp.retrieve_status()
        assert_matches_type(LspRetrieveStatusResponse, lsp, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_status_with_all_params(self, async_client: AsyncOpencodeSDK) -> None:
        lsp = await async_client.lsp.retrieve_status(
            directory="directory",
        )
        assert_matches_type(LspRetrieveStatusResponse, lsp, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_status(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.lsp.with_raw_response.retrieve_status()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        lsp = await response.parse()
        assert_matches_type(LspRetrieveStatusResponse, lsp, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_status(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.lsp.with_streaming_response.retrieve_status() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            lsp = await response.parse()
            assert_matches_type(LspRetrieveStatusResponse, lsp, path=["response"])

        assert cast(Any, response.is_closed) is True
