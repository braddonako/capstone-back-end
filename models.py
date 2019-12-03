from peewee import *

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


def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Recipe], safe=True)
    print("TABLES Created")
    DATABASE.close()