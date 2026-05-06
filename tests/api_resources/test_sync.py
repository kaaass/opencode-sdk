# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from ai4pa_opencode_sdk import OpencodeSDK, AsyncOpencodeSDK
from ai4pa_opencode_sdk.types import (
    SyncStartResponse,
    SyncReplayResponse,
    SyncListEventsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSync:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_events(self, client: OpencodeSDK) -> None:
        sync = client.sync.list_events()
        assert_matches_type(SyncListEventsResponse, sync, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_events_with_all_params(self, client: OpencodeSDK) -> None:
        sync = client.sync.list_events(
            directory="directory",
            workspace="workspace",
            body={"foo": 0},
        )
        assert_matches_type(SyncListEventsResponse, sync, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_events(self, client: OpencodeSDK) -> None:
        response = client.sync.with_raw_response.list_events()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sync = response.parse()
        assert_matches_type(SyncListEventsResponse, sync, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_events(self, client: OpencodeSDK) -> None:
        with client.sync.with_streaming_response.list_events() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sync = response.parse()
            assert_matches_type(SyncListEventsResponse, sync, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_replay(self, client: OpencodeSDK) -> None:
        sync = client.sync.replay(
            body_directory="directory",
            events=[
                {
                    "id": "id",
                    "aggregate_id": "aggregateID",
                    "data": {"foo": "bar"},
                    "seq": 0,
                    "type": "type",
                }
            ],
        )
        assert_matches_type(SyncReplayResponse, sync, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_replay_with_all_params(self, client: OpencodeSDK) -> None:
        sync = client.sync.replay(
            body_directory="directory",
            events=[
                {
                    "id": "id",
                    "aggregate_id": "aggregateID",
                    "data": {"foo": "bar"},
                    "seq": 0,
                    "type": "type",
                }
            ],
            query_directory="directory",
            workspace="workspace",
        )
        assert_matches_type(SyncReplayResponse, sync, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_replay(self, client: OpencodeSDK) -> None:
        response = client.sync.with_raw_response.replay(
            body_directory="directory",
            events=[
                {
                    "id": "id",
                    "aggregate_id": "aggregateID",
                    "data": {"foo": "bar"},
                    "seq": 0,
                    "type": "type",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sync = response.parse()
        assert_matches_type(SyncReplayResponse, sync, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_replay(self, client: OpencodeSDK) -> None:
        with client.sync.with_streaming_response.replay(
            body_directory="directory",
            events=[
                {
                    "id": "id",
                    "aggregate_id": "aggregateID",
                    "data": {"foo": "bar"},
                    "seq": 0,
                    "type": "type",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sync = response.parse()
            assert_matches_type(SyncReplayResponse, sync, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_start(self, client: OpencodeSDK) -> None:
        sync = client.sync.start()
        assert_matches_type(SyncStartResponse, sync, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_start_with_all_params(self, client: OpencodeSDK) -> None:
        sync = client.sync.start(
            directory="directory",
            workspace="workspace",
        )
        assert_matches_type(SyncStartResponse, sync, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_start(self, client: OpencodeSDK) -> None:
        response = client.sync.with_raw_response.start()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sync = response.parse()
        assert_matches_type(SyncStartResponse, sync, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_start(self, client: OpencodeSDK) -> None:
        with client.sync.with_streaming_response.start() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sync = response.parse()
            assert_matches_type(SyncStartResponse, sync, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSync:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_events(self, async_client: AsyncOpencodeSDK) -> None:
        sync = await async_client.sync.list_events()
        assert_matches_type(SyncListEventsResponse, sync, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_events_with_all_params(self, async_client: AsyncOpencodeSDK) -> None:
        sync = await async_client.sync.list_events(
            directory="directory",
            workspace="workspace",
            body={"foo": 0},
        )
        assert_matches_type(SyncListEventsResponse, sync, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_events(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.sync.with_raw_response.list_events()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sync = await response.parse()
        assert_matches_type(SyncListEventsResponse, sync, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_events(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.sync.with_streaming_response.list_events() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sync = await response.parse()
            assert_matches_type(SyncListEventsResponse, sync, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_replay(self, async_client: AsyncOpencodeSDK) -> None:
        sync = await async_client.sync.replay(
            body_directory="directory",
            events=[
                {
                    "id": "id",
                    "aggregate_id": "aggregateID",
                    "data": {"foo": "bar"},
                    "seq": 0,
                    "type": "type",
                }
            ],
        )
        assert_matches_type(SyncReplayResponse, sync, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_replay_with_all_params(self, async_client: AsyncOpencodeSDK) -> None:
        sync = await async_client.sync.replay(
            body_directory="directory",
            events=[
                {
                    "id": "id",
                    "aggregate_id": "aggregateID",
                    "data": {"foo": "bar"},
                    "seq": 0,
                    "type": "type",
                }
            ],
            query_directory="directory",
            workspace="workspace",
        )
        assert_matches_type(SyncReplayResponse, sync, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_replay(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.sync.with_raw_response.replay(
            body_directory="directory",
            events=[
                {
                    "id": "id",
                    "aggregate_id": "aggregateID",
                    "data": {"foo": "bar"},
                    "seq": 0,
                    "type": "type",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sync = await response.parse()
        assert_matches_type(SyncReplayResponse, sync, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_replay(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.sync.with_streaming_response.replay(
            body_directory="directory",
            events=[
                {
                    "id": "id",
                    "aggregate_id": "aggregateID",
                    "data": {"foo": "bar"},
                    "seq": 0,
                    "type": "type",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sync = await response.parse()
            assert_matches_type(SyncReplayResponse, sync, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_start(self, async_client: AsyncOpencodeSDK) -> None:
        sync = await async_client.sync.start()
        assert_matches_type(SyncStartResponse, sync, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_start_with_all_params(self, async_client: AsyncOpencodeSDK) -> None:
        sync = await async_client.sync.start(
            directory="directory",
            workspace="workspace",
        )
        assert_matches_type(SyncStartResponse, sync, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_start(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.sync.with_raw_response.start()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sync = await response.parse()
        assert_matches_type(SyncStartResponse, sync, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_start(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.sync.with_streaming_response.start() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sync = await response.parse()
            assert_matches_type(SyncStartResponse, sync, path=["response"])

        assert cast(Any, response.is_closed) is True
