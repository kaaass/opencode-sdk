# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "AgentListResponse",
    "AgentListResponseItem",
    "AgentListResponseItemPermission",
    "AgentListResponseItemModel",
]


class AgentListResponseItemPermission(BaseModel):
    bash: Dict[str, Literal["ask", "allow", "deny"]]

    edit: Literal["ask", "allow", "deny"]

    webfetch: Optional[Literal["ask", "allow", "deny"]] = None


class AgentListResponseItemModel(BaseModel):
    api_model_id: str = FieldInfo(alias="modelID")

    provider_id: str = FieldInfo(alias="providerID")


class AgentListResponseItem(BaseModel):
    built_in: bool = FieldInfo(alias="builtIn")

    mode: Literal["subagent", "primary", "all"]

    name: str

    options: Dict[str, object]

    permission: AgentListResponseItemPermission

    tools: Dict[str, bool]

    description: Optional[str] = None

    model: Optional[AgentListResponseItemModel] = None

    prompt: Optional[str] = None

    temperature: Optional[float] = None

    top_p: Optional[float] = FieldInfo(alias="topP", default=None)


AgentListResponse: TypeAlias = List[AgentListResponseItem]
