# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from opencode_sdk import OpencodeSDK, AsyncOpencodeSDK
from opencode_sdk.types import SessionListResponse
from opencode_sdk.types.session import Session

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSession:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: OpencodeSDK) -> None:
        session = client.session.create()
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: OpencodeSDK) -> None:
        session = client.session.create(
            directory="directory",
            parent_id="sesJ!",
            title="title",
        )
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: OpencodeSDK) -> None:
        response = client.session.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: OpencodeSDK) -> None:
        with client.session.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(Session, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: OpencodeSDK) -> None:
        session = client.session.list()
        assert_matches_type(SessionListResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: OpencodeSDK) -> None:
        session = client.session.list(
            directory="directory",
        )
        assert_matches_type(SessionListResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: OpencodeSDK) -> None:
        response = client.session.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionListResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: OpencodeSDK) -> None:
        with client.session.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(SessionListResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSession:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncOpencodeSDK) -> None:
        session = await async_client.session.create()
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncOpencodeSDK) -> None:
        session = await async_client.session.create(
            directory="directory",
            parent_id="sesJ!",
            title="title",
        )
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.session.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.session.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(Session, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncOpencodeSDK) -> None:
        session = await async_client.session.list()
        assert_matches_type(SessionListResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncOpencodeSDK) -> None:
        session = await async_client.session.list(
            directory="directory",
        )
        assert_matches_type(SessionListResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.session.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(SessionListResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.session.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(SessionListResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True
