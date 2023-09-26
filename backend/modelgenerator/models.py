from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy import DateTime, Text
from sqlalchemy.orm import relationship
from datetime import datetime

from modelgenerator.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(String(255), primary_key=True, index=True)
    email = Column(String(120), unique=True, nullable=False)
    username = Column(String(255), unique=True)
    lastname = Column(String(255))
    firstname = Column(String(255))
    phone = Column(String(20), unique=True)
    thirdparty = Column(String(50), default="")
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

    def generate_auth_token(self, expiration=600):
        pass


class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    description = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)
    user_id = Column(String(255), ForeignKey("users.id"))


class Table(Base):
    __tablename__ = "tables"

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    description = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)
    project_id = Column(Integer, ForeignKey("projects.id"))

class Attribut(Base):
    __tablename__ = "attributs"

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    primary_key = Column(Boolean, default=False)
    index_key = Column(Boolean, default=False)
    unique_key = Column(Boolean, default=False)
    type = Column(String(50), nullable=False)
    size = Column(Integer)
    description = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)
    table_id = Column(Integer, ForeignKey("tables.id"))
