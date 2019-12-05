from peewee import *
from flask_login import UserMixin

DATABASE = SqliteDatabase('recipes.sqlite')

class Recipe(Model):
    sourceURL = CharField()
    spoonacularId = IntegerField()
    title = CharField()
    readyInMinutes = IntegerField()
    servings = IntegerField()
    image = CharField()

    class Meta:
        database = DATABASE


class BreakfastRecipe(Model):
    sourceURL = CharField()
    spoonacularId = IntegerField()
    title = CharField()
    readyInMinutes = IntegerField()
    servings = IntegerField()
    image = CharField()

    class Meta:
        database = DATABASE


class User(Model, UserMixin):
    email = CharField(unique=True)
    password = CharField()

    class Meta:
        db_table = 'users'
        database = DATABASE


# class SavedRecipe(Model):
#     sourceURL = CharField()
#     spoonacularId = IntegerField()
#     user = ForeignKeyField(User, backref='recipes')

#     class Meta:
#         db_table = 'savedRecipes'
#         database = DATABASE


def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Recipe, User, BreakfastRecipe], safe=True)
    print("TABLES Created")
    DATABASE.close()
