from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from modelgenerator.schemas.projects import (Project as ProjectSchema,
                                ProjectCreate as ProjectCreateSchema,
                                ProjectUpdate as ProjectUpdateSchema)
from modelgenerator.models import Project as ProjectModel
from modelgenerator.dependencies import get_db

router = APIRouter(
    prefix="/projects",
    tags=["projects"],
    responses={404: {"description": "Not found"}},
)


@router.get(
    "",
    response_model=List[ProjectSchema],
    responses={403: {"description": "Operation forbidden"}}
)
async def read_projects(db: Session = Depends(get_db)):
    data = db.query(ProjectModel).all()
    return data


@router.get(
    "/{project_id}",
    response_model=ProjectSchema,
    responses={403: {"description": "Operation forbidden"}},
)
async def get_project(project_id: int, db: Session = Depends(get_db)):
    data = db.query(ProjectModel).filter_by(id=project_id).first()
    return data


@router.post(
    "",
    response_model=ProjectSchema,
    responses={403: {"description": "Operation forbidden"}},
)
async def create_project(
    project: ProjectCreateSchema,
    db: Session = Depends(get_db)
):
    db_project: ProjectModel = ProjectModel()
    db_project.name = project.name
    db_project.description = project.description
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project


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
    response_model=ProjectSchema,
    responses={403: {"description": "Operation forbidden"}},
)
async def delete_project(project_id: int, db: Session = Depends(get_db)):
    project = db.query(ProjectModel).get(project_id)
    if not project:
        raise HTTPException(status_code=400, detail="Bad project's id!")
    try:
        db.delete(project)
        db.commit()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return project
