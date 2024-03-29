from datetime import datetime
from typing import Union

from pydantic import BaseModel
from pydantic_choices import choice


class AttributBase(BaseModel):
    name: str
    primary_key: bool
    index_key: bool
    unique_key: bool
    is_required: bool
    type: choice([
        "int", "str", "float", "bool",
        "datetime", "time", "date", "ref"
    ])
    size: Union[int, None]
    table_id: int


class AttributCreate(AttributBase):
    description: Union[str, None] = None


class AttributUpdate(AttributBase):
    id: int
    description: Union[str, None]


class Attribut(AttributBase):
    id: int
    description: Union[str, None]
    created_at: datetime
    updated_at: datetime
    table_id: int

    class Config:
        orm_mode = True
