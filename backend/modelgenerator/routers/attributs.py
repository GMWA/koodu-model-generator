from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from modelgenerator.schemas.attributs import (Attribut as AttributSchema,
                                AttributCreate as AttributCreateSchema,
                                AttributUpdate as AttributUpdateSchema)
from modelgenerator.models import Attribut as AttributModel
from modelgenerator.dependencies import get_db

router = APIRouter(
    prefix="/attributs",
    tags=["attributs"],
    responses={404: {"description": "Not found"}},
)


@router.get(
    "",
    response_model=List[AttributSchema],
    responses={403: {"description": "Operation forbidden"}}
)
async def read_attributs(db: Session = Depends(get_db)):
    data = db.query(AttributModel).all()
    return data


@router.get(
    "/{attribut_id}",
    response_model=AttributSchema,
    responses={403: {"description": "Operation forbidden"}},
)
async def get_attribut(attribut_id: int, db: Session = Depends(get_db)):
    data = db.query(AttributModel).filter_by(id=attribut_id).first()
    return data


@router.post(
    "",
    response_model=AttributSchema,
    responses={403: {"description": "Operation forbidden"}},
)
async def create_attribut(
    attribut: AttributCreateSchema,
    db: Session = Depends(get_db)
):
    return {}


@router.put(
    "/{attribut_id}",
    responses={403: {"description": "Operation forbidden"}},
)
async def update_attribut(
    attribut_id: int,
    attribut: AttributUpdateSchema,
    db: Session = Depends(get_db)
):
    return {}


@router.delete(
    "/{attribut_id}",
    response_model=AttributSchema,
    responses={403: {"description": "Operation forbidden"}},
)
async def delete_attribut(attribut_id: int, db: Session = Depends(get_db)):
    attrib = db.query(AttributModel).get(attribut_id)
    if not attrib:
        raise HTTPException(status_code=400, detail="Bad attribut's id!")
    try:
        db.delete(attrib)
        db.commit()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return attrib
