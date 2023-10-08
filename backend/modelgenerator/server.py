from fastapi import FastAPI
import os
from dotenv import load_dotenv
load_dotenv()

from supertokens_python import (
    InputAppInfo,
    SupertokensConfig,
    get_all_cors_headers,
    init,
)
from starlette.middleware.cors import CORSMiddleware
from supertokens_python.framework.fastapi import get_middleware
from supertokens_python.recipe import session, thirdpartyemailpassword
from supertokens_python.recipe.thirdpartyemailpassword import (
    Google,
    Facebook,
    Github
)

from modelgenerator.models import Base
from modelgenerator.routers.attributs import router as attributs_router
from modelgenerator.routers.commons import router as commons_router
from modelgenerator.routers.projects import router as projects_router
from modelgenerator.routers.tables import router as tables_router
from modelgenerator.routers.users import router as users_router
from modelgenerator.database import engine


Base.metadata.create_all(bind=engine)
app = FastAPI(docs_url="/api/docs")


init(
    app_info=InputAppInfo(
        app_name=os.environ.get("APP_NAME"),
        api_domain=os.environ.get("API_DOMAIN"),
        website_domain=os.environ.get("WEBSITE_DOMAIN"),
        api_base_path=os.environ.get("API_BASE_PATH"),
        website_base_path=os.environ.get("WEBSITE_BASE_PATH")
    ),
    supertokens_config=SupertokensConfig(
        connection_uri=os.environ.get("CONNECTION_URI"),
        api_key=os.environ.get("API_KEY")
    ),
    framework='fastapi',
    recipe_list=[
        session.init(),
        thirdpartyemailpassword.init(
            providers=[
                Google(
                    client_id=os.environ.get("GOOGLE_CLIENT_ID"),
                    client_secret=os.environ.get("GOOGLE_CLIENT_SECRET")
                ),
                Facebook(
                    client_id=os.environ.get("FACEBOOK_CLIENT_ID"),
                    client_secret=os.environ.get("FACEBOOK_CLIENT_SECRET")
                ),
                Github(
                    client_id=os.environ.get("GITHUB_CLIENT_ID"),
                    client_secret=os.environ.get("GITHUB_CLIENT_SECRET")
                )
            ]
        )
    ],
    mode='asgi' # use wsgi if you are running using gunicorn
)


app.add_middleware(get_middleware())
app.add_middleware(
    CORSMiddleware,
    allow_origins=[os.environ.get("WEBSITE_DOMAIN")],
    allow_credentials=True,
    allow_methods=["GET", "PUT", "POST", "DELETE", "OPTIONS", "PATCH"],
    allow_headers=["Content-Type"] + get_all_cors_headers()
)

# Add the app Endpoints
app.include_router(attributs_router, prefix="/api")
app.include_router(commons_router, prefix="/api")
app.include_router(projects_router, prefix="/api")
app.include_router(tables_router, prefix="/api")
app.include_router(users_router, prefix="/api")


@app.get("/")
async def root():
    return {"message": "Modelgenerator Backend made with FastApi"}