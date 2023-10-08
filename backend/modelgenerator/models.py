from datetime import datetime

from sqlalchemy import (Boolean, Column, DateTime, ForeignKey, Integer, String,
                        Text)

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
    is_admin = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

    def generate_auth_token(self, expiration=600):
        pass

    def to_json(self):
        return {
            "id": self.id,
            "email": self.email,
            "username": self.username,
            "lastname": self.lastname,
            "firstname": self.firstname,
            "phone": self.phone,
            "thirdparty": self.thirdparty,
            "is_admin": self.is_admin,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }


class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    description = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)
    user_id = Column(String(255), ForeignKey("users.id"))

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "user_id": self.user_id,
        }


class Table(Base):
    __tablename__ = "tables"

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    description = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)
    project_id = Column(Integer, ForeignKey("projects.id"))

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "project_id": self.project_id,
        }


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

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "primary_key": self.primary_key,
            "index_key": self.index_key,
            "unique_key": self.unique_key,
            "type": self.type,
            "size": self.size,
            "description": self.description,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "table_id": self.table_id,
        }
