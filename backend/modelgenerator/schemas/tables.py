from typing import List, Union
from pydantic import BaseModel
from datetime import datetime


class TableBase(BaseModel):
    name: str


class TableCreate(TableBase):
    description: Union[str, None]


class TableUpdate(TableBase):
    id: int
    description: Union[str, None]
    table_id: Union[int, None]


class Table(TableBase):
    id: int
    description: Union[str, None]
    created_at: datetime
    updated_at: datetime
    user_id: int
