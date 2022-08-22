from flask_restful import Api
from .projects.controllers import ProjectAllRessource, ProjectOneRessource


def make_api(app):
    """Create a Flask-Restx api, add some Ressources and add it to the app."""
    api = Api()

    api.add_resource(ProjectAllRessource, "/v1/projects")
    api.add_resource(ProjectOneRessource, "/v1/projects/<int:project_id>")

    api.init_app(app)

    print("API is running!!!!")
    return app