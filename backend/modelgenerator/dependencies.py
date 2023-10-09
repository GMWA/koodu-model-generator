from fastapi import HTTPException, status

from modelgenerator.database import SessionLocal


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
