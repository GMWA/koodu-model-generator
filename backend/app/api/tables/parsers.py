from flask_restful import reqparse



get_parser = reqparse.RequestParser()
get_parser.add_argument(
    "id",
    type=int,
    location=["args", "values", "form", "json", "headers"]
)


post_parser = reqparse.RequestParser()
post_parser.add_argument(
    "name",
    required=True,
    type=str,
    location=["args", "values", "form", "json", "headers"]
)
post_parser.add_argument(
    "description",
    type=str,
    location=["args", "values", "form", "json", "headers"]
)


put_parser = reqparse.RequestParser()
put_parser.add_argument(
    "id",
    type=int,
    location=["args", "values", "form", "json", "headers"]
)
put_parser.add_argument(
    "name",
    required=True,
    type=str,
    location=["args", "values", "form", "json", "headers"]
)
put_parser.add_argument(
    "description",
    type=str,
    location=["args", "values", "form", "json", "headers"]
)


delete_parser = reqparse.RequestParser()
delete_parser.add_argument(
    "id",
    type=int,
    location=["args", "values", "form", "json", "headers"]
)