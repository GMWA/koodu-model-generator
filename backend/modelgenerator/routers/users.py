from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..schemas.users import (User as UserSchema,
                                UserCreate as UserCreateSchema,
                                UserUpdate as UserUpdateSchema)
from ..models import User as UserModel
from ..dependencies import get_db

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)


@router.get(
    "/",
    response_model=List[UserSchema],
    responses={403: {"description": "Operation forbidden"}}
)
async def read_users(db: Session = Depends(get_db)):
    data = db.query(UserModel).all()
    return data


@router.get(
    "/{user_id}",
    response_model=UserSchema,
    responses={403: {"description": "Operation forbidden"}},
)
async def get_user(user_id: int, db: Session = Depends(get_db)):
    data = db.query(UserModel).filter_by(id=user_id).first()
    return data


@router.post(
    "/",
    response_model=UserSchema,
    responses={403: {"description": "Operation forbidden"}},
)
async def create_user(
    user: UserCreateSchema,
    db: Session = Depends(get_db)
):
    return {}


@router.put(
    "/{user_id}",
    responses={403: {"description": "Operation forbidden"}},
)
async def update_user(
    user_id: int,
    user: UserUpdateSchema,
    db: Session = Depends(get_db)
):
    return {}


@router.delete(
    "/{user_id}",
    responses={403: {"description": "Operation forbidden"}},
)
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    return {}
