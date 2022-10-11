from typing import List, Union
from pydantic import BaseModel
from datetime import datetime


class UserBase(BaseModel):
    email: str
    username: str


class UserCreate(UserBase):
    description: Union[str, None]


class UserUpdate(UserBase):
    id: int
    lastname: Union[str, None]
    firstname: Union[str, None]
    phone: Union[str, None]
    password: Union[str, None]
    is_verified: Union[bool, None]


class User(UserBase):
    id: int
    lastname: Union[str, None]
    firstname: Union[str, None]
    phone: Union[str, None]
    is_verified: Union[bool, None]
    created_at: datetime
    updated_at: datetime