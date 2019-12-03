from resources.recipes import recipe
from flask import Flask, g
import models
from flask_cors import CORS

DEBUG = True
PORT = 8000

from resources.recipes import recipe

app = Flask(__name__)

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

@app.route('/')
def index():
    return 'This is going to be a mouthatruckinnnn bitch'

# Run the app when the program starts!
if __name__ == '__main__':
    models.initialize()
    app.run(debug=DEBUG, port=PORT)
