# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from ai4pa_opencode_sdk import OpencodeSDK, AsyncOpencodeSDK
from ai4pa_opencode_sdk.types.mcp import (
    McpStatus,
    AuthStartOAuthResponse,
    AuthRemoveOAuthResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAuth:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_authenticate_oauth(self, client: OpencodeSDK) -> None:
        auth = client.mcp.auth.authenticate_oauth(
            name="name",
        )
        assert_matches_type(McpStatus, auth, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_authenticate_oauth_with_all_params(self, client: OpencodeSDK) -> None:
        auth = client.mcp.auth.authenticate_oauth(
            name="name",
            directory="directory",
            workspace="workspace",
        )
        assert_matches_type(McpStatus, auth, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_authenticate_oauth(self, client: OpencodeSDK) -> None:
        response = client.mcp.auth.with_raw_response.authenticate_oauth(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = response.parse()
        assert_matches_type(McpStatus, auth, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_authenticate_oauth(self, client: OpencodeSDK) -> None:
        with client.mcp.auth.with_streaming_response.authenticate_oauth(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = response.parse()
            assert_matches_type(McpStatus, auth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_authenticate_oauth(self, client: OpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            client.mcp.auth.with_raw_response.authenticate_oauth(
                name="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_complete_oauth(self, client: OpencodeSDK) -> None:
        auth = client.mcp.auth.complete_oauth(
            name="name",
            code="code",
        )
        assert_matches_type(McpStatus, auth, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_complete_oauth_with_all_params(self, client: OpencodeSDK) -> None:
        auth = client.mcp.auth.complete_oauth(
            name="name",
            code="code",
            directory="directory",
            workspace="workspace",
        )
        assert_matches_type(McpStatus, auth, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_complete_oauth(self, client: OpencodeSDK) -> None:
        response = client.mcp.auth.with_raw_response.complete_oauth(
            name="name",
            code="code",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = response.parse()
        assert_matches_type(McpStatus, auth, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_complete_oauth(self, client: OpencodeSDK) -> None:
        with client.mcp.auth.with_streaming_response.complete_oauth(
            name="name",
            code="code",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = response.parse()
            assert_matches_type(McpStatus, auth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_complete_oauth(self, client: OpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            client.mcp.auth.with_raw_response.complete_oauth(
                name="",
                code="code",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_remove_oauth(self, client: OpencodeSDK) -> None:
        auth = client.mcp.auth.remove_oauth(
            name="name",
        )
        assert_matches_type(AuthRemoveOAuthResponse, auth, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_remove_oauth_with_all_params(self, client: OpencodeSDK) -> None:
        auth = client.mcp.auth.remove_oauth(
            name="name",
            directory="directory",
            workspace="workspace",
        )
        assert_matches_type(AuthRemoveOAuthResponse, auth, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_remove_oauth(self, client: OpencodeSDK) -> None:
        response = client.mcp.auth.with_raw_response.remove_oauth(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = response.parse()
        assert_matches_type(AuthRemoveOAuthResponse, auth, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_remove_oauth(self, client: OpencodeSDK) -> None:
        with client.mcp.auth.with_streaming_response.remove_oauth(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = response.parse()
            assert_matches_type(AuthRemoveOAuthResponse, auth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_remove_oauth(self, client: OpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            client.mcp.auth.with_raw_response.remove_oauth(
                name="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_start_oauth(self, client: OpencodeSDK) -> None:
        auth = client.mcp.auth.start_oauth(
            name="name",
        )
        assert_matches_type(AuthStartOAuthResponse, auth, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_start_oauth_with_all_params(self, client: OpencodeSDK) -> None:
        auth = client.mcp.auth.start_oauth(
            name="name",
            directory="directory",
            workspace="workspace",
        )
        assert_matches_type(AuthStartOAuthResponse, auth, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_start_oauth(self, client: OpencodeSDK) -> None:
        response = client.mcp.auth.with_raw_response.start_oauth(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = response.parse()
        assert_matches_type(AuthStartOAuthResponse, auth, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_start_oauth(self, client: OpencodeSDK) -> None:
        with client.mcp.auth.with_streaming_response.start_oauth(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = response.parse()
            assert_matches_type(AuthStartOAuthResponse, auth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_start_oauth(self, client: OpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            client.mcp.auth.with_raw_response.start_oauth(
                name="",
            )


class TestAsyncAuth:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_authenticate_oauth(self, async_client: AsyncOpencodeSDK) -> None:
        auth = await async_client.mcp.auth.authenticate_oauth(
            name="name",
        )
        assert_matches_type(McpStatus, auth, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_authenticate_oauth_with_all_params(self, async_client: AsyncOpencodeSDK) -> None:
        auth = await async_client.mcp.auth.authenticate_oauth(
            name="name",
            directory="directory",
            workspace="workspace",
        )
        assert_matches_type(McpStatus, auth, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_authenticate_oauth(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.mcp.auth.with_raw_response.authenticate_oauth(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = await response.parse()
        assert_matches_type(McpStatus, auth, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_authenticate_oauth(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.mcp.auth.with_streaming_response.authenticate_oauth(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = await response.parse()
            assert_matches_type(McpStatus, auth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_authenticate_oauth(self, async_client: AsyncOpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            await async_client.mcp.auth.with_raw_response.authenticate_oauth(
                name="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_complete_oauth(self, async_client: AsyncOpencodeSDK) -> None:
        auth = await async_client.mcp.auth.complete_oauth(
            name="name",
            code="code",
        )
        assert_matches_type(McpStatus, auth, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_complete_oauth_with_all_params(self, async_client: AsyncOpencodeSDK) -> None:
        auth = await async_client.mcp.auth.complete_oauth(
            name="name",
            code="code",
            directory="directory",
            workspace="workspace",
        )
        assert_matches_type(McpStatus, auth, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_complete_oauth(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.mcp.auth.with_raw_response.complete_oauth(
            name="name",
            code="code",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = await response.parse()
        assert_matches_type(McpStatus, auth, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_complete_oauth(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.mcp.auth.with_streaming_response.complete_oauth(
            name="name",
            code="code",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = await response.parse()
            assert_matches_type(McpStatus, auth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_complete_oauth(self, async_client: AsyncOpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            await async_client.mcp.auth.with_raw_response.complete_oauth(
                name="",
                code="code",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_remove_oauth(self, async_client: AsyncOpencodeSDK) -> None:
        auth = await async_client.mcp.auth.remove_oauth(
            name="name",
        )
        assert_matches_type(AuthRemoveOAuthResponse, auth, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_remove_oauth_with_all_params(self, async_client: AsyncOpencodeSDK) -> None:
        auth = await async_client.mcp.auth.remove_oauth(
            name="name",
            directory="directory",
            workspace="workspace",
        )
        assert_matches_type(AuthRemoveOAuthResponse, auth, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_remove_oauth(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.mcp.auth.with_raw_response.remove_oauth(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = await response.parse()
        assert_matches_type(AuthRemoveOAuthResponse, auth, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_remove_oauth(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.mcp.auth.with_streaming_response.remove_oauth(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = await response.parse()
            assert_matches_type(AuthRemoveOAuthResponse, auth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_remove_oauth(self, async_client: AsyncOpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            await async_client.mcp.auth.with_raw_response.remove_oauth(
                name="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_start_oauth(self, async_client: AsyncOpencodeSDK) -> None:
        auth = await async_client.mcp.auth.start_oauth(
            name="name",
        )
        assert_matches_type(AuthStartOAuthResponse, auth, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_start_oauth_with_all_params(self, async_client: AsyncOpencodeSDK) -> None:
        auth = await async_client.mcp.auth.start_oauth(
            name="name",
            directory="directory",
            workspace="workspace",
        )
        assert_matches_type(AuthStartOAuthResponse, auth, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_start_oauth(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.mcp.auth.with_raw_response.start_oauth(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = await response.parse()
        assert_matches_type(AuthStartOAuthResponse, auth, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_start_oauth(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.mcp.auth.with_streaming_response.start_oauth(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = await response.parse()
            assert_matches_type(AuthStartOAuthResponse, auth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_start_oauth(self, async_client: AsyncOpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            await async_client.mcp.auth.with_raw_response.start_oauth(
                name="",
            )
