from datetime import datetime
from typing import Union
from modelgenerator.utils import check_password_policy
from pydantic import BaseModel, ValidationError, model_validator


class UserBase(BaseModel):
    email: str
    is_admin: bool


class UserCreate(UserBase):
    pass


class UserUpdate(UserBase):
    id: int
    username: Union[str, None] = None
    lastname: Union[str, None]
    firstname: Union[str, None]
    phone: Union[str, None]


class User(UserBase):
    id: int
    username: Union[str, None] = None
    lastname: Union[str, None] = None
    firstname: Union[str, None] = None
    phone: Union[str, None] = None
    created_at: datetime
    updated_at: datetime
    activated_at: Union[datetime, None] = None

    class config:
        from_attributes = True


class UserRegister(UserBase):
    username: Union[str, None] = None
    lastname: Union[str, None]
    firstname: Union[str, None]
    phone: Union[str, None]
    password: str
    password_confirmation: str
    created_at: Union[datetime, None] = None
    updated_at: Union[datetime, None] = None
    activated_at: Union[datetime, None] = None

    @model_validator(mode='after')
    def validate(self):
        if not check_password_policy(self.password):
            print("Password does not meet the policy")
            raise ValidationError(
                [
                    {
                        "loc": ["password"],
                        "msg": "Password does not meet the policy",
                        "type": "value_error",
                    }
                ],
                self,
            )
        if not self.password == self.password_confirmation:
            print("Passwords do not match")
            raise ValidationError(
                [
                    {
                        "loc": ["password_confirmation"],
                        "msg": "Passwords do not match",
                        "type": "value_error",
                    }
                ],
                self,
            )
        return self
