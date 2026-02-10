# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from opencode_sdk import OpencodeSDK, AsyncOpencodeSDK
from opencode_sdk.types import (
    ClientSkillListResponse,
    ClientSkillDeleteResponse,
    ClientSkillUploadResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestClientSkill:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: OpencodeSDK) -> None:
        client_skill = client.client_skill.list()
        assert_matches_type(ClientSkillListResponse, client_skill, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: OpencodeSDK) -> None:
        client_skill = client.client_skill.list(
            directory="directory",
        )
        assert_matches_type(ClientSkillListResponse, client_skill, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: OpencodeSDK) -> None:
        response = client.client_skill.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client_skill = response.parse()
        assert_matches_type(ClientSkillListResponse, client_skill, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: OpencodeSDK) -> None:
        with client.client_skill.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client_skill = response.parse()
            assert_matches_type(ClientSkillListResponse, client_skill, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: OpencodeSDK) -> None:
        client_skill = client.client_skill.delete(
            name="name",
        )
        assert_matches_type(ClientSkillDeleteResponse, client_skill, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete_with_all_params(self, client: OpencodeSDK) -> None:
        client_skill = client.client_skill.delete(
            name="name",
            directory="directory",
        )
        assert_matches_type(ClientSkillDeleteResponse, client_skill, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: OpencodeSDK) -> None:
        response = client.client_skill.with_raw_response.delete(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client_skill = response.parse()
        assert_matches_type(ClientSkillDeleteResponse, client_skill, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: OpencodeSDK) -> None:
        with client.client_skill.with_streaming_response.delete(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client_skill = response.parse()
            assert_matches_type(ClientSkillDeleteResponse, client_skill, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: OpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            client.client_skill.with_raw_response.delete(
                name="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_upload(self, client: OpencodeSDK) -> None:
        client_skill = client.client_skill.upload()
        assert_matches_type(ClientSkillUploadResponse, client_skill, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_upload_with_all_params(self, client: OpencodeSDK) -> None:
        client_skill = client.client_skill.upload(
            directory="directory",
        )
        assert_matches_type(ClientSkillUploadResponse, client_skill, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_upload(self, client: OpencodeSDK) -> None:
        response = client.client_skill.with_raw_response.upload()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client_skill = response.parse()
        assert_matches_type(ClientSkillUploadResponse, client_skill, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_upload(self, client: OpencodeSDK) -> None:
        with client.client_skill.with_streaming_response.upload() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client_skill = response.parse()
            assert_matches_type(ClientSkillUploadResponse, client_skill, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncClientSkill:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncOpencodeSDK) -> None:
        client_skill = await async_client.client_skill.list()
        assert_matches_type(ClientSkillListResponse, client_skill, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncOpencodeSDK) -> None:
        client_skill = await async_client.client_skill.list(
            directory="directory",
        )
        assert_matches_type(ClientSkillListResponse, client_skill, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.client_skill.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client_skill = await response.parse()
        assert_matches_type(ClientSkillListResponse, client_skill, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.client_skill.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client_skill = await response.parse()
            assert_matches_type(ClientSkillListResponse, client_skill, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncOpencodeSDK) -> None:
        client_skill = await async_client.client_skill.delete(
            name="name",
        )
        assert_matches_type(ClientSkillDeleteResponse, client_skill, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncOpencodeSDK) -> None:
        client_skill = await async_client.client_skill.delete(
            name="name",
            directory="directory",
        )
        assert_matches_type(ClientSkillDeleteResponse, client_skill, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.client_skill.with_raw_response.delete(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client_skill = await response.parse()
        assert_matches_type(ClientSkillDeleteResponse, client_skill, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.client_skill.with_streaming_response.delete(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client_skill = await response.parse()
            assert_matches_type(ClientSkillDeleteResponse, client_skill, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncOpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            await async_client.client_skill.with_raw_response.delete(
                name="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_upload(self, async_client: AsyncOpencodeSDK) -> None:
        client_skill = await async_client.client_skill.upload()
        assert_matches_type(ClientSkillUploadResponse, client_skill, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_upload_with_all_params(self, async_client: AsyncOpencodeSDK) -> None:
        client_skill = await async_client.client_skill.upload(
            directory="directory",
        )
        assert_matches_type(ClientSkillUploadResponse, client_skill, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_upload(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.client_skill.with_raw_response.upload()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        client_skill = await response.parse()
        assert_matches_type(ClientSkillUploadResponse, client_skill, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_upload(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.client_skill.with_streaming_response.upload() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            client_skill = await response.parse()
            assert_matches_type(ClientSkillUploadResponse, client_skill, path=["response"])

        assert cast(Any, response.is_closed) is True
