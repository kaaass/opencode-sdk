# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from opencode_sdk import OpencodeSDK, AsyncOpencodeSDK
from opencode_sdk.types.tui import (
    ControlGetNextRequestResponse,
    ControlSubmitResponseResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestControl:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_next_request(self, client: OpencodeSDK) -> None:
        control = client.tui.control.get_next_request()
        assert_matches_type(ControlGetNextRequestResponse, control, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_next_request_with_all_params(self, client: OpencodeSDK) -> None:
        control = client.tui.control.get_next_request(
            directory="directory",
        )
        assert_matches_type(ControlGetNextRequestResponse, control, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_next_request(self, client: OpencodeSDK) -> None:
        response = client.tui.control.with_raw_response.get_next_request()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        control = response.parse()
        assert_matches_type(ControlGetNextRequestResponse, control, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_next_request(self, client: OpencodeSDK) -> None:
        with client.tui.control.with_streaming_response.get_next_request() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            control = response.parse()
            assert_matches_type(ControlGetNextRequestResponse, control, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_submit_response(self, client: OpencodeSDK) -> None:
        control = client.tui.control.submit_response()
        assert_matches_type(ControlSubmitResponseResponse, control, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_submit_response_with_all_params(self, client: OpencodeSDK) -> None:
        control = client.tui.control.submit_response(
            directory="directory",
            body={},
        )
        assert_matches_type(ControlSubmitResponseResponse, control, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_submit_response(self, client: OpencodeSDK) -> None:
        response = client.tui.control.with_raw_response.submit_response()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        control = response.parse()
        assert_matches_type(ControlSubmitResponseResponse, control, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_submit_response(self, client: OpencodeSDK) -> None:
        with client.tui.control.with_streaming_response.submit_response() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            control = response.parse()
            assert_matches_type(ControlSubmitResponseResponse, control, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncControl:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_next_request(self, async_client: AsyncOpencodeSDK) -> None:
        control = await async_client.tui.control.get_next_request()
        assert_matches_type(ControlGetNextRequestResponse, control, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_next_request_with_all_params(self, async_client: AsyncOpencodeSDK) -> None:
        control = await async_client.tui.control.get_next_request(
            directory="directory",
        )
        assert_matches_type(ControlGetNextRequestResponse, control, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_next_request(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.tui.control.with_raw_response.get_next_request()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        control = await response.parse()
        assert_matches_type(ControlGetNextRequestResponse, control, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_next_request(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.tui.control.with_streaming_response.get_next_request() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            control = await response.parse()
            assert_matches_type(ControlGetNextRequestResponse, control, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_submit_response(self, async_client: AsyncOpencodeSDK) -> None:
        control = await async_client.tui.control.submit_response()
        assert_matches_type(ControlSubmitResponseResponse, control, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_submit_response_with_all_params(self, async_client: AsyncOpencodeSDK) -> None:
        control = await async_client.tui.control.submit_response(
            directory="directory",
            body={},
        )
        assert_matches_type(ControlSubmitResponseResponse, control, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_submit_response(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.tui.control.with_raw_response.submit_response()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        control = await response.parse()
        assert_matches_type(ControlSubmitResponseResponse, control, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_submit_response(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.tui.control.with_streaming_response.submit_response() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            control = await response.parse()
            assert_matches_type(ControlSubmitResponseResponse, control, path=["response"])

        assert cast(Any, response.is_closed) is True
