from typing import List, Union
from pydantic import BaseModel
from pydantic_choices import choice
from datetime import datetime


class AttributBase(BaseModel):
    name: str
    primary_key: bool
    index_key: bool
    unique_key: bool
    type: choice(["int", "str"])
    size: Union[int, None]


class AttributCreate(AttributBase):
    description: Union[str, None]


class AttributUpdate(AttributBase):
    id: int
    description: Union[str, None]
    table_id: Union[int, None]


class Attribut(AttributBase):
    id: int
    description: Union[str, None]
    created_at: datetime
    updated_at: datetime
    table_id: int
    