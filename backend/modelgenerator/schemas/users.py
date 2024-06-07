from datetime import datetime
from typing import Union
from modelgenerator.utils import check_password_policy
from pydantic import BaseModel, ValidationError, model_validator


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
    activated_at: Union[datetime, None]

    # class Config:
    #     from_attributes = True


class UserRegister(User):
    password: str
    password_confirmation: str

    def validate(self):
        if not check_password_policy(self.password):
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
