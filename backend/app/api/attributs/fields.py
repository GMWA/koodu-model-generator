from flask_restful import fields


get_fields = {
    "id": fields.Integer(),
    "name": fields.String(),
    "primary_key": fields.Boolean(),
    "index_key": fields.Boolean(),
    "unique_kex": fields.Boolean(),
    "size": fields.Integer(),
    "type": fields.String(),
    "description": fields.String(),
    "created_at": fields.String(),
    "updated_at": fields.String(),
    "table_id": fields.Integer(),
}