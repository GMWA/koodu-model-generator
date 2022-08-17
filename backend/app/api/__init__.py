from flask_restx import Api


def make_api(app):
    """Create a Flask-Restx api, add some Ressources and add it to the app."""
    api = Api()

    api.init_app(app)
    return app