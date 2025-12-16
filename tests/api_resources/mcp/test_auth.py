# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from opencode_sdk import OpencodeSDK, AsyncOpencodeSDK
from opencode_sdk.types.mcp import (
    AuthStartResponse,
    AuthRemoveResponse,
    AuthCompleteResponse,
    AuthAuthenticateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAuth:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_authenticate(self, client: OpencodeSDK) -> None:
        auth = client.mcp.auth.authenticate(
            name="name",
        )
        assert_matches_type(AuthAuthenticateResponse, auth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_authenticate_with_all_params(self, client: OpencodeSDK) -> None:
        auth = client.mcp.auth.authenticate(
            name="name",
            directory="directory",
        )
        assert_matches_type(AuthAuthenticateResponse, auth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_authenticate(self, client: OpencodeSDK) -> None:
        response = client.mcp.auth.with_raw_response.authenticate(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = response.parse()
        assert_matches_type(AuthAuthenticateResponse, auth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_authenticate(self, client: OpencodeSDK) -> None:
        with client.mcp.auth.with_streaming_response.authenticate(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = response.parse()
            assert_matches_type(AuthAuthenticateResponse, auth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_authenticate(self, client: OpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            client.mcp.auth.with_raw_response.authenticate(
                name="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_complete(self, client: OpencodeSDK) -> None:
        auth = client.mcp.auth.complete(
            name="name",
            code="code",
        )
        assert_matches_type(AuthCompleteResponse, auth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_complete_with_all_params(self, client: OpencodeSDK) -> None:
        auth = client.mcp.auth.complete(
            name="name",
            code="code",
            directory="directory",
        )
        assert_matches_type(AuthCompleteResponse, auth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_complete(self, client: OpencodeSDK) -> None:
        response = client.mcp.auth.with_raw_response.complete(
            name="name",
            code="code",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = response.parse()
        assert_matches_type(AuthCompleteResponse, auth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_complete(self, client: OpencodeSDK) -> None:
        with client.mcp.auth.with_streaming_response.complete(
            name="name",
            code="code",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = response.parse()
            assert_matches_type(AuthCompleteResponse, auth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_complete(self, client: OpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            client.mcp.auth.with_raw_response.complete(
                name="",
                code="code",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_remove(self, client: OpencodeSDK) -> None:
        auth = client.mcp.auth.remove(
            name="name",
        )
        assert_matches_type(AuthRemoveResponse, auth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_remove_with_all_params(self, client: OpencodeSDK) -> None:
        auth = client.mcp.auth.remove(
            name="name",
            directory="directory",
        )
        assert_matches_type(AuthRemoveResponse, auth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_remove(self, client: OpencodeSDK) -> None:
        response = client.mcp.auth.with_raw_response.remove(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = response.parse()
        assert_matches_type(AuthRemoveResponse, auth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_remove(self, client: OpencodeSDK) -> None:
        with client.mcp.auth.with_streaming_response.remove(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = response.parse()
            assert_matches_type(AuthRemoveResponse, auth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_remove(self, client: OpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            client.mcp.auth.with_raw_response.remove(
                name="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_start(self, client: OpencodeSDK) -> None:
        auth = client.mcp.auth.start(
            name="name",
        )
        assert_matches_type(AuthStartResponse, auth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_start_with_all_params(self, client: OpencodeSDK) -> None:
        auth = client.mcp.auth.start(
            name="name",
            directory="directory",
        )
        assert_matches_type(AuthStartResponse, auth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_start(self, client: OpencodeSDK) -> None:
        response = client.mcp.auth.with_raw_response.start(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = response.parse()
        assert_matches_type(AuthStartResponse, auth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_start(self, client: OpencodeSDK) -> None:
        with client.mcp.auth.with_streaming_response.start(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = response.parse()
            assert_matches_type(AuthStartResponse, auth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_start(self, client: OpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            client.mcp.auth.with_raw_response.start(
                name="",
            )


class TestAsyncAuth:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_authenticate(self, async_client: AsyncOpencodeSDK) -> None:
        auth = await async_client.mcp.auth.authenticate(
            name="name",
        )
        assert_matches_type(AuthAuthenticateResponse, auth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_authenticate_with_all_params(self, async_client: AsyncOpencodeSDK) -> None:
        auth = await async_client.mcp.auth.authenticate(
            name="name",
            directory="directory",
        )
        assert_matches_type(AuthAuthenticateResponse, auth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_authenticate(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.mcp.auth.with_raw_response.authenticate(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = await response.parse()
        assert_matches_type(AuthAuthenticateResponse, auth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_authenticate(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.mcp.auth.with_streaming_response.authenticate(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = await response.parse()
            assert_matches_type(AuthAuthenticateResponse, auth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_authenticate(self, async_client: AsyncOpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            await async_client.mcp.auth.with_raw_response.authenticate(
                name="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_complete(self, async_client: AsyncOpencodeSDK) -> None:
        auth = await async_client.mcp.auth.complete(
            name="name",
            code="code",
        )
        assert_matches_type(AuthCompleteResponse, auth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_complete_with_all_params(self, async_client: AsyncOpencodeSDK) -> None:
        auth = await async_client.mcp.auth.complete(
            name="name",
            code="code",
            directory="directory",
        )
        assert_matches_type(AuthCompleteResponse, auth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_complete(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.mcp.auth.with_raw_response.complete(
            name="name",
            code="code",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = await response.parse()
        assert_matches_type(AuthCompleteResponse, auth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_complete(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.mcp.auth.with_streaming_response.complete(
            name="name",
            code="code",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = await response.parse()
            assert_matches_type(AuthCompleteResponse, auth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_complete(self, async_client: AsyncOpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            await async_client.mcp.auth.with_raw_response.complete(
                name="",
                code="code",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_remove(self, async_client: AsyncOpencodeSDK) -> None:
        auth = await async_client.mcp.auth.remove(
            name="name",
        )
        assert_matches_type(AuthRemoveResponse, auth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_remove_with_all_params(self, async_client: AsyncOpencodeSDK) -> None:
        auth = await async_client.mcp.auth.remove(
            name="name",
            directory="directory",
        )
        assert_matches_type(AuthRemoveResponse, auth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_remove(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.mcp.auth.with_raw_response.remove(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = await response.parse()
        assert_matches_type(AuthRemoveResponse, auth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_remove(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.mcp.auth.with_streaming_response.remove(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = await response.parse()
            assert_matches_type(AuthRemoveResponse, auth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_remove(self, async_client: AsyncOpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            await async_client.mcp.auth.with_raw_response.remove(
                name="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_start(self, async_client: AsyncOpencodeSDK) -> None:
        auth = await async_client.mcp.auth.start(
            name="name",
        )
        assert_matches_type(AuthStartResponse, auth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_start_with_all_params(self, async_client: AsyncOpencodeSDK) -> None:
        auth = await async_client.mcp.auth.start(
            name="name",
            directory="directory",
        )
        assert_matches_type(AuthStartResponse, auth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_start(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.mcp.auth.with_raw_response.start(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = await response.parse()
        assert_matches_type(AuthStartResponse, auth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_start(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.mcp.auth.with_streaming_response.start(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = await response.parse()
            assert_matches_type(AuthStartResponse, auth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_start(self, async_client: AsyncOpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            await async_client.mcp.auth.with_raw_response.start(
                name="",
            )
