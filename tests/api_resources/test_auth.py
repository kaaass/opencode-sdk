# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from opencode_sdk import OpencodeSDK, AsyncOpencodeSDK
from opencode_sdk.types import AuthSetCredentialsResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAuth:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_set_credentials_overload_1(self, client: OpencodeSDK) -> None:
        auth = client.auth.set_credentials(
            provider_id="providerID",
            access="access",
            expires=0,
            refresh="refresh",
            type="oauth",
        )
        assert_matches_type(AuthSetCredentialsResponse, auth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_set_credentials_with_all_params_overload_1(self, client: OpencodeSDK) -> None:
        auth = client.auth.set_credentials(
            provider_id="providerID",
            access="access",
            expires=0,
            refresh="refresh",
            type="oauth",
            directory="directory",
            account_id="accountId",
            enterprise_url="enterpriseUrl",
        )
        assert_matches_type(AuthSetCredentialsResponse, auth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_set_credentials_overload_1(self, client: OpencodeSDK) -> None:
        response = client.auth.with_raw_response.set_credentials(
            provider_id="providerID",
            access="access",
            expires=0,
            refresh="refresh",
            type="oauth",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = response.parse()
        assert_matches_type(AuthSetCredentialsResponse, auth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_set_credentials_overload_1(self, client: OpencodeSDK) -> None:
        with client.auth.with_streaming_response.set_credentials(
            provider_id="providerID",
            access="access",
            expires=0,
            refresh="refresh",
            type="oauth",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = response.parse()
            assert_matches_type(AuthSetCredentialsResponse, auth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_set_credentials_overload_1(self, client: OpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `provider_id` but received ''"):
            client.auth.with_raw_response.set_credentials(
                provider_id="",
                access="access",
                expires=0,
                refresh="refresh",
                type="oauth",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_set_credentials_overload_2(self, client: OpencodeSDK) -> None:
        auth = client.auth.set_credentials(
            provider_id="providerID",
            key="key",
            type="api",
        )
        assert_matches_type(AuthSetCredentialsResponse, auth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_set_credentials_with_all_params_overload_2(self, client: OpencodeSDK) -> None:
        auth = client.auth.set_credentials(
            provider_id="providerID",
            key="key",
            type="api",
            directory="directory",
        )
        assert_matches_type(AuthSetCredentialsResponse, auth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_set_credentials_overload_2(self, client: OpencodeSDK) -> None:
        response = client.auth.with_raw_response.set_credentials(
            provider_id="providerID",
            key="key",
            type="api",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = response.parse()
        assert_matches_type(AuthSetCredentialsResponse, auth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_set_credentials_overload_2(self, client: OpencodeSDK) -> None:
        with client.auth.with_streaming_response.set_credentials(
            provider_id="providerID",
            key="key",
            type="api",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = response.parse()
            assert_matches_type(AuthSetCredentialsResponse, auth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_set_credentials_overload_2(self, client: OpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `provider_id` but received ''"):
            client.auth.with_raw_response.set_credentials(
                provider_id="",
                key="key",
                type="api",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_set_credentials_overload_3(self, client: OpencodeSDK) -> None:
        auth = client.auth.set_credentials(
            provider_id="providerID",
            token="token",
            key="key",
            type="wellknown",
        )
        assert_matches_type(AuthSetCredentialsResponse, auth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_set_credentials_with_all_params_overload_3(self, client: OpencodeSDK) -> None:
        auth = client.auth.set_credentials(
            provider_id="providerID",
            token="token",
            key="key",
            type="wellknown",
            directory="directory",
        )
        assert_matches_type(AuthSetCredentialsResponse, auth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_set_credentials_overload_3(self, client: OpencodeSDK) -> None:
        response = client.auth.with_raw_response.set_credentials(
            provider_id="providerID",
            token="token",
            key="key",
            type="wellknown",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = response.parse()
        assert_matches_type(AuthSetCredentialsResponse, auth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_set_credentials_overload_3(self, client: OpencodeSDK) -> None:
        with client.auth.with_streaming_response.set_credentials(
            provider_id="providerID",
            token="token",
            key="key",
            type="wellknown",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = response.parse()
            assert_matches_type(AuthSetCredentialsResponse, auth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_set_credentials_overload_3(self, client: OpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `provider_id` but received ''"):
            client.auth.with_raw_response.set_credentials(
                provider_id="",
                token="token",
                key="key",
                type="wellknown",
            )


class TestAsyncAuth:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_set_credentials_overload_1(self, async_client: AsyncOpencodeSDK) -> None:
        auth = await async_client.auth.set_credentials(
            provider_id="providerID",
            access="access",
            expires=0,
            refresh="refresh",
            type="oauth",
        )
        assert_matches_type(AuthSetCredentialsResponse, auth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_set_credentials_with_all_params_overload_1(self, async_client: AsyncOpencodeSDK) -> None:
        auth = await async_client.auth.set_credentials(
            provider_id="providerID",
            access="access",
            expires=0,
            refresh="refresh",
            type="oauth",
            directory="directory",
            account_id="accountId",
            enterprise_url="enterpriseUrl",
        )
        assert_matches_type(AuthSetCredentialsResponse, auth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_set_credentials_overload_1(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.auth.with_raw_response.set_credentials(
            provider_id="providerID",
            access="access",
            expires=0,
            refresh="refresh",
            type="oauth",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = await response.parse()
        assert_matches_type(AuthSetCredentialsResponse, auth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_set_credentials_overload_1(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.auth.with_streaming_response.set_credentials(
            provider_id="providerID",
            access="access",
            expires=0,
            refresh="refresh",
            type="oauth",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = await response.parse()
            assert_matches_type(AuthSetCredentialsResponse, auth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_set_credentials_overload_1(self, async_client: AsyncOpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `provider_id` but received ''"):
            await async_client.auth.with_raw_response.set_credentials(
                provider_id="",
                access="access",
                expires=0,
                refresh="refresh",
                type="oauth",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_set_credentials_overload_2(self, async_client: AsyncOpencodeSDK) -> None:
        auth = await async_client.auth.set_credentials(
            provider_id="providerID",
            key="key",
            type="api",
        )
        assert_matches_type(AuthSetCredentialsResponse, auth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_set_credentials_with_all_params_overload_2(self, async_client: AsyncOpencodeSDK) -> None:
        auth = await async_client.auth.set_credentials(
            provider_id="providerID",
            key="key",
            type="api",
            directory="directory",
        )
        assert_matches_type(AuthSetCredentialsResponse, auth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_set_credentials_overload_2(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.auth.with_raw_response.set_credentials(
            provider_id="providerID",
            key="key",
            type="api",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = await response.parse()
        assert_matches_type(AuthSetCredentialsResponse, auth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_set_credentials_overload_2(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.auth.with_streaming_response.set_credentials(
            provider_id="providerID",
            key="key",
            type="api",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = await response.parse()
            assert_matches_type(AuthSetCredentialsResponse, auth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_set_credentials_overload_2(self, async_client: AsyncOpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `provider_id` but received ''"):
            await async_client.auth.with_raw_response.set_credentials(
                provider_id="",
                key="key",
                type="api",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_set_credentials_overload_3(self, async_client: AsyncOpencodeSDK) -> None:
        auth = await async_client.auth.set_credentials(
            provider_id="providerID",
            token="token",
            key="key",
            type="wellknown",
        )
        assert_matches_type(AuthSetCredentialsResponse, auth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_set_credentials_with_all_params_overload_3(self, async_client: AsyncOpencodeSDK) -> None:
        auth = await async_client.auth.set_credentials(
            provider_id="providerID",
            token="token",
            key="key",
            type="wellknown",
            directory="directory",
        )
        assert_matches_type(AuthSetCredentialsResponse, auth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_set_credentials_overload_3(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.auth.with_raw_response.set_credentials(
            provider_id="providerID",
            token="token",
            key="key",
            type="wellknown",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = await response.parse()
        assert_matches_type(AuthSetCredentialsResponse, auth, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_set_credentials_overload_3(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.auth.with_streaming_response.set_credentials(
            provider_id="providerID",
            token="token",
            key="key",
            type="wellknown",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = await response.parse()
            assert_matches_type(AuthSetCredentialsResponse, auth, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_set_credentials_overload_3(self, async_client: AsyncOpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `provider_id` but received ''"):
            await async_client.auth.with_raw_response.set_credentials(
                provider_id="",
                token="token",
                key="key",
                type="wellknown",
            )
