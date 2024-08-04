from modelgenerator.schemas.projects import Project
from modelgenerator.schemas.tables import Table
from modelgenerator.schemas.attributs import Attribut
from pydantic import BaseModel
from typing import List


class ExportModel(BaseModel):
    project: int


class KooduTable(Table):
    attributs: List[Attribut] = []


class KooduProject(Project):
    tables: List[KooduTable] = []