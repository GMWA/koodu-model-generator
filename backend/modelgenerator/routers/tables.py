from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from modelgenerator.schemas.tables import (Table as TableSchema,
                                TableCreate as TableCreateSchema,
                                TableUpdate as TableUpdateSchema)
from modelgenerator.models import (Table as TableModel,
                                   Project as ProjectModel)
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
    "/project/{project_id}",
    response_model=List[TableSchema],
    responses={403: {"description": "Operation forbidden"}}
)
async def read_tables_by_project(project_id: int, db: Session = Depends(get_db)):
    data = db.query(TableModel).filter_by(project_id=project_id).all()
    return data


@router.get(
    "/{table_id}",
    response_model=TableUpdateSchema,
    responses={403: {"description": "Operation forbidden"}},
)
async def get_Table(table_id: int, db: Session = Depends(get_db)):
    data = db.query(TableModel).get(table_id)
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
    db_project: ProjectModel = db.query(ProjectModel).get(table.project_id)
    if not db_project:
        raise HTTPException(status_code=404, detail="Project Not found!")
    db_table = TableModel()
    db_table.name = table.name
    db_table.project_id = table.project_id
    if table.description:
        db_table.description = table.description
    try:
        db.add(db_table)
        db.commit()
        db.refresh(db_table)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return db_table


@router.put(
    "/{table_id}",
    responses={403: {"description": "Operation forbidden"}},
)
async def update_table(
    table_id: int,
    table: TableUpdateSchema,
    db: Session = Depends(get_db)
):
    db_table: TableModel = db.query(TableModel).get(table_id)
    if not db_table:
        raise HTTPException(status_code=400, detail="Bad project's id!")
    try:
        db_table.name = table.name
        if table.description:
            db_table.description = table.description
        db.commit()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return db_table


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
