import models 
import requests

from flask import Blueprint, jsonify, request, Response

from playhouse.shortcuts import model_to_dict

recipe = Blueprint('recipes', 'recipe')

## here we are retrieving the random recipe from the spoonacular API
@recipe.route('/', methods=["GET"])
def get_random_recipes():
    try:
        recipe="test code"
        recipe = requests.get('https://api.spoonacular.com/recipes/random?apiKey=40b4dc4ae9fe4482b9d5633dd6ff2738&number=1&tags=lunch')
        print(recipe.content)
        # recipe.headers['content-type':]
        # return jsonify(data=recipe.content, status={"code": 200, "message": "Success"})
        return Response(recipe, mimetype='application/json')
    except models.DoesNotExist:
        return jsonify(data={}, status={"code": 401, "message": "Error getting the resources"})


