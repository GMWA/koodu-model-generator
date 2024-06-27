import os

from dotenv import load_dotenv
from fastapi import FastAPI

load_dotenv()

from starlette.middleware.cors import CORSMiddleware
from modelgenerator.database import engine
from modelgenerator.models import Base
from modelgenerator.routers.attributs import router as attributs_router
from modelgenerator.routers.commons import router as commons_router
from modelgenerator.routers.projects import router as projects_router
from modelgenerator.routers.tables import router as tables_router
from modelgenerator.routers.users import router as users_router
from modelgenerator.routers.tokens import router as tokens_router

Base.metadata.create_all(bind=engine)
app = FastAPI(docs_url="/api/docs")

origins = [
    "http://localhost:9000",
]


# app.add_middleware(get_middleware())
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add the app Endpoints
app.include_router(attributs_router, prefix="/api")
app.include_router(commons_router, prefix="/api")
app.include_router(projects_router, prefix="/api")
app.include_router(tables_router, prefix="/api")
app.include_router(users_router, prefix="/api")
app.include_router(tokens_router, prefix="/api")


@app.get("/")
async def root():
    return {"message": "Modelgenerator Backend made with FastApi"}
