from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..schemas.attributs import Attribut as AttributSchema
from ..models import Attribut as AttributModel
from ..dependencies import get_db

router = APIRouter(
    prefix="/attributs",
    tags=["attributs"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def read_attributs(db: Session = Depends(get_db)):
    data = db.query(AttributModel).all()
    return data


@router.get("/{attribut_id}")
async def get_attribut(attribut_id: int, db: Session = Depends(get_db)):
    data = db.query(AttributModel).filter_by(id=attribut_id).first()
    return data


@router.post(
    "/",
    tags=["attributs"],
    responses={403: {"description": "Operation forbidden"}},
)
async def create_attribut(attribut: AttributSchema, db: Session = Depends(get_db)):
    return {}


@router.put(
    "/{attribut_id}",
    tags=["attributs"],
    responses={403: {"description": "Operation forbidden"}},
)
async def update_attribut(
    attribut_id: int,
    attribut: AttributSchema,
    db: Session = Depends(get_db)
):
    return {}


@router.delete(
    "/{attribut_id}",
    tags=["attributs"],
    responses={403: {"description": "Operation forbidden"}},
)
async def delete_attribut(attribut_id: int, db: Session = Depends(get_db)):
    return {}
