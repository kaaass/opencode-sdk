# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["LspClientDiagnostics", "Properties"]


class Properties(BaseModel):
    path: str

    server_id: str = FieldInfo(alias="serverID")


class LspClientDiagnostics(BaseModel):
    properties: Properties

    type: Literal["lsp.client.diagnostics"]
