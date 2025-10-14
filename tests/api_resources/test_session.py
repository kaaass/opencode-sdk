# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from opencode_sdk import OpencodeSDK, AsyncOpencodeSDK
from opencode_sdk.types import (
    AssistantMessage,
    SessionListResponse,
    SessionAbortResponse,
    SessionDeleteResponse,
    SessionAnalyzeResponse,
    SessionGetTodoResponse,
    SessionSummarizeResponse,
    SessionGetChildrenResponse,
    SessionSendCommandResponse,
    SessionRespondToPermissionResponse,
)
from opencode_sdk.types.session import Session

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSession:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: OpencodeSDK) -> None:
        session = client.session.create()
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: OpencodeSDK) -> None:
        session = client.session.create(
            directory="directory",
            parent_id="sesJ!",
            title="title",
        )
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: OpencodeSDK) -> None:
        response = client.session.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: OpencodeSDK) -> None:
        with client.session.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(Session, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: OpencodeSDK) -> None:
        session = client.session.retrieve(
            id="sesJ!",
        )
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: OpencodeSDK) -> None:
        session = client.session.retrieve(
            id="sesJ!",
            directory="directory",
        )
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: OpencodeSDK) -> None:
        response = client.session.with_raw_response.retrieve(
            id="sesJ!",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: OpencodeSDK) -> None:
        with client.session.with_streaming_response.retrieve(
            id="sesJ!",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(Session, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: OpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.session.with_raw_response.retrieve(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: OpencodeSDK) -> None:
        session = client.session.update(
            id="id",
        )
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: OpencodeSDK) -> None:
        session = client.session.update(
            id="id",
            directory="directory",
            title="title",
        )
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: OpencodeSDK) -> None:
        response = client.session.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: OpencodeSDK) -> None:
        with client.session.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(Session, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: OpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.session.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: OpencodeSDK) -> None:
        session = client.session.list()
        assert_matches_type(SessionListResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: OpencodeSDK) -> None:
        session = client.session.list(
            directory="directory",
        )
        assert_matches_type(SessionListResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: OpencodeSDK) -> None:
        response = client.session.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionListResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: OpencodeSDK) -> None:
        with client.session.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(SessionListResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: OpencodeSDK) -> None:
        session = client.session.delete(
            id="sesJ!",
        )
        assert_matches_type(SessionDeleteResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete_with_all_params(self, client: OpencodeSDK) -> None:
        session = client.session.delete(
            id="sesJ!",
            directory="directory",
        )
        assert_matches_type(SessionDeleteResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: OpencodeSDK) -> None:
        response = client.session.with_raw_response.delete(
            id="sesJ!",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionDeleteResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: OpencodeSDK) -> None:
        with client.session.with_streaming_response.delete(
            id="sesJ!",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(SessionDeleteResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: OpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.session.with_raw_response.delete(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_abort(self, client: OpencodeSDK) -> None:
        session = client.session.abort(
            id="id",
        )
        assert_matches_type(SessionAbortResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_abort_with_all_params(self, client: OpencodeSDK) -> None:
        session = client.session.abort(
            id="id",
            directory="directory",
        )
        assert_matches_type(SessionAbortResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_abort(self, client: OpencodeSDK) -> None:
        response = client.session.with_raw_response.abort(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionAbortResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_abort(self, client: OpencodeSDK) -> None:
        with client.session.with_streaming_response.abort(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(SessionAbortResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_abort(self, client: OpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.session.with_raw_response.abort(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_analyze(self, client: OpencodeSDK) -> None:
        session = client.session.analyze(
            id="id",
            message_id="msgJ!",
            model_id="modelID",
            provider_id="providerID",
        )
        assert_matches_type(SessionAnalyzeResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_analyze_with_all_params(self, client: OpencodeSDK) -> None:
        session = client.session.analyze(
            id="id",
            message_id="msgJ!",
            model_id="modelID",
            provider_id="providerID",
            directory="directory",
        )
        assert_matches_type(SessionAnalyzeResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_analyze(self, client: OpencodeSDK) -> None:
        response = client.session.with_raw_response.analyze(
            id="id",
            message_id="msgJ!",
            model_id="modelID",
            provider_id="providerID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionAnalyzeResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_analyze(self, client: OpencodeSDK) -> None:
        with client.session.with_streaming_response.analyze(
            id="id",
            message_id="msgJ!",
            model_id="modelID",
            provider_id="providerID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(SessionAnalyzeResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_analyze(self, client: OpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.session.with_raw_response.analyze(
                id="",
                message_id="msgJ!",
                model_id="modelID",
                provider_id="providerID",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_fork(self, client: OpencodeSDK) -> None:
        session = client.session.fork(
            id="sesJ!",
        )
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_fork_with_all_params(self, client: OpencodeSDK) -> None:
        session = client.session.fork(
            id="sesJ!",
            directory="directory",
            message_id="msgJ!",
        )
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_fork(self, client: OpencodeSDK) -> None:
        response = client.session.with_raw_response.fork(
            id="sesJ!",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_fork(self, client: OpencodeSDK) -> None:
        with client.session.with_streaming_response.fork(
            id="sesJ!",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(Session, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_fork(self, client: OpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.session.with_raw_response.fork(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_children(self, client: OpencodeSDK) -> None:
        session = client.session.get_children(
            id="sesJ!",
        )
        assert_matches_type(SessionGetChildrenResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_children_with_all_params(self, client: OpencodeSDK) -> None:
        session = client.session.get_children(
            id="sesJ!",
            directory="directory",
        )
        assert_matches_type(SessionGetChildrenResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_children(self, client: OpencodeSDK) -> None:
        response = client.session.with_raw_response.get_children(
            id="sesJ!",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionGetChildrenResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_children(self, client: OpencodeSDK) -> None:
        with client.session.with_streaming_response.get_children(
            id="sesJ!",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(SessionGetChildrenResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_children(self, client: OpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.session.with_raw_response.get_children(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_todo(self, client: OpencodeSDK) -> None:
        session = client.session.get_todo(
            id="id",
        )
        assert_matches_type(SessionGetTodoResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_todo_with_all_params(self, client: OpencodeSDK) -> None:
        session = client.session.get_todo(
            id="id",
            directory="directory",
        )
        assert_matches_type(SessionGetTodoResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_todo(self, client: OpencodeSDK) -> None:
        response = client.session.with_raw_response.get_todo(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionGetTodoResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_todo(self, client: OpencodeSDK) -> None:
        with client.session.with_streaming_response.get_todo(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(SessionGetTodoResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_todo(self, client: OpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.session.with_raw_response.get_todo(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_respond_to_permission(self, client: OpencodeSDK) -> None:
        session = client.session.respond_to_permission(
            permission_id="permissionID",
            id="id",
            response="once",
        )
        assert_matches_type(SessionRespondToPermissionResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_respond_to_permission_with_all_params(self, client: OpencodeSDK) -> None:
        session = client.session.respond_to_permission(
            permission_id="permissionID",
            id="id",
            response="once",
            directory="directory",
        )
        assert_matches_type(SessionRespondToPermissionResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_respond_to_permission(self, client: OpencodeSDK) -> None:
        response = client.session.with_raw_response.respond_to_permission(
            permission_id="permissionID",
            id="id",
            response="once",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionRespondToPermissionResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_respond_to_permission(self, client: OpencodeSDK) -> None:
        with client.session.with_streaming_response.respond_to_permission(
            permission_id="permissionID",
            id="id",
            response="once",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(SessionRespondToPermissionResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_respond_to_permission(self, client: OpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.session.with_raw_response.respond_to_permission(
                permission_id="permissionID",
                id="",
                response="once",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `permission_id` but received ''"):
            client.session.with_raw_response.respond_to_permission(
                permission_id="",
                id="id",
                response="once",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_restore_reverted(self, client: OpencodeSDK) -> None:
        session = client.session.restore_reverted(
            id="id",
        )
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_restore_reverted_with_all_params(self, client: OpencodeSDK) -> None:
        session = client.session.restore_reverted(
            id="id",
            directory="directory",
        )
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_restore_reverted(self, client: OpencodeSDK) -> None:
        response = client.session.with_raw_response.restore_reverted(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_restore_reverted(self, client: OpencodeSDK) -> None:
        with client.session.with_streaming_response.restore_reverted(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(Session, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_restore_reverted(self, client: OpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.session.with_raw_response.restore_reverted(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_revert(self, client: OpencodeSDK) -> None:
        session = client.session.revert(
            id="id",
            message_id="msgJ!",
        )
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_revert_with_all_params(self, client: OpencodeSDK) -> None:
        session = client.session.revert(
            id="id",
            message_id="msgJ!",
            directory="directory",
            part_id="prtJ!",
        )
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_revert(self, client: OpencodeSDK) -> None:
        response = client.session.with_raw_response.revert(
            id="id",
            message_id="msgJ!",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_revert(self, client: OpencodeSDK) -> None:
        with client.session.with_streaming_response.revert(
            id="id",
            message_id="msgJ!",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(Session, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_revert(self, client: OpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.session.with_raw_response.revert(
                id="",
                message_id="msgJ!",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_run_shell(self, client: OpencodeSDK) -> None:
        session = client.session.run_shell(
            id="id",
            agent="agent",
            command="command",
        )
        assert_matches_type(AssistantMessage, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_run_shell_with_all_params(self, client: OpencodeSDK) -> None:
        session = client.session.run_shell(
            id="id",
            agent="agent",
            command="command",
            directory="directory",
        )
        assert_matches_type(AssistantMessage, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_run_shell(self, client: OpencodeSDK) -> None:
        response = client.session.with_raw_response.run_shell(
            id="id",
            agent="agent",
            command="command",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(AssistantMessage, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_run_shell(self, client: OpencodeSDK) -> None:
        with client.session.with_streaming_response.run_shell(
            id="id",
            agent="agent",
            command="command",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(AssistantMessage, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_run_shell(self, client: OpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.session.with_raw_response.run_shell(
                id="",
                agent="agent",
                command="command",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_send_command(self, client: OpencodeSDK) -> None:
        session = client.session.send_command(
            id="id",
            arguments="arguments",
            command="command",
        )
        assert_matches_type(SessionSendCommandResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_send_command_with_all_params(self, client: OpencodeSDK) -> None:
        session = client.session.send_command(
            id="id",
            arguments="arguments",
            command="command",
            directory="directory",
            agent="agent",
            message_id="msgJ!",
            model="model",
        )
        assert_matches_type(SessionSendCommandResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_send_command(self, client: OpencodeSDK) -> None:
        response = client.session.with_raw_response.send_command(
            id="id",
            arguments="arguments",
            command="command",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionSendCommandResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_send_command(self, client: OpencodeSDK) -> None:
        with client.session.with_streaming_response.send_command(
            id="id",
            arguments="arguments",
            command="command",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(SessionSendCommandResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_send_command(self, client: OpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.session.with_raw_response.send_command(
                id="",
                arguments="arguments",
                command="command",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_summarize(self, client: OpencodeSDK) -> None:
        session = client.session.summarize(
            id="id",
            model_id="modelID",
            provider_id="providerID",
        )
        assert_matches_type(SessionSummarizeResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_summarize_with_all_params(self, client: OpencodeSDK) -> None:
        session = client.session.summarize(
            id="id",
            model_id="modelID",
            provider_id="providerID",
            directory="directory",
        )
        assert_matches_type(SessionSummarizeResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_summarize(self, client: OpencodeSDK) -> None:
        response = client.session.with_raw_response.summarize(
            id="id",
            model_id="modelID",
            provider_id="providerID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionSummarizeResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_summarize(self, client: OpencodeSDK) -> None:
        with client.session.with_streaming_response.summarize(
            id="id",
            model_id="modelID",
            provider_id="providerID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(SessionSummarizeResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_summarize(self, client: OpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.session.with_raw_response.summarize(
                id="",
                model_id="modelID",
                provider_id="providerID",
            )


class TestAsyncSession:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncOpencodeSDK) -> None:
        session = await async_client.session.create()
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncOpencodeSDK) -> None:
        session = await async_client.session.create(
            directory="directory",
            parent_id="sesJ!",
            title="title",
        )
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.session.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.session.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(Session, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncOpencodeSDK) -> None:
        session = await async_client.session.retrieve(
            id="sesJ!",
        )
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncOpencodeSDK) -> None:
        session = await async_client.session.retrieve(
            id="sesJ!",
            directory="directory",
        )
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.session.with_raw_response.retrieve(
            id="sesJ!",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.session.with_streaming_response.retrieve(
            id="sesJ!",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(Session, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncOpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.session.with_raw_response.retrieve(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncOpencodeSDK) -> None:
        session = await async_client.session.update(
            id="id",
        )
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncOpencodeSDK) -> None:
        session = await async_client.session.update(
            id="id",
            directory="directory",
            title="title",
        )
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.session.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.session.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(Session, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncOpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.session.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncOpencodeSDK) -> None:
        session = await async_client.session.list()
        assert_matches_type(SessionListResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncOpencodeSDK) -> None:
        session = await async_client.session.list(
            directory="directory",
        )
        assert_matches_type(SessionListResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.session.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(SessionListResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.session.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(SessionListResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncOpencodeSDK) -> None:
        session = await async_client.session.delete(
            id="sesJ!",
        )
        assert_matches_type(SessionDeleteResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncOpencodeSDK) -> None:
        session = await async_client.session.delete(
            id="sesJ!",
            directory="directory",
        )
        assert_matches_type(SessionDeleteResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.session.with_raw_response.delete(
            id="sesJ!",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(SessionDeleteResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.session.with_streaming_response.delete(
            id="sesJ!",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(SessionDeleteResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncOpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.session.with_raw_response.delete(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_abort(self, async_client: AsyncOpencodeSDK) -> None:
        session = await async_client.session.abort(
            id="id",
        )
        assert_matches_type(SessionAbortResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_abort_with_all_params(self, async_client: AsyncOpencodeSDK) -> None:
        session = await async_client.session.abort(
            id="id",
            directory="directory",
        )
        assert_matches_type(SessionAbortResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_abort(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.session.with_raw_response.abort(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(SessionAbortResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_abort(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.session.with_streaming_response.abort(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(SessionAbortResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_abort(self, async_client: AsyncOpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.session.with_raw_response.abort(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_analyze(self, async_client: AsyncOpencodeSDK) -> None:
        session = await async_client.session.analyze(
            id="id",
            message_id="msgJ!",
            model_id="modelID",
            provider_id="providerID",
        )
        assert_matches_type(SessionAnalyzeResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_analyze_with_all_params(self, async_client: AsyncOpencodeSDK) -> None:
        session = await async_client.session.analyze(
            id="id",
            message_id="msgJ!",
            model_id="modelID",
            provider_id="providerID",
            directory="directory",
        )
        assert_matches_type(SessionAnalyzeResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_analyze(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.session.with_raw_response.analyze(
            id="id",
            message_id="msgJ!",
            model_id="modelID",
            provider_id="providerID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(SessionAnalyzeResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_analyze(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.session.with_streaming_response.analyze(
            id="id",
            message_id="msgJ!",
            model_id="modelID",
            provider_id="providerID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(SessionAnalyzeResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_analyze(self, async_client: AsyncOpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.session.with_raw_response.analyze(
                id="",
                message_id="msgJ!",
                model_id="modelID",
                provider_id="providerID",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_fork(self, async_client: AsyncOpencodeSDK) -> None:
        session = await async_client.session.fork(
            id="sesJ!",
        )
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_fork_with_all_params(self, async_client: AsyncOpencodeSDK) -> None:
        session = await async_client.session.fork(
            id="sesJ!",
            directory="directory",
            message_id="msgJ!",
        )
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_fork(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.session.with_raw_response.fork(
            id="sesJ!",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_fork(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.session.with_streaming_response.fork(
            id="sesJ!",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(Session, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_fork(self, async_client: AsyncOpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.session.with_raw_response.fork(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_children(self, async_client: AsyncOpencodeSDK) -> None:
        session = await async_client.session.get_children(
            id="sesJ!",
        )
        assert_matches_type(SessionGetChildrenResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_children_with_all_params(self, async_client: AsyncOpencodeSDK) -> None:
        session = await async_client.session.get_children(
            id="sesJ!",
            directory="directory",
        )
        assert_matches_type(SessionGetChildrenResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_children(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.session.with_raw_response.get_children(
            id="sesJ!",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(SessionGetChildrenResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_children(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.session.with_streaming_response.get_children(
            id="sesJ!",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(SessionGetChildrenResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_children(self, async_client: AsyncOpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.session.with_raw_response.get_children(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_todo(self, async_client: AsyncOpencodeSDK) -> None:
        session = await async_client.session.get_todo(
            id="id",
        )
        assert_matches_type(SessionGetTodoResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_todo_with_all_params(self, async_client: AsyncOpencodeSDK) -> None:
        session = await async_client.session.get_todo(
            id="id",
            directory="directory",
        )
        assert_matches_type(SessionGetTodoResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_todo(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.session.with_raw_response.get_todo(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(SessionGetTodoResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_todo(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.session.with_streaming_response.get_todo(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(SessionGetTodoResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_todo(self, async_client: AsyncOpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.session.with_raw_response.get_todo(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_respond_to_permission(self, async_client: AsyncOpencodeSDK) -> None:
        session = await async_client.session.respond_to_permission(
            permission_id="permissionID",
            id="id",
            response="once",
        )
        assert_matches_type(SessionRespondToPermissionResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_respond_to_permission_with_all_params(self, async_client: AsyncOpencodeSDK) -> None:
        session = await async_client.session.respond_to_permission(
            permission_id="permissionID",
            id="id",
            response="once",
            directory="directory",
        )
        assert_matches_type(SessionRespondToPermissionResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_respond_to_permission(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.session.with_raw_response.respond_to_permission(
            permission_id="permissionID",
            id="id",
            response="once",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(SessionRespondToPermissionResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_respond_to_permission(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.session.with_streaming_response.respond_to_permission(
            permission_id="permissionID",
            id="id",
            response="once",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(SessionRespondToPermissionResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_respond_to_permission(self, async_client: AsyncOpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.session.with_raw_response.respond_to_permission(
                permission_id="permissionID",
                id="",
                response="once",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `permission_id` but received ''"):
            await async_client.session.with_raw_response.respond_to_permission(
                permission_id="",
                id="id",
                response="once",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_restore_reverted(self, async_client: AsyncOpencodeSDK) -> None:
        session = await async_client.session.restore_reverted(
            id="id",
        )
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_restore_reverted_with_all_params(self, async_client: AsyncOpencodeSDK) -> None:
        session = await async_client.session.restore_reverted(
            id="id",
            directory="directory",
        )
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_restore_reverted(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.session.with_raw_response.restore_reverted(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_restore_reverted(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.session.with_streaming_response.restore_reverted(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(Session, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_restore_reverted(self, async_client: AsyncOpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.session.with_raw_response.restore_reverted(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_revert(self, async_client: AsyncOpencodeSDK) -> None:
        session = await async_client.session.revert(
            id="id",
            message_id="msgJ!",
        )
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_revert_with_all_params(self, async_client: AsyncOpencodeSDK) -> None:
        session = await async_client.session.revert(
            id="id",
            message_id="msgJ!",
            directory="directory",
            part_id="prtJ!",
        )
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_revert(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.session.with_raw_response.revert(
            id="id",
            message_id="msgJ!",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_revert(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.session.with_streaming_response.revert(
            id="id",
            message_id="msgJ!",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(Session, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_revert(self, async_client: AsyncOpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.session.with_raw_response.revert(
                id="",
                message_id="msgJ!",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_run_shell(self, async_client: AsyncOpencodeSDK) -> None:
        session = await async_client.session.run_shell(
            id="id",
            agent="agent",
            command="command",
        )
        assert_matches_type(AssistantMessage, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_run_shell_with_all_params(self, async_client: AsyncOpencodeSDK) -> None:
        session = await async_client.session.run_shell(
            id="id",
            agent="agent",
            command="command",
            directory="directory",
        )
        assert_matches_type(AssistantMessage, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_run_shell(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.session.with_raw_response.run_shell(
            id="id",
            agent="agent",
            command="command",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(AssistantMessage, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_run_shell(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.session.with_streaming_response.run_shell(
            id="id",
            agent="agent",
            command="command",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(AssistantMessage, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_run_shell(self, async_client: AsyncOpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.session.with_raw_response.run_shell(
                id="",
                agent="agent",
                command="command",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_send_command(self, async_client: AsyncOpencodeSDK) -> None:
        session = await async_client.session.send_command(
            id="id",
            arguments="arguments",
            command="command",
        )
        assert_matches_type(SessionSendCommandResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_send_command_with_all_params(self, async_client: AsyncOpencodeSDK) -> None:
        session = await async_client.session.send_command(
            id="id",
            arguments="arguments",
            command="command",
            directory="directory",
            agent="agent",
            message_id="msgJ!",
            model="model",
        )
        assert_matches_type(SessionSendCommandResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_send_command(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.session.with_raw_response.send_command(
            id="id",
            arguments="arguments",
            command="command",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(SessionSendCommandResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_send_command(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.session.with_streaming_response.send_command(
            id="id",
            arguments="arguments",
            command="command",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(SessionSendCommandResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_send_command(self, async_client: AsyncOpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.session.with_raw_response.send_command(
                id="",
                arguments="arguments",
                command="command",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_summarize(self, async_client: AsyncOpencodeSDK) -> None:
        session = await async_client.session.summarize(
            id="id",
            model_id="modelID",
            provider_id="providerID",
        )
        assert_matches_type(SessionSummarizeResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_summarize_with_all_params(self, async_client: AsyncOpencodeSDK) -> None:
        session = await async_client.session.summarize(
            id="id",
            model_id="modelID",
            provider_id="providerID",
            directory="directory",
        )
        assert_matches_type(SessionSummarizeResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_summarize(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.session.with_raw_response.summarize(
            id="id",
            model_id="modelID",
            provider_id="providerID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(SessionSummarizeResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_summarize(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.session.with_streaming_response.summarize(
            id="id",
            model_id="modelID",
            provider_id="providerID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(SessionSummarizeResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_summarize(self, async_client: AsyncOpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.session.with_raw_response.summarize(
                id="",
                model_id="modelID",
                provider_id="providerID",
            )
