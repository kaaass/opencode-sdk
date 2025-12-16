# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from opencode_sdk import OpencodeSDK, AsyncOpencodeSDK
from opencode_sdk.types import VcRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVcs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: OpencodeSDK) -> None:
        vc = client.vcs.retrieve()
        assert_matches_type(VcRetrieveResponse, vc, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: OpencodeSDK) -> None:
        vc = client.vcs.retrieve(
            directory="directory",
        )
        assert_matches_type(VcRetrieveResponse, vc, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: OpencodeSDK) -> None:
        response = client.vcs.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vc = response.parse()
        assert_matches_type(VcRetrieveResponse, vc, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: OpencodeSDK) -> None:
        with client.vcs.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vc = response.parse()
            assert_matches_type(VcRetrieveResponse, vc, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncVcs:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncOpencodeSDK) -> None:
        vc = await async_client.vcs.retrieve()
        assert_matches_type(VcRetrieveResponse, vc, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncOpencodeSDK) -> None:
        vc = await async_client.vcs.retrieve(
            directory="directory",
        )
        assert_matches_type(VcRetrieveResponse, vc, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.vcs.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vc = await response.parse()
        assert_matches_type(VcRetrieveResponse, vc, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.vcs.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vc = await response.parse()
            assert_matches_type(VcRetrieveResponse, vc, path=["response"])

        assert cast(Any, response.is_closed) is True
