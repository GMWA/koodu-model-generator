
from flask import abort
from flask_restful import Resource, marshal_with
from flask_jwt_extended import get_jwt_identity, jwt_required
from app import db
from app.models import Project, User
from .parsers import get_parser, post_parser, put_parser
from .fields import get_fields


class ProjectAllRessource(Resource):
    @jwt_required()
    def get(self):
        args = get_parser.parse_args()

        if args["id"]:
            project = Project.query.get(args["id"])
            if project is None:
                abort(400, "")
            
            return project
        else:
            projects = Project.query.all()
            return projects

    @jwt_required()
    def post(self):
        args = post_parser.parse_args()
        user_id = get_jwt_identity()

        projekt = Project()
        projekt.name = args["name"]
        projekt.description = args["description"]
        projekt.user_id = user_id

        db.session.add(projekt)
        db.session.commit()

class ProjectOneRessource(Resource):
    @jwt_required()
    def put(self, project_id):
        if not project_id:
            abort(500, "The id must be provided")

        project = Project.query.get(project_id)
        if not project:
            abort(500, message="Bad project's id")

        user_id = get_jwt_identity()
        if user_id != project.user_id:
            abort(403, message="You are not allowed to delete this Project")

        args = put_parser.parse_args()

        if args["name"]:
            project.name = args["name"]

        if args["description"]:
            project.name = args["description"]

        db.session.commit()

    @jwt_required()
    def delete(self, project_id):
        if not project_id:
            abort(500, "The id must be provided")

        project = Project.query.get(project_id)
        if not project:
            abort(500, message="Bad project's id")

        user_id = get_jwt_identity()
        if user_id != project.user_id:
            abort(403, message="You are not allowed to delete this Project")

        db.session.delete(project)
        db.session.commit()