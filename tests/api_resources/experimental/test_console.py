# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from ai4pa_opencode_sdk import OpencodeSDK, AsyncOpencodeSDK
from ai4pa_opencode_sdk.types.experimental import (
    ConsoleListOrgsResponse,
    ConsoleRetrieveResponse,
    ConsoleSwitchOrgResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestConsole:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: OpencodeSDK) -> None:
        console = client.experimental.console.retrieve()
        assert_matches_type(ConsoleRetrieveResponse, console, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: OpencodeSDK) -> None:
        console = client.experimental.console.retrieve(
            directory="directory",
            workspace="workspace",
        )
        assert_matches_type(ConsoleRetrieveResponse, console, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: OpencodeSDK) -> None:
        response = client.experimental.console.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        console = response.parse()
        assert_matches_type(ConsoleRetrieveResponse, console, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: OpencodeSDK) -> None:
        with client.experimental.console.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            console = response.parse()
            assert_matches_type(ConsoleRetrieveResponse, console, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_orgs(self, client: OpencodeSDK) -> None:
        console = client.experimental.console.list_orgs()
        assert_matches_type(ConsoleListOrgsResponse, console, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_orgs_with_all_params(self, client: OpencodeSDK) -> None:
        console = client.experimental.console.list_orgs(
            directory="directory",
            workspace="workspace",
        )
        assert_matches_type(ConsoleListOrgsResponse, console, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_orgs(self, client: OpencodeSDK) -> None:
        response = client.experimental.console.with_raw_response.list_orgs()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        console = response.parse()
        assert_matches_type(ConsoleListOrgsResponse, console, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_orgs(self, client: OpencodeSDK) -> None:
        with client.experimental.console.with_streaming_response.list_orgs() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            console = response.parse()
            assert_matches_type(ConsoleListOrgsResponse, console, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_switch_org(self, client: OpencodeSDK) -> None:
        console = client.experimental.console.switch_org(
            account_id="accountID",
            org_id="orgID",
        )
        assert_matches_type(ConsoleSwitchOrgResponse, console, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_switch_org_with_all_params(self, client: OpencodeSDK) -> None:
        console = client.experimental.console.switch_org(
            account_id="accountID",
            org_id="orgID",
            directory="directory",
            workspace="workspace",
        )
        assert_matches_type(ConsoleSwitchOrgResponse, console, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_switch_org(self, client: OpencodeSDK) -> None:
        response = client.experimental.console.with_raw_response.switch_org(
            account_id="accountID",
            org_id="orgID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        console = response.parse()
        assert_matches_type(ConsoleSwitchOrgResponse, console, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_switch_org(self, client: OpencodeSDK) -> None:
        with client.experimental.console.with_streaming_response.switch_org(
            account_id="accountID",
            org_id="orgID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            console = response.parse()
            assert_matches_type(ConsoleSwitchOrgResponse, console, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncConsole:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncOpencodeSDK) -> None:
        console = await async_client.experimental.console.retrieve()
        assert_matches_type(ConsoleRetrieveResponse, console, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncOpencodeSDK) -> None:
        console = await async_client.experimental.console.retrieve(
            directory="directory",
            workspace="workspace",
        )
        assert_matches_type(ConsoleRetrieveResponse, console, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.experimental.console.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        console = await response.parse()
        assert_matches_type(ConsoleRetrieveResponse, console, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.experimental.console.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            console = await response.parse()
            assert_matches_type(ConsoleRetrieveResponse, console, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_orgs(self, async_client: AsyncOpencodeSDK) -> None:
        console = await async_client.experimental.console.list_orgs()
        assert_matches_type(ConsoleListOrgsResponse, console, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_orgs_with_all_params(self, async_client: AsyncOpencodeSDK) -> None:
        console = await async_client.experimental.console.list_orgs(
            directory="directory",
            workspace="workspace",
        )
        assert_matches_type(ConsoleListOrgsResponse, console, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_orgs(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.experimental.console.with_raw_response.list_orgs()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        console = await response.parse()
        assert_matches_type(ConsoleListOrgsResponse, console, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_orgs(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.experimental.console.with_streaming_response.list_orgs() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            console = await response.parse()
            assert_matches_type(ConsoleListOrgsResponse, console, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_switch_org(self, async_client: AsyncOpencodeSDK) -> None:
        console = await async_client.experimental.console.switch_org(
            account_id="accountID",
            org_id="orgID",
        )
        assert_matches_type(ConsoleSwitchOrgResponse, console, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_switch_org_with_all_params(self, async_client: AsyncOpencodeSDK) -> None:
        console = await async_client.experimental.console.switch_org(
            account_id="accountID",
            org_id="orgID",
            directory="directory",
            workspace="workspace",
        )
        assert_matches_type(ConsoleSwitchOrgResponse, console, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_switch_org(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.experimental.console.with_raw_response.switch_org(
            account_id="accountID",
            org_id="orgID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        console = await response.parse()
        assert_matches_type(ConsoleSwitchOrgResponse, console, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_switch_org(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.experimental.console.with_streaming_response.switch_org(
            account_id="accountID",
            org_id="orgID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            console = await response.parse()
            assert_matches_type(ConsoleSwitchOrgResponse, console, path=["response"])

        assert cast(Any, response.is_closed) is True
