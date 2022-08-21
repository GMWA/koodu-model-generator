
from flask import abort
from flask_restful import Resource, marshal_with
from app import db
from app.models import Project, User
from .parsers import get_parser, post_parser, put_parser, delete_parser
from .fields import get_fields


class ProjectRessource(Resource):
    def get(self):
        pass

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        args = delete_parser.parse_args()
        project_id = args["id"]

        if not project_id:
            abort(400)

        project = Project.query.get(id)
        if not property:
            abort(403, message="You are not allowed to delete this Project")

        db.session.delete(project)
        db.session.commit()