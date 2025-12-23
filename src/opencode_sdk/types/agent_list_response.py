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

    doom_loop: Optional[Literal["ask", "allow", "deny"]] = None

    external_directory: Optional[Literal["ask", "allow", "deny"]] = None

    webfetch: Optional[Literal["ask", "allow", "deny"]] = None


class AgentListResponseItemModel(BaseModel):
    api_model_id: str = FieldInfo(alias="modelID")

    provider_id: str = FieldInfo(alias="providerID")


class AgentListResponseItem(BaseModel):
    mode: Literal["subagent", "primary", "all"]

    name: str

    options: Dict[str, object]

    permission: AgentListResponseItemPermission

    tools: Dict[str, bool]

    color: Optional[str] = None

    description: Optional[str] = None

    hidden: Optional[bool] = None

    max_steps: Optional[int] = FieldInfo(alias="maxSteps", default=None)

    model: Optional[AgentListResponseItemModel] = None

    native: Optional[bool] = None

    prompt: Optional[str] = None

    sub_agents: Optional[List[str]] = FieldInfo(alias="subAgents", default=None)

    temperature: Optional[float] = None

    top_p: Optional[float] = FieldInfo(alias="topP", default=None)


AgentListResponse: TypeAlias = List[AgentListResponseItem]
