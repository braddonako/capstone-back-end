from flask import Flask, g
from flask_cors import CORS
from flask_login import LoginManager
from playhouse.shortcuts import model_to_dict
import os

DEBUG = True
PORT = 8000

import models

from resources.recipes import recipe
from resources.users import user
from resources.breakfastRecipes import breakfastRecipe
from resources.savedRecipes import savedRecipe

login_manager = LoginManager()

app = Flask(__name__)

app.secret_key = "secretkeyhfjdkalhfadsjkhdasjkladfhshahahahlol"  # Need this to encode the session
login_manager.init_app(app)  # set up the sessions on the app


# decorator function, that will load the user object whenever we access the session, we can get the user
@login_manager.user_loader
# by importing current_user from the flask_login
def load_user(userid):
    try:
        return models.User.get(models.User.id == userid)
    except models.DoesNotExist:
        return None

@app.before_request
def before_request():
    """Connect to the database before each request."""
    g.db = models.DATABASE
    g.db.connect()


@app.after_request
def after_request(response):
    """Close the database connection after each request."""
    g.db.close()
    return response


CORS(recipe, origins=['http://localhost:3000'], supports_credentials=True)
app.register_blueprint(recipe, url_prefix='/api/v1/recipes')

CORS(breakfastRecipe, origins=['http://localhost:3000'], supports_credentials=True)
app.register_blueprint(breakfastRecipe, url_prefix='/api/v1/breakfastRecipes')

CORS(user, origins=['http://localhost:3000'], supports_credentials=True)
app.register_blueprint(user, url_prefix='/api/v1/user')

CORS(savedRecipe, origins=['http://localhost:3000'], supports_credentials=True)
app.register_blueprint(savedRecipe, url_prefix='/api/v1/savedRecipes')


# CORS(savedRecipe, origins=['http://localhost:3000'], supports_credentials=True)
# app.register_blueprint(savedRecipe, url_prefix='/api/v1/savedRecipes')

@app.route('/')
def index():
    return 'This is going to be a mouthatruckinnnn bitch'

# Run the app when the program starts!
if __name__ == '__main__':
    models.initialize()
    app.run(debug=DEBUG, port=PORT)
