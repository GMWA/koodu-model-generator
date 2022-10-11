from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..schemas.projects import (Project as ProjectSchema,
                                ProjectCreate as ProjectCreateSchema,
                                ProjectUpdate as ProjectUpdateSchema)
from ..models import Project as ProjectModel
from ..dependencies import get_db

router = APIRouter(
    prefix="/projects",
    tags=["projects"],
    responses={404: {"description": "Not found"}},
)


@router.get(
    "/",
    response_model=List[ProjectModel],
    responses={403: {"description": "Operation forbidden"}}
)
async def read_projects(db: Session = Depends(get_db)):
    data = db.query(ProjectModel).all()
    return data


@router.get(
    "/{project_id}",
    response_model=ProjectModel,
    responses={403: {"description": "Operation forbidden"}},
)
async def get_project(project_id: int, db: Session = Depends(get_db)):
    data = db.query(ProjectModel).filter_by(id=project_id).first()
    return data


@router.post(
    "/",
    response_model=ProjectSchema,
    responses={403: {"description": "Operation forbidden"}},
)
async def create_project(
    project: ProjectCreateSchema,
    db: Session = Depends(get_db)
):
    return {}


@router.put(
    "/{project_id}",
    responses={403: {"description": "Operation forbidden"}},
)
async def update_project(
    project_id: int,
    project: ProjectUpdateSchema,
    db: Session = Depends(get_db)
):
    return {}


@router.delete(
    "/{project_id}",
    responses={403: {"description": "Operation forbidden"}},
)
async def delete_project(project_id: int, db: Session = Depends(get_db)):
    return {}
