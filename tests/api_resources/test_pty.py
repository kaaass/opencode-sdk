# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from opencode_sdk import OpencodeSDK, AsyncOpencodeSDK
from opencode_sdk.types import (
    PtyListResponse,
    PtyCreateResponse,
    PtyDeleteResponse,
    PtyUpdateResponse,
    PtyConnectResponse,
    PtyRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPty:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: OpencodeSDK) -> None:
        pty = client.pty.create()
        assert_matches_type(PtyCreateResponse, pty, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: OpencodeSDK) -> None:
        pty = client.pty.create(
            directory="directory",
            args=["string"],
            command="command",
            cwd="cwd",
            env={"foo": "string"},
            title="title",
        )
        assert_matches_type(PtyCreateResponse, pty, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: OpencodeSDK) -> None:
        response = client.pty.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pty = response.parse()
        assert_matches_type(PtyCreateResponse, pty, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: OpencodeSDK) -> None:
        with client.pty.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pty = response.parse()
            assert_matches_type(PtyCreateResponse, pty, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: OpencodeSDK) -> None:
        pty = client.pty.retrieve(
            pty_id="ptyID",
        )
        assert_matches_type(PtyRetrieveResponse, pty, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: OpencodeSDK) -> None:
        pty = client.pty.retrieve(
            pty_id="ptyID",
            directory="directory",
        )
        assert_matches_type(PtyRetrieveResponse, pty, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: OpencodeSDK) -> None:
        response = client.pty.with_raw_response.retrieve(
            pty_id="ptyID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pty = response.parse()
        assert_matches_type(PtyRetrieveResponse, pty, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: OpencodeSDK) -> None:
        with client.pty.with_streaming_response.retrieve(
            pty_id="ptyID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pty = response.parse()
            assert_matches_type(PtyRetrieveResponse, pty, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: OpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pty_id` but received ''"):
            client.pty.with_raw_response.retrieve(
                pty_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: OpencodeSDK) -> None:
        pty = client.pty.update(
            pty_id="ptyID",
        )
        assert_matches_type(PtyUpdateResponse, pty, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: OpencodeSDK) -> None:
        pty = client.pty.update(
            pty_id="ptyID",
            directory="directory",
            size={
                "cols": 0,
                "rows": 0,
            },
            title="title",
        )
        assert_matches_type(PtyUpdateResponse, pty, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: OpencodeSDK) -> None:
        response = client.pty.with_raw_response.update(
            pty_id="ptyID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pty = response.parse()
        assert_matches_type(PtyUpdateResponse, pty, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: OpencodeSDK) -> None:
        with client.pty.with_streaming_response.update(
            pty_id="ptyID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pty = response.parse()
            assert_matches_type(PtyUpdateResponse, pty, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: OpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pty_id` but received ''"):
            client.pty.with_raw_response.update(
                pty_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: OpencodeSDK) -> None:
        pty = client.pty.list()
        assert_matches_type(PtyListResponse, pty, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: OpencodeSDK) -> None:
        pty = client.pty.list(
            directory="directory",
        )
        assert_matches_type(PtyListResponse, pty, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: OpencodeSDK) -> None:
        response = client.pty.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pty = response.parse()
        assert_matches_type(PtyListResponse, pty, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: OpencodeSDK) -> None:
        with client.pty.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pty = response.parse()
            assert_matches_type(PtyListResponse, pty, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: OpencodeSDK) -> None:
        pty = client.pty.delete(
            pty_id="ptyID",
        )
        assert_matches_type(PtyDeleteResponse, pty, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete_with_all_params(self, client: OpencodeSDK) -> None:
        pty = client.pty.delete(
            pty_id="ptyID",
            directory="directory",
        )
        assert_matches_type(PtyDeleteResponse, pty, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: OpencodeSDK) -> None:
        response = client.pty.with_raw_response.delete(
            pty_id="ptyID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pty = response.parse()
        assert_matches_type(PtyDeleteResponse, pty, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: OpencodeSDK) -> None:
        with client.pty.with_streaming_response.delete(
            pty_id="ptyID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pty = response.parse()
            assert_matches_type(PtyDeleteResponse, pty, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: OpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pty_id` but received ''"):
            client.pty.with_raw_response.delete(
                pty_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_connect(self, client: OpencodeSDK) -> None:
        pty = client.pty.connect(
            pty_id="ptyID",
        )
        assert_matches_type(PtyConnectResponse, pty, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_connect_with_all_params(self, client: OpencodeSDK) -> None:
        pty = client.pty.connect(
            pty_id="ptyID",
            directory="directory",
        )
        assert_matches_type(PtyConnectResponse, pty, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_connect(self, client: OpencodeSDK) -> None:
        response = client.pty.with_raw_response.connect(
            pty_id="ptyID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pty = response.parse()
        assert_matches_type(PtyConnectResponse, pty, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_connect(self, client: OpencodeSDK) -> None:
        with client.pty.with_streaming_response.connect(
            pty_id="ptyID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pty = response.parse()
            assert_matches_type(PtyConnectResponse, pty, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_connect(self, client: OpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pty_id` but received ''"):
            client.pty.with_raw_response.connect(
                pty_id="",
            )


class TestAsyncPty:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncOpencodeSDK) -> None:
        pty = await async_client.pty.create()
        assert_matches_type(PtyCreateResponse, pty, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncOpencodeSDK) -> None:
        pty = await async_client.pty.create(
            directory="directory",
            args=["string"],
            command="command",
            cwd="cwd",
            env={"foo": "string"},
            title="title",
        )
        assert_matches_type(PtyCreateResponse, pty, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.pty.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pty = await response.parse()
        assert_matches_type(PtyCreateResponse, pty, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.pty.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pty = await response.parse()
            assert_matches_type(PtyCreateResponse, pty, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncOpencodeSDK) -> None:
        pty = await async_client.pty.retrieve(
            pty_id="ptyID",
        )
        assert_matches_type(PtyRetrieveResponse, pty, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncOpencodeSDK) -> None:
        pty = await async_client.pty.retrieve(
            pty_id="ptyID",
            directory="directory",
        )
        assert_matches_type(PtyRetrieveResponse, pty, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.pty.with_raw_response.retrieve(
            pty_id="ptyID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pty = await response.parse()
        assert_matches_type(PtyRetrieveResponse, pty, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.pty.with_streaming_response.retrieve(
            pty_id="ptyID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pty = await response.parse()
            assert_matches_type(PtyRetrieveResponse, pty, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncOpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pty_id` but received ''"):
            await async_client.pty.with_raw_response.retrieve(
                pty_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncOpencodeSDK) -> None:
        pty = await async_client.pty.update(
            pty_id="ptyID",
        )
        assert_matches_type(PtyUpdateResponse, pty, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncOpencodeSDK) -> None:
        pty = await async_client.pty.update(
            pty_id="ptyID",
            directory="directory",
            size={
                "cols": 0,
                "rows": 0,
            },
            title="title",
        )
        assert_matches_type(PtyUpdateResponse, pty, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.pty.with_raw_response.update(
            pty_id="ptyID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pty = await response.parse()
        assert_matches_type(PtyUpdateResponse, pty, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.pty.with_streaming_response.update(
            pty_id="ptyID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pty = await response.parse()
            assert_matches_type(PtyUpdateResponse, pty, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncOpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pty_id` but received ''"):
            await async_client.pty.with_raw_response.update(
                pty_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncOpencodeSDK) -> None:
        pty = await async_client.pty.list()
        assert_matches_type(PtyListResponse, pty, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncOpencodeSDK) -> None:
        pty = await async_client.pty.list(
            directory="directory",
        )
        assert_matches_type(PtyListResponse, pty, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.pty.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pty = await response.parse()
        assert_matches_type(PtyListResponse, pty, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.pty.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pty = await response.parse()
            assert_matches_type(PtyListResponse, pty, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncOpencodeSDK) -> None:
        pty = await async_client.pty.delete(
            pty_id="ptyID",
        )
        assert_matches_type(PtyDeleteResponse, pty, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncOpencodeSDK) -> None:
        pty = await async_client.pty.delete(
            pty_id="ptyID",
            directory="directory",
        )
        assert_matches_type(PtyDeleteResponse, pty, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.pty.with_raw_response.delete(
            pty_id="ptyID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pty = await response.parse()
        assert_matches_type(PtyDeleteResponse, pty, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.pty.with_streaming_response.delete(
            pty_id="ptyID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pty = await response.parse()
            assert_matches_type(PtyDeleteResponse, pty, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncOpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pty_id` but received ''"):
            await async_client.pty.with_raw_response.delete(
                pty_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_connect(self, async_client: AsyncOpencodeSDK) -> None:
        pty = await async_client.pty.connect(
            pty_id="ptyID",
        )
        assert_matches_type(PtyConnectResponse, pty, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_connect_with_all_params(self, async_client: AsyncOpencodeSDK) -> None:
        pty = await async_client.pty.connect(
            pty_id="ptyID",
            directory="directory",
        )
        assert_matches_type(PtyConnectResponse, pty, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_connect(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.pty.with_raw_response.connect(
            pty_id="ptyID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pty = await response.parse()
        assert_matches_type(PtyConnectResponse, pty, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_connect(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.pty.with_streaming_response.connect(
            pty_id="ptyID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pty = await response.parse()
            assert_matches_type(PtyConnectResponse, pty, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_connect(self, async_client: AsyncOpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `pty_id` but received ''"):
            await async_client.pty.with_raw_response.connect(
                pty_id="",
            )
