# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from ai4pa_opencode_sdk import OpencodeSDK, AsyncOpencodeSDK

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAttach:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_attach(self, client: OpencodeSDK) -> None:
        attach = client.session.attach.attach(
            session_id="sessionID",
        )
        assert attach is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_attach_with_all_params(self, client: OpencodeSDK) -> None:
        attach = client.session.attach.attach(
            session_id="sessionID",
            directory="directory",
            workspace="workspace",
        )
        assert attach is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_attach(self, client: OpencodeSDK) -> None:
        response = client.session.attach.with_raw_response.attach(
            session_id="sessionID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attach = response.parse()
        assert attach is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_attach(self, client: OpencodeSDK) -> None:
        with client.session.attach.with_streaming_response.attach(
            session_id="sessionID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attach = response.parse()
            assert attach is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_attach(self, client: OpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.session.attach.with_raw_response.attach(
                session_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_detach(self, client: OpencodeSDK) -> None:
        attach = client.session.attach.detach(
            session_id="sessionID",
        )
        assert attach is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_detach_with_all_params(self, client: OpencodeSDK) -> None:
        attach = client.session.attach.detach(
            session_id="sessionID",
            directory="directory",
            workspace="workspace",
        )
        assert attach is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_detach(self, client: OpencodeSDK) -> None:
        response = client.session.attach.with_raw_response.detach(
            session_id="sessionID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attach = response.parse()
        assert attach is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_detach(self, client: OpencodeSDK) -> None:
        with client.session.attach.with_streaming_response.detach(
            session_id="sessionID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attach = response.parse()
            assert attach is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_detach(self, client: OpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.session.attach.with_raw_response.detach(
                session_id="",
            )


class TestAsyncAttach:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_attach(self, async_client: AsyncOpencodeSDK) -> None:
        attach = await async_client.session.attach.attach(
            session_id="sessionID",
        )
        assert attach is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_attach_with_all_params(self, async_client: AsyncOpencodeSDK) -> None:
        attach = await async_client.session.attach.attach(
            session_id="sessionID",
            directory="directory",
            workspace="workspace",
        )
        assert attach is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_attach(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.session.attach.with_raw_response.attach(
            session_id="sessionID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attach = await response.parse()
        assert attach is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_attach(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.session.attach.with_streaming_response.attach(
            session_id="sessionID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attach = await response.parse()
            assert attach is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_attach(self, async_client: AsyncOpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.session.attach.with_raw_response.attach(
                session_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_detach(self, async_client: AsyncOpencodeSDK) -> None:
        attach = await async_client.session.attach.detach(
            session_id="sessionID",
        )
        assert attach is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_detach_with_all_params(self, async_client: AsyncOpencodeSDK) -> None:
        attach = await async_client.session.attach.detach(
            session_id="sessionID",
            directory="directory",
            workspace="workspace",
        )
        assert attach is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_detach(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.session.attach.with_raw_response.detach(
            session_id="sessionID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        attach = await response.parse()
        assert attach is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_detach(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.session.attach.with_streaming_response.detach(
            session_id="sessionID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            attach = await response.parse()
            assert attach is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_detach(self, async_client: AsyncOpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.session.attach.with_raw_response.detach(
                session_id="",
            )
