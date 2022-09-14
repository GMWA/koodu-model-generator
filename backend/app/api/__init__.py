from flask_restful import Api
from .projects.controllers import ProjectAllRessource, ProjectOneRessource
from .users.controllers import UserAllResource, UserLoginResource, UserOneResource
from .attributs.controllers import AttributAllRessource, AttributOneRessource
from .tables.controllers import TablesAllRessource, TableOneRessource


def make_api(app):
    """Create a Flask-Restx api, add some Ressources and add it to the app."""
    api = Api()

    api.add_resource(AttributAllRessource, "/api/v1/attributs")
    api.add_resource(AttributOneRessource, "/api/v1/attributs/<int:attrib_id>")
    api.add_resource(ProjectAllRessource, "/api/v1/projects")
    api.add_resource(ProjectOneRessource, "/api/v1/projects/<int:project_id>")
    api.add_resource(TablesAllRessource, "/api/v1/tables")
    api.add_resource(TableOneRessource, "/api/v1/tables/<int:table_id>")
    api.add_resource(UserAllResource, "/api/v1/users")
    api.add_resource(UserOneResource, "/api/v1/users/<int:project_id>")
    api.add_resource(UserLoginResource, "/api/v1/users/login")

    api.init_app(app)

    print("API is running!!!!")
    return app