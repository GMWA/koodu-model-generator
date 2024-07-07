from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from modelgenerator.dependencies import get_db
from modelgenerator.models import Project as ProjectModel
from modelgenerator.schemas.projects import Project as ProjectSchema
from modelgenerator.schemas.projects import \
    ProjectCreate as ProjectCreateSchema
from modelgenerator.schemas.projects import \
    ProjectUpdate as ProjectUpdateSchema

router = APIRouter(
    prefix="/projects",
    tags=["projects"],
    responses={404: {"description": "Not found"}},
)


@router.get(
    "",
    response_model=List[ProjectSchema],
    responses={403: {"description": "Operation forbidden"}},
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
async def create_project(project: ProjectCreateSchema, db: Session = Depends(get_db)):
    db_project: ProjectModel = ProjectModel()
    db_project.name = project.name
    db_project.user_id = project.user_id
    db_project.description = project.description
    try:
        db.add(db_project)
        db.commit()
        db.refresh(db_project)
        return db_project
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
        )


@router.put(
    "/{project_id}",
    response_model=ProjectSchema,
    responses={403: {"description": "Operation forbidden"}},
)
async def update_project(
    project_id: int, project: ProjectUpdateSchema, db: Session = Depends(get_db)
):
    db_project: ProjectModel = (
        db.query(ProjectModel).filter_by(id=project_id).first()
    )
    if not db_project:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Bad project's id!"
        )
    try:
        db_project.name = project.name
        if project.description:
            db_project.description = project.description
        db.commit()
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
        )
    return db_project


@router.delete(
    "/{project_id}",
    response_model=ProjectSchema,
    responses={403: {"description": "Operation forbidden"}},
)
async def delete_project(project_id: int, db: Session = Depends(get_db)):
    project = db.query(ProjectModel).get(project_id)
    if not project:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Bad project's id!"
        )
    try:
        db.delete(project)
        db.commit()
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
        )
    return project
