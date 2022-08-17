import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from config import DevConfig, ProdConfig


app = Flask(__name__)

if os.environ.get("ENV") == "production":
    app.config.from_object(ProdConfig)
else:
    app.config.from_object(DevConfig)

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
cors = CORS(app)

from .api import make_api

make_api(app=app)