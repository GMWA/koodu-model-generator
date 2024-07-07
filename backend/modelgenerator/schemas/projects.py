from datetime import datetime
from typing import Union

from pydantic import BaseModel


class ProjectBase(BaseModel):
    name: str
    user_id: str


class ProjectCreate(ProjectBase):
    description: Union[str, None] = None


class ProjectUpdate(ProjectBase):
    id: int
    description: Union[str, None] = None


class Project(ProjectBase):
    id: int
    description: Union[str, None] = None
    created_at: Union[datetime, None] = None
    updated_at: Union[datetime, None] = None

    class Config:
        from_attributes = True
