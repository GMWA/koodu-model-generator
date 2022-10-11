from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..schemas.tables import (Table as TableSchema,
                                TableCreate as TableCreateSchema,
                                TableUpdate as TableUpdateSchema)
from ..models import Table as TableModel
from ..dependencies import get_db

router = APIRouter(
    prefix="/tables",
    tags=["tables"],
    responses={404: {"description": "Not found"}},
)


@router.get(
    "/",
    response_model=List[TableModel],
    responses={403: {"description": "Operation forbidden"}}
)
async def read_tables(db: Session = Depends(get_db)):
    data = db.query(TableModel).all()
    return data


@router.get(
    "/{table_id}",
    response_model=TableModel,
    responses={403: {"description": "Operation forbidden"}},
)
async def get_Table(table_id: int, db: Session = Depends(get_db)):
    data = db.query(TableModel).filter_by(id=table_id).first()
    return data


@router.post(
    "/",
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
    responses={403: {"description": "Operation forbidden"}},
)
async def delete_Table(table_id: int, db: Session = Depends(get_db)):
    return {}
