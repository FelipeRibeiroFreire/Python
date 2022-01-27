from flask import request
from flask_restful import Resource
from http import HTTPStatus
from models.recipes import Recipes


class RecipeListResource(Resource):

    def get(self):
        data = []

        for recipe in recipes_list:
            if recipe.is_publish is True:
                data.append(recipe.data)

        return {'data': data}, HTTPStatus.OK

    def post(self):
        data = request.get_json()

        recipe = Recipes(name=data['name'],
                         description=data['description'],
                         num_of_servings=data['num_of_servings'],
                         cook_time=data['cook_time'],
                         directions=data['directions'])

        recipes_list.append(recipe)
        return recipe.data, HTTPStatus.OK

#-----------------------------------------------------------------------------------------------------------------------

class RecipesResource(Resource):

    def get(self, recipe_id):
        recipe = next((recipe for recipe in recipes_list if recipe.id == recipe_id and recipe.is_publish == True), None)

        if recipe is None:
            return {'message': 'recipe not found'}, HTTPStatus.NOT_FOUND

        return recipe.data, HTTPStatus.OK

    def put(self, recipe_id):
        data = request.get_json()
        recipe = next((recipe for recipe in recipes_list if recipe.id==recipe_id),None)

        if recipe == None:
            return {'message': 'recipe not found'}, HTTPStatus.NOT_FOUND

        recipe.name = data['name']
        recipe.description = data['description']
        recipe.num_of_servings = data['num_of_servings']
        recipe.cook_time = data['cook_time']
        recipe.directions = data['directions']

        return recipe.data, HTTPStatus.OK

    def delete(self, recipe_id):
        global recipes_list
        recipes_list = [next((recipe for recipe in recipes_list if recipe.id != recipe_id), None)]

        return HTTPStatus.OK

#-----------------------------------------------------------------------------------------------------------------------

class RecipesPublishResource(Resource):
    def put(self, recipe_id):
        recipe = next((recipe for recipe in recipes_list if recipe.id == recipe_id), None)

        if recipe is None:
            return {'message': 'recipe not found'}, HTTPStatus.NOT_FOUND

        recipe.is_publish = True
        return {}, HTTPStatus.NO_CONTENT

    #deletar publicação

    def delete(self, recipe_id):
        recipe = next((recipe for recipe in recipes_list if recipe['id'] == recipe_id),None)

        if recipe is None:
            return {'message': 'recipe not found'}, HTTPStatus.NOT_FOUND

        recipe.is_publish = False
        return {}, HTTPStatus.NO_CONTENT
    
