# python manage.py makemigrations
# python manage.py migrate
# python manage.py shell < add_products.py
# python manage.py createsuperuser --username admin

from fridge.models import *
import json
from django.contrib.auth.models import User

# u = User.objects.get(username='admin')
# u.set_password('admin')
# u.save()

with open('fridge/static/products.json') as json_file:
    data = json.load(json_file)
fridge, ok = Fridge.objects.get_or_create(id=0)
for x in data:
    print(x['name'])
    product, ok = Product.objects.get_or_create(name=x['name'])
    product.img_name = x['image_name']
    typex, ok = Type.objects.get_or_create(name=x['type'])
    # unit, ok = Unit.objects.get_or_create(name=x['unit'])
    product.type = typex
    # product.unit = unit
    # product.amount = int(x['amount'])
    product.save()



with open('fridge/static/recipes.json') as json_file:
    data = json.load(json_file)

for x in data:
    print(x['name'])
    recipe, ok = Recipe.objects.get_or_create(name=x['name'])
    recipe.img_name = x['image_name']
    recipe.short_description = x['short_description']
    recipe.long_description = x['long_description']
    recipe.save()
    for product_id in x['products']:
        print(recipe.id, product_id)
        recipe_product, ok = RecipeProduct.objects.get_or_create(recipe_id=recipe.id, product_id=product_id)



