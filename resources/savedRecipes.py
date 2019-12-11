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
@savedRecipe.route('/', methods=["GET"])
def get_all_saved_recipes():
    print(id, 'yeeet')
    # recipe = models.SavedRecipe.get_by_id()
    # print(recipe.__dict__)
    get_all_saved_recipes = [model_to_dict(savedRecipe, max_depth=1) for savedRecipe in models.SavedRecipe.select()]
    return jsonify(data=get_all_saved_recipes, status={'code': 200, 'message': 'Success'})

@savedRecipe.route('/<id>', methods=["Delete"])
# @login_required
def recipe_to_delete_recipe(id):
    recipe_to_delete = models.SavedRecipe.get(id=id)
    print(recipe_to_delete)
    query = models.SavedRecipe.delete().where(models.SavedRecipe.id == id)
    print(models.SavedRecipe.id)
    query.execute()
    return jsonify(data='resource successfully deleted', status={"code": 200, "message": "resource deleted successfully"})