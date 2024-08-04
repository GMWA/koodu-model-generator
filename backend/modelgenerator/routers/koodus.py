from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from modelgenerator.dependencies import get_db
from modelgenerator.models import Attribut as AttributModel
from modelgenerator.models import Project as ProjectModel
from modelgenerator.models import Table as TableModel
from modelgenerator.schemas.koodus import ExportModel, KooduProject
from modelgenerator.schemas.koodus import KooduTable


router = APIRouter(
    prefix="/koodu",
    tags=["koodu"],
    responses={404: {"description": "Not found"}},
)


@router.post(
    "/export-model",
    response_model=KooduProject,
    responses={403: {"description": "Operation forbidden"}},
)
def export_model(data: ExportModel, db: Session = Depends(get_db)):
    project: ProjectModel = db.query(ProjectModel).get(data.project)
    if not project:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Project Not found!"
        )
    project_resp = KooduProject(**project.to_json())
    tables: List[TableModel] = db.query(TableModel).filter_by(project_id=project.id).all()
    for table in tables:
        resp_table = KooduTable(**table.to_json())
        attributs: List[AttributModel] = db.query(AttributModel).filter_by(table_id=table.id).all()
        for attribut in attributs:
            resp_table.attributs.append(AttributModel(**attribut.to_json()))
        project_resp.tables.append(resp_table)
    return project_resp