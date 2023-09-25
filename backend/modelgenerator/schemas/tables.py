from typing import List, Union
from pydantic import BaseModel
from datetime import datetime


class TableBase(BaseModel):
    name: str
    project_id: int


class TableCreate(TableBase):
    description: Union[str, None]


class TableUpdate(TableBase):
    id: int
    description: Union[str, None]


class Table(TableBase):
    id: int
    description: Union[str, None]
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
