# python manage.py shell < add_products.py
from fridge.models import *

import json


def add_products():
    with open('fridge/static/products.json') as json_file:
        data = json.load(json_file)

    fridge, ok = Fridge.objects.get_or_create(id=0)

    for x in data:
        # print(x['name'])
        product, ok = Product.objects.get_or_create(name=x['name'])
        product.img_name = x['image_name']
        typex, ok = Type.objects.get_or_create(type=x['type'])
        unit, ok = Unit.objects.get_or_create(unit=x['unit'])
        product.type = typex
        product.unit = unit
        product.amount = int(x['amount'])
        product.save()

def add_recipes():
    with open('fridge/static/recipes.json') as json_file:
        data = json.load(json_file)

    for x in data:
        print(x['name'])
        recipe, ok = Recipe.objects.get_or_create(name=x['name'])
        recipe.img_name = x['image_name']
        recipe.short_description =x['short_description']
        recipe.long_description = x['long_description']
        recipe.save()

        print(x['products'])

add_products()
add_recipes()