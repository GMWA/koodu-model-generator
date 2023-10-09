from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from modelgenerator.dependencies import get_db
from modelgenerator.models import Attribut as AttributModel
from modelgenerator.models import Project as ProjectModel
from modelgenerator.models import Table as TableModel
from modelgenerator.schemas.commons import CommonProject

router = APIRouter(
    prefix="",
    tags=[],
    responses={404: {"description": "Not found"}},
)


@router.get(
    "/project-json/{project_id}",
    response_model=CommonProject,
    responses={403: {"description": "Operation forbidden"}},
)
async def get_project_as_json(project_id: int, db: Session = Depends(get_db)):
    data: ProjectModel = db.query(ProjectModel).filter_by(id=project_id).first()
    if not data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Bad project's id!"
        )
    project = data.to_json()
    tables = []
    db_tables: List[TableModel] = (
        db.query(TableModel).filter_by(project_id=project_id).all()
    )
    for tab in db_tables:
        tab_json = tab.to_json()
        attributs = []
        db_Attribs: List[AttributModel] = (
            db.query(AttributModel).filter_by(table_id=tab.id).all()
        )
        for attr in db_Attribs:
            attr_json = attr.to_json()
            attributs.append(attr_json)
        tab_json["attributs"] = attributs
        tables.append(tab_json)
    project["tables"] = tables
    return project
