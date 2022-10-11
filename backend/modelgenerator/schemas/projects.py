from typing import List, Union
from pydantic import BaseModel
from datetime import datetime


class ProjectBase(BaseModel):
    name: str


class ProjectCreate(ProjectBase):
    pass


class ProjectUpdate(ProjectBase):
    id: int
    description: Union[str, None]
    user_id = Union[int, None]


class Project(ProjectBase):
    id: int
    description: Union[str, None]
    created_at = Union[datetime, None]
    updated_at = Union[datetime, None]
    user_id = int