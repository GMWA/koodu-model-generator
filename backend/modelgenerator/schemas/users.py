from typing import List, Union
from pydantic import BaseModel
from datetime import datetime


class UserBase(BaseModel):
    email: str
    username: str


class UserCreate(UserBase):
    description: Union[str, None]


class UserUpdate(UserBase):
    id: str
    lastname: Union[str, None]
    firstname: Union[str, None]
    phone: Union[str, None]
    password: Union[str, None]
    is_verified: Union[bool, None]


class User(UserBase):
    id: str
    lastname: Union[str, None]
    firstname: Union[str, None]
    phone: Union[str, None]
    is_verified: Union[bool, None]
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True