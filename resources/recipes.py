import models 
import requests

from flask import Blueprint, jsonify, request, Response

from playhouse.shortcuts import model_to_dict

recipe = Blueprint('recipes', 'recipe') ## this will be my route

## here we are retrieving the random recipe from the spoonacular API
@recipe.route('/', methods=["GET"])
def get_random_recipes():
    try:
        recipe="test code"
        recipe = requests.get('https://api.spoonacular.com/recipes/random?apiKey=40b4dc4ae9fe4482b9d5633dd6ff2738&number=1&tags=dinner')
        # print(recipe.content)
        # recipe.headers['content-type':]
        # return jsonify(data=recipe.content, status={"code": 200, "message": "Success"})
        return Response(recipe, mimetype='application/json')
    except models.DoesNotExist:
        return jsonify(data={}, status={"code": 401, "message": "Error getting the resources"})


@recipe.route('/', methods=["POST"])
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

#show route
# @recipe.route('/<id>', methods=["GET"])
# def get_one_recipe(id):
#     print(id, 'yeeet')
#     recipe = models.Recipe.get_by_id(id)
#     print(recipe.__dict__)
#     return jsonify(data=model_to_dict(recipe), status={"code": 200, "message": "Success"})


# ## update route Not really sure I need this route
# @recipe.route('/<id>', methods=["PUT"])
# def recipe_update(id):
#     print('UPDATINGGG')
#     print(id)
#     payload = request.get_json()
#     print(payload)
#     payload['user'] = payload['user']['id']
#     query = models.Recipe.update(**payload).where(models.Recipe.id == id)
#     print(query)
#     query.execute()
#     return jsonify(data=model_to_dict(models.Recipe.get_by_id(id)), status={"code": 200, "message": "resource updated successfully"})

# @recipe.route('/<id>', methods=["Delete"])
# # @login_required
# def delete_recipe(id):
#     query = models.SavedRecipe.delete().where(models.SavedRecipe.id == id)
#     print(models.SavedRecipe.id)
#     query.execute()
#     return jsonify(data='resource successfully deleted', status={"code": 200, "message": "resource deleted successfully"})

