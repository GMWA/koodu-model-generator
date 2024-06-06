from enum import Enum
from datetime import datetime
from typing import Union

from pydantic import BaseModel
from modelgenerator.enums.types import TypeEnum

class AttributBase(BaseModel):
    name: str
    primary_key: bool
    index_key: bool
    unique_key: bool
    is_required: bool
    type: TypeEnum
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
