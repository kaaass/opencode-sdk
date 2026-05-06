# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from ai4pa_opencode_sdk import OpencodeSDK, AsyncOpencodeSDK
from ai4pa_opencode_sdk.types.experimental import (
    Workspace,
    WorkspaceListResponse,
    WorkspaceStatusResponse,
    WorkspaceListAdaptorsResponse,
    WorkspaceRestoreSessionResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWorkspace:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: OpencodeSDK) -> None:
        workspace = client.experimental.workspace.create(
            branch="branch",
            extra={},
            type="type",
        )
        assert_matches_type(Workspace, workspace, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: OpencodeSDK) -> None:
        workspace = client.experimental.workspace.create(
            branch="branch",
            extra={},
            type="type",
            directory="directory",
            workspace="workspace",
            id="wrkJ!",
        )
        assert_matches_type(Workspace, workspace, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: OpencodeSDK) -> None:
        response = client.experimental.workspace.with_raw_response.create(
            branch="branch",
            extra={},
            type="type",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workspace = response.parse()
        assert_matches_type(Workspace, workspace, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: OpencodeSDK) -> None:
        with client.experimental.workspace.with_streaming_response.create(
            branch="branch",
            extra={},
            type="type",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workspace = response.parse()
            assert_matches_type(Workspace, workspace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: OpencodeSDK) -> None:
        workspace = client.experimental.workspace.list()
        assert_matches_type(WorkspaceListResponse, workspace, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: OpencodeSDK) -> None:
        workspace = client.experimental.workspace.list(
            directory="directory",
            workspace="workspace",
        )
        assert_matches_type(WorkspaceListResponse, workspace, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: OpencodeSDK) -> None:
        response = client.experimental.workspace.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workspace = response.parse()
        assert_matches_type(WorkspaceListResponse, workspace, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: OpencodeSDK) -> None:
        with client.experimental.workspace.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workspace = response.parse()
            assert_matches_type(WorkspaceListResponse, workspace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_adaptors(self, client: OpencodeSDK) -> None:
        workspace = client.experimental.workspace.list_adaptors()
        assert_matches_type(WorkspaceListAdaptorsResponse, workspace, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_adaptors_with_all_params(self, client: OpencodeSDK) -> None:
        workspace = client.experimental.workspace.list_adaptors(
            directory="directory",
            workspace="workspace",
        )
        assert_matches_type(WorkspaceListAdaptorsResponse, workspace, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_adaptors(self, client: OpencodeSDK) -> None:
        response = client.experimental.workspace.with_raw_response.list_adaptors()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workspace = response.parse()
        assert_matches_type(WorkspaceListAdaptorsResponse, workspace, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_adaptors(self, client: OpencodeSDK) -> None:
        with client.experimental.workspace.with_streaming_response.list_adaptors() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workspace = response.parse()
            assert_matches_type(WorkspaceListAdaptorsResponse, workspace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_remove(self, client: OpencodeSDK) -> None:
        workspace = client.experimental.workspace.remove(
            id="wrkJ!",
        )
        assert_matches_type(Workspace, workspace, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_remove_with_all_params(self, client: OpencodeSDK) -> None:
        workspace = client.experimental.workspace.remove(
            id="wrkJ!",
            directory="directory",
            workspace="workspace",
        )
        assert_matches_type(Workspace, workspace, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_remove(self, client: OpencodeSDK) -> None:
        response = client.experimental.workspace.with_raw_response.remove(
            id="wrkJ!",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workspace = response.parse()
        assert_matches_type(Workspace, workspace, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_remove(self, client: OpencodeSDK) -> None:
        with client.experimental.workspace.with_streaming_response.remove(
            id="wrkJ!",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workspace = response.parse()
            assert_matches_type(Workspace, workspace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_remove(self, client: OpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.experimental.workspace.with_raw_response.remove(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_restore_session(self, client: OpencodeSDK) -> None:
        workspace = client.experimental.workspace.restore_session(
            id="wrkJ!",
            session_id="sessionID",
        )
        assert_matches_type(WorkspaceRestoreSessionResponse, workspace, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_restore_session_with_all_params(self, client: OpencodeSDK) -> None:
        workspace = client.experimental.workspace.restore_session(
            id="wrkJ!",
            session_id="sessionID",
            directory="directory",
            workspace="workspace",
        )
        assert_matches_type(WorkspaceRestoreSessionResponse, workspace, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_restore_session(self, client: OpencodeSDK) -> None:
        response = client.experimental.workspace.with_raw_response.restore_session(
            id="wrkJ!",
            session_id="sessionID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workspace = response.parse()
        assert_matches_type(WorkspaceRestoreSessionResponse, workspace, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_restore_session(self, client: OpencodeSDK) -> None:
        with client.experimental.workspace.with_streaming_response.restore_session(
            id="wrkJ!",
            session_id="sessionID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workspace = response.parse()
            assert_matches_type(WorkspaceRestoreSessionResponse, workspace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_restore_session(self, client: OpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.experimental.workspace.with_raw_response.restore_session(
                id="",
                session_id="sessionID",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_status(self, client: OpencodeSDK) -> None:
        workspace = client.experimental.workspace.status()
        assert_matches_type(WorkspaceStatusResponse, workspace, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_status_with_all_params(self, client: OpencodeSDK) -> None:
        workspace = client.experimental.workspace.status(
            directory="directory",
            workspace="workspace",
        )
        assert_matches_type(WorkspaceStatusResponse, workspace, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_status(self, client: OpencodeSDK) -> None:
        response = client.experimental.workspace.with_raw_response.status()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workspace = response.parse()
        assert_matches_type(WorkspaceStatusResponse, workspace, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_status(self, client: OpencodeSDK) -> None:
        with client.experimental.workspace.with_streaming_response.status() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workspace = response.parse()
            assert_matches_type(WorkspaceStatusResponse, workspace, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncWorkspace:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncOpencodeSDK) -> None:
        workspace = await async_client.experimental.workspace.create(
            branch="branch",
            extra={},
            type="type",
        )
        assert_matches_type(Workspace, workspace, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncOpencodeSDK) -> None:
        workspace = await async_client.experimental.workspace.create(
            branch="branch",
            extra={},
            type="type",
            directory="directory",
            workspace="workspace",
            id="wrkJ!",
        )
        assert_matches_type(Workspace, workspace, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.experimental.workspace.with_raw_response.create(
            branch="branch",
            extra={},
            type="type",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workspace = await response.parse()
        assert_matches_type(Workspace, workspace, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.experimental.workspace.with_streaming_response.create(
            branch="branch",
            extra={},
            type="type",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workspace = await response.parse()
            assert_matches_type(Workspace, workspace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncOpencodeSDK) -> None:
        workspace = await async_client.experimental.workspace.list()
        assert_matches_type(WorkspaceListResponse, workspace, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncOpencodeSDK) -> None:
        workspace = await async_client.experimental.workspace.list(
            directory="directory",
            workspace="workspace",
        )
        assert_matches_type(WorkspaceListResponse, workspace, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.experimental.workspace.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workspace = await response.parse()
        assert_matches_type(WorkspaceListResponse, workspace, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.experimental.workspace.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workspace = await response.parse()
            assert_matches_type(WorkspaceListResponse, workspace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_adaptors(self, async_client: AsyncOpencodeSDK) -> None:
        workspace = await async_client.experimental.workspace.list_adaptors()
        assert_matches_type(WorkspaceListAdaptorsResponse, workspace, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_adaptors_with_all_params(self, async_client: AsyncOpencodeSDK) -> None:
        workspace = await async_client.experimental.workspace.list_adaptors(
            directory="directory",
            workspace="workspace",
        )
        assert_matches_type(WorkspaceListAdaptorsResponse, workspace, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_adaptors(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.experimental.workspace.with_raw_response.list_adaptors()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workspace = await response.parse()
        assert_matches_type(WorkspaceListAdaptorsResponse, workspace, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_adaptors(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.experimental.workspace.with_streaming_response.list_adaptors() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workspace = await response.parse()
            assert_matches_type(WorkspaceListAdaptorsResponse, workspace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_remove(self, async_client: AsyncOpencodeSDK) -> None:
        workspace = await async_client.experimental.workspace.remove(
            id="wrkJ!",
        )
        assert_matches_type(Workspace, workspace, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_remove_with_all_params(self, async_client: AsyncOpencodeSDK) -> None:
        workspace = await async_client.experimental.workspace.remove(
            id="wrkJ!",
            directory="directory",
            workspace="workspace",
        )
        assert_matches_type(Workspace, workspace, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_remove(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.experimental.workspace.with_raw_response.remove(
            id="wrkJ!",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workspace = await response.parse()
        assert_matches_type(Workspace, workspace, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_remove(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.experimental.workspace.with_streaming_response.remove(
            id="wrkJ!",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workspace = await response.parse()
            assert_matches_type(Workspace, workspace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_remove(self, async_client: AsyncOpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.experimental.workspace.with_raw_response.remove(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_restore_session(self, async_client: AsyncOpencodeSDK) -> None:
        workspace = await async_client.experimental.workspace.restore_session(
            id="wrkJ!",
            session_id="sessionID",
        )
        assert_matches_type(WorkspaceRestoreSessionResponse, workspace, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_restore_session_with_all_params(self, async_client: AsyncOpencodeSDK) -> None:
        workspace = await async_client.experimental.workspace.restore_session(
            id="wrkJ!",
            session_id="sessionID",
            directory="directory",
            workspace="workspace",
        )
        assert_matches_type(WorkspaceRestoreSessionResponse, workspace, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_restore_session(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.experimental.workspace.with_raw_response.restore_session(
            id="wrkJ!",
            session_id="sessionID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workspace = await response.parse()
        assert_matches_type(WorkspaceRestoreSessionResponse, workspace, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_restore_session(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.experimental.workspace.with_streaming_response.restore_session(
            id="wrkJ!",
            session_id="sessionID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workspace = await response.parse()
            assert_matches_type(WorkspaceRestoreSessionResponse, workspace, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_restore_session(self, async_client: AsyncOpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.experimental.workspace.with_raw_response.restore_session(
                id="",
                session_id="sessionID",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_status(self, async_client: AsyncOpencodeSDK) -> None:
        workspace = await async_client.experimental.workspace.status()
        assert_matches_type(WorkspaceStatusResponse, workspace, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_status_with_all_params(self, async_client: AsyncOpencodeSDK) -> None:
        workspace = await async_client.experimental.workspace.status(
            directory="directory",
            workspace="workspace",
        )
        assert_matches_type(WorkspaceStatusResponse, workspace, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_status(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.experimental.workspace.with_raw_response.status()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        workspace = await response.parse()
        assert_matches_type(WorkspaceStatusResponse, workspace, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_status(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.experimental.workspace.with_streaming_response.status() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            workspace = await response.parse()
            assert_matches_type(WorkspaceStatusResponse, workspace, path=["response"])

        assert cast(Any, response.is_closed) is True
