import recipe as recipe
from flask import request
from flask_restful import Resource
from flask_jwt_extended import get_jwt_identity, jwt_required, jwt_optional
from http import HTTPStatus
from models.recipes import Recipes

#armazena as receitas
class RecipeListResource(Resource):

    def get(self):
        recipes = Recipes.get_all_published()
        data = []

        for recipe in recipes:
            data.append(recipe)

        return {'data': data}, HTTPStatus.OK

    @jwt_required
    def post(self):
        json_data = request.get_json()

        current_user = get_jwt_identity()
        recipe = Recipes(name=json_data['name'],
                         description=json_data['description'],
                         num_of_servings=json_data['num_of_servings'],
                         cook_time=json_data['cook_time'],
                         directions=json_data['directions'],
                         user_id = current_user)

        recipe.save()
        return recipe.data(), HTTPStatus.OK

#buscar uma receita
class RecipesResource(Resource):

    @jwt_optional
    def get(self, recipe_id):
        recipe = Recipes.get_by_id(recipe_id=recipe_id)

        if recipe is None:
            return {'message': 'recipe not found'}, HTTPStatus.NOT_FOUND

        current_user = get_jwt_identity()
        if recipe.is_publish == False and recipe.user_id != current_user:
            return {'message': 'Access is not allowed'}, HTTPStatus.FORBIDDEN

        return recipe.data(), HTTPStatus.OK

    def put(self, recipe_id):
        json_data = request.get_json()
        recipe = Recipes.get_by_id(recipe_id=recipe_id)

        if recipe == None:
            return {'message': 'recipe not found'}, HTTPStatus.NOT_FOUND

        current_user = get_jwt_identity()
        if current_user != recipe.user_id:
            return {'message': 'Access is not allowed'}, HTTPStatus.FORBIDDEN

        recipe.name = json_data['name']
        recipe.description = json_data['description']
        recipe.num_of_servings = json_data['num_of_servings']
        recipe.cook_time = json_data['cook_time']
        recipe.directions = json_data['directions']

        recipe.save()
        return recipe.data(), HTTPStatus.OK

    @jwt_required
    def delete(self, recipe_id):
        recipe = Recipes.get_by_id(recipe_id = recipe_id)

        if recipe is None:
            return {'message': 'Recipe not found'}, HTTPStatus.NOT_FOUND

        current_user = get_jwt_identity()
        if current_user != recipe.user_id:
            return {'message': 'Access is not allowed'}, HTTPStatus.FORBIDDEN

        recipe.delete()
        return {}, HTTPStatus.NO_CONTENT


class RecipesPublishResource(Resource):
    @jwt_required
    def put(self, recipe_id):
        recipe =Recipes.get_by_id(recipe_id=recipe_id)

        if recipe is None:
            return {'message': 'recipe not found'}, HTTPStatus.NOT_FOUND

        current_user = get_jwt_identity()
        if current_user != recipe.user_id:
            return {'message': 'Access is not allowed'}, HTTPStatus.FORBIDDEN

        recipe.is_publish = True
        recipe.save()
        return recipe.data(), HTTPStatus.NO_CONTENT

    #deletar publicação
    @jwt_required
    def delete(self, recipe_id):
        recipe =Recipes.get_by_id(recipe_id=recipe_id)

        if recipe is None:
            return {'message': 'recipe not found'}, HTTPStatus.NOT_FOUND

        recipe.is_publish = False
        recipe.save()
        return {}, HTTPStatus.NO_CONTENT

