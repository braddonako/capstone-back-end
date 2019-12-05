import models
import requests

from flask import Blueprint, jsonify, request, Response

from playhouse.shortcuts import model_to_dict

breakfastRecipe = Blueprint('breakfastRecipes', 'breakfastRecipe')  # this will be my route

## here we are retrieving the random recipe from the spoonacular API
@breakfastRecipe.route('/', methods=["GET"])
def get_random_recipes():
    try:
        breakfastRecipe = "test code"
        breakfastRecipe = requests.get('https://api.spoonacular.com/recipes/random?apiKey=40b4dc4ae9fe4482b9d5633dd6ff2738&number=2&tags=breakfast')
        print(breakfastRecipe.content)
        # recipe.headers['content-type':]
        # return jsonify(data=recipe.content, status={"code": 200, "message": "Success"})
        return Response(breakfastRecipe, mimetype='application/json')
    except models.DoesNotExist:
        return jsonify(data={}, status={"code": 401, "message": "Error getting the resources"})


# @breakfastRecipe.route('/', methods=["POST"])
# def create_recipes():
#     ## see request payload anagolous to req.body in express
#     payload = request.get_json()
#     print(type(payload), 'payload')
#     recipe = models.Recipe.create(**payload)
#     ## see the object
#     print(recipe.__dict__)
#     ## Look at all the methods
#     print(dir(recipe))
#     # Change the model to a dict
#     print(model_to_dict(recipe), 'model to dict')
#     recipe_dict = model_to_dict(recipe)
#     return jsonify(data=recipe_dict, status={"code": 201, "message": "Success"})

# #show route
# @breakfastRecipe.route('/<id>', methods=["GET"])
# def get_one_post(id):
#     print(id, 'yeeet')
#     recipe = models.Recipe.get_by_id(id)
#     print(recipe.__dict__)
#     return jsonify(data=model_to_dict(recipe), status={"code": 200, "message": "Success"})
