import datetime

from sqlalchemy import (Boolean, Column, DateTime, ForeignKey, Integer, String,
                        Text)

from modelgenerator.database import Base


def utcnow():
    return datetime.datetime.now(datetime.timezone.utc)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer(), primary_key=True, index=True, autoincrement=True)
    email = Column(String(120), unique=True, nullable=False)
    username = Column(String(255), unique=True)
    lastname = Column(String(255))
    firstname = Column(String(255))
    hashed_password = Column(String(255), nullable=True)
    phone = Column(String(20))
    is_admin = Column(Boolean, default=False)
    created_at = Column(DateTime, default=utcnow)
    activated_at = Column(DateTime, nullable=True)
    updated_at = Column(DateTime, default=utcnow)

    def generate_auth_token(self, expiration=600):
        pass

    def __dict__(self):
        return self.to_json()

    def to_json(self):
        return {
            "id": self.id,
            "email": self.email,
            "username": self.username,
            "lastname": self.lastname,
            "firstname": self.firstname,
            "phone": self.phone,
            "is_admin": self.is_admin,
            "activated_at": self.activated_at.strftime("%d.%m.%Y %H:%M:%S") if self.activated_at else None,
            "created_at": self.created_at.strftime("%d.%m.%Y %H:%M:%S") if self.created_at else None,
            "updated_at": self.updated_at.strftime("%d.%m.%Y %H:%M:%S") if self.updated_at else None,
        }


class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    description = Column(Text)
    created_at = Column(DateTime, default=utcnow)
    updated_at = Column(DateTime, default=utcnow)
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
    created_at = Column(DateTime, default=utcnow)
    updated_at = Column(DateTime, default=utcnow)
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
    is_required = Column(Boolean, default=False)
    type = Column(String(50), nullable=False)
    size = Column(Integer)
    description = Column(Text)
    created_at = Column(DateTime, default=utcnow)
    updated_at = Column(DateTime, default=utcnow)
    table_id = Column(Integer, ForeignKey("tables.id"))

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "primary_key": self.primary_key,
            "index_key": self.index_key,
            "unique_key": self.unique_key,
            "is_required": self.is_required,
            "type": self.type,
            "size": self.size,
            "description": self.description,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "table_id": self.table_id,
        }
