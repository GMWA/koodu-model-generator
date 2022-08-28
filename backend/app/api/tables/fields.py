from flask_restful import fields


get_fields = {
    "id": fields.Integer(),
    "name": fields.String(),
    "description": fields.String(),
    "created_at": fields.String(),
    "updated_at": fields.String(),
    "project_id": fields.Integer()
}