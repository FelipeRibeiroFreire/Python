from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api
from config import Config
from extensions import db, jwt
from resources.user import UserListResource
from resources.recipes import RecipeListResource, RecipesResource, RecipesPublishResource

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    register_extension(app)
    register_recoucers(app)
    return app

def register_extension(app):
    #conectar com o banco de dados
    db.init_app(app)
    migrate = Migrate(app, db)
    #autenticação jwt
    jwt.init_app(app)

def register_recoucers(app):
    api = Api(app)
    api.add_resource(UserListResource, '/user')
    api.add_resource(RecipeListResource, '/recipes')
    api.add_resource(RecipesResource, '/recipes/<int:recipe_id>')
    api.add_resource(RecipesPublishResource, '/recipes/<int:recipe_id>/publish')

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)