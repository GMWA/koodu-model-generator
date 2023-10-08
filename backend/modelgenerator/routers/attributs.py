from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from modelgenerator.dependencies import get_db
from modelgenerator.models import Attribut as AttributModel
from modelgenerator.schemas.attributs import Attribut as AttributSchema
from modelgenerator.schemas.attributs import \
    AttributCreate as AttributCreateSchema
from modelgenerator.schemas.attributs import \
    AttributUpdate as AttributUpdateSchema

router = APIRouter(
    prefix="/attributs",
    tags=["attributs"],
    responses={404: {"description": "Not found"}},
)


@router.get(
    "",
    response_model=List[AttributSchema],
    responses={403: {"description": "Operation forbidden"}},
)
async def read_attributs(db: Session = Depends(get_db)):
    data = db.query(AttributModel).all()
    return data


@router.get(
    "/table/{table_id}",
    response_model=List[AttributSchema],
    responses={403: {"description": "Operation forbidden"}},
)
async def read_attributs_by_table(table_id: int, db: Session = Depends(get_db)):
    data = db.query(AttributModel).filter_by(table_id=table_id).all()
    return data


@router.get(
    "/{attribut_id}",
    response_model=AttributSchema,
    responses={403: {"description": "Operation forbidden"}},
)
async def get_attribut(attribut_id: int, db: Session = Depends(get_db)):
    data = db.query(AttributModel).get(attribut_id)
    return data


@router.post(
    "",
    response_model=AttributSchema,
    responses={403: {"description": "Operation forbidden"}},
)
async def create_attribut(
    attribut: AttributCreateSchema, db: Session = Depends(get_db)
):
    db_attribut = AttributModel()
    db_attribut.table_id = attribut.table_id
    db_attribut.name = attribut.name
    db_attribut.primary_key = attribut.primary_key
    db_attribut.index_key = attribut.index_key
    db_attribut.unique_key = attribut.unique_key
    db_attribut.type = attribut.type
    db_attribut.size = attribut.size
    if attribut.description:
        db_attribut.description = attribut.description
    try:
        db.add(db_attribut)
        db.commit()
        db.refresh(db_attribut)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return db_attribut


@router.put(
    "/{attribut_id}",
    responses={403: {"description": "Operation forbidden"}},
)
async def update_attribut(
    attribut_id: int, attribut: AttributUpdateSchema, db: Session = Depends(get_db)
):
    db_attrib: AttributModel = db.query(AttributModel).get(attribut_id)
    if not db_attrib:
        raise HTTPException(status_code=400, detail="Bad project's id!")
    try:
        db_attrib.name = attribut.name
        db_attrib.primary_key = attribut.primary_key
        db_attrib.index_key = attribut.index_key
        db_attrib.unique_key = attribut.unique_key
        db_attrib.type = attribut.type
        db_attrib.size = attribut.size
        if attribut.description:
            db_attrib.description = attribut.description
        db.commit()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return db_attrib


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
