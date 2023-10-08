from datetime import datetime
from typing import Union

from pydantic import BaseModel


class UserBase(BaseModel):
    email: str
    thirdparty: str
    is_admin: bool


class UserCreate(UserBase):
    pass


class UserUpdate(UserBase):
    id: str
    username: Union[str, None] = None
    lastname: Union[str, None]
    firstname: Union[str, None]
    phone: Union[str, None]


class User(UserBase):
    id: str
    username: Union[str, None] = None
    lastname: Union[str, None]
    firstname: Union[str, None]
    phone: Union[str, None]
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
