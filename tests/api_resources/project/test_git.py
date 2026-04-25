# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from opencode_sdk import OpencodeSDK, AsyncOpencodeSDK
from opencode_sdk.types.project import Project

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestGit:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_initialize(self, client: OpencodeSDK) -> None:
        git = client.project.git.initialize()
        assert_matches_type(Project, git, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_initialize_with_all_params(self, client: OpencodeSDK) -> None:
        git = client.project.git.initialize(
            directory="directory",
            workspace="workspace",
        )
        assert_matches_type(Project, git, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_initialize(self, client: OpencodeSDK) -> None:
        response = client.project.git.with_raw_response.initialize()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        git = response.parse()
        assert_matches_type(Project, git, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_initialize(self, client: OpencodeSDK) -> None:
        with client.project.git.with_streaming_response.initialize() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            git = response.parse()
            assert_matches_type(Project, git, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncGit:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_initialize(self, async_client: AsyncOpencodeSDK) -> None:
        git = await async_client.project.git.initialize()
        assert_matches_type(Project, git, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_initialize_with_all_params(self, async_client: AsyncOpencodeSDK) -> None:
        git = await async_client.project.git.initialize(
            directory="directory",
            workspace="workspace",
        )
        assert_matches_type(Project, git, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_initialize(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.project.git.with_raw_response.initialize()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        git = await response.parse()
        assert_matches_type(Project, git, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_initialize(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.project.git.with_streaming_response.initialize() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            git = await response.parse()
            assert_matches_type(Project, git, path=["response"])

        assert cast(Any, response.is_closed) is True
