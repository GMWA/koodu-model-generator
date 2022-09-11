from flask_restful import reqparse


get_parser = reqparse.RequestParser()
get_parser.add_argument(
    "id",
    type=int,
    location=["args", "values", "form", "json", "headers"]
)


post_parser = reqparse.RequestParser()
post_parser.add_argument(
    "table_id",
    required=True,
    type=int,
    location=["args", "values", "form", "json", "headers"]
)
post_parser.add_argument(
    "name",
    required=True,
    type=str,
    location=["args", "values", "form", "json", "headers"]
)
post_parser.add_argument(
    "type",
    required=True,
    type=str,
    location=["args", "values", "form", "json", "headers"]
)
post_parser.add_argument(
    "description",
    type=str,
    default="",
    location=["args", "values", "form", "json", "headers"]
)
post_parser.add_argument(
    "primary_key",
    type=bool,
    default=False,
    location=["args", "values", "form", "json", "headers"]
)
post_parser.add_argument(
    "index_key",
    type=bool,
    default=False,
    location=["args", "values", "form", "json", "headers"]
)
post_parser.add_argument(
    "unique_key",
    type=bool,
    default=False,
    location=["args", "values", "form", "json", "headers"]
)


put_parser = reqparse.RequestParser()
put_parser.add_argument(
    "table_id",
    required=True,
    type=int,
    location=["args", "values", "form", "json", "headers"]
)
put_parser.add_argument(
    "name",
    type=str,
    location=["args", "values", "form", "json", "headers"]
)
put_parser.add_argument(
    "type",
    type=str,
    location=["args", "values", "form", "json", "headers"]
)
put_parser.add_argument(
    "description",
    type=str,
    location=["args", "values", "form", "json", "headers"]
)
put_parser.add_argument(
    "primary_key",
    type=bool,
    location=["args", "values", "form", "json", "headers"]
)
put_parser.add_argument(
    "index_key",
    type=bool,
    location=["args", "values", "form", "json", "headers"]
)
put_parser.add_argument(
    "unique_key",
    type=bool,
    location=["args", "values", "form", "json", "headers"]
)