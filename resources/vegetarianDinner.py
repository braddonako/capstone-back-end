import models
import requests

from flask import Blueprint, jsonify, request, Response

from playhouse.shortcuts import model_to_dict

vegetarianDinner = Blueprint('vegetarianDinners', 'vegetarianDinner')  # this will be my route

## here we are retrieving the random recipe from the spoonacular API
@vegetarianDinner.route('/', methods=["GET"])
def get_random_recipes():
    try:
        vegetarianDinner = "test code"
        vegetarianDinner = requests.get('https://api.spoonacular.com/recipes/random?apiKey=40b4dc4ae9fe4482b9d5633dd6ff2738&number=1&tags=vegetarian,dinner')
        # print(breakfastRecipe.content)
        # recipe.headers['content-type':]
        # return jsonify(data=recipe.content, status={"code": 200, "message": "Success"})
        return Response(vegetarianDinner, mimetype='application/json')
    except models.DoesNotExist:
        return jsonify(data={}, status={"code": 401, "message": "Error getting the resources"})


@vegetarianDinner.route('/', methods=["POST"])
def saved_recipe():
    ## see request payload anagolous to req.body in express
    payload = request.get_json()
    print(type(payload), 'payload')
    saved_recipe = models.SavedRecipe.create(**payload)
    ## see the object
    print(saved_recipe.__dict__)
    ## Look at all the methods
    print(dir(saved_recipe))
    # Change the model to a dict
    print(model_to_dict(saved_recipe), 'model to dict')
    saved_recipe_dict = model_to_dict(saved_recipe)
    return jsonify(data=saved_recipe_dict, status={"code": 201, "message": "Success"})