# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from opencode_sdk import OpencodeSDK, AsyncOpencodeSDK
from opencode_sdk.types import GlobalDisposeInstanceResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestGlobal:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_dispose_instance(self, client: OpencodeSDK) -> None:
        global_ = client.global_.dispose_instance()
        assert_matches_type(GlobalDisposeInstanceResponse, global_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_dispose_instance(self, client: OpencodeSDK) -> None:
        response = client.global_.with_raw_response.dispose_instance()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        global_ = response.parse()
        assert_matches_type(GlobalDisposeInstanceResponse, global_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_dispose_instance(self, client: OpencodeSDK) -> None:
        with client.global_.with_streaming_response.dispose_instance() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            global_ = response.parse()
            assert_matches_type(GlobalDisposeInstanceResponse, global_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism doesn't support text/event-stream responses")
    @parametrize
    def test_method_retrieve_events(self, client: OpencodeSDK) -> None:
        global__stream = client.global_.retrieve_events()
        global__stream.response.close()

    @pytest.mark.skip(reason="Prism doesn't support text/event-stream responses")
    @parametrize
    def test_raw_response_retrieve_events(self, client: OpencodeSDK) -> None:
        response = client.global_.with_raw_response.retrieve_events()

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = response.parse()
        stream.close()

    @pytest.mark.skip(reason="Prism doesn't support text/event-stream responses")
    @parametrize
    def test_streaming_response_retrieve_events(self, client: OpencodeSDK) -> None:
        with client.global_.with_streaming_response.retrieve_events() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = response.parse()
            stream.close()

        assert cast(Any, response.is_closed) is True


class TestAsyncGlobal:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_dispose_instance(self, async_client: AsyncOpencodeSDK) -> None:
        global_ = await async_client.global_.dispose_instance()
        assert_matches_type(GlobalDisposeInstanceResponse, global_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_dispose_instance(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.global_.with_raw_response.dispose_instance()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        global_ = await response.parse()
        assert_matches_type(GlobalDisposeInstanceResponse, global_, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_dispose_instance(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.global_.with_streaming_response.dispose_instance() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            global_ = await response.parse()
            assert_matches_type(GlobalDisposeInstanceResponse, global_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism doesn't support text/event-stream responses")
    @parametrize
    async def test_method_retrieve_events(self, async_client: AsyncOpencodeSDK) -> None:
        global__stream = await async_client.global_.retrieve_events()
        await global__stream.response.aclose()

    @pytest.mark.skip(reason="Prism doesn't support text/event-stream responses")
    @parametrize
    async def test_raw_response_retrieve_events(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.global_.with_raw_response.retrieve_events()

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = await response.parse()
        await stream.close()

    @pytest.mark.skip(reason="Prism doesn't support text/event-stream responses")
    @parametrize
    async def test_streaming_response_retrieve_events(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.global_.with_streaming_response.retrieve_events() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = await response.parse()
            await stream.close()

        assert cast(Any, response.is_closed) is True
