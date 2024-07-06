import os
import jwt
from datetime import datetime, timedelta, timezone
from typing import Annotated, List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext
from modelgenerator.dependencies import get_db
from modelgenerator.dependencies import get_current_user, get_user_by_token
from modelgenerator.models import User as UserModel
from modelgenerator.schemas.users import Token, ResetPassword, ForgetPasswordResponse
from modelgenerator.schemas.users import User as UserSchema, UserRegister, ForgetPassword
from modelgenerator.schemas.users import UserUpdate as UserUpdateSchema


SECRET_KEY = os.environ.get("SECRET_KEY")
ALGORITHM = os.environ.get("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = float(os.environ.get("ACCESS_TOKEN_EXPIRE_MINUTES", 15))
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def authenticate_user(username: str, password: str, db: Session) -> UserSchema | None:
    db_user: UserModel = db.query(UserModel).filter_by(email=username).first()
    if not db_user or not verify_password(password, db_user.hashed_password):
        return None
    return db_user


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def get_current_active_user(
    current_user: Annotated[UserSchema, Depends(get_current_user)],
):
    if current_user.activated_at is None:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


@router.get(
    "",
    response_model=List[UserSchema],
    responses={403: {"description": "Operation forbidden"}},
)
async def read_users(db: Session = Depends(get_db)):
	try:
		data = db.query(UserModel).all()
		return data
	except Exception as e:
		print("Error: ", str(e))
		raise HTTPException(
			status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
		)


@router.post(
    "/login",
    response_model=Token,
    responses={403: {"description": "Operation forbidden"}}
)
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: Session = Depends(get_db)
) -> Token:
    user: UserSchema = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")


@router.post(
    "/refresh-token",
    response_model=Token,
    responses={403: {"description": "Operation forbidden"}}
)
async def refresh_token(current_user: Annotated[UserSchema, Depends(get_current_active_user)]):
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": current_user.email}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")


@router.post(
    "/register",
    response_model=UserSchema,
    responses={403: {"description": "Operation forbidden"}}
)
async def register_user(user: UserRegister, db: Session = Depends(get_db)):
    try:
        db_user: UserModel = UserModel()
        db_user.username = user.username
        db_user.email = user.email
        db_user.lastname = user.lastname
        db_user.firstname = user.firstname
        db_user.phone = user.phone
        db_user.hashed_password = get_password_hash(user.password)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
        )


@router.get("/me", response_model=UserSchema)
async def read_users_me(
    current_user: Annotated[UserSchema, Depends(get_current_user)],
):
    return current_user


@router.post(
    "activate/{user_id}",
    response_model=UserSchema,
    responses={403: {"description": "Operation forbidden"}},
)
async def activate_user(user_id: int, current_user: Annotated[UserSchema, Depends(get_current_user)], db: Session = Depends(get_db)):
    user: UserModel = db.query(UserModel).filter_by(id=user_id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="user not found"
        )
    if current_user.id != user.id and not current_user.is_admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Operation forbidden"
        )
    try:
        user.activated_at = datetime.now()
        db.commit()
        db.refresh(user)
        return user
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
        )


@router.get(
    "activate-link/{token}",
    response_model=UserSchema,
    responses={403: {"description": "Operation forbidden"}},
)
async def activate_user_by_token(token: str, db: Session = Depends(get_db)):
    current_user = get_user_by_token(token, db)
    if not current_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="user not found"
        )
    try:
        current_user.activated_at = datetime.now()
        db.commit()
        db.refresh(current_user)
        return current_user
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
        )


@router.post(
    "/forgot-password",
    response_model=ForgetPasswordResponse,
    responses={403: {"description": "Operation forbidden"}},
)
async def forgot_password(data: ForgetPassword, db: Session = Depends(get_db)):
    print(db, data)
    try:
        user: UserModel = db.query(UserModel).filter_by(email=data.email).first()
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="user not found"
            )
        # generate token
        token = create_access_token(data={"sub": user.email}, expires_delta=timedelta(days=1))
        APP_URL = os.environ.get("WEBSITE_DOMAIN", "http://localhost:5173")
        url = f"{APP_URL}/reset-password/{token}"
        # send email
        return ForgetPasswordResponse(
            message=f"Reset password link sent to {user.email}",
            url=url
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
        )


@router.post(
    "/reset-password",
    response_model=UserSchema,
    responses={403: {"description": "Operation forbidden"}},
)
async def reset_password(data: ResetPassword, db: Session = Depends(get_db)):
    user: UserModel = get_user_by_token(data.token, db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="user not found"
        )
    try:
        user.hashed_password = get_password_hash(data.password)
        db.commit()
        db.refresh(user)
        return user
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
        )


@router.get(
    "/{user_id}",
    response_model=UserSchema,
    responses={403: {"description": "Operation forbidden"}},
)
async def get_user(user_id: int, db: Session = Depends(get_db)):
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
