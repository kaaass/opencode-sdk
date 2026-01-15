# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from opencode_sdk import OpencodeSDK, AsyncOpencodeSDK
from opencode_sdk.types import ExperimentalGetResourcesResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestExperimental:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_resources(self, client: OpencodeSDK) -> None:
        experimental = client.experimental.get_resources()
        assert_matches_type(ExperimentalGetResourcesResponse, experimental, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_resources_with_all_params(self, client: OpencodeSDK) -> None:
        experimental = client.experimental.get_resources(
            directory="directory",
        )
        assert_matches_type(ExperimentalGetResourcesResponse, experimental, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_resources(self, client: OpencodeSDK) -> None:
        response = client.experimental.with_raw_response.get_resources()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        experimental = response.parse()
        assert_matches_type(ExperimentalGetResourcesResponse, experimental, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_resources(self, client: OpencodeSDK) -> None:
        with client.experimental.with_streaming_response.get_resources() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            experimental = response.parse()
            assert_matches_type(ExperimentalGetResourcesResponse, experimental, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncExperimental:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_resources(self, async_client: AsyncOpencodeSDK) -> None:
        experimental = await async_client.experimental.get_resources()
        assert_matches_type(ExperimentalGetResourcesResponse, experimental, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_resources_with_all_params(self, async_client: AsyncOpencodeSDK) -> None:
        experimental = await async_client.experimental.get_resources(
            directory="directory",
        )
        assert_matches_type(ExperimentalGetResourcesResponse, experimental, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_resources(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.experimental.with_raw_response.get_resources()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        experimental = await response.parse()
        assert_matches_type(ExperimentalGetResourcesResponse, experimental, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_resources(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.experimental.with_streaming_response.get_resources() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            experimental = await response.parse()
            assert_matches_type(ExperimentalGetResourcesResponse, experimental, path=["response"])

        assert cast(Any, response.is_closed) is True
