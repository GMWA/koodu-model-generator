
from ast import arg
from flask import abort
from flask_restful import Resource, marshal_with
from flask_jwt_extended import get_jwt_identity, jwt_required
from app import db
from app.models import Table, Project
from .parsers import get_parser, post_parser, put_parser
from .fields import get_fields


class TablesAllRessource(Resource):
    @jwt_required()
    def get(self):
        args = get_parser.parse_args()

        if args["id"]:
            table = Table.query.get(args["id"])
            if table is None:
                abort(400, "")
            
            return table
        else:
            tables = Project.query.all()
            return table

    @jwt_required()
    def post(self):
        args = post_parser.parse_args()
        project_id = args["project_id"]

        project = Project.query.get(project_id)
        if not project:
            abort(500, "Not Project with given Project's id")

        table = Table()
        table.name = args["name"]
        table.description = args["description"]
        table.project_id = project.id

        db.session.add(table)
        db.session.commit()

class TableOneRessource(Resource):
    @jwt_required()
    def put(self, table_id):
        if not table_id:
            abort(500, "The id must be provided")

        table = Table.query.get(table)
        if not table:
            abort(500, message="Bad table's id")

        args = put_parser.parse_args()

        project = Project.query.get(args["project_id"])
        if not project:
            abort(500, "Not Project with given Project's id")

        if args["name"]:
            table.name = args["name"]

        if args["description"]:
            table.name = args["description"]

        db.session.commit()

    @jwt_required()
    def delete(self, table_id):
        if not table_id:
            abort(500, "The id must be provided")

        table = Table.query.get(table_id)
        if not table:
            abort(500, message="Bad table's id")

        user_id = get_jwt_identity()
        if user_id != table.project.user_id:
            abort(403, message="You are not allowed to delete this Table")

        db.session.delete(table)
        db.session.commit()