# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from opencode_sdk import OpencodeSDK, AsyncOpencodeSDK
from opencode_sdk.types.session import Session

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestShare:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: OpencodeSDK) -> None:
        share = client.session.share.create(
            id="id",
        )
        assert_matches_type(Session, share, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: OpencodeSDK) -> None:
        share = client.session.share.create(
            id="id",
            directory="directory",
        )
        assert_matches_type(Session, share, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: OpencodeSDK) -> None:
        response = client.session.share.with_raw_response.create(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        share = response.parse()
        assert_matches_type(Session, share, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: OpencodeSDK) -> None:
        with client.session.share.with_streaming_response.create(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            share = response.parse()
            assert_matches_type(Session, share, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_create(self, client: OpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.session.share.with_raw_response.create(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: OpencodeSDK) -> None:
        share = client.session.share.delete(
            id="sesJ!",
        )
        assert_matches_type(Session, share, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete_with_all_params(self, client: OpencodeSDK) -> None:
        share = client.session.share.delete(
            id="sesJ!",
            directory="directory",
        )
        assert_matches_type(Session, share, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: OpencodeSDK) -> None:
        response = client.session.share.with_raw_response.delete(
            id="sesJ!",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        share = response.parse()
        assert_matches_type(Session, share, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: OpencodeSDK) -> None:
        with client.session.share.with_streaming_response.delete(
            id="sesJ!",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            share = response.parse()
            assert_matches_type(Session, share, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: OpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.session.share.with_raw_response.delete(
                id="",
            )


class TestAsyncShare:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncOpencodeSDK) -> None:
        share = await async_client.session.share.create(
            id="id",
        )
        assert_matches_type(Session, share, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncOpencodeSDK) -> None:
        share = await async_client.session.share.create(
            id="id",
            directory="directory",
        )
        assert_matches_type(Session, share, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.session.share.with_raw_response.create(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        share = await response.parse()
        assert_matches_type(Session, share, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.session.share.with_streaming_response.create(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            share = await response.parse()
            assert_matches_type(Session, share, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncOpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.session.share.with_raw_response.create(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncOpencodeSDK) -> None:
        share = await async_client.session.share.delete(
            id="sesJ!",
        )
        assert_matches_type(Session, share, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncOpencodeSDK) -> None:
        share = await async_client.session.share.delete(
            id="sesJ!",
            directory="directory",
        )
        assert_matches_type(Session, share, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.session.share.with_raw_response.delete(
            id="sesJ!",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        share = await response.parse()
        assert_matches_type(Session, share, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.session.share.with_streaming_response.delete(
            id="sesJ!",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            share = await response.parse()
            assert_matches_type(Session, share, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncOpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.session.share.with_raw_response.delete(
                id="",
            )
