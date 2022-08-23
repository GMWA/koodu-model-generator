from flask_restful import reqparse


login_parser = reqparse.RequestParser()
login_parser.add_argument(
    "username",
    required=True,
    type=str,
    location=["args", "values", "form", "json", "headers"]
)
login_parser.add_argument(
    "password",
    required=True,
    type=str,
    location=["args", "values", "form", "json", "headers"]
)

get_parser = reqparse.RequestParser()
get_parser.add_argument(
    "id",
    type=int,
    location=["args", "values", "form", "json", "headers"]
)

post_parser = reqparse.RequestParser()
post_parser.add_argument(
    "email",
    required=True,
    type=str,
    location=["args", "values", "form", "json", "headers"]
)
post_parser.add_argument(
    "username",
    required=True,
    type=str,
    location=["args", "values", "form", "json", "headers"]
)
post_parser.add_argument(
    "lastname",
    type=str,
    location=["args", "values", "form", "json", "headers"]
)
post_parser.add_argument(
    "firstname",
    type=str,
    location=["args", "values", "form", "json", "headers"]
)
post_parser.add_argument(
    "phone",
    type=str,
    location=["args", "values", "form", "json", "headers"]
)
post_parser.add_argument(
    "password",
    type=str,
    location=["args", "values", "form", "json", "headers"]
)

put_parser = reqparse.RequestParser()
put_parser.add_argument(
    "username",
    type=str,
    location=["args", "values", "form", "json", "headers"]
)
put_parser.add_argument(
    "lastname",
    type=str,
    location=["args", "values", "form", "json", "headers"]
)
put_parser.add_argument(
    "firstname",
    type=str,
    location=["args", "values", "form", "json", "headers"]
)
put_parser.add_argument(
    "phone",
    type=str,
    location=["args", "values", "form", "json", "headers"]
)