import os
import jwt
from fastapi import Depends, HTTPException, status
from modelgenerator.database import SessionLocal
from typing import Annotated
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer
from jwt.exceptions import InvalidTokenError
from modelgenerator.models import User as UserModel
from modelgenerator.schemas.users import TokenData
from modelgenerator.schemas.users import User


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
SECRET_KEY = os.environ.get("SECRET_KEY")
ALGORITHM = os.environ.get("ALGORITHM")

def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception as e:
        db.rollback()
        print(e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    finally:
        if db:
            db.close()



async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)], db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except InvalidTokenError:
        raise credentials_exception
    user = db.query(UserModel).filter_by(email=token_data.username).first()
    if user is None: # or not user.activated_at:
        raise credentials_exception
    return user
