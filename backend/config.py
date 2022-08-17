from distutils.debug import DEBUG
import os


class BaseConfig(object):
    CORS_HEADERS = "Content-Type"
    API_VERSION = os.environ.get("API_VERSION")
    API_TITLE = os.environ.get("API_TITLE")
    API_DESCRIPTION = os.environ.get("API_DESCRIPTION")


class DevConfig(BaseConfig):
    DEBUG=True
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")

class ProdConfig(BaseConfig):
    DEBUG=False
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")