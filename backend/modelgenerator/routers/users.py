from datetime import datetime
from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from modelgenerator.dependencies import get_db
from modelgenerator.models import User as UserModel
from modelgenerator.schemas.users import User as UserSchema
from modelgenerator.schemas.users import UserUpdate as UserUpdateSchema

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)


@router.get(
    "",
    response_model=List[UserSchema],
    responses={403: {"description": "Operation forbidden"}},
)
async def read_users(db: Session = Depends(get_db)):
    data = db.query(UserModel).all()
    return data


@router.get(
    "/{user_id}",
    response_model=UserSchema,
    responses={403: {"description": "Operation forbidden"}},
)
async def get_user(user_id: str, db: Session = Depends(get_db)):
    user = db.query(UserModel).filter_by(id=user_id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="user not found"
        )
    return user


@router.put(
    "/{user_id}",
    responses={403: {"description": "Operation forbidden"}},
)
async def update_user(
    user_id: int, user: UserUpdateSchema, db: Session = Depends(get_db)
):
    return HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED)


@router.delete(
    "/{user_id}",
    responses={403: {"description": "Operation forbidden"}},
)
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    return HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED)
