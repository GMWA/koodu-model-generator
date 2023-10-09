from datetime import datetime
from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from supertokens_python.recipe.session import SessionContainer
from supertokens_python.recipe.session.framework.fastapi import verify_session
from supertokens_python.recipe.thirdpartyemailpassword.asyncio import \
    get_user_by_id

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


@router.post(
    "",
    response_model=UserSchema,
    responses={403: {"description": "Operation forbidden"}},
)
async def create_user(
    session: SessionContainer = Depends(verify_session()), db: Session = Depends(get_db)
):
    user_id = session.get_user_id()
    s_user = await get_user_by_id(user_id)
    if not s_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Not logged user!"
        )
    db_user = UserModel()
    db_user.id = s_user.user_id
    db_user.email = s_user.email
    db_user.thirdparty = s_user.third_party_info.id
    db_user.created_at = datetime.fromtimestamp(s_user.time_joined / 1e3)
    db_user.updated_at = datetime.fromtimestamp(s_user.time_joined / 1e3)
    try:
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
        )
    return db_user


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
