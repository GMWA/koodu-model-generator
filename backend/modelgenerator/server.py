import os

from dotenv import load_dotenv
from fastapi import FastAPI

load_dotenv()

# List of required environment variables
REQUIRED_ENV_VARS = [
    "SQLALCHEMY_DATABASE_URL",
    "WEBSITE_DOMAIN",
    "SECRET_KEY",
    "ALGORITHM",
    "ACCESS_TOKEN_EXPIRE_MINUTES"
]

def check_env_vars():
    for var in REQUIRED_ENV_VARS:
        if not os.environ.get(var, None):
            raise EnvironmentError(f"Required environment variable '{var}' is not set.")
        DB_URL = os.environ.get("SQLALCHEMY_DATABASE_URL")
        # Check if the database URL is sqlite and the database file exists
        if "sqlite" in DB_URL:
            db_file = DB_URL.replace("sqlite:///", "")
            if not os.path.isfile(db_file):
                raise EnvironmentError(f"SQLite database file '{db_file}' does not exist.")
        # make sure the ACCESS_TOKEN_EXPIRE_MINUTES can be converted to a float
        try:
            float(os.environ.get("ACCESS_TOKEN_EXPIRE_MINUTES"))
        except ValueError:
            raise EnvironmentError("ACCESS_TOKEN_EXPIRE_MINUTES must be a number.")
        # make sure the WEBSITE_DOMAIN is a valid domain
        if not os.environ.get("WEBSITE_DOMAIN").startswith("http"):
            raise EnvironmentError("WEBSITE_DOMAIN must start with 'http' or 'https'.")

# Perform the environment variable check before initializing the FastAPI app
check_env_vars()

from starlette.middleware.cors import CORSMiddleware
from modelgenerator.database import engine
from modelgenerator.models import Base
from modelgenerator.routers.attributs import router as attributs_router
from modelgenerator.routers.commons import router as commons_router
from modelgenerator.routers.projects import router as projects_router
from modelgenerator.routers.tables import router as tables_router
from modelgenerator.routers.users import router as users_router
from modelgenerator.routers.koodus import router as koodus_router


Base.metadata.create_all(bind=engine)
app = FastAPI(docs_url="/api/docs")

origins = [
    os.environ.get("WEBSITE_DOMAIN"),
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
app.include_router(koodus_router, prefix="/api")


@app.get("/")
async def root():
    return {"message": "Modelgenerator Backend made with FastApi"}
