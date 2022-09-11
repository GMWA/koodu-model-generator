
from ast import arg
from flask import abort
from flask_restful import Resource, marshal_with
from flask_jwt_extended import get_jwt_identity, jwt_required
from app import db
from app.models import Table, Attribut
from .parsers import get_parser, post_parser, put_parser
from .fields import get_fields


class AttributAllRessource(Resource):
    @jwt_required()
    def get(self):
        args = get_parser.parse_args()

        if args["id"]:
            attrib = Attribut.query.get(args["id"])
            if attrib is None:
                abort(400, "")
            
            return attrib
        else:
            attribs = Attribut.query.all()
            return attribs

    @jwt_required()
    def post(self):
        args = post_parser.parse_args()
        table_id = args["table_id"]

        table = Table.query.get(table_id)
        if not table:
            abort(500, "Not Project with given Table's id")

        attrib = Attribut()
        attrib.name = args["name"]
        attrib.type = args["type"]
        attrib.size = args["size"]
        attrib.description = args["description"]
        attrib.primary_key = args["primary_key"]
        attrib.unique_key = args["unique_key"]
        attrib.index_key = args["index_key"]
        attrib.table_id = table.id

        db.session.add(attrib)
        db.session.commit()

class AttributOneRessource(Resource):
    @jwt_required()
    def put(self, attrib_id):
        if not attrib_id:
            abort(500, "The id must be provided")

        attrib = Attribut.query.get(attrib_id)
        if not attrib:
            abort(500, message="Bad attribut's id")

        args = put_parser.parse_args()

        table = Table.query.get(args["table_id"])
        if not table:
            abort(500, "Not Table with given Table's id")

        if args["name"]:
            attrib.name = args["name"]
        
        if args["type"]:
            attrib.type = args["type"]

        if args["size"]:
            attrib.size = args["size"]

        if args["description"]:
            attrib.description = args["description"]

        if args["primary_key"]:
            attrib.primary_key = args["primary_key"]

        if args["index_key"]:
            attrib.index_key = args["index_key"]

        if args["unique_key"]:
            attrib.unique_key = args["unique_key"]

        db.session.commit()

    @jwt_required()
    def delete(self, attrib_id):
        if not attrib_id:
            abort(500, "The id must be provided")

        attrib = Attribut.query.get(attrib_id)
        if not attrib:
            abort(500, message="Bad attrib's id")

        user_id = get_jwt_identity()
        if user_id != attrib.table.project.user_id:
            abort(403, message="You are not allowed to delete this Attribut")

        db.session.delete(attrib)
        db.session.commit()