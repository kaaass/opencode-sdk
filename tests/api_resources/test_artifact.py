# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from tests.utils import assert_matches_type
from opencode_sdk import OpencodeSDK, AsyncOpencodeSDK
from opencode_sdk.types import ArtifactDeleteResponse
from opencode_sdk._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestArtifact:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: OpencodeSDK) -> None:
        artifact = client.artifact.delete(
            artifact_id="artifactID",
            session_id="sessionID",
        )
        assert_matches_type(ArtifactDeleteResponse, artifact, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete_with_all_params(self, client: OpencodeSDK) -> None:
        artifact = client.artifact.delete(
            artifact_id="artifactID",
            session_id="sessionID",
            directory="directory",
        )
        assert_matches_type(ArtifactDeleteResponse, artifact, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: OpencodeSDK) -> None:
        response = client.artifact.with_raw_response.delete(
            artifact_id="artifactID",
            session_id="sessionID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        artifact = response.parse()
        assert_matches_type(ArtifactDeleteResponse, artifact, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: OpencodeSDK) -> None:
        with client.artifact.with_streaming_response.delete(
            artifact_id="artifactID",
            session_id="sessionID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            artifact = response.parse()
            assert_matches_type(ArtifactDeleteResponse, artifact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: OpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `artifact_id` but received ''"):
            client.artifact.with_raw_response.delete(
                artifact_id="",
                session_id="sessionID",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_download(self, client: OpencodeSDK, respx_mock: MockRouter) -> None:
        respx_mock.get("/artifact/artifactID/download").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        artifact = client.artifact.download(
            artifact_id="artifactID",
            session_id="sessionID",
        )
        assert artifact.is_closed
        assert artifact.json() == {"foo": "bar"}
        assert cast(Any, artifact.is_closed) is True
        assert isinstance(artifact, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_download_with_all_params(self, client: OpencodeSDK, respx_mock: MockRouter) -> None:
        respx_mock.get("/artifact/artifactID/download").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        artifact = client.artifact.download(
            artifact_id="artifactID",
            session_id="sessionID",
            directory="directory",
        )
        assert artifact.is_closed
        assert artifact.json() == {"foo": "bar"}
        assert cast(Any, artifact.is_closed) is True
        assert isinstance(artifact, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_download(self, client: OpencodeSDK, respx_mock: MockRouter) -> None:
        respx_mock.get("/artifact/artifactID/download").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        artifact = client.artifact.with_raw_response.download(
            artifact_id="artifactID",
            session_id="sessionID",
        )

        assert artifact.is_closed is True
        assert artifact.http_request.headers.get("X-Stainless-Lang") == "python"
        assert artifact.json() == {"foo": "bar"}
        assert isinstance(artifact, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_download(self, client: OpencodeSDK, respx_mock: MockRouter) -> None:
        respx_mock.get("/artifact/artifactID/download").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.artifact.with_streaming_response.download(
            artifact_id="artifactID",
            session_id="sessionID",
        ) as artifact:
            assert not artifact.is_closed
            assert artifact.http_request.headers.get("X-Stainless-Lang") == "python"

            assert artifact.json() == {"foo": "bar"}
            assert cast(Any, artifact.is_closed) is True
            assert isinstance(artifact, StreamedBinaryAPIResponse)

        assert cast(Any, artifact.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_download(self, client: OpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `artifact_id` but received ''"):
            client.artifact.with_raw_response.download(
                artifact_id="",
                session_id="sessionID",
            )


class TestAsyncArtifact:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncOpencodeSDK) -> None:
        artifact = await async_client.artifact.delete(
            artifact_id="artifactID",
            session_id="sessionID",
        )
        assert_matches_type(ArtifactDeleteResponse, artifact, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncOpencodeSDK) -> None:
        artifact = await async_client.artifact.delete(
            artifact_id="artifactID",
            session_id="sessionID",
            directory="directory",
        )
        assert_matches_type(ArtifactDeleteResponse, artifact, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncOpencodeSDK) -> None:
        response = await async_client.artifact.with_raw_response.delete(
            artifact_id="artifactID",
            session_id="sessionID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        artifact = await response.parse()
        assert_matches_type(ArtifactDeleteResponse, artifact, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncOpencodeSDK) -> None:
        async with async_client.artifact.with_streaming_response.delete(
            artifact_id="artifactID",
            session_id="sessionID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            artifact = await response.parse()
            assert_matches_type(ArtifactDeleteResponse, artifact, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncOpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `artifact_id` but received ''"):
            await async_client.artifact.with_raw_response.delete(
                artifact_id="",
                session_id="sessionID",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_download(self, async_client: AsyncOpencodeSDK, respx_mock: MockRouter) -> None:
        respx_mock.get("/artifact/artifactID/download").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        artifact = await async_client.artifact.download(
            artifact_id="artifactID",
            session_id="sessionID",
        )
        assert artifact.is_closed
        assert await artifact.json() == {"foo": "bar"}
        assert cast(Any, artifact.is_closed) is True
        assert isinstance(artifact, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_download_with_all_params(
        self, async_client: AsyncOpencodeSDK, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/artifact/artifactID/download").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        artifact = await async_client.artifact.download(
            artifact_id="artifactID",
            session_id="sessionID",
            directory="directory",
        )
        assert artifact.is_closed
        assert await artifact.json() == {"foo": "bar"}
        assert cast(Any, artifact.is_closed) is True
        assert isinstance(artifact, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_download(self, async_client: AsyncOpencodeSDK, respx_mock: MockRouter) -> None:
        respx_mock.get("/artifact/artifactID/download").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        artifact = await async_client.artifact.with_raw_response.download(
            artifact_id="artifactID",
            session_id="sessionID",
        )

        assert artifact.is_closed is True
        assert artifact.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await artifact.json() == {"foo": "bar"}
        assert isinstance(artifact, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_download(self, async_client: AsyncOpencodeSDK, respx_mock: MockRouter) -> None:
        respx_mock.get("/artifact/artifactID/download").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.artifact.with_streaming_response.download(
            artifact_id="artifactID",
            session_id="sessionID",
        ) as artifact:
            assert not artifact.is_closed
            assert artifact.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await artifact.json() == {"foo": "bar"}
            assert cast(Any, artifact.is_closed) is True
            assert isinstance(artifact, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, artifact.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_download(self, async_client: AsyncOpencodeSDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `artifact_id` but received ''"):
            await async_client.artifact.with_raw_response.download(
                artifact_id="",
                session_id="sessionID",
            )
