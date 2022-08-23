import re
from flask import abort
from flask_restful import Resource, marshal_with
from flask_bcrypt import check_password_hash, generate_password_hash
from flask_jwt_extended import get_jwt_identity, jwt_required, create_access_token, create_refresh_token
from app import db
from app.models import User
from .parsers import get_parser, post_parser, put_parser, delete_parser, login_parser
from .fields import get_fields


class UserLoginResource(Resource):
    def post(self):
        args = login_parser.parse_args()

        username = args["username"]
        password = args["password"]

        if not username or not password:
            abort(403)

        regex = re.compile(r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+")

        if re.fullmatch(regex, username):
            user = User.query.filter_by(email=username).first()
        else:
            user = User.query.filter_by(username=username).first()

        if not user:
            return {
                "message": "Invalid username or password, Please try again",
                "token": "",
                "refreshToken": "",
                "ok": False,
            }, 403

        if not user.is_active:
            return (
                {
                    "message": "The user's account is not yet active! Please \
                    check your mail and follow the link to activate the Account.",
                    "token": "",
                    "refreshToken": "",
                    "ok": False,
                },
                403,
            )

        if not check_password_hash(user.password, password):
            return {
                "message": "Invalid email or password, Please try again",
                "token": "",
                "refreshToken": "",
                "ok": False,
            }, 403

        token = create_access_token(identity=user.id)
        refresh_token = create_refresh_token(identity=user.id)

        return {
            "message": "You logged in successfully.",
            "token": token,
            "refreshToken": refresh_token,
            "ok": True,
        }, 200


class UserAllResource(Resource):
    def post(self):
        args = post_parser.parse_args()
        email = args["email"]
        username = args["username"]
        lastname = args["lastname"]
        password = args["password"]
        firstname = args["firstname"] if args["firstname"] else ""
        phone = args["phone"] if args["phone"] else ""

        if User.query.filter_by(email=email).first():
            return {
                "message": "The is already a user with this Email",
                "id": None,
                "ok": False,
            }, 400

        if User.query.filter_by(username=username).first():
            return {
                "message": "The is already a user with this Username",
                "id": None,
                "ok": False,
            }, 400

        if phone and User.query.filter_by(phone=phone).first():
            return {
                "message": "The is already a user with this Phone number",
                "id": None,
                "ok": False,
            }, 400

        try:
            user = User()
            user.email = email
            user.lastname = lastname
            user.username = username
            user.firstname = firstname
            user.password = generate_password_hash(password)
            user.phone = phone
            user.is_verified = False

            db.session.add(user)
            db.session.commit()

            return {
                "message": "success: the user has been created",
                "id": user.id,
                "ok": True,
            }, 201
        except:
            return {"message": "An error occurs", "id": None, "ok": False}, 400


class UserOneResource(Resource):
    @jwt_required()
    def get(self):
        user_id = get_jwt_identity()
        if not user_id:
            abort(500, "The user's id must be provided")

        user = User.query.get(user_id)
        if not user:
            abort(500, message="Bad user's id")

        return user

    @get_jwt_identity()
    def put(self):
        user_id = get_jwt_identity()
        if not user_id:
            abort(500, "The user's id must be provided")

        user = User.query.get(user_id)
        if not user:
            abort(500, message="Bad user's id")

        args = put_parser.parse_args()

        if args["lastname"]:
            user.lastname = args["lastname"]

        if args["firstname"]:
            user.firstname = args["firstname"]

        db.session.commit()
    
    @jwt_required()
    def delete(self):
        user_id = get_jwt_identity()
        if not user_id:
            abort(500, "The user's id must be provided")

        user = User.query.get(user_id)
        if not user:
            abort(500, message="Bad user's id")

        db.session.delete(user)
        db.session.commit()