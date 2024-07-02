from datetime import datetime
from typing import Union
from modelgenerator.utils import check_password_policy
from pydantic import BaseModel, EmailStr, ValidationError, model_validator


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


class ForgetPassword(BaseModel):
    email: EmailStr


class ForgetPasswordResponse(BaseModel):
    message: str
    url: str


class UserBase(BaseModel):
    email: EmailStr
    is_admin: bool


class PasswordBase(BaseModel):
    password: str
    password_confirmation: str


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
    created_at: Union[datetime, None] = None
    updated_at: Union[datetime, None] = None
    activated_at: Union[datetime, None] = None

    class Config:
        from_attributes = True


class UserRegister(PasswordBase):
    username: Union[str, None] = None
    lastname: Union[str, None]
    firstname: Union[str, None]
    phone: Union[str, None]
    created_at: Union[datetime, None] = None
    updated_at: Union[datetime, None] = None
    activated_at: Union[datetime, None] = None


class ResetPassword(PasswordBase):
    token: str
    alt_password: str
