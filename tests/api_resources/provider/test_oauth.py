# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from opencode_sdk import OpencodeSDK, AsyncOpencodeSDK
from opencode_sdk.types.provider import (
    OAuthAuthorizeResponse,
    OAuthHandleCallbackResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOAuth:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_authorize(self, client: OpencodeSDK) -> None:
        oauth = client.provider.oauth.authorize(
            provider_id="providerID",
            method=0,
        )
        assert_matches_type(OAuthAuthorizeResponse, oauth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_authorize_with_all_params(self, client: OpencodeSDK) -> None:
        oauth = client.provider.oauth.authorize(
            provider_id="providerID",
            method=0,
            directory="directory",
        )
        assert_matches_type(OAuthAuthorizeResponse, oauth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_authorize(self, client: OpencodeSDK) -> None:
        response = client.provider.oauth.with_raw_response.authorize(
            provider_id="providerID",
            method=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        oauth = response.parse()
        assert_matches_type(OAuthAuthorizeResponse, oauth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_authorize(self, client: OpencodeSDK) -> None:
        with client.provider.oauth.with_streaming_response.authorize(
            provider_id="providerID",
            method=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            oauth = response.parse()
            assert_matches_type(OAuthAuthorizeResponse, oauth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_authorize(self, client: OpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `provider_id` but received ''"):
            client.provider.oauth.with_raw_response.authorize(
                provider_id="",
                method=0,
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_handle_callback(self, client: OpencodeSDK) -> None:
        oauth = client.provider.oauth.handle_callback(
            provider_id="providerID",
            method=0,
        )
        assert_matches_type(OAuthHandleCallbackResponse, oauth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_handle_callback_with_all_params(self, client: OpencodeSDK) -> None:
        oauth = client.provider.oauth.handle_callback(
            provider_id="providerID",
            method=0,
            directory="directory",
            code="code",
        )
        assert_matches_type(OAuthHandleCallbackResponse, oauth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_handle_callback(self, client: OpencodeSDK) -> None:
        response = client.provider.oauth.with_raw_response.handle_callback(
            provider_id="providerID",
            method=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        oauth = response.parse()
        assert_matches_type(OAuthHandleCallbackResponse, oauth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_handle_callback(self, client: OpencodeSDK) -> None:
        with client.provider.oauth.with_streaming_response.handle_callback(
            provider_id="providerID",
            method=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            oauth = response.parse()
            assert_matches_type(OAuthHandleCallbackResponse, oauth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_handle_callback(self, client: OpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `provider_id` but received ''"):
            client.provider.oauth.with_raw_response.handle_callback(
                provider_id="",
                method=0,
            )


class TestAsyncOAuth:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_authorize(self, async_client: AsyncOpencodeSDK) -> None:
        oauth = await async_client.provider.oauth.authorize(
            provider_id="providerID",
            method=0,
        )
        assert_matches_type(OAuthAuthorizeResponse, oauth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_authorize_with_all_params(self, async_client: AsyncOpencodeSDK) -> None:
        oauth = await async_client.provider.oauth.authorize(
            provider_id="providerID",
            method=0,
            directory="directory",
        )
        assert_matches_type(OAuthAuthorizeResponse, oauth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_authorize(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.provider.oauth.with_raw_response.authorize(
            provider_id="providerID",
            method=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        oauth = await response.parse()
        assert_matches_type(OAuthAuthorizeResponse, oauth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_authorize(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.provider.oauth.with_streaming_response.authorize(
            provider_id="providerID",
            method=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            oauth = await response.parse()
            assert_matches_type(OAuthAuthorizeResponse, oauth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_authorize(self, async_client: AsyncOpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `provider_id` but received ''"):
            await async_client.provider.oauth.with_raw_response.authorize(
                provider_id="",
                method=0,
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_handle_callback(self, async_client: AsyncOpencodeSDK) -> None:
        oauth = await async_client.provider.oauth.handle_callback(
            provider_id="providerID",
            method=0,
        )
        assert_matches_type(OAuthHandleCallbackResponse, oauth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_handle_callback_with_all_params(self, async_client: AsyncOpencodeSDK) -> None:
        oauth = await async_client.provider.oauth.handle_callback(
            provider_id="providerID",
            method=0,
            directory="directory",
            code="code",
        )
        assert_matches_type(OAuthHandleCallbackResponse, oauth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_handle_callback(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.provider.oauth.with_raw_response.handle_callback(
            provider_id="providerID",
            method=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        oauth = await response.parse()
        assert_matches_type(OAuthHandleCallbackResponse, oauth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_handle_callback(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.provider.oauth.with_streaming_response.handle_callback(
            provider_id="providerID",
            method=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            oauth = await response.parse()
            assert_matches_type(OAuthHandleCallbackResponse, oauth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_handle_callback(self, async_client: AsyncOpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `provider_id` but received ''"):
            await async_client.provider.oauth.with_raw_response.handle_callback(
                provider_id="",
                method=0,
            )
