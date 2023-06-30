from typing import List, Union
from pydantic import BaseModel
from datetime import datetime


class ProjectBase(BaseModel):
    name: str


class ProjectCreate(ProjectBase):
    description: Union[str, None] = None


class ProjectUpdate(ProjectBase):
    id: int
    description: Union[str, None] = None
    user_id: Union[int, None] = None


class Project(ProjectBase):
    id: int
    description: Union[str, None] = None
    created_at: Union[datetime, None] = None
    updated_at: Union[datetime, None] = None
    user_id = int

    class Config:
        orm_mode = True