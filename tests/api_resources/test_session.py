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
    SessionGetDiffResponse,
    SessionGetTodoResponse,
    SessionGetStatusResponse,
    SessionSummarizeResponse,
    SessionInitializeResponse,
    SessionGetChildrenResponse,
    SessionSendCommandResponse,
    SessionRetrieveStatusResponse,
    SessionSubmitToolResultsResponse,
    SessionRespondToPermissionResponse,
)
from opencode_sdk.types.session import Session

# pyright: reportDeprecated=false

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
            permission=[
                {
                    "action": "allow",
                    "pattern": "pattern",
                    "permission": "permission",
                }
            ],
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
            session_id="sessionID",
        )
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: OpencodeSDK) -> None:
        session = client.session.retrieve(
            session_id="sessionID",
            directory="directory",
        )
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: OpencodeSDK) -> None:
        response = client.session.with_raw_response.retrieve(
            session_id="sessionID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: OpencodeSDK) -> None:
        with client.session.with_streaming_response.retrieve(
            session_id="sessionID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(Session, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: OpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.session.with_raw_response.retrieve(
                session_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: OpencodeSDK) -> None:
        session = client.session.update(
            session_id="sessionID",
        )
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: OpencodeSDK) -> None:
        session = client.session.update(
            session_id="sessionID",
            directory="directory",
            time={"archived": 0},
            title="title",
        )
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: OpencodeSDK) -> None:
        response = client.session.with_raw_response.update(
            session_id="sessionID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: OpencodeSDK) -> None:
        with client.session.with_streaming_response.update(
            session_id="sessionID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(Session, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: OpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.session.with_raw_response.update(
                session_id="",
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
            limit=0,
            search="search",
            start=0,
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
            session_id="sessionID",
        )
        assert_matches_type(SessionDeleteResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete_with_all_params(self, client: OpencodeSDK) -> None:
        session = client.session.delete(
            session_id="sessionID",
            directory="directory",
        )
        assert_matches_type(SessionDeleteResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: OpencodeSDK) -> None:
        response = client.session.with_raw_response.delete(
            session_id="sessionID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionDeleteResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: OpencodeSDK) -> None:
        with client.session.with_streaming_response.delete(
            session_id="sessionID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(SessionDeleteResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: OpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.session.with_raw_response.delete(
                session_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_abort(self, client: OpencodeSDK) -> None:
        session = client.session.abort(
            session_id="sessionID",
        )
        assert_matches_type(SessionAbortResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_abort_with_all_params(self, client: OpencodeSDK) -> None:
        session = client.session.abort(
            session_id="sessionID",
            directory="directory",
        )
        assert_matches_type(SessionAbortResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_abort(self, client: OpencodeSDK) -> None:
        response = client.session.with_raw_response.abort(
            session_id="sessionID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionAbortResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_abort(self, client: OpencodeSDK) -> None:
        with client.session.with_streaming_response.abort(
            session_id="sessionID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(SessionAbortResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_abort(self, client: OpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.session.with_raw_response.abort(
                session_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_fork(self, client: OpencodeSDK) -> None:
        session = client.session.fork(
            session_id="sessionID",
        )
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_fork_with_all_params(self, client: OpencodeSDK) -> None:
        session = client.session.fork(
            session_id="sessionID",
            directory="directory",
            message_id="msgJ!",
        )
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_fork(self, client: OpencodeSDK) -> None:
        response = client.session.with_raw_response.fork(
            session_id="sessionID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_fork(self, client: OpencodeSDK) -> None:
        with client.session.with_streaming_response.fork(
            session_id="sessionID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(Session, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_fork(self, client: OpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.session.with_raw_response.fork(
                session_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_children(self, client: OpencodeSDK) -> None:
        session = client.session.get_children(
            session_id="sessionID",
        )
        assert_matches_type(SessionGetChildrenResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_children_with_all_params(self, client: OpencodeSDK) -> None:
        session = client.session.get_children(
            session_id="sessionID",
            directory="directory",
        )
        assert_matches_type(SessionGetChildrenResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_children(self, client: OpencodeSDK) -> None:
        response = client.session.with_raw_response.get_children(
            session_id="sessionID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionGetChildrenResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_children(self, client: OpencodeSDK) -> None:
        with client.session.with_streaming_response.get_children(
            session_id="sessionID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(SessionGetChildrenResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_children(self, client: OpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.session.with_raw_response.get_children(
                session_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_diff(self, client: OpencodeSDK) -> None:
        session = client.session.get_diff(
            session_id="sessionID",
        )
        assert_matches_type(SessionGetDiffResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_diff_with_all_params(self, client: OpencodeSDK) -> None:
        session = client.session.get_diff(
            session_id="sessionID",
            directory="directory",
            message_id="msgJ!",
        )
        assert_matches_type(SessionGetDiffResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_diff(self, client: OpencodeSDK) -> None:
        response = client.session.with_raw_response.get_diff(
            session_id="sessionID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionGetDiffResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_diff(self, client: OpencodeSDK) -> None:
        with client.session.with_streaming_response.get_diff(
            session_id="sessionID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(SessionGetDiffResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_diff(self, client: OpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.session.with_raw_response.get_diff(
                session_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_status(self, client: OpencodeSDK) -> None:
        session = client.session.get_status()
        assert_matches_type(SessionGetStatusResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_status_with_all_params(self, client: OpencodeSDK) -> None:
        session = client.session.get_status(
            directory="directory",
        )
        assert_matches_type(SessionGetStatusResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_status(self, client: OpencodeSDK) -> None:
        response = client.session.with_raw_response.get_status()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionGetStatusResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_status(self, client: OpencodeSDK) -> None:
        with client.session.with_streaming_response.get_status() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(SessionGetStatusResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_todo(self, client: OpencodeSDK) -> None:
        session = client.session.get_todo(
            session_id="sessionID",
        )
        assert_matches_type(SessionGetTodoResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_todo_with_all_params(self, client: OpencodeSDK) -> None:
        session = client.session.get_todo(
            session_id="sessionID",
            directory="directory",
        )
        assert_matches_type(SessionGetTodoResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_todo(self, client: OpencodeSDK) -> None:
        response = client.session.with_raw_response.get_todo(
            session_id="sessionID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionGetTodoResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_todo(self, client: OpencodeSDK) -> None:
        with client.session.with_streaming_response.get_todo(
            session_id="sessionID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(SessionGetTodoResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_todo(self, client: OpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.session.with_raw_response.get_todo(
                session_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_initialize(self, client: OpencodeSDK) -> None:
        session = client.session.initialize(
            session_id="sessionID",
            message_id="msgJ!",
            model_id="modelID",
            provider_id="providerID",
        )
        assert_matches_type(SessionInitializeResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_initialize_with_all_params(self, client: OpencodeSDK) -> None:
        session = client.session.initialize(
            session_id="sessionID",
            message_id="msgJ!",
            model_id="modelID",
            provider_id="providerID",
            directory="directory",
        )
        assert_matches_type(SessionInitializeResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_initialize(self, client: OpencodeSDK) -> None:
        response = client.session.with_raw_response.initialize(
            session_id="sessionID",
            message_id="msgJ!",
            model_id="modelID",
            provider_id="providerID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionInitializeResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_initialize(self, client: OpencodeSDK) -> None:
        with client.session.with_streaming_response.initialize(
            session_id="sessionID",
            message_id="msgJ!",
            model_id="modelID",
            provider_id="providerID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(SessionInitializeResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_initialize(self, client: OpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.session.with_raw_response.initialize(
                session_id="",
                message_id="msgJ!",
                model_id="modelID",
                provider_id="providerID",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_respond_to_permission(self, client: OpencodeSDK) -> None:
        with pytest.warns(DeprecationWarning):
            session = client.session.respond_to_permission(
                permission_id="permissionID",
                session_id="sessionID",
                response="once",
            )

        assert_matches_type(SessionRespondToPermissionResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_respond_to_permission_with_all_params(self, client: OpencodeSDK) -> None:
        with pytest.warns(DeprecationWarning):
            session = client.session.respond_to_permission(
                permission_id="permissionID",
                session_id="sessionID",
                response="once",
                directory="directory",
            )

        assert_matches_type(SessionRespondToPermissionResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_respond_to_permission(self, client: OpencodeSDK) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.session.with_raw_response.respond_to_permission(
                permission_id="permissionID",
                session_id="sessionID",
                response="once",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionRespondToPermissionResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_respond_to_permission(self, client: OpencodeSDK) -> None:
        with pytest.warns(DeprecationWarning):
            with client.session.with_streaming_response.respond_to_permission(
                permission_id="permissionID",
                session_id="sessionID",
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
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
                client.session.with_raw_response.respond_to_permission(
                    permission_id="permissionID",
                    session_id="",
                    response="once",
                )

            with pytest.raises(ValueError, match=r"Expected a non-empty value for `permission_id` but received ''"):
                client.session.with_raw_response.respond_to_permission(
                    permission_id="",
                    session_id="sessionID",
                    response="once",
                )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_restore_reverted_messages(self, client: OpencodeSDK) -> None:
        session = client.session.restore_reverted_messages(
            session_id="sessionID",
        )
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_restore_reverted_messages_with_all_params(self, client: OpencodeSDK) -> None:
        session = client.session.restore_reverted_messages(
            session_id="sessionID",
            directory="directory",
        )
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_restore_reverted_messages(self, client: OpencodeSDK) -> None:
        response = client.session.with_raw_response.restore_reverted_messages(
            session_id="sessionID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_restore_reverted_messages(self, client: OpencodeSDK) -> None:
        with client.session.with_streaming_response.restore_reverted_messages(
            session_id="sessionID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(Session, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_restore_reverted_messages(self, client: OpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.session.with_raw_response.restore_reverted_messages(
                session_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_status(self, client: OpencodeSDK) -> None:
        session = client.session.retrieve_status(
            session_id="sessionID",
        )
        assert_matches_type(SessionRetrieveStatusResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_status_with_all_params(self, client: OpencodeSDK) -> None:
        session = client.session.retrieve_status(
            session_id="sessionID",
            directory="directory",
        )
        assert_matches_type(SessionRetrieveStatusResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_status(self, client: OpencodeSDK) -> None:
        response = client.session.with_raw_response.retrieve_status(
            session_id="sessionID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionRetrieveStatusResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_status(self, client: OpencodeSDK) -> None:
        with client.session.with_streaming_response.retrieve_status(
            session_id="sessionID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(SessionRetrieveStatusResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve_status(self, client: OpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.session.with_raw_response.retrieve_status(
                session_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_revert_message(self, client: OpencodeSDK) -> None:
        session = client.session.revert_message(
            session_id="sessionID",
            message_id="msgJ!",
        )
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_revert_message_with_all_params(self, client: OpencodeSDK) -> None:
        session = client.session.revert_message(
            session_id="sessionID",
            message_id="msgJ!",
            directory="directory",
            part_id="prtJ!",
        )
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_revert_message(self, client: OpencodeSDK) -> None:
        response = client.session.with_raw_response.revert_message(
            session_id="sessionID",
            message_id="msgJ!",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_revert_message(self, client: OpencodeSDK) -> None:
        with client.session.with_streaming_response.revert_message(
            session_id="sessionID",
            message_id="msgJ!",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(Session, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_revert_message(self, client: OpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.session.with_raw_response.revert_message(
                session_id="",
                message_id="msgJ!",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_run_shell_command(self, client: OpencodeSDK) -> None:
        session = client.session.run_shell_command(
            session_id="sessionID",
            agent="agent",
            command="command",
        )
        assert_matches_type(AssistantMessage, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_run_shell_command_with_all_params(self, client: OpencodeSDK) -> None:
        session = client.session.run_shell_command(
            session_id="sessionID",
            agent="agent",
            command="command",
            directory="directory",
            model={
                "model_id": "modelID",
                "provider_id": "providerID",
            },
        )
        assert_matches_type(AssistantMessage, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_run_shell_command(self, client: OpencodeSDK) -> None:
        response = client.session.with_raw_response.run_shell_command(
            session_id="sessionID",
            agent="agent",
            command="command",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(AssistantMessage, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_run_shell_command(self, client: OpencodeSDK) -> None:
        with client.session.with_streaming_response.run_shell_command(
            session_id="sessionID",
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
    def test_path_params_run_shell_command(self, client: OpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.session.with_raw_response.run_shell_command(
                session_id="",
                agent="agent",
                command="command",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_send_async_message(self, client: OpencodeSDK) -> None:
        session = client.session.send_async_message(
            session_id="sessionID",
            parts=[
                {
                    "text": "text",
                    "type": "text",
                }
            ],
        )
        assert session is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_send_async_message_with_all_params(self, client: OpencodeSDK) -> None:
        session = client.session.send_async_message(
            session_id="sessionID",
            parts=[
                {
                    "text": "text",
                    "type": "text",
                    "id": "id",
                    "ignored": True,
                    "metadata": {"foo": "bar"},
                    "synthetic": True,
                    "time": {
                        "start": 0,
                        "end": 0,
                    },
                }
            ],
            directory="directory",
            agent="agent",
            message_id="msgJ!",
            model={
                "model_id": "modelID",
                "provider_id": "providerID",
            },
            no_reply=True,
            system="system",
            tools={"foo": True},
            variant="variant",
        )
        assert session is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_send_async_message(self, client: OpencodeSDK) -> None:
        response = client.session.with_raw_response.send_async_message(
            session_id="sessionID",
            parts=[
                {
                    "text": "text",
                    "type": "text",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert session is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_send_async_message(self, client: OpencodeSDK) -> None:
        with client.session.with_streaming_response.send_async_message(
            session_id="sessionID",
            parts=[
                {
                    "text": "text",
                    "type": "text",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert session is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_send_async_message(self, client: OpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.session.with_raw_response.send_async_message(
                session_id="",
                parts=[
                    {
                        "text": "text",
                        "type": "text",
                    }
                ],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_send_command(self, client: OpencodeSDK) -> None:
        session = client.session.send_command(
            session_id="sessionID",
            arguments="arguments",
            command="command",
        )
        assert_matches_type(SessionSendCommandResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_send_command_with_all_params(self, client: OpencodeSDK) -> None:
        session = client.session.send_command(
            session_id="sessionID",
            arguments="arguments",
            command="command",
            directory="directory",
            agent="agent",
            message_id="msgJ!",
            model="model",
            parts=[
                {
                    "mime": "mime",
                    "type": "file",
                    "url": "url",
                    "id": "id",
                    "filename": "filename",
                    "source": {
                        "path": "path",
                        "text": {
                            "end": -9007199254740991,
                            "start": -9007199254740991,
                            "value": "value",
                        },
                        "type": "file",
                    },
                }
            ],
            variant="variant",
        )
        assert_matches_type(SessionSendCommandResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_send_command(self, client: OpencodeSDK) -> None:
        response = client.session.with_raw_response.send_command(
            session_id="sessionID",
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
            session_id="sessionID",
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
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.session.with_raw_response.send_command(
                session_id="",
                arguments="arguments",
                command="command",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_submit_tool_results(self, client: OpencodeSDK) -> None:
        session = client.session.submit_tool_results(
            session_id="sessionID",
            results=[
                {
                    "call_id": "callID",
                    "output": "output",
                }
            ],
        )
        assert_matches_type(SessionSubmitToolResultsResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_submit_tool_results_with_all_params(self, client: OpencodeSDK) -> None:
        session = client.session.submit_tool_results(
            session_id="sessionID",
            results=[
                {
                    "call_id": "callID",
                    "output": "output",
                    "attachments": [
                        {
                            "id": "id",
                            "message_id": "messageID",
                            "mime": "mime",
                            "session_id": "sessionID",
                            "type": "file",
                            "url": "url",
                            "filename": "filename",
                            "source": {
                                "path": "path",
                                "text": {
                                    "end": -9007199254740991,
                                    "start": -9007199254740991,
                                    "value": "value",
                                },
                                "type": "file",
                            },
                        }
                    ],
                    "metadata": {"foo": "bar"},
                    "title": "title",
                }
            ],
            directory="directory",
            async_=True,
            continue_loop=True,
        )
        assert_matches_type(SessionSubmitToolResultsResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_submit_tool_results(self, client: OpencodeSDK) -> None:
        response = client.session.with_raw_response.submit_tool_results(
            session_id="sessionID",
            results=[
                {
                    "call_id": "callID",
                    "output": "output",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionSubmitToolResultsResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_submit_tool_results(self, client: OpencodeSDK) -> None:
        with client.session.with_streaming_response.submit_tool_results(
            session_id="sessionID",
            results=[
                {
                    "call_id": "callID",
                    "output": "output",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(SessionSubmitToolResultsResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_submit_tool_results(self, client: OpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.session.with_raw_response.submit_tool_results(
                session_id="",
                results=[
                    {
                        "call_id": "callID",
                        "output": "output",
                    }
                ],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_summarize(self, client: OpencodeSDK) -> None:
        session = client.session.summarize(
            session_id="sessionID",
            model_id="modelID",
            provider_id="providerID",
        )
        assert_matches_type(SessionSummarizeResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_summarize_with_all_params(self, client: OpencodeSDK) -> None:
        session = client.session.summarize(
            session_id="sessionID",
            model_id="modelID",
            provider_id="providerID",
            directory="directory",
            auto=True,
        )
        assert_matches_type(SessionSummarizeResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_summarize(self, client: OpencodeSDK) -> None:
        response = client.session.with_raw_response.summarize(
            session_id="sessionID",
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
            session_id="sessionID",
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
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.session.with_raw_response.summarize(
                session_id="",
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
            permission=[
                {
                    "action": "allow",
                    "pattern": "pattern",
                    "permission": "permission",
                }
            ],
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
            session_id="sessionID",
        )
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncOpencodeSDK) -> None:
        session = await async_client.session.retrieve(
            session_id="sessionID",
            directory="directory",
        )
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.session.with_raw_response.retrieve(
            session_id="sessionID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.session.with_streaming_response.retrieve(
            session_id="sessionID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(Session, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncOpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.session.with_raw_response.retrieve(
                session_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncOpencodeSDK) -> None:
        session = await async_client.session.update(
            session_id="sessionID",
        )
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncOpencodeSDK) -> None:
        session = await async_client.session.update(
            session_id="sessionID",
            directory="directory",
            time={"archived": 0},
            title="title",
        )
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.session.with_raw_response.update(
            session_id="sessionID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.session.with_streaming_response.update(
            session_id="sessionID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(Session, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncOpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.session.with_raw_response.update(
                session_id="",
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
            limit=0,
            search="search",
            start=0,
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
            session_id="sessionID",
        )
        assert_matches_type(SessionDeleteResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncOpencodeSDK) -> None:
        session = await async_client.session.delete(
            session_id="sessionID",
            directory="directory",
        )
        assert_matches_type(SessionDeleteResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.session.with_raw_response.delete(
            session_id="sessionID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(SessionDeleteResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.session.with_streaming_response.delete(
            session_id="sessionID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(SessionDeleteResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncOpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.session.with_raw_response.delete(
                session_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_abort(self, async_client: AsyncOpencodeSDK) -> None:
        session = await async_client.session.abort(
            session_id="sessionID",
        )
        assert_matches_type(SessionAbortResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_abort_with_all_params(self, async_client: AsyncOpencodeSDK) -> None:
        session = await async_client.session.abort(
            session_id="sessionID",
            directory="directory",
        )
        assert_matches_type(SessionAbortResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_abort(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.session.with_raw_response.abort(
            session_id="sessionID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(SessionAbortResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_abort(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.session.with_streaming_response.abort(
            session_id="sessionID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(SessionAbortResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_abort(self, async_client: AsyncOpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.session.with_raw_response.abort(
                session_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_fork(self, async_client: AsyncOpencodeSDK) -> None:
        session = await async_client.session.fork(
            session_id="sessionID",
        )
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_fork_with_all_params(self, async_client: AsyncOpencodeSDK) -> None:
        session = await async_client.session.fork(
            session_id="sessionID",
            directory="directory",
            message_id="msgJ!",
        )
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_fork(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.session.with_raw_response.fork(
            session_id="sessionID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_fork(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.session.with_streaming_response.fork(
            session_id="sessionID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(Session, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_fork(self, async_client: AsyncOpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.session.with_raw_response.fork(
                session_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_children(self, async_client: AsyncOpencodeSDK) -> None:
        session = await async_client.session.get_children(
            session_id="sessionID",
        )
        assert_matches_type(SessionGetChildrenResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_children_with_all_params(self, async_client: AsyncOpencodeSDK) -> None:
        session = await async_client.session.get_children(
            session_id="sessionID",
            directory="directory",
        )
        assert_matches_type(SessionGetChildrenResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_children(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.session.with_raw_response.get_children(
            session_id="sessionID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(SessionGetChildrenResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_children(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.session.with_streaming_response.get_children(
            session_id="sessionID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(SessionGetChildrenResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_children(self, async_client: AsyncOpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.session.with_raw_response.get_children(
                session_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_diff(self, async_client: AsyncOpencodeSDK) -> None:
        session = await async_client.session.get_diff(
            session_id="sessionID",
        )
        assert_matches_type(SessionGetDiffResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_diff_with_all_params(self, async_client: AsyncOpencodeSDK) -> None:
        session = await async_client.session.get_diff(
            session_id="sessionID",
            directory="directory",
            message_id="msgJ!",
        )
        assert_matches_type(SessionGetDiffResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_diff(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.session.with_raw_response.get_diff(
            session_id="sessionID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(SessionGetDiffResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_diff(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.session.with_streaming_response.get_diff(
            session_id="sessionID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(SessionGetDiffResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_diff(self, async_client: AsyncOpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.session.with_raw_response.get_diff(
                session_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_status(self, async_client: AsyncOpencodeSDK) -> None:
        session = await async_client.session.get_status()
        assert_matches_type(SessionGetStatusResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_status_with_all_params(self, async_client: AsyncOpencodeSDK) -> None:
        session = await async_client.session.get_status(
            directory="directory",
        )
        assert_matches_type(SessionGetStatusResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_status(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.session.with_raw_response.get_status()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(SessionGetStatusResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_status(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.session.with_streaming_response.get_status() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(SessionGetStatusResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_todo(self, async_client: AsyncOpencodeSDK) -> None:
        session = await async_client.session.get_todo(
            session_id="sessionID",
        )
        assert_matches_type(SessionGetTodoResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_todo_with_all_params(self, async_client: AsyncOpencodeSDK) -> None:
        session = await async_client.session.get_todo(
            session_id="sessionID",
            directory="directory",
        )
        assert_matches_type(SessionGetTodoResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_todo(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.session.with_raw_response.get_todo(
            session_id="sessionID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(SessionGetTodoResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_todo(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.session.with_streaming_response.get_todo(
            session_id="sessionID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(SessionGetTodoResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_todo(self, async_client: AsyncOpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.session.with_raw_response.get_todo(
                session_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_initialize(self, async_client: AsyncOpencodeSDK) -> None:
        session = await async_client.session.initialize(
            session_id="sessionID",
            message_id="msgJ!",
            model_id="modelID",
            provider_id="providerID",
        )
        assert_matches_type(SessionInitializeResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_initialize_with_all_params(self, async_client: AsyncOpencodeSDK) -> None:
        session = await async_client.session.initialize(
            session_id="sessionID",
            message_id="msgJ!",
            model_id="modelID",
            provider_id="providerID",
            directory="directory",
        )
        assert_matches_type(SessionInitializeResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_initialize(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.session.with_raw_response.initialize(
            session_id="sessionID",
            message_id="msgJ!",
            model_id="modelID",
            provider_id="providerID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(SessionInitializeResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_initialize(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.session.with_streaming_response.initialize(
            session_id="sessionID",
            message_id="msgJ!",
            model_id="modelID",
            provider_id="providerID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(SessionInitializeResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_initialize(self, async_client: AsyncOpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.session.with_raw_response.initialize(
                session_id="",
                message_id="msgJ!",
                model_id="modelID",
                provider_id="providerID",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_respond_to_permission(self, async_client: AsyncOpencodeSDK) -> None:
        with pytest.warns(DeprecationWarning):
            session = await async_client.session.respond_to_permission(
                permission_id="permissionID",
                session_id="sessionID",
                response="once",
            )

        assert_matches_type(SessionRespondToPermissionResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_respond_to_permission_with_all_params(self, async_client: AsyncOpencodeSDK) -> None:
        with pytest.warns(DeprecationWarning):
            session = await async_client.session.respond_to_permission(
                permission_id="permissionID",
                session_id="sessionID",
                response="once",
                directory="directory",
            )

        assert_matches_type(SessionRespondToPermissionResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_respond_to_permission(self, async_client: AsyncOpencodeSDK) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.session.with_raw_response.respond_to_permission(
                permission_id="permissionID",
                session_id="sessionID",
                response="once",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(SessionRespondToPermissionResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_respond_to_permission(self, async_client: AsyncOpencodeSDK) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.session.with_streaming_response.respond_to_permission(
                permission_id="permissionID",
                session_id="sessionID",
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
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
                await async_client.session.with_raw_response.respond_to_permission(
                    permission_id="permissionID",
                    session_id="",
                    response="once",
                )

            with pytest.raises(ValueError, match=r"Expected a non-empty value for `permission_id` but received ''"):
                await async_client.session.with_raw_response.respond_to_permission(
                    permission_id="",
                    session_id="sessionID",
                    response="once",
                )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_restore_reverted_messages(self, async_client: AsyncOpencodeSDK) -> None:
        session = await async_client.session.restore_reverted_messages(
            session_id="sessionID",
        )
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_restore_reverted_messages_with_all_params(self, async_client: AsyncOpencodeSDK) -> None:
        session = await async_client.session.restore_reverted_messages(
            session_id="sessionID",
            directory="directory",
        )
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_restore_reverted_messages(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.session.with_raw_response.restore_reverted_messages(
            session_id="sessionID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_restore_reverted_messages(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.session.with_streaming_response.restore_reverted_messages(
            session_id="sessionID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(Session, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_restore_reverted_messages(self, async_client: AsyncOpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.session.with_raw_response.restore_reverted_messages(
                session_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_status(self, async_client: AsyncOpencodeSDK) -> None:
        session = await async_client.session.retrieve_status(
            session_id="sessionID",
        )
        assert_matches_type(SessionRetrieveStatusResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_status_with_all_params(self, async_client: AsyncOpencodeSDK) -> None:
        session = await async_client.session.retrieve_status(
            session_id="sessionID",
            directory="directory",
        )
        assert_matches_type(SessionRetrieveStatusResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_status(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.session.with_raw_response.retrieve_status(
            session_id="sessionID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(SessionRetrieveStatusResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_status(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.session.with_streaming_response.retrieve_status(
            session_id="sessionID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(SessionRetrieveStatusResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve_status(self, async_client: AsyncOpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.session.with_raw_response.retrieve_status(
                session_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_revert_message(self, async_client: AsyncOpencodeSDK) -> None:
        session = await async_client.session.revert_message(
            session_id="sessionID",
            message_id="msgJ!",
        )
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_revert_message_with_all_params(self, async_client: AsyncOpencodeSDK) -> None:
        session = await async_client.session.revert_message(
            session_id="sessionID",
            message_id="msgJ!",
            directory="directory",
            part_id="prtJ!",
        )
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_revert_message(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.session.with_raw_response.revert_message(
            session_id="sessionID",
            message_id="msgJ!",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(Session, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_revert_message(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.session.with_streaming_response.revert_message(
            session_id="sessionID",
            message_id="msgJ!",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(Session, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_revert_message(self, async_client: AsyncOpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.session.with_raw_response.revert_message(
                session_id="",
                message_id="msgJ!",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_run_shell_command(self, async_client: AsyncOpencodeSDK) -> None:
        session = await async_client.session.run_shell_command(
            session_id="sessionID",
            agent="agent",
            command="command",
        )
        assert_matches_type(AssistantMessage, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_run_shell_command_with_all_params(self, async_client: AsyncOpencodeSDK) -> None:
        session = await async_client.session.run_shell_command(
            session_id="sessionID",
            agent="agent",
            command="command",
            directory="directory",
            model={
                "model_id": "modelID",
                "provider_id": "providerID",
            },
        )
        assert_matches_type(AssistantMessage, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_run_shell_command(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.session.with_raw_response.run_shell_command(
            session_id="sessionID",
            agent="agent",
            command="command",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(AssistantMessage, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_run_shell_command(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.session.with_streaming_response.run_shell_command(
            session_id="sessionID",
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
    async def test_path_params_run_shell_command(self, async_client: AsyncOpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.session.with_raw_response.run_shell_command(
                session_id="",
                agent="agent",
                command="command",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_send_async_message(self, async_client: AsyncOpencodeSDK) -> None:
        session = await async_client.session.send_async_message(
            session_id="sessionID",
            parts=[
                {
                    "text": "text",
                    "type": "text",
                }
            ],
        )
        assert session is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_send_async_message_with_all_params(self, async_client: AsyncOpencodeSDK) -> None:
        session = await async_client.session.send_async_message(
            session_id="sessionID",
            parts=[
                {
                    "text": "text",
                    "type": "text",
                    "id": "id",
                    "ignored": True,
                    "metadata": {"foo": "bar"},
                    "synthetic": True,
                    "time": {
                        "start": 0,
                        "end": 0,
                    },
                }
            ],
            directory="directory",
            agent="agent",
            message_id="msgJ!",
            model={
                "model_id": "modelID",
                "provider_id": "providerID",
            },
            no_reply=True,
            system="system",
            tools={"foo": True},
            variant="variant",
        )
        assert session is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_send_async_message(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.session.with_raw_response.send_async_message(
            session_id="sessionID",
            parts=[
                {
                    "text": "text",
                    "type": "text",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert session is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_send_async_message(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.session.with_streaming_response.send_async_message(
            session_id="sessionID",
            parts=[
                {
                    "text": "text",
                    "type": "text",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert session is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_send_async_message(self, async_client: AsyncOpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.session.with_raw_response.send_async_message(
                session_id="",
                parts=[
                    {
                        "text": "text",
                        "type": "text",
                    }
                ],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_send_command(self, async_client: AsyncOpencodeSDK) -> None:
        session = await async_client.session.send_command(
            session_id="sessionID",
            arguments="arguments",
            command="command",
        )
        assert_matches_type(SessionSendCommandResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_send_command_with_all_params(self, async_client: AsyncOpencodeSDK) -> None:
        session = await async_client.session.send_command(
            session_id="sessionID",
            arguments="arguments",
            command="command",
            directory="directory",
            agent="agent",
            message_id="msgJ!",
            model="model",
            parts=[
                {
                    "mime": "mime",
                    "type": "file",
                    "url": "url",
                    "id": "id",
                    "filename": "filename",
                    "source": {
                        "path": "path",
                        "text": {
                            "end": -9007199254740991,
                            "start": -9007199254740991,
                            "value": "value",
                        },
                        "type": "file",
                    },
                }
            ],
            variant="variant",
        )
        assert_matches_type(SessionSendCommandResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_send_command(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.session.with_raw_response.send_command(
            session_id="sessionID",
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
            session_id="sessionID",
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
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.session.with_raw_response.send_command(
                session_id="",
                arguments="arguments",
                command="command",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_submit_tool_results(self, async_client: AsyncOpencodeSDK) -> None:
        session = await async_client.session.submit_tool_results(
            session_id="sessionID",
            results=[
                {
                    "call_id": "callID",
                    "output": "output",
                }
            ],
        )
        assert_matches_type(SessionSubmitToolResultsResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_submit_tool_results_with_all_params(self, async_client: AsyncOpencodeSDK) -> None:
        session = await async_client.session.submit_tool_results(
            session_id="sessionID",
            results=[
                {
                    "call_id": "callID",
                    "output": "output",
                    "attachments": [
                        {
                            "id": "id",
                            "message_id": "messageID",
                            "mime": "mime",
                            "session_id": "sessionID",
                            "type": "file",
                            "url": "url",
                            "filename": "filename",
                            "source": {
                                "path": "path",
                                "text": {
                                    "end": -9007199254740991,
                                    "start": -9007199254740991,
                                    "value": "value",
                                },
                                "type": "file",
                            },
                        }
                    ],
                    "metadata": {"foo": "bar"},
                    "title": "title",
                }
            ],
            directory="directory",
            async_=True,
            continue_loop=True,
        )
        assert_matches_type(SessionSubmitToolResultsResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_submit_tool_results(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.session.with_raw_response.submit_tool_results(
            session_id="sessionID",
            results=[
                {
                    "call_id": "callID",
                    "output": "output",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(SessionSubmitToolResultsResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_submit_tool_results(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.session.with_streaming_response.submit_tool_results(
            session_id="sessionID",
            results=[
                {
                    "call_id": "callID",
                    "output": "output",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(SessionSubmitToolResultsResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_submit_tool_results(self, async_client: AsyncOpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.session.with_raw_response.submit_tool_results(
                session_id="",
                results=[
                    {
                        "call_id": "callID",
                        "output": "output",
                    }
                ],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_summarize(self, async_client: AsyncOpencodeSDK) -> None:
        session = await async_client.session.summarize(
            session_id="sessionID",
            model_id="modelID",
            provider_id="providerID",
        )
        assert_matches_type(SessionSummarizeResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_summarize_with_all_params(self, async_client: AsyncOpencodeSDK) -> None:
        session = await async_client.session.summarize(
            session_id="sessionID",
            model_id="modelID",
            provider_id="providerID",
            directory="directory",
            auto=True,
        )
        assert_matches_type(SessionSummarizeResponse, session, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_summarize(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.session.with_raw_response.summarize(
            session_id="sessionID",
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
            session_id="sessionID",
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
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.session.with_raw_response.summarize(
                session_id="",
                model_id="modelID",
                provider_id="providerID",
            )
