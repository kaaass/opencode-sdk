# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["SkillListResponse", "SkillListResponseItem"]


class SkillListResponseItem(BaseModel):
    description: str

    location: str

    name: str

    use_when: Optional[str] = FieldInfo(alias="useWhen", default=None)


SkillListResponse: TypeAlias = List[SkillListResponseItem]
