# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from opencode_sdk import OpencodeSDK, AsyncOpencodeSDK
from opencode_sdk.types import (
    QuestionReplyResponse,
    QuestionRejectResponse,
    QuestionListPendingResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestQuestion:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_pending(self, client: OpencodeSDK) -> None:
        question = client.question.list_pending()
        assert_matches_type(QuestionListPendingResponse, question, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_pending_with_all_params(self, client: OpencodeSDK) -> None:
        question = client.question.list_pending(
            directory="directory",
        )
        assert_matches_type(QuestionListPendingResponse, question, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_pending(self, client: OpencodeSDK) -> None:
        response = client.question.with_raw_response.list_pending()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        question = response.parse()
        assert_matches_type(QuestionListPendingResponse, question, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_pending(self, client: OpencodeSDK) -> None:
        with client.question.with_streaming_response.list_pending() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            question = response.parse()
            assert_matches_type(QuestionListPendingResponse, question, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_reject(self, client: OpencodeSDK) -> None:
        question = client.question.reject(
            request_id="requestID",
        )
        assert_matches_type(QuestionRejectResponse, question, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_reject_with_all_params(self, client: OpencodeSDK) -> None:
        question = client.question.reject(
            request_id="requestID",
            directory="directory",
        )
        assert_matches_type(QuestionRejectResponse, question, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_reject(self, client: OpencodeSDK) -> None:
        response = client.question.with_raw_response.reject(
            request_id="requestID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        question = response.parse()
        assert_matches_type(QuestionRejectResponse, question, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_reject(self, client: OpencodeSDK) -> None:
        with client.question.with_streaming_response.reject(
            request_id="requestID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            question = response.parse()
            assert_matches_type(QuestionRejectResponse, question, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_reject(self, client: OpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `request_id` but received ''"):
            client.question.with_raw_response.reject(
                request_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_reply(self, client: OpencodeSDK) -> None:
        question = client.question.reply(
            request_id="requestID",
            answers=[["string"]],
        )
        assert_matches_type(QuestionReplyResponse, question, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_reply_with_all_params(self, client: OpencodeSDK) -> None:
        question = client.question.reply(
            request_id="requestID",
            answers=[["string"]],
            directory="directory",
        )
        assert_matches_type(QuestionReplyResponse, question, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_reply(self, client: OpencodeSDK) -> None:
        response = client.question.with_raw_response.reply(
            request_id="requestID",
            answers=[["string"]],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        question = response.parse()
        assert_matches_type(QuestionReplyResponse, question, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_reply(self, client: OpencodeSDK) -> None:
        with client.question.with_streaming_response.reply(
            request_id="requestID",
            answers=[["string"]],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            question = response.parse()
            assert_matches_type(QuestionReplyResponse, question, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_reply(self, client: OpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `request_id` but received ''"):
            client.question.with_raw_response.reply(
                request_id="",
                answers=[["string"]],
            )


class TestAsyncQuestion:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_pending(self, async_client: AsyncOpencodeSDK) -> None:
        question = await async_client.question.list_pending()
        assert_matches_type(QuestionListPendingResponse, question, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_pending_with_all_params(self, async_client: AsyncOpencodeSDK) -> None:
        question = await async_client.question.list_pending(
            directory="directory",
        )
        assert_matches_type(QuestionListPendingResponse, question, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_pending(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.question.with_raw_response.list_pending()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        question = await response.parse()
        assert_matches_type(QuestionListPendingResponse, question, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_pending(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.question.with_streaming_response.list_pending() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            question = await response.parse()
            assert_matches_type(QuestionListPendingResponse, question, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_reject(self, async_client: AsyncOpencodeSDK) -> None:
        question = await async_client.question.reject(
            request_id="requestID",
        )
        assert_matches_type(QuestionRejectResponse, question, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_reject_with_all_params(self, async_client: AsyncOpencodeSDK) -> None:
        question = await async_client.question.reject(
            request_id="requestID",
            directory="directory",
        )
        assert_matches_type(QuestionRejectResponse, question, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_reject(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.question.with_raw_response.reject(
            request_id="requestID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        question = await response.parse()
        assert_matches_type(QuestionRejectResponse, question, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_reject(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.question.with_streaming_response.reject(
            request_id="requestID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            question = await response.parse()
            assert_matches_type(QuestionRejectResponse, question, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_reject(self, async_client: AsyncOpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `request_id` but received ''"):
            await async_client.question.with_raw_response.reject(
                request_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_reply(self, async_client: AsyncOpencodeSDK) -> None:
        question = await async_client.question.reply(
            request_id="requestID",
            answers=[["string"]],
        )
        assert_matches_type(QuestionReplyResponse, question, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_reply_with_all_params(self, async_client: AsyncOpencodeSDK) -> None:
        question = await async_client.question.reply(
            request_id="requestID",
            answers=[["string"]],
            directory="directory",
        )
        assert_matches_type(QuestionReplyResponse, question, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_reply(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.question.with_raw_response.reply(
            request_id="requestID",
            answers=[["string"]],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        question = await response.parse()
        assert_matches_type(QuestionReplyResponse, question, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_reply(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.question.with_streaming_response.reply(
            request_id="requestID",
            answers=[["string"]],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            question = await response.parse()
            assert_matches_type(QuestionReplyResponse, question, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_reply(self, async_client: AsyncOpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `request_id` but received ''"):
            await async_client.question.with_raw_response.reply(
                request_id="",
                answers=[["string"]],
            )
