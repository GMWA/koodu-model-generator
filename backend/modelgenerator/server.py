from fastapi import FastAPI

from dotenv import load_dotenv
load_dotenv()

from .models import Base
from .routers.attributs import router as attributs_router
from .routers.projects import router as projects_router
from .routers.tables import router as tables_router
from .routers.users import router as users_router
from .database import engine


Base.metadata.create_all(bind=engine)
app = FastAPI()


app.include_router(attributs_router)
app.include_router(projects_router)
app.include_router(tables_router)
app.include_router(users_router)


@app.get("/")
async def root():
    return {"message": "Modelgenerator Backend made with FastApi"}