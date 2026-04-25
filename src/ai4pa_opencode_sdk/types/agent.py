# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .permission_rule import PermissionRule

__all__ = ["Agent", "Model"]


class Model(BaseModel):
    api_model_id: str = FieldInfo(alias="modelID")

    provider_id: str = FieldInfo(alias="providerID")


class Agent(BaseModel):
    mode: Literal["subagent", "primary", "all"]

    name: str

    options: Dict[str, object]

    permission: List[PermissionRule]

    color: Optional[str] = None

    description: Optional[str] = None

    hidden: Optional[bool] = None

    model: Optional[Model] = None

    native: Optional[bool] = None

    prompt: Optional[str] = None

    skills: Optional[List[str]] = None

    steps: Optional[int] = None

    sub_agents: Optional[List[str]] = FieldInfo(alias="subAgents", default=None)

    temperature: Optional[float] = None

    top_p: Optional[float] = FieldInfo(alias="topP", default=None)

    variant: Optional[str] = None
