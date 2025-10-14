# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from opencode_sdk import OpencodeSDK, AsyncOpencodeSDK
from opencode_sdk.types import LogWriteResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLog:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_write(self, client: OpencodeSDK) -> None:
        log = client.log.write(
            level="debug",
            message="message",
            service="service",
        )
        assert_matches_type(LogWriteResponse, log, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_write_with_all_params(self, client: OpencodeSDK) -> None:
        log = client.log.write(
            level="debug",
            message="message",
            service="service",
            directory="directory",
            extra={"foo": "bar"},
        )
        assert_matches_type(LogWriteResponse, log, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_write(self, client: OpencodeSDK) -> None:
        response = client.log.with_raw_response.write(
            level="debug",
            message="message",
            service="service",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        log = response.parse()
        assert_matches_type(LogWriteResponse, log, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_write(self, client: OpencodeSDK) -> None:
        with client.log.with_streaming_response.write(
            level="debug",
            message="message",
            service="service",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            log = response.parse()
            assert_matches_type(LogWriteResponse, log, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncLog:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_write(self, async_client: AsyncOpencodeSDK) -> None:
        log = await async_client.log.write(
            level="debug",
            message="message",
            service="service",
        )
        assert_matches_type(LogWriteResponse, log, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_write_with_all_params(self, async_client: AsyncOpencodeSDK) -> None:
        log = await async_client.log.write(
            level="debug",
            message="message",
            service="service",
            directory="directory",
            extra={"foo": "bar"},
        )
        assert_matches_type(LogWriteResponse, log, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_write(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.log.with_raw_response.write(
            level="debug",
            message="message",
            service="service",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        log = await response.parse()
        assert_matches_type(LogWriteResponse, log, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_write(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.log.with_streaming_response.write(
            level="debug",
            message="message",
            service="service",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            log = await response.parse()
            assert_matches_type(LogWriteResponse, log, path=["response"])

        assert cast(Any, response.is_closed) is True
