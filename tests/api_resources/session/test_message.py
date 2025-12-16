# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from opencode_sdk import OpencodeSDK, AsyncOpencodeSDK
from opencode_sdk.types.session import (
    MessageSendResponse,
    MessageGetAllResponse,
    MessageRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMessage:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: OpencodeSDK) -> None:
        message = client.session.message.retrieve(
            message_id="messageID",
            session_id="sessionID",
        )
        assert_matches_type(MessageRetrieveResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: OpencodeSDK) -> None:
        message = client.session.message.retrieve(
            message_id="messageID",
            session_id="sessionID",
            directory="directory",
        )
        assert_matches_type(MessageRetrieveResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: OpencodeSDK) -> None:
        response = client.session.message.with_raw_response.retrieve(
            message_id="messageID",
            session_id="sessionID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(MessageRetrieveResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: OpencodeSDK) -> None:
        with client.session.message.with_streaming_response.retrieve(
            message_id="messageID",
            session_id="sessionID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(MessageRetrieveResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: OpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.session.message.with_raw_response.retrieve(
                message_id="messageID",
                session_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            client.session.message.with_raw_response.retrieve(
                message_id="",
                session_id="sessionID",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_all(self, client: OpencodeSDK) -> None:
        message = client.session.message.get_all(
            session_id="sessionID",
        )
        assert_matches_type(MessageGetAllResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_all_with_all_params(self, client: OpencodeSDK) -> None:
        message = client.session.message.get_all(
            session_id="sessionID",
            directory="directory",
            limit=0,
        )
        assert_matches_type(MessageGetAllResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_all(self, client: OpencodeSDK) -> None:
        response = client.session.message.with_raw_response.get_all(
            session_id="sessionID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert_matches_type(MessageGetAllResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_all(self, client: OpencodeSDK) -> None:
        with client.session.message.with_streaming_response.get_all(
            session_id="sessionID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert_matches_type(MessageGetAllResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_all(self, client: OpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.session.message.with_raw_response.get_all(
                session_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_send(self, client: OpencodeSDK) -> None:
        message = client.session.message.send(
            session_id="sessionID",
            parts=[
                {
                    "text": "text",
                    "type": "text",
                }
            ],
        )
        assert_matches_type(MessageSendResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_send_with_all_params(self, client: OpencodeSDK) -> None:
        message = client.session.message.send(
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
        )
        assert_matches_type(MessageSendResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_send(self, client: OpencodeSDK) -> None:
        response = client.session.message.with_raw_response.send(
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
        message = response.parse()
        assert_matches_type(MessageSendResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_send(self, client: OpencodeSDK) -> None:
        with client.session.message.with_streaming_response.send(
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

            message = response.parse()
            assert_matches_type(MessageSendResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_send(self, client: OpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.session.message.with_raw_response.send(
                session_id="",
                parts=[
                    {
                        "text": "text",
                        "type": "text",
                    }
                ],
            )


class TestAsyncMessage:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncOpencodeSDK) -> None:
        message = await async_client.session.message.retrieve(
            message_id="messageID",
            session_id="sessionID",
        )
        assert_matches_type(MessageRetrieveResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncOpencodeSDK) -> None:
        message = await async_client.session.message.retrieve(
            message_id="messageID",
            session_id="sessionID",
            directory="directory",
        )
        assert_matches_type(MessageRetrieveResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.session.message.with_raw_response.retrieve(
            message_id="messageID",
            session_id="sessionID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(MessageRetrieveResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.session.message.with_streaming_response.retrieve(
            message_id="messageID",
            session_id="sessionID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(MessageRetrieveResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncOpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.session.message.with_raw_response.retrieve(
                message_id="messageID",
                session_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            await async_client.session.message.with_raw_response.retrieve(
                message_id="",
                session_id="sessionID",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_all(self, async_client: AsyncOpencodeSDK) -> None:
        message = await async_client.session.message.get_all(
            session_id="sessionID",
        )
        assert_matches_type(MessageGetAllResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_all_with_all_params(self, async_client: AsyncOpencodeSDK) -> None:
        message = await async_client.session.message.get_all(
            session_id="sessionID",
            directory="directory",
            limit=0,
        )
        assert_matches_type(MessageGetAllResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_all(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.session.message.with_raw_response.get_all(
            session_id="sessionID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert_matches_type(MessageGetAllResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_all(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.session.message.with_streaming_response.get_all(
            session_id="sessionID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert_matches_type(MessageGetAllResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_all(self, async_client: AsyncOpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.session.message.with_raw_response.get_all(
                session_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_send(self, async_client: AsyncOpencodeSDK) -> None:
        message = await async_client.session.message.send(
            session_id="sessionID",
            parts=[
                {
                    "text": "text",
                    "type": "text",
                }
            ],
        )
        assert_matches_type(MessageSendResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_send_with_all_params(self, async_client: AsyncOpencodeSDK) -> None:
        message = await async_client.session.message.send(
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
        )
        assert_matches_type(MessageSendResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_send(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.session.message.with_raw_response.send(
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
        message = await response.parse()
        assert_matches_type(MessageSendResponse, message, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_send(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.session.message.with_streaming_response.send(
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

            message = await response.parse()
            assert_matches_type(MessageSendResponse, message, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_send(self, async_client: AsyncOpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.session.message.with_raw_response.send(
                session_id="",
                parts=[
                    {
                        "text": "text",
                        "type": "text",
                    }
                ],
            )
