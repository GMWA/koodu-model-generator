from modelgenerator.database import SessionLocal
from fastapi import HTTPException, status

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
