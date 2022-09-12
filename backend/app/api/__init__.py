from flask_restful import Api
from .projects.controllers import ProjectAllRessource, ProjectOneRessource
from .users.controllers import UserAllResource, UserLoginResource, UserOneResource
from .attributs.controllers import AttributAllRessource, AttributOneRessource
from .tables.controllers import TablesAllRessource, TableOneRessource


def make_api(app):
    """Create a Flask-Restx api, add some Ressources and add it to the app."""
    api = Api()

    api.add_resource(AttributAllRessource, "/v1/attributs")
    api.add_resource(AttributOneRessource, "/v1/attributs/<int:attrib_id>")
    api.add_resource(ProjectAllRessource, "/v1/projects")
    api.add_resource(ProjectOneRessource, "/v1/projects/<int:project_id>")
    api.add_resource(TablesAllRessource, "/v1/tables")
    api.add_resource(TableOneRessource, "/v1/tables/<int:table_id>")
    api.add_resource(UserAllResource, "/v1/users")
    api.add_resource(UserOneResource, "/v1/users/<int:project_id>")
    api.add_resource(UserLoginResource, "/v1/users/login")

    api.init_app(app)

    print("API is running!!!!")
    return app