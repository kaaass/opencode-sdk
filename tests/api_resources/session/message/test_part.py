# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from opencode_sdk import OpencodeSDK, AsyncOpencodeSDK
from opencode_sdk.types.session import Part
from opencode_sdk.types.session.message import PartDeleteResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPart:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_overload_1(self, client: OpencodeSDK) -> None:
        part = client.session.message.part.update(
            part_id="partID",
            path_session_id="sessionID",
            path_message_id="messageID",
            id="id",
            body_message_id="messageID",
            body_session_id="sessionID",
            text="text",
            type="text",
        )
        assert_matches_type(Part, part, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params_overload_1(self, client: OpencodeSDK) -> None:
        part = client.session.message.part.update(
            part_id="partID",
            path_session_id="sessionID",
            path_message_id="messageID",
            id="id",
            body_message_id="messageID",
            body_session_id="sessionID",
            text="text",
            type="text",
            directory="directory",
            ignored=True,
            metadata={"foo": "bar"},
            synthetic=True,
            time={
                "start": 0,
                "end": 0,
            },
        )
        assert_matches_type(Part, part, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_overload_1(self, client: OpencodeSDK) -> None:
        response = client.session.message.part.with_raw_response.update(
            part_id="partID",
            path_session_id="sessionID",
            path_message_id="messageID",
            id="id",
            body_message_id="messageID",
            body_session_id="sessionID",
            text="text",
            type="text",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        part = response.parse()
        assert_matches_type(Part, part, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_overload_1(self, client: OpencodeSDK) -> None:
        with client.session.message.part.with_streaming_response.update(
            part_id="partID",
            path_session_id="sessionID",
            path_message_id="messageID",
            id="id",
            body_message_id="messageID",
            body_session_id="sessionID",
            text="text",
            type="text",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            part = response.parse()
            assert_matches_type(Part, part, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update_overload_1(self, client: OpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_session_id` but received ''"):
            client.session.message.part.with_raw_response.update(
                part_id="partID",
                path_session_id="",
                path_message_id="messageID",
                id="id",
                body_message_id="messageID",
                body_session_id="sessionID",
                text="text",
                type="text",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_message_id` but received ''"):
            client.session.message.part.with_raw_response.update(
                part_id="partID",
                path_session_id="sessionID",
                path_message_id="",
                id="id",
                body_message_id="messageID",
                body_session_id="sessionID",
                text="text",
                type="text",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `part_id` but received ''"):
            client.session.message.part.with_raw_response.update(
                part_id="",
                path_session_id="sessionID",
                path_message_id="messageID",
                id="id",
                body_message_id="messageID",
                body_session_id="sessionID",
                text="text",
                type="text",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_overload_2(self, client: OpencodeSDK) -> None:
        part = client.session.message.part.update(
            part_id="partID",
            path_session_id="sessionID",
            path_message_id="messageID",
            id="id",
            agent="agent",
            description="description",
            body_message_id="messageID",
            prompt="prompt",
            body_session_id="sessionID",
            type="subtask",
        )
        assert_matches_type(Part, part, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params_overload_2(self, client: OpencodeSDK) -> None:
        part = client.session.message.part.update(
            part_id="partID",
            path_session_id="sessionID",
            path_message_id="messageID",
            id="id",
            agent="agent",
            description="description",
            body_message_id="messageID",
            prompt="prompt",
            body_session_id="sessionID",
            type="subtask",
            directory="directory",
            command="command",
        )
        assert_matches_type(Part, part, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_overload_2(self, client: OpencodeSDK) -> None:
        response = client.session.message.part.with_raw_response.update(
            part_id="partID",
            path_session_id="sessionID",
            path_message_id="messageID",
            id="id",
            agent="agent",
            description="description",
            body_message_id="messageID",
            prompt="prompt",
            body_session_id="sessionID",
            type="subtask",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        part = response.parse()
        assert_matches_type(Part, part, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_overload_2(self, client: OpencodeSDK) -> None:
        with client.session.message.part.with_streaming_response.update(
            part_id="partID",
            path_session_id="sessionID",
            path_message_id="messageID",
            id="id",
            agent="agent",
            description="description",
            body_message_id="messageID",
            prompt="prompt",
            body_session_id="sessionID",
            type="subtask",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            part = response.parse()
            assert_matches_type(Part, part, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update_overload_2(self, client: OpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_session_id` but received ''"):
            client.session.message.part.with_raw_response.update(
                part_id="partID",
                path_session_id="",
                path_message_id="messageID",
                id="id",
                agent="agent",
                description="description",
                body_message_id="messageID",
                prompt="prompt",
                body_session_id="sessionID",
                type="subtask",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_message_id` but received ''"):
            client.session.message.part.with_raw_response.update(
                part_id="partID",
                path_session_id="sessionID",
                path_message_id="",
                id="id",
                agent="agent",
                description="description",
                body_message_id="messageID",
                prompt="prompt",
                body_session_id="sessionID",
                type="subtask",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `part_id` but received ''"):
            client.session.message.part.with_raw_response.update(
                part_id="",
                path_session_id="sessionID",
                path_message_id="messageID",
                id="id",
                agent="agent",
                description="description",
                body_message_id="messageID",
                prompt="prompt",
                body_session_id="sessionID",
                type="subtask",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_overload_3(self, client: OpencodeSDK) -> None:
        part = client.session.message.part.update(
            part_id="partID",
            path_session_id="sessionID",
            path_message_id="messageID",
            id="id",
            body_message_id="messageID",
            body_session_id="sessionID",
            text="text",
            time={"start": 0},
            type="reasoning",
        )
        assert_matches_type(Part, part, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params_overload_3(self, client: OpencodeSDK) -> None:
        part = client.session.message.part.update(
            part_id="partID",
            path_session_id="sessionID",
            path_message_id="messageID",
            id="id",
            body_message_id="messageID",
            body_session_id="sessionID",
            text="text",
            time={
                "start": 0,
                "end": 0,
            },
            type="reasoning",
            directory="directory",
            metadata={"foo": "bar"},
        )
        assert_matches_type(Part, part, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_overload_3(self, client: OpencodeSDK) -> None:
        response = client.session.message.part.with_raw_response.update(
            part_id="partID",
            path_session_id="sessionID",
            path_message_id="messageID",
            id="id",
            body_message_id="messageID",
            body_session_id="sessionID",
            text="text",
            time={"start": 0},
            type="reasoning",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        part = response.parse()
        assert_matches_type(Part, part, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_overload_3(self, client: OpencodeSDK) -> None:
        with client.session.message.part.with_streaming_response.update(
            part_id="partID",
            path_session_id="sessionID",
            path_message_id="messageID",
            id="id",
            body_message_id="messageID",
            body_session_id="sessionID",
            text="text",
            time={"start": 0},
            type="reasoning",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            part = response.parse()
            assert_matches_type(Part, part, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update_overload_3(self, client: OpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_session_id` but received ''"):
            client.session.message.part.with_raw_response.update(
                part_id="partID",
                path_session_id="",
                path_message_id="messageID",
                id="id",
                body_message_id="messageID",
                body_session_id="sessionID",
                text="text",
                time={"start": 0},
                type="reasoning",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_message_id` but received ''"):
            client.session.message.part.with_raw_response.update(
                part_id="partID",
                path_session_id="sessionID",
                path_message_id="",
                id="id",
                body_message_id="messageID",
                body_session_id="sessionID",
                text="text",
                time={"start": 0},
                type="reasoning",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `part_id` but received ''"):
            client.session.message.part.with_raw_response.update(
                part_id="",
                path_session_id="sessionID",
                path_message_id="messageID",
                id="id",
                body_message_id="messageID",
                body_session_id="sessionID",
                text="text",
                time={"start": 0},
                type="reasoning",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_overload_4(self, client: OpencodeSDK) -> None:
        part = client.session.message.part.update(
            part_id="partID",
            path_session_id="sessionID",
            path_message_id="messageID",
            id="id",
            body_message_id="messageID",
            mime="mime",
            body_session_id="sessionID",
            type="file",
            url="url",
        )
        assert_matches_type(Part, part, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params_overload_4(self, client: OpencodeSDK) -> None:
        part = client.session.message.part.update(
            part_id="partID",
            path_session_id="sessionID",
            path_message_id="messageID",
            id="id",
            body_message_id="messageID",
            mime="mime",
            body_session_id="sessionID",
            type="file",
            url="url",
            directory="directory",
            filename="filename",
            source={
                "path": "path",
                "text": {
                    "end": -9007199254740991,
                    "start": -9007199254740991,
                    "value": "value",
                },
                "type": "file",
            },
        )
        assert_matches_type(Part, part, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_overload_4(self, client: OpencodeSDK) -> None:
        response = client.session.message.part.with_raw_response.update(
            part_id="partID",
            path_session_id="sessionID",
            path_message_id="messageID",
            id="id",
            body_message_id="messageID",
            mime="mime",
            body_session_id="sessionID",
            type="file",
            url="url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        part = response.parse()
        assert_matches_type(Part, part, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_overload_4(self, client: OpencodeSDK) -> None:
        with client.session.message.part.with_streaming_response.update(
            part_id="partID",
            path_session_id="sessionID",
            path_message_id="messageID",
            id="id",
            body_message_id="messageID",
            mime="mime",
            body_session_id="sessionID",
            type="file",
            url="url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            part = response.parse()
            assert_matches_type(Part, part, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update_overload_4(self, client: OpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_session_id` but received ''"):
            client.session.message.part.with_raw_response.update(
                part_id="partID",
                path_session_id="",
                path_message_id="messageID",
                id="id",
                body_message_id="messageID",
                mime="mime",
                body_session_id="sessionID",
                type="file",
                url="url",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_message_id` but received ''"):
            client.session.message.part.with_raw_response.update(
                part_id="partID",
                path_session_id="sessionID",
                path_message_id="",
                id="id",
                body_message_id="messageID",
                mime="mime",
                body_session_id="sessionID",
                type="file",
                url="url",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `part_id` but received ''"):
            client.session.message.part.with_raw_response.update(
                part_id="",
                path_session_id="sessionID",
                path_message_id="messageID",
                id="id",
                body_message_id="messageID",
                mime="mime",
                body_session_id="sessionID",
                type="file",
                url="url",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_overload_5(self, client: OpencodeSDK) -> None:
        part = client.session.message.part.update(
            part_id="partID",
            path_session_id="sessionID",
            path_message_id="messageID",
            id="id",
            call_id="callID",
            body_message_id="messageID",
            body_session_id="sessionID",
            state={
                "input": {"foo": "bar"},
                "raw": "raw",
                "status": "pending",
            },
            tool="tool",
            type="tool",
        )
        assert_matches_type(Part, part, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params_overload_5(self, client: OpencodeSDK) -> None:
        part = client.session.message.part.update(
            part_id="partID",
            path_session_id="sessionID",
            path_message_id="messageID",
            id="id",
            call_id="callID",
            body_message_id="messageID",
            body_session_id="sessionID",
            state={
                "input": {"foo": "bar"},
                "raw": "raw",
                "status": "pending",
            },
            tool="tool",
            type="tool",
            directory="directory",
            metadata={"foo": "bar"},
        )
        assert_matches_type(Part, part, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_overload_5(self, client: OpencodeSDK) -> None:
        response = client.session.message.part.with_raw_response.update(
            part_id="partID",
            path_session_id="sessionID",
            path_message_id="messageID",
            id="id",
            call_id="callID",
            body_message_id="messageID",
            body_session_id="sessionID",
            state={
                "input": {"foo": "bar"},
                "raw": "raw",
                "status": "pending",
            },
            tool="tool",
            type="tool",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        part = response.parse()
        assert_matches_type(Part, part, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_overload_5(self, client: OpencodeSDK) -> None:
        with client.session.message.part.with_streaming_response.update(
            part_id="partID",
            path_session_id="sessionID",
            path_message_id="messageID",
            id="id",
            call_id="callID",
            body_message_id="messageID",
            body_session_id="sessionID",
            state={
                "input": {"foo": "bar"},
                "raw": "raw",
                "status": "pending",
            },
            tool="tool",
            type="tool",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            part = response.parse()
            assert_matches_type(Part, part, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update_overload_5(self, client: OpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_session_id` but received ''"):
            client.session.message.part.with_raw_response.update(
                part_id="partID",
                path_session_id="",
                path_message_id="messageID",
                id="id",
                call_id="callID",
                body_message_id="messageID",
                body_session_id="sessionID",
                state={
                    "input": {"foo": "bar"},
                    "raw": "raw",
                    "status": "pending",
                },
                tool="tool",
                type="tool",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_message_id` but received ''"):
            client.session.message.part.with_raw_response.update(
                part_id="partID",
                path_session_id="sessionID",
                path_message_id="",
                id="id",
                call_id="callID",
                body_message_id="messageID",
                body_session_id="sessionID",
                state={
                    "input": {"foo": "bar"},
                    "raw": "raw",
                    "status": "pending",
                },
                tool="tool",
                type="tool",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `part_id` but received ''"):
            client.session.message.part.with_raw_response.update(
                part_id="",
                path_session_id="sessionID",
                path_message_id="messageID",
                id="id",
                call_id="callID",
                body_message_id="messageID",
                body_session_id="sessionID",
                state={
                    "input": {"foo": "bar"},
                    "raw": "raw",
                    "status": "pending",
                },
                tool="tool",
                type="tool",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_overload_6(self, client: OpencodeSDK) -> None:
        part = client.session.message.part.update(
            part_id="partID",
            path_session_id="sessionID",
            path_message_id="messageID",
            id="id",
            body_message_id="messageID",
            body_session_id="sessionID",
            type="step-start",
        )
        assert_matches_type(Part, part, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params_overload_6(self, client: OpencodeSDK) -> None:
        part = client.session.message.part.update(
            part_id="partID",
            path_session_id="sessionID",
            path_message_id="messageID",
            id="id",
            body_message_id="messageID",
            body_session_id="sessionID",
            type="step-start",
            directory="directory",
            snapshot="snapshot",
        )
        assert_matches_type(Part, part, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_overload_6(self, client: OpencodeSDK) -> None:
        response = client.session.message.part.with_raw_response.update(
            part_id="partID",
            path_session_id="sessionID",
            path_message_id="messageID",
            id="id",
            body_message_id="messageID",
            body_session_id="sessionID",
            type="step-start",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        part = response.parse()
        assert_matches_type(Part, part, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_overload_6(self, client: OpencodeSDK) -> None:
        with client.session.message.part.with_streaming_response.update(
            part_id="partID",
            path_session_id="sessionID",
            path_message_id="messageID",
            id="id",
            body_message_id="messageID",
            body_session_id="sessionID",
            type="step-start",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            part = response.parse()
            assert_matches_type(Part, part, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update_overload_6(self, client: OpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_session_id` but received ''"):
            client.session.message.part.with_raw_response.update(
                part_id="partID",
                path_session_id="",
                path_message_id="messageID",
                id="id",
                body_message_id="messageID",
                body_session_id="sessionID",
                type="step-start",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_message_id` but received ''"):
            client.session.message.part.with_raw_response.update(
                part_id="partID",
                path_session_id="sessionID",
                path_message_id="",
                id="id",
                body_message_id="messageID",
                body_session_id="sessionID",
                type="step-start",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `part_id` but received ''"):
            client.session.message.part.with_raw_response.update(
                part_id="",
                path_session_id="sessionID",
                path_message_id="messageID",
                id="id",
                body_message_id="messageID",
                body_session_id="sessionID",
                type="step-start",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_overload_7(self, client: OpencodeSDK) -> None:
        part = client.session.message.part.update(
            part_id="partID",
            path_session_id="sessionID",
            path_message_id="messageID",
            id="id",
            cost=0,
            body_message_id="messageID",
            reason="reason",
            body_session_id="sessionID",
            tokens={
                "cache": {
                    "read": 0,
                    "write": 0,
                },
                "input": 0,
                "output": 0,
                "reasoning": 0,
            },
            type="step-finish",
        )
        assert_matches_type(Part, part, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params_overload_7(self, client: OpencodeSDK) -> None:
        part = client.session.message.part.update(
            part_id="partID",
            path_session_id="sessionID",
            path_message_id="messageID",
            id="id",
            cost=0,
            body_message_id="messageID",
            reason="reason",
            body_session_id="sessionID",
            tokens={
                "cache": {
                    "read": 0,
                    "write": 0,
                },
                "input": 0,
                "output": 0,
                "reasoning": 0,
            },
            type="step-finish",
            directory="directory",
            snapshot="snapshot",
        )
        assert_matches_type(Part, part, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_overload_7(self, client: OpencodeSDK) -> None:
        response = client.session.message.part.with_raw_response.update(
            part_id="partID",
            path_session_id="sessionID",
            path_message_id="messageID",
            id="id",
            cost=0,
            body_message_id="messageID",
            reason="reason",
            body_session_id="sessionID",
            tokens={
                "cache": {
                    "read": 0,
                    "write": 0,
                },
                "input": 0,
                "output": 0,
                "reasoning": 0,
            },
            type="step-finish",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        part = response.parse()
        assert_matches_type(Part, part, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_overload_7(self, client: OpencodeSDK) -> None:
        with client.session.message.part.with_streaming_response.update(
            part_id="partID",
            path_session_id="sessionID",
            path_message_id="messageID",
            id="id",
            cost=0,
            body_message_id="messageID",
            reason="reason",
            body_session_id="sessionID",
            tokens={
                "cache": {
                    "read": 0,
                    "write": 0,
                },
                "input": 0,
                "output": 0,
                "reasoning": 0,
            },
            type="step-finish",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            part = response.parse()
            assert_matches_type(Part, part, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update_overload_7(self, client: OpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_session_id` but received ''"):
            client.session.message.part.with_raw_response.update(
                part_id="partID",
                path_session_id="",
                path_message_id="messageID",
                id="id",
                cost=0,
                body_message_id="messageID",
                reason="reason",
                body_session_id="sessionID",
                tokens={
                    "cache": {
                        "read": 0,
                        "write": 0,
                    },
                    "input": 0,
                    "output": 0,
                    "reasoning": 0,
                },
                type="step-finish",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_message_id` but received ''"):
            client.session.message.part.with_raw_response.update(
                part_id="partID",
                path_session_id="sessionID",
                path_message_id="",
                id="id",
                cost=0,
                body_message_id="messageID",
                reason="reason",
                body_session_id="sessionID",
                tokens={
                    "cache": {
                        "read": 0,
                        "write": 0,
                    },
                    "input": 0,
                    "output": 0,
                    "reasoning": 0,
                },
                type="step-finish",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `part_id` but received ''"):
            client.session.message.part.with_raw_response.update(
                part_id="",
                path_session_id="sessionID",
                path_message_id="messageID",
                id="id",
                cost=0,
                body_message_id="messageID",
                reason="reason",
                body_session_id="sessionID",
                tokens={
                    "cache": {
                        "read": 0,
                        "write": 0,
                    },
                    "input": 0,
                    "output": 0,
                    "reasoning": 0,
                },
                type="step-finish",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_overload_8(self, client: OpencodeSDK) -> None:
        part = client.session.message.part.update(
            part_id="partID",
            path_session_id="sessionID",
            path_message_id="messageID",
            id="id",
            body_message_id="messageID",
            body_session_id="sessionID",
            snapshot="snapshot",
            type="snapshot",
        )
        assert_matches_type(Part, part, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params_overload_8(self, client: OpencodeSDK) -> None:
        part = client.session.message.part.update(
            part_id="partID",
            path_session_id="sessionID",
            path_message_id="messageID",
            id="id",
            body_message_id="messageID",
            body_session_id="sessionID",
            snapshot="snapshot",
            type="snapshot",
            directory="directory",
        )
        assert_matches_type(Part, part, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_overload_8(self, client: OpencodeSDK) -> None:
        response = client.session.message.part.with_raw_response.update(
            part_id="partID",
            path_session_id="sessionID",
            path_message_id="messageID",
            id="id",
            body_message_id="messageID",
            body_session_id="sessionID",
            snapshot="snapshot",
            type="snapshot",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        part = response.parse()
        assert_matches_type(Part, part, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_overload_8(self, client: OpencodeSDK) -> None:
        with client.session.message.part.with_streaming_response.update(
            part_id="partID",
            path_session_id="sessionID",
            path_message_id="messageID",
            id="id",
            body_message_id="messageID",
            body_session_id="sessionID",
            snapshot="snapshot",
            type="snapshot",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            part = response.parse()
            assert_matches_type(Part, part, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update_overload_8(self, client: OpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_session_id` but received ''"):
            client.session.message.part.with_raw_response.update(
                part_id="partID",
                path_session_id="",
                path_message_id="messageID",
                id="id",
                body_message_id="messageID",
                body_session_id="sessionID",
                snapshot="snapshot",
                type="snapshot",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_message_id` but received ''"):
            client.session.message.part.with_raw_response.update(
                part_id="partID",
                path_session_id="sessionID",
                path_message_id="",
                id="id",
                body_message_id="messageID",
                body_session_id="sessionID",
                snapshot="snapshot",
                type="snapshot",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `part_id` but received ''"):
            client.session.message.part.with_raw_response.update(
                part_id="",
                path_session_id="sessionID",
                path_message_id="messageID",
                id="id",
                body_message_id="messageID",
                body_session_id="sessionID",
                snapshot="snapshot",
                type="snapshot",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_overload_9(self, client: OpencodeSDK) -> None:
        part = client.session.message.part.update(
            part_id="partID",
            path_session_id="sessionID",
            path_message_id="messageID",
            id="id",
            files=["string"],
            hash="hash",
            body_message_id="messageID",
            body_session_id="sessionID",
            type="patch",
        )
        assert_matches_type(Part, part, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params_overload_9(self, client: OpencodeSDK) -> None:
        part = client.session.message.part.update(
            part_id="partID",
            path_session_id="sessionID",
            path_message_id="messageID",
            id="id",
            files=["string"],
            hash="hash",
            body_message_id="messageID",
            body_session_id="sessionID",
            type="patch",
            directory="directory",
        )
        assert_matches_type(Part, part, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_overload_9(self, client: OpencodeSDK) -> None:
        response = client.session.message.part.with_raw_response.update(
            part_id="partID",
            path_session_id="sessionID",
            path_message_id="messageID",
            id="id",
            files=["string"],
            hash="hash",
            body_message_id="messageID",
            body_session_id="sessionID",
            type="patch",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        part = response.parse()
        assert_matches_type(Part, part, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_overload_9(self, client: OpencodeSDK) -> None:
        with client.session.message.part.with_streaming_response.update(
            part_id="partID",
            path_session_id="sessionID",
            path_message_id="messageID",
            id="id",
            files=["string"],
            hash="hash",
            body_message_id="messageID",
            body_session_id="sessionID",
            type="patch",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            part = response.parse()
            assert_matches_type(Part, part, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update_overload_9(self, client: OpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_session_id` but received ''"):
            client.session.message.part.with_raw_response.update(
                part_id="partID",
                path_session_id="",
                path_message_id="messageID",
                id="id",
                files=["string"],
                hash="hash",
                body_message_id="messageID",
                body_session_id="sessionID",
                type="patch",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_message_id` but received ''"):
            client.session.message.part.with_raw_response.update(
                part_id="partID",
                path_session_id="sessionID",
                path_message_id="",
                id="id",
                files=["string"],
                hash="hash",
                body_message_id="messageID",
                body_session_id="sessionID",
                type="patch",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `part_id` but received ''"):
            client.session.message.part.with_raw_response.update(
                part_id="",
                path_session_id="sessionID",
                path_message_id="messageID",
                id="id",
                files=["string"],
                hash="hash",
                body_message_id="messageID",
                body_session_id="sessionID",
                type="patch",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_overload_10(self, client: OpencodeSDK) -> None:
        part = client.session.message.part.update(
            part_id="partID",
            path_session_id="sessionID",
            path_message_id="messageID",
            id="id",
            body_message_id="messageID",
            name="name",
            body_session_id="sessionID",
            type="agent",
        )
        assert_matches_type(Part, part, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params_overload_10(self, client: OpencodeSDK) -> None:
        part = client.session.message.part.update(
            part_id="partID",
            path_session_id="sessionID",
            path_message_id="messageID",
            id="id",
            body_message_id="messageID",
            name="name",
            body_session_id="sessionID",
            type="agent",
            directory="directory",
            source={
                "end": -9007199254740991,
                "start": -9007199254740991,
                "value": "value",
            },
        )
        assert_matches_type(Part, part, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_overload_10(self, client: OpencodeSDK) -> None:
        response = client.session.message.part.with_raw_response.update(
            part_id="partID",
            path_session_id="sessionID",
            path_message_id="messageID",
            id="id",
            body_message_id="messageID",
            name="name",
            body_session_id="sessionID",
            type="agent",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        part = response.parse()
        assert_matches_type(Part, part, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_overload_10(self, client: OpencodeSDK) -> None:
        with client.session.message.part.with_streaming_response.update(
            part_id="partID",
            path_session_id="sessionID",
            path_message_id="messageID",
            id="id",
            body_message_id="messageID",
            name="name",
            body_session_id="sessionID",
            type="agent",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            part = response.parse()
            assert_matches_type(Part, part, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update_overload_10(self, client: OpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_session_id` but received ''"):
            client.session.message.part.with_raw_response.update(
                part_id="partID",
                path_session_id="",
                path_message_id="messageID",
                id="id",
                body_message_id="messageID",
                name="name",
                body_session_id="sessionID",
                type="agent",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_message_id` but received ''"):
            client.session.message.part.with_raw_response.update(
                part_id="partID",
                path_session_id="sessionID",
                path_message_id="",
                id="id",
                body_message_id="messageID",
                name="name",
                body_session_id="sessionID",
                type="agent",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `part_id` but received ''"):
            client.session.message.part.with_raw_response.update(
                part_id="",
                path_session_id="sessionID",
                path_message_id="messageID",
                id="id",
                body_message_id="messageID",
                name="name",
                body_session_id="sessionID",
                type="agent",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_overload_11(self, client: OpencodeSDK) -> None:
        part = client.session.message.part.update(
            part_id="partID",
            path_session_id="sessionID",
            path_message_id="messageID",
            id="id",
            attempt=0,
            error={
                "data": {
                    "is_retryable": True,
                    "message": "message",
                },
                "name": "APIError",
            },
            body_message_id="messageID",
            body_session_id="sessionID",
            time={"created": 0},
            type="retry",
        )
        assert_matches_type(Part, part, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params_overload_11(self, client: OpencodeSDK) -> None:
        part = client.session.message.part.update(
            part_id="partID",
            path_session_id="sessionID",
            path_message_id="messageID",
            id="id",
            attempt=0,
            error={
                "data": {
                    "is_retryable": True,
                    "message": "message",
                    "metadata": {"foo": "string"},
                    "response_body": "responseBody",
                    "response_headers": {"foo": "string"},
                    "status_code": 0,
                },
                "name": "APIError",
            },
            body_message_id="messageID",
            body_session_id="sessionID",
            time={"created": 0},
            type="retry",
            directory="directory",
        )
        assert_matches_type(Part, part, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_overload_11(self, client: OpencodeSDK) -> None:
        response = client.session.message.part.with_raw_response.update(
            part_id="partID",
            path_session_id="sessionID",
            path_message_id="messageID",
            id="id",
            attempt=0,
            error={
                "data": {
                    "is_retryable": True,
                    "message": "message",
                },
                "name": "APIError",
            },
            body_message_id="messageID",
            body_session_id="sessionID",
            time={"created": 0},
            type="retry",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        part = response.parse()
        assert_matches_type(Part, part, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_overload_11(self, client: OpencodeSDK) -> None:
        with client.session.message.part.with_streaming_response.update(
            part_id="partID",
            path_session_id="sessionID",
            path_message_id="messageID",
            id="id",
            attempt=0,
            error={
                "data": {
                    "is_retryable": True,
                    "message": "message",
                },
                "name": "APIError",
            },
            body_message_id="messageID",
            body_session_id="sessionID",
            time={"created": 0},
            type="retry",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            part = response.parse()
            assert_matches_type(Part, part, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update_overload_11(self, client: OpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_session_id` but received ''"):
            client.session.message.part.with_raw_response.update(
                part_id="partID",
                path_session_id="",
                path_message_id="messageID",
                id="id",
                attempt=0,
                error={
                    "data": {
                        "is_retryable": True,
                        "message": "message",
                    },
                    "name": "APIError",
                },
                body_message_id="messageID",
                body_session_id="sessionID",
                time={"created": 0},
                type="retry",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_message_id` but received ''"):
            client.session.message.part.with_raw_response.update(
                part_id="partID",
                path_session_id="sessionID",
                path_message_id="",
                id="id",
                attempt=0,
                error={
                    "data": {
                        "is_retryable": True,
                        "message": "message",
                    },
                    "name": "APIError",
                },
                body_message_id="messageID",
                body_session_id="sessionID",
                time={"created": 0},
                type="retry",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `part_id` but received ''"):
            client.session.message.part.with_raw_response.update(
                part_id="",
                path_session_id="sessionID",
                path_message_id="messageID",
                id="id",
                attempt=0,
                error={
                    "data": {
                        "is_retryable": True,
                        "message": "message",
                    },
                    "name": "APIError",
                },
                body_message_id="messageID",
                body_session_id="sessionID",
                time={"created": 0},
                type="retry",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_overload_12(self, client: OpencodeSDK) -> None:
        part = client.session.message.part.update(
            part_id="partID",
            path_session_id="sessionID",
            path_message_id="messageID",
            id="id",
            auto=True,
            body_message_id="messageID",
            body_session_id="sessionID",
            type="compaction",
        )
        assert_matches_type(Part, part, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params_overload_12(self, client: OpencodeSDK) -> None:
        part = client.session.message.part.update(
            part_id="partID",
            path_session_id="sessionID",
            path_message_id="messageID",
            id="id",
            auto=True,
            body_message_id="messageID",
            body_session_id="sessionID",
            type="compaction",
            directory="directory",
        )
        assert_matches_type(Part, part, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_overload_12(self, client: OpencodeSDK) -> None:
        response = client.session.message.part.with_raw_response.update(
            part_id="partID",
            path_session_id="sessionID",
            path_message_id="messageID",
            id="id",
            auto=True,
            body_message_id="messageID",
            body_session_id="sessionID",
            type="compaction",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        part = response.parse()
        assert_matches_type(Part, part, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_overload_12(self, client: OpencodeSDK) -> None:
        with client.session.message.part.with_streaming_response.update(
            part_id="partID",
            path_session_id="sessionID",
            path_message_id="messageID",
            id="id",
            auto=True,
            body_message_id="messageID",
            body_session_id="sessionID",
            type="compaction",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            part = response.parse()
            assert_matches_type(Part, part, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update_overload_12(self, client: OpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_session_id` but received ''"):
            client.session.message.part.with_raw_response.update(
                part_id="partID",
                path_session_id="",
                path_message_id="messageID",
                id="id",
                auto=True,
                body_message_id="messageID",
                body_session_id="sessionID",
                type="compaction",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_message_id` but received ''"):
            client.session.message.part.with_raw_response.update(
                part_id="partID",
                path_session_id="sessionID",
                path_message_id="",
                id="id",
                auto=True,
                body_message_id="messageID",
                body_session_id="sessionID",
                type="compaction",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `part_id` but received ''"):
            client.session.message.part.with_raw_response.update(
                part_id="",
                path_session_id="sessionID",
                path_message_id="messageID",
                id="id",
                auto=True,
                body_message_id="messageID",
                body_session_id="sessionID",
                type="compaction",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: OpencodeSDK) -> None:
        part = client.session.message.part.delete(
            part_id="partID",
            session_id="sessionID",
            message_id="messageID",
        )
        assert_matches_type(PartDeleteResponse, part, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete_with_all_params(self, client: OpencodeSDK) -> None:
        part = client.session.message.part.delete(
            part_id="partID",
            session_id="sessionID",
            message_id="messageID",
            directory="directory",
        )
        assert_matches_type(PartDeleteResponse, part, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: OpencodeSDK) -> None:
        response = client.session.message.part.with_raw_response.delete(
            part_id="partID",
            session_id="sessionID",
            message_id="messageID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        part = response.parse()
        assert_matches_type(PartDeleteResponse, part, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: OpencodeSDK) -> None:
        with client.session.message.part.with_streaming_response.delete(
            part_id="partID",
            session_id="sessionID",
            message_id="messageID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            part = response.parse()
            assert_matches_type(PartDeleteResponse, part, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: OpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.session.message.part.with_raw_response.delete(
                part_id="partID",
                session_id="",
                message_id="messageID",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            client.session.message.part.with_raw_response.delete(
                part_id="partID",
                session_id="sessionID",
                message_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `part_id` but received ''"):
            client.session.message.part.with_raw_response.delete(
                part_id="",
                session_id="sessionID",
                message_id="messageID",
            )


class TestAsyncPart:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_overload_1(self, async_client: AsyncOpencodeSDK) -> None:
        part = await async_client.session.message.part.update(
            part_id="partID",
            path_session_id="sessionID",
            path_message_id="messageID",
            id="id",
            body_message_id="messageID",
            body_session_id="sessionID",
            text="text",
            type="text",
        )
        assert_matches_type(Part, part, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params_overload_1(self, async_client: AsyncOpencodeSDK) -> None:
        part = await async_client.session.message.part.update(
            part_id="partID",
            path_session_id="sessionID",
            path_message_id="messageID",
            id="id",
            body_message_id="messageID",
            body_session_id="sessionID",
            text="text",
            type="text",
            directory="directory",
            ignored=True,
            metadata={"foo": "bar"},
            synthetic=True,
            time={
                "start": 0,
                "end": 0,
            },
        )
        assert_matches_type(Part, part, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_overload_1(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.session.message.part.with_raw_response.update(
            part_id="partID",
            path_session_id="sessionID",
            path_message_id="messageID",
            id="id",
            body_message_id="messageID",
            body_session_id="sessionID",
            text="text",
            type="text",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        part = await response.parse()
        assert_matches_type(Part, part, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_overload_1(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.session.message.part.with_streaming_response.update(
            part_id="partID",
            path_session_id="sessionID",
            path_message_id="messageID",
            id="id",
            body_message_id="messageID",
            body_session_id="sessionID",
            text="text",
            type="text",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            part = await response.parse()
            assert_matches_type(Part, part, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update_overload_1(self, async_client: AsyncOpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_session_id` but received ''"):
            await async_client.session.message.part.with_raw_response.update(
                part_id="partID",
                path_session_id="",
                path_message_id="messageID",
                id="id",
                body_message_id="messageID",
                body_session_id="sessionID",
                text="text",
                type="text",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_message_id` but received ''"):
            await async_client.session.message.part.with_raw_response.update(
                part_id="partID",
                path_session_id="sessionID",
                path_message_id="",
                id="id",
                body_message_id="messageID",
                body_session_id="sessionID",
                text="text",
                type="text",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `part_id` but received ''"):
            await async_client.session.message.part.with_raw_response.update(
                part_id="",
                path_session_id="sessionID",
                path_message_id="messageID",
                id="id",
                body_message_id="messageID",
                body_session_id="sessionID",
                text="text",
                type="text",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_overload_2(self, async_client: AsyncOpencodeSDK) -> None:
        part = await async_client.session.message.part.update(
            part_id="partID",
            path_session_id="sessionID",
            path_message_id="messageID",
            id="id",
            agent="agent",
            description="description",
            body_message_id="messageID",
            prompt="prompt",
            body_session_id="sessionID",
            type="subtask",
        )
        assert_matches_type(Part, part, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params_overload_2(self, async_client: AsyncOpencodeSDK) -> None:
        part = await async_client.session.message.part.update(
            part_id="partID",
            path_session_id="sessionID",
            path_message_id="messageID",
            id="id",
            agent="agent",
            description="description",
            body_message_id="messageID",
            prompt="prompt",
            body_session_id="sessionID",
            type="subtask",
            directory="directory",
            command="command",
        )
        assert_matches_type(Part, part, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_overload_2(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.session.message.part.with_raw_response.update(
            part_id="partID",
            path_session_id="sessionID",
            path_message_id="messageID",
            id="id",
            agent="agent",
            description="description",
            body_message_id="messageID",
            prompt="prompt",
            body_session_id="sessionID",
            type="subtask",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        part = await response.parse()
        assert_matches_type(Part, part, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_overload_2(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.session.message.part.with_streaming_response.update(
            part_id="partID",
            path_session_id="sessionID",
            path_message_id="messageID",
            id="id",
            agent="agent",
            description="description",
            body_message_id="messageID",
            prompt="prompt",
            body_session_id="sessionID",
            type="subtask",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            part = await response.parse()
            assert_matches_type(Part, part, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update_overload_2(self, async_client: AsyncOpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_session_id` but received ''"):
            await async_client.session.message.part.with_raw_response.update(
                part_id="partID",
                path_session_id="",
                path_message_id="messageID",
                id="id",
                agent="agent",
                description="description",
                body_message_id="messageID",
                prompt="prompt",
                body_session_id="sessionID",
                type="subtask",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_message_id` but received ''"):
            await async_client.session.message.part.with_raw_response.update(
                part_id="partID",
                path_session_id="sessionID",
                path_message_id="",
                id="id",
                agent="agent",
                description="description",
                body_message_id="messageID",
                prompt="prompt",
                body_session_id="sessionID",
                type="subtask",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `part_id` but received ''"):
            await async_client.session.message.part.with_raw_response.update(
                part_id="",
                path_session_id="sessionID",
                path_message_id="messageID",
                id="id",
                agent="agent",
                description="description",
                body_message_id="messageID",
                prompt="prompt",
                body_session_id="sessionID",
                type="subtask",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_overload_3(self, async_client: AsyncOpencodeSDK) -> None:
        part = await async_client.session.message.part.update(
            part_id="partID",
            path_session_id="sessionID",
            path_message_id="messageID",
            id="id",
            body_message_id="messageID",
            body_session_id="sessionID",
            text="text",
            time={"start": 0},
            type="reasoning",
        )
        assert_matches_type(Part, part, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params_overload_3(self, async_client: AsyncOpencodeSDK) -> None:
        part = await async_client.session.message.part.update(
            part_id="partID",
            path_session_id="sessionID",
            path_message_id="messageID",
            id="id",
            body_message_id="messageID",
            body_session_id="sessionID",
            text="text",
            time={
                "start": 0,
                "end": 0,
            },
            type="reasoning",
            directory="directory",
            metadata={"foo": "bar"},
        )
        assert_matches_type(Part, part, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_overload_3(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.session.message.part.with_raw_response.update(
            part_id="partID",
            path_session_id="sessionID",
            path_message_id="messageID",
            id="id",
            body_message_id="messageID",
            body_session_id="sessionID",
            text="text",
            time={"start": 0},
            type="reasoning",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        part = await response.parse()
        assert_matches_type(Part, part, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_overload_3(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.session.message.part.with_streaming_response.update(
            part_id="partID",
            path_session_id="sessionID",
            path_message_id="messageID",
            id="id",
            body_message_id="messageID",
            body_session_id="sessionID",
            text="text",
            time={"start": 0},
            type="reasoning",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            part = await response.parse()
            assert_matches_type(Part, part, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update_overload_3(self, async_client: AsyncOpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_session_id` but received ''"):
            await async_client.session.message.part.with_raw_response.update(
                part_id="partID",
                path_session_id="",
                path_message_id="messageID",
                id="id",
                body_message_id="messageID",
                body_session_id="sessionID",
                text="text",
                time={"start": 0},
                type="reasoning",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_message_id` but received ''"):
            await async_client.session.message.part.with_raw_response.update(
                part_id="partID",
                path_session_id="sessionID",
                path_message_id="",
                id="id",
                body_message_id="messageID",
                body_session_id="sessionID",
                text="text",
                time={"start": 0},
                type="reasoning",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `part_id` but received ''"):
            await async_client.session.message.part.with_raw_response.update(
                part_id="",
                path_session_id="sessionID",
                path_message_id="messageID",
                id="id",
                body_message_id="messageID",
                body_session_id="sessionID",
                text="text",
                time={"start": 0},
                type="reasoning",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_overload_4(self, async_client: AsyncOpencodeSDK) -> None:
        part = await async_client.session.message.part.update(
            part_id="partID",
            path_session_id="sessionID",
            path_message_id="messageID",
            id="id",
            body_message_id="messageID",
            mime="mime",
            body_session_id="sessionID",
            type="file",
            url="url",
        )
        assert_matches_type(Part, part, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params_overload_4(self, async_client: AsyncOpencodeSDK) -> None:
        part = await async_client.session.message.part.update(
            part_id="partID",
            path_session_id="sessionID",
            path_message_id="messageID",
            id="id",
            body_message_id="messageID",
            mime="mime",
            body_session_id="sessionID",
            type="file",
            url="url",
            directory="directory",
            filename="filename",
            source={
                "path": "path",
                "text": {
                    "end": -9007199254740991,
                    "start": -9007199254740991,
                    "value": "value",
                },
                "type": "file",
            },
        )
        assert_matches_type(Part, part, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_overload_4(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.session.message.part.with_raw_response.update(
            part_id="partID",
            path_session_id="sessionID",
            path_message_id="messageID",
            id="id",
            body_message_id="messageID",
            mime="mime",
            body_session_id="sessionID",
            type="file",
            url="url",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        part = await response.parse()
        assert_matches_type(Part, part, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_overload_4(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.session.message.part.with_streaming_response.update(
            part_id="partID",
            path_session_id="sessionID",
            path_message_id="messageID",
            id="id",
            body_message_id="messageID",
            mime="mime",
            body_session_id="sessionID",
            type="file",
            url="url",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            part = await response.parse()
            assert_matches_type(Part, part, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update_overload_4(self, async_client: AsyncOpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_session_id` but received ''"):
            await async_client.session.message.part.with_raw_response.update(
                part_id="partID",
                path_session_id="",
                path_message_id="messageID",
                id="id",
                body_message_id="messageID",
                mime="mime",
                body_session_id="sessionID",
                type="file",
                url="url",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_message_id` but received ''"):
            await async_client.session.message.part.with_raw_response.update(
                part_id="partID",
                path_session_id="sessionID",
                path_message_id="",
                id="id",
                body_message_id="messageID",
                mime="mime",
                body_session_id="sessionID",
                type="file",
                url="url",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `part_id` but received ''"):
            await async_client.session.message.part.with_raw_response.update(
                part_id="",
                path_session_id="sessionID",
                path_message_id="messageID",
                id="id",
                body_message_id="messageID",
                mime="mime",
                body_session_id="sessionID",
                type="file",
                url="url",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_overload_5(self, async_client: AsyncOpencodeSDK) -> None:
        part = await async_client.session.message.part.update(
            part_id="partID",
            path_session_id="sessionID",
            path_message_id="messageID",
            id="id",
            call_id="callID",
            body_message_id="messageID",
            body_session_id="sessionID",
            state={
                "input": {"foo": "bar"},
                "raw": "raw",
                "status": "pending",
            },
            tool="tool",
            type="tool",
        )
        assert_matches_type(Part, part, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params_overload_5(self, async_client: AsyncOpencodeSDK) -> None:
        part = await async_client.session.message.part.update(
            part_id="partID",
            path_session_id="sessionID",
            path_message_id="messageID",
            id="id",
            call_id="callID",
            body_message_id="messageID",
            body_session_id="sessionID",
            state={
                "input": {"foo": "bar"},
                "raw": "raw",
                "status": "pending",
            },
            tool="tool",
            type="tool",
            directory="directory",
            metadata={"foo": "bar"},
        )
        assert_matches_type(Part, part, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_overload_5(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.session.message.part.with_raw_response.update(
            part_id="partID",
            path_session_id="sessionID",
            path_message_id="messageID",
            id="id",
            call_id="callID",
            body_message_id="messageID",
            body_session_id="sessionID",
            state={
                "input": {"foo": "bar"},
                "raw": "raw",
                "status": "pending",
            },
            tool="tool",
            type="tool",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        part = await response.parse()
        assert_matches_type(Part, part, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_overload_5(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.session.message.part.with_streaming_response.update(
            part_id="partID",
            path_session_id="sessionID",
            path_message_id="messageID",
            id="id",
            call_id="callID",
            body_message_id="messageID",
            body_session_id="sessionID",
            state={
                "input": {"foo": "bar"},
                "raw": "raw",
                "status": "pending",
            },
            tool="tool",
            type="tool",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            part = await response.parse()
            assert_matches_type(Part, part, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update_overload_5(self, async_client: AsyncOpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_session_id` but received ''"):
            await async_client.session.message.part.with_raw_response.update(
                part_id="partID",
                path_session_id="",
                path_message_id="messageID",
                id="id",
                call_id="callID",
                body_message_id="messageID",
                body_session_id="sessionID",
                state={
                    "input": {"foo": "bar"},
                    "raw": "raw",
                    "status": "pending",
                },
                tool="tool",
                type="tool",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_message_id` but received ''"):
            await async_client.session.message.part.with_raw_response.update(
                part_id="partID",
                path_session_id="sessionID",
                path_message_id="",
                id="id",
                call_id="callID",
                body_message_id="messageID",
                body_session_id="sessionID",
                state={
                    "input": {"foo": "bar"},
                    "raw": "raw",
                    "status": "pending",
                },
                tool="tool",
                type="tool",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `part_id` but received ''"):
            await async_client.session.message.part.with_raw_response.update(
                part_id="",
                path_session_id="sessionID",
                path_message_id="messageID",
                id="id",
                call_id="callID",
                body_message_id="messageID",
                body_session_id="sessionID",
                state={
                    "input": {"foo": "bar"},
                    "raw": "raw",
                    "status": "pending",
                },
                tool="tool",
                type="tool",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_overload_6(self, async_client: AsyncOpencodeSDK) -> None:
        part = await async_client.session.message.part.update(
            part_id="partID",
            path_session_id="sessionID",
            path_message_id="messageID",
            id="id",
            body_message_id="messageID",
            body_session_id="sessionID",
            type="step-start",
        )
        assert_matches_type(Part, part, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params_overload_6(self, async_client: AsyncOpencodeSDK) -> None:
        part = await async_client.session.message.part.update(
            part_id="partID",
            path_session_id="sessionID",
            path_message_id="messageID",
            id="id",
            body_message_id="messageID",
            body_session_id="sessionID",
            type="step-start",
            directory="directory",
            snapshot="snapshot",
        )
        assert_matches_type(Part, part, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_overload_6(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.session.message.part.with_raw_response.update(
            part_id="partID",
            path_session_id="sessionID",
            path_message_id="messageID",
            id="id",
            body_message_id="messageID",
            body_session_id="sessionID",
            type="step-start",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        part = await response.parse()
        assert_matches_type(Part, part, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_overload_6(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.session.message.part.with_streaming_response.update(
            part_id="partID",
            path_session_id="sessionID",
            path_message_id="messageID",
            id="id",
            body_message_id="messageID",
            body_session_id="sessionID",
            type="step-start",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            part = await response.parse()
            assert_matches_type(Part, part, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update_overload_6(self, async_client: AsyncOpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_session_id` but received ''"):
            await async_client.session.message.part.with_raw_response.update(
                part_id="partID",
                path_session_id="",
                path_message_id="messageID",
                id="id",
                body_message_id="messageID",
                body_session_id="sessionID",
                type="step-start",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_message_id` but received ''"):
            await async_client.session.message.part.with_raw_response.update(
                part_id="partID",
                path_session_id="sessionID",
                path_message_id="",
                id="id",
                body_message_id="messageID",
                body_session_id="sessionID",
                type="step-start",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `part_id` but received ''"):
            await async_client.session.message.part.with_raw_response.update(
                part_id="",
                path_session_id="sessionID",
                path_message_id="messageID",
                id="id",
                body_message_id="messageID",
                body_session_id="sessionID",
                type="step-start",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_overload_7(self, async_client: AsyncOpencodeSDK) -> None:
        part = await async_client.session.message.part.update(
            part_id="partID",
            path_session_id="sessionID",
            path_message_id="messageID",
            id="id",
            cost=0,
            body_message_id="messageID",
            reason="reason",
            body_session_id="sessionID",
            tokens={
                "cache": {
                    "read": 0,
                    "write": 0,
                },
                "input": 0,
                "output": 0,
                "reasoning": 0,
            },
            type="step-finish",
        )
        assert_matches_type(Part, part, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params_overload_7(self, async_client: AsyncOpencodeSDK) -> None:
        part = await async_client.session.message.part.update(
            part_id="partID",
            path_session_id="sessionID",
            path_message_id="messageID",
            id="id",
            cost=0,
            body_message_id="messageID",
            reason="reason",
            body_session_id="sessionID",
            tokens={
                "cache": {
                    "read": 0,
                    "write": 0,
                },
                "input": 0,
                "output": 0,
                "reasoning": 0,
            },
            type="step-finish",
            directory="directory",
            snapshot="snapshot",
        )
        assert_matches_type(Part, part, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_overload_7(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.session.message.part.with_raw_response.update(
            part_id="partID",
            path_session_id="sessionID",
            path_message_id="messageID",
            id="id",
            cost=0,
            body_message_id="messageID",
            reason="reason",
            body_session_id="sessionID",
            tokens={
                "cache": {
                    "read": 0,
                    "write": 0,
                },
                "input": 0,
                "output": 0,
                "reasoning": 0,
            },
            type="step-finish",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        part = await response.parse()
        assert_matches_type(Part, part, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_overload_7(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.session.message.part.with_streaming_response.update(
            part_id="partID",
            path_session_id="sessionID",
            path_message_id="messageID",
            id="id",
            cost=0,
            body_message_id="messageID",
            reason="reason",
            body_session_id="sessionID",
            tokens={
                "cache": {
                    "read": 0,
                    "write": 0,
                },
                "input": 0,
                "output": 0,
                "reasoning": 0,
            },
            type="step-finish",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            part = await response.parse()
            assert_matches_type(Part, part, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update_overload_7(self, async_client: AsyncOpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_session_id` but received ''"):
            await async_client.session.message.part.with_raw_response.update(
                part_id="partID",
                path_session_id="",
                path_message_id="messageID",
                id="id",
                cost=0,
                body_message_id="messageID",
                reason="reason",
                body_session_id="sessionID",
                tokens={
                    "cache": {
                        "read": 0,
                        "write": 0,
                    },
                    "input": 0,
                    "output": 0,
                    "reasoning": 0,
                },
                type="step-finish",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_message_id` but received ''"):
            await async_client.session.message.part.with_raw_response.update(
                part_id="partID",
                path_session_id="sessionID",
                path_message_id="",
                id="id",
                cost=0,
                body_message_id="messageID",
                reason="reason",
                body_session_id="sessionID",
                tokens={
                    "cache": {
                        "read": 0,
                        "write": 0,
                    },
                    "input": 0,
                    "output": 0,
                    "reasoning": 0,
                },
                type="step-finish",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `part_id` but received ''"):
            await async_client.session.message.part.with_raw_response.update(
                part_id="",
                path_session_id="sessionID",
                path_message_id="messageID",
                id="id",
                cost=0,
                body_message_id="messageID",
                reason="reason",
                body_session_id="sessionID",
                tokens={
                    "cache": {
                        "read": 0,
                        "write": 0,
                    },
                    "input": 0,
                    "output": 0,
                    "reasoning": 0,
                },
                type="step-finish",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_overload_8(self, async_client: AsyncOpencodeSDK) -> None:
        part = await async_client.session.message.part.update(
            part_id="partID",
            path_session_id="sessionID",
            path_message_id="messageID",
            id="id",
            body_message_id="messageID",
            body_session_id="sessionID",
            snapshot="snapshot",
            type="snapshot",
        )
        assert_matches_type(Part, part, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params_overload_8(self, async_client: AsyncOpencodeSDK) -> None:
        part = await async_client.session.message.part.update(
            part_id="partID",
            path_session_id="sessionID",
            path_message_id="messageID",
            id="id",
            body_message_id="messageID",
            body_session_id="sessionID",
            snapshot="snapshot",
            type="snapshot",
            directory="directory",
        )
        assert_matches_type(Part, part, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_overload_8(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.session.message.part.with_raw_response.update(
            part_id="partID",
            path_session_id="sessionID",
            path_message_id="messageID",
            id="id",
            body_message_id="messageID",
            body_session_id="sessionID",
            snapshot="snapshot",
            type="snapshot",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        part = await response.parse()
        assert_matches_type(Part, part, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_overload_8(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.session.message.part.with_streaming_response.update(
            part_id="partID",
            path_session_id="sessionID",
            path_message_id="messageID",
            id="id",
            body_message_id="messageID",
            body_session_id="sessionID",
            snapshot="snapshot",
            type="snapshot",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            part = await response.parse()
            assert_matches_type(Part, part, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update_overload_8(self, async_client: AsyncOpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_session_id` but received ''"):
            await async_client.session.message.part.with_raw_response.update(
                part_id="partID",
                path_session_id="",
                path_message_id="messageID",
                id="id",
                body_message_id="messageID",
                body_session_id="sessionID",
                snapshot="snapshot",
                type="snapshot",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_message_id` but received ''"):
            await async_client.session.message.part.with_raw_response.update(
                part_id="partID",
                path_session_id="sessionID",
                path_message_id="",
                id="id",
                body_message_id="messageID",
                body_session_id="sessionID",
                snapshot="snapshot",
                type="snapshot",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `part_id` but received ''"):
            await async_client.session.message.part.with_raw_response.update(
                part_id="",
                path_session_id="sessionID",
                path_message_id="messageID",
                id="id",
                body_message_id="messageID",
                body_session_id="sessionID",
                snapshot="snapshot",
                type="snapshot",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_overload_9(self, async_client: AsyncOpencodeSDK) -> None:
        part = await async_client.session.message.part.update(
            part_id="partID",
            path_session_id="sessionID",
            path_message_id="messageID",
            id="id",
            files=["string"],
            hash="hash",
            body_message_id="messageID",
            body_session_id="sessionID",
            type="patch",
        )
        assert_matches_type(Part, part, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params_overload_9(self, async_client: AsyncOpencodeSDK) -> None:
        part = await async_client.session.message.part.update(
            part_id="partID",
            path_session_id="sessionID",
            path_message_id="messageID",
            id="id",
            files=["string"],
            hash="hash",
            body_message_id="messageID",
            body_session_id="sessionID",
            type="patch",
            directory="directory",
        )
        assert_matches_type(Part, part, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_overload_9(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.session.message.part.with_raw_response.update(
            part_id="partID",
            path_session_id="sessionID",
            path_message_id="messageID",
            id="id",
            files=["string"],
            hash="hash",
            body_message_id="messageID",
            body_session_id="sessionID",
            type="patch",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        part = await response.parse()
        assert_matches_type(Part, part, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_overload_9(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.session.message.part.with_streaming_response.update(
            part_id="partID",
            path_session_id="sessionID",
            path_message_id="messageID",
            id="id",
            files=["string"],
            hash="hash",
            body_message_id="messageID",
            body_session_id="sessionID",
            type="patch",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            part = await response.parse()
            assert_matches_type(Part, part, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update_overload_9(self, async_client: AsyncOpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_session_id` but received ''"):
            await async_client.session.message.part.with_raw_response.update(
                part_id="partID",
                path_session_id="",
                path_message_id="messageID",
                id="id",
                files=["string"],
                hash="hash",
                body_message_id="messageID",
                body_session_id="sessionID",
                type="patch",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_message_id` but received ''"):
            await async_client.session.message.part.with_raw_response.update(
                part_id="partID",
                path_session_id="sessionID",
                path_message_id="",
                id="id",
                files=["string"],
                hash="hash",
                body_message_id="messageID",
                body_session_id="sessionID",
                type="patch",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `part_id` but received ''"):
            await async_client.session.message.part.with_raw_response.update(
                part_id="",
                path_session_id="sessionID",
                path_message_id="messageID",
                id="id",
                files=["string"],
                hash="hash",
                body_message_id="messageID",
                body_session_id="sessionID",
                type="patch",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_overload_10(self, async_client: AsyncOpencodeSDK) -> None:
        part = await async_client.session.message.part.update(
            part_id="partID",
            path_session_id="sessionID",
            path_message_id="messageID",
            id="id",
            body_message_id="messageID",
            name="name",
            body_session_id="sessionID",
            type="agent",
        )
        assert_matches_type(Part, part, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params_overload_10(self, async_client: AsyncOpencodeSDK) -> None:
        part = await async_client.session.message.part.update(
            part_id="partID",
            path_session_id="sessionID",
            path_message_id="messageID",
            id="id",
            body_message_id="messageID",
            name="name",
            body_session_id="sessionID",
            type="agent",
            directory="directory",
            source={
                "end": -9007199254740991,
                "start": -9007199254740991,
                "value": "value",
            },
        )
        assert_matches_type(Part, part, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_overload_10(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.session.message.part.with_raw_response.update(
            part_id="partID",
            path_session_id="sessionID",
            path_message_id="messageID",
            id="id",
            body_message_id="messageID",
            name="name",
            body_session_id="sessionID",
            type="agent",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        part = await response.parse()
        assert_matches_type(Part, part, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_overload_10(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.session.message.part.with_streaming_response.update(
            part_id="partID",
            path_session_id="sessionID",
            path_message_id="messageID",
            id="id",
            body_message_id="messageID",
            name="name",
            body_session_id="sessionID",
            type="agent",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            part = await response.parse()
            assert_matches_type(Part, part, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update_overload_10(self, async_client: AsyncOpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_session_id` but received ''"):
            await async_client.session.message.part.with_raw_response.update(
                part_id="partID",
                path_session_id="",
                path_message_id="messageID",
                id="id",
                body_message_id="messageID",
                name="name",
                body_session_id="sessionID",
                type="agent",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_message_id` but received ''"):
            await async_client.session.message.part.with_raw_response.update(
                part_id="partID",
                path_session_id="sessionID",
                path_message_id="",
                id="id",
                body_message_id="messageID",
                name="name",
                body_session_id="sessionID",
                type="agent",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `part_id` but received ''"):
            await async_client.session.message.part.with_raw_response.update(
                part_id="",
                path_session_id="sessionID",
                path_message_id="messageID",
                id="id",
                body_message_id="messageID",
                name="name",
                body_session_id="sessionID",
                type="agent",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_overload_11(self, async_client: AsyncOpencodeSDK) -> None:
        part = await async_client.session.message.part.update(
            part_id="partID",
            path_session_id="sessionID",
            path_message_id="messageID",
            id="id",
            attempt=0,
            error={
                "data": {
                    "is_retryable": True,
                    "message": "message",
                },
                "name": "APIError",
            },
            body_message_id="messageID",
            body_session_id="sessionID",
            time={"created": 0},
            type="retry",
        )
        assert_matches_type(Part, part, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params_overload_11(self, async_client: AsyncOpencodeSDK) -> None:
        part = await async_client.session.message.part.update(
            part_id="partID",
            path_session_id="sessionID",
            path_message_id="messageID",
            id="id",
            attempt=0,
            error={
                "data": {
                    "is_retryable": True,
                    "message": "message",
                    "metadata": {"foo": "string"},
                    "response_body": "responseBody",
                    "response_headers": {"foo": "string"},
                    "status_code": 0,
                },
                "name": "APIError",
            },
            body_message_id="messageID",
            body_session_id="sessionID",
            time={"created": 0},
            type="retry",
            directory="directory",
        )
        assert_matches_type(Part, part, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_overload_11(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.session.message.part.with_raw_response.update(
            part_id="partID",
            path_session_id="sessionID",
            path_message_id="messageID",
            id="id",
            attempt=0,
            error={
                "data": {
                    "is_retryable": True,
                    "message": "message",
                },
                "name": "APIError",
            },
            body_message_id="messageID",
            body_session_id="sessionID",
            time={"created": 0},
            type="retry",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        part = await response.parse()
        assert_matches_type(Part, part, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_overload_11(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.session.message.part.with_streaming_response.update(
            part_id="partID",
            path_session_id="sessionID",
            path_message_id="messageID",
            id="id",
            attempt=0,
            error={
                "data": {
                    "is_retryable": True,
                    "message": "message",
                },
                "name": "APIError",
            },
            body_message_id="messageID",
            body_session_id="sessionID",
            time={"created": 0},
            type="retry",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            part = await response.parse()
            assert_matches_type(Part, part, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update_overload_11(self, async_client: AsyncOpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_session_id` but received ''"):
            await async_client.session.message.part.with_raw_response.update(
                part_id="partID",
                path_session_id="",
                path_message_id="messageID",
                id="id",
                attempt=0,
                error={
                    "data": {
                        "is_retryable": True,
                        "message": "message",
                    },
                    "name": "APIError",
                },
                body_message_id="messageID",
                body_session_id="sessionID",
                time={"created": 0},
                type="retry",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_message_id` but received ''"):
            await async_client.session.message.part.with_raw_response.update(
                part_id="partID",
                path_session_id="sessionID",
                path_message_id="",
                id="id",
                attempt=0,
                error={
                    "data": {
                        "is_retryable": True,
                        "message": "message",
                    },
                    "name": "APIError",
                },
                body_message_id="messageID",
                body_session_id="sessionID",
                time={"created": 0},
                type="retry",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `part_id` but received ''"):
            await async_client.session.message.part.with_raw_response.update(
                part_id="",
                path_session_id="sessionID",
                path_message_id="messageID",
                id="id",
                attempt=0,
                error={
                    "data": {
                        "is_retryable": True,
                        "message": "message",
                    },
                    "name": "APIError",
                },
                body_message_id="messageID",
                body_session_id="sessionID",
                time={"created": 0},
                type="retry",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_overload_12(self, async_client: AsyncOpencodeSDK) -> None:
        part = await async_client.session.message.part.update(
            part_id="partID",
            path_session_id="sessionID",
            path_message_id="messageID",
            id="id",
            auto=True,
            body_message_id="messageID",
            body_session_id="sessionID",
            type="compaction",
        )
        assert_matches_type(Part, part, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params_overload_12(self, async_client: AsyncOpencodeSDK) -> None:
        part = await async_client.session.message.part.update(
            part_id="partID",
            path_session_id="sessionID",
            path_message_id="messageID",
            id="id",
            auto=True,
            body_message_id="messageID",
            body_session_id="sessionID",
            type="compaction",
            directory="directory",
        )
        assert_matches_type(Part, part, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_overload_12(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.session.message.part.with_raw_response.update(
            part_id="partID",
            path_session_id="sessionID",
            path_message_id="messageID",
            id="id",
            auto=True,
            body_message_id="messageID",
            body_session_id="sessionID",
            type="compaction",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        part = await response.parse()
        assert_matches_type(Part, part, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_overload_12(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.session.message.part.with_streaming_response.update(
            part_id="partID",
            path_session_id="sessionID",
            path_message_id="messageID",
            id="id",
            auto=True,
            body_message_id="messageID",
            body_session_id="sessionID",
            type="compaction",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            part = await response.parse()
            assert_matches_type(Part, part, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update_overload_12(self, async_client: AsyncOpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_session_id` but received ''"):
            await async_client.session.message.part.with_raw_response.update(
                part_id="partID",
                path_session_id="",
                path_message_id="messageID",
                id="id",
                auto=True,
                body_message_id="messageID",
                body_session_id="sessionID",
                type="compaction",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_message_id` but received ''"):
            await async_client.session.message.part.with_raw_response.update(
                part_id="partID",
                path_session_id="sessionID",
                path_message_id="",
                id="id",
                auto=True,
                body_message_id="messageID",
                body_session_id="sessionID",
                type="compaction",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `part_id` but received ''"):
            await async_client.session.message.part.with_raw_response.update(
                part_id="",
                path_session_id="sessionID",
                path_message_id="messageID",
                id="id",
                auto=True,
                body_message_id="messageID",
                body_session_id="sessionID",
                type="compaction",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncOpencodeSDK) -> None:
        part = await async_client.session.message.part.delete(
            part_id="partID",
            session_id="sessionID",
            message_id="messageID",
        )
        assert_matches_type(PartDeleteResponse, part, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncOpencodeSDK) -> None:
        part = await async_client.session.message.part.delete(
            part_id="partID",
            session_id="sessionID",
            message_id="messageID",
            directory="directory",
        )
        assert_matches_type(PartDeleteResponse, part, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.session.message.part.with_raw_response.delete(
            part_id="partID",
            session_id="sessionID",
            message_id="messageID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        part = await response.parse()
        assert_matches_type(PartDeleteResponse, part, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.session.message.part.with_streaming_response.delete(
            part_id="partID",
            session_id="sessionID",
            message_id="messageID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            part = await response.parse()
            assert_matches_type(PartDeleteResponse, part, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncOpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.session.message.part.with_raw_response.delete(
                part_id="partID",
                session_id="",
                message_id="messageID",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            await async_client.session.message.part.with_raw_response.delete(
                part_id="partID",
                session_id="sessionID",
                message_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `part_id` but received ''"):
            await async_client.session.message.part.with_raw_response.delete(
                part_id="",
                session_id="sessionID",
                message_id="messageID",
            )
