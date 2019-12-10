import models
import requests
from flask_login import login_user, current_user, logout_user
from flask import Blueprint, jsonify, request, Response

from playhouse.shortcuts import model_to_dict

savedRecipe = Blueprint('savedRecipes', 'savedRecipe')

@savedRecipe.route('/', methods=["POST"])
def save_recipe():
    ## see request payload anagolous to req.body in express
    payload = request.get_json()
    print(type(payload), 'payload')
    payload['user'] = current_user.id
    savedRecipe = models.SavedRecipe.create(**payload)
    ## see the object
    print(savedRecipe.__dict__)

    ## Look at all the methods
    print(dir(savedRecipe))
    # Change the model to a dict
    print(model_to_dict(savedRecipe), 'model to dict')
    savedRecipe_dict = model_to_dict(savedRecipe)
    return jsonify(data=savedRecipe_dict, status={"code": 201, "message": "Success"})

#show route on saved recipe page
@savedRecipe.route('/<id>', methods=["GET"])
def get_saved_recipes(id):
    print(id, 'yeeet')
    recipe = models.SavedRecipe.get_by_id(id)
    print(recipe.__dict__)
    return jsonify(data=model_to_dict(recipe), status={"code": 200, "message": "Success"})
