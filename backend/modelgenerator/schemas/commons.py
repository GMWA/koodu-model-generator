from datetime import datetime
from typing import List, Union

from pydantic import BaseModel
from pydantic_choices import choice


class CommonBase(BaseModel):
    id: int


class CommonAttribut(CommonBase):
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
    description: Union[str, None]
    created_at: Union[datetime, None] = None
    updated_at: Union[datetime, None] = None
    table_id: int


class CommonTable(CommonBase):
    name: str
    description: Union[str, None]
    created_at: Union[datetime, None] = None
    updated_at: Union[datetime, None] = None
    project_id: int
    attributs: List[CommonAttribut]


class CommonProject(CommonBase):
    name: str
    description: Union[str, None] = None
    created_at: Union[datetime, None] = None
    updated_at: Union[datetime, None] = None
    user_id: str
    tables: List[CommonTable]
