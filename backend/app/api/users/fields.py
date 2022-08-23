from flask_restful import fields


get_fields = {
    "id": fields.Integer(),
    "email": fields.String(),
    "username": fields.String(),
    "phone": fields.String(),
    "is_verified": fields.Boolean()
}