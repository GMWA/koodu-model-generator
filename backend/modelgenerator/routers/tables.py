from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from modelgenerator.schemas.tables import (Table as TableSchema,
                                TableCreate as TableCreateSchema,
                                TableUpdate as TableUpdateSchema)
from modelgenerator.models import Table as TableModel
from modelgenerator.dependencies import get_db

router = APIRouter(
    prefix="/tables",
    tags=["tables"],
    responses={404: {"description": "Not found"}},
)


@router.get(
    "",
    response_model=List[TableSchema],
    responses={403: {"description": "Operation forbidden"}}
)
async def read_tables(db: Session = Depends(get_db)):
    data = db.query(TableModel).all()
    return data


@router.get(
    "/{table_id}",
    response_model=TableUpdateSchema,
    responses={403: {"description": "Operation forbidden"}},
)
async def get_Table(table_id: int, db: Session = Depends(get_db)):
    data = db.query(TableModel).filter_by(id=table_id).first()
    return data


@router.post(
    "",
    response_model=TableSchema,
    responses={403: {"description": "Operation forbidden"}},
)
async def create_table(
    table: TableCreateSchema,
    db: Session = Depends(get_db)
):
    return {}


@router.put(
    "/{table_id}",
    responses={403: {"description": "Operation forbidden"}},
)
async def update_table(
    table_id: int,
    table: TableUpdateSchema,
    db: Session = Depends(get_db)
):
    return {}


@router.delete(
    "/{table_id}",
    response_model=TableSchema,
    responses={403: {"description": "Operation forbidden"}},
)
async def delete_Table(table_id: int, db: Session = Depends(get_db)):
    table = db.query(TableModel).get(table_id)
    if not table:
        raise HTTPException(status_code=400, detail="Bad table's id!")
    try:
        db.delete(table)
        db.commit()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return table
