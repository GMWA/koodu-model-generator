from flask_restx import Api


def make_api(app):
    """Create a Flask-Restx api, add some Ressources and add it to the app."""
    api = Api(
        version=app.config.get("API_VERSION"),
        title=app.config.get("API_TITLE"),
        description=app.config.get("API_DESCRIPTION")
    )

    api.init_app(app)
    return app