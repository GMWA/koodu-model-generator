from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from modelgenerator.schemas.users import (User as UserSchema,
                                UserCreate as UserCreateSchema,
                                UserUpdate as UserUpdateSchema)
from modelgenerator.models import User as UserModel
from modelgenerator.dependencies import get_db
from supertokens_python.recipe.session.framework.fastapi import verify_session
from supertokens_python.recipe.thirdpartyemailpassword.asyncio import get_user_by_id
from supertokens_python.recipe.session import SessionContainer


router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)


@router.get(
    "",
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
    "",
    response_model=UserSchema,
    responses={403: {"description": "Operation forbidden"}},
)
async def create_user(
    session: SessionContainer = Depends(verify_session()),
    db: Session = Depends(get_db)
):
    user_id = session.get_user_id()
    s_user = await get_user_by_id(user_id)
    if not s_user:
        raise HTTPException(status_code=500, detail="Not logged user!")

    db_user = UserModel()
    db_user.id = s_user.user_id
    db_user.email = s_user.email
    db_user.thirdparty = s_user.third_party_info
    db_user.created_at = s_user.time_joined
    db_user.updated_at = s_user.time_joined

    try:
        db.add(db_user)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return db_user


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
