# python manage.py makemigrations
# python manage.py migrate
# python manage.py createsuperuser --username admin
# python manage.py shell < add_products.py

from fridge.models import *
import json



with open('fridge/static/products.json') as json_file:
    data = json.load(json_file)
fridge, ok = Fridge.objects.get_or_create(id=0)
fridge.owner_id = 1
fridge.save()
for x in data:
    print(x['name'])
    product, ok = Product.objects.get_or_create(name=x['name'])
    product.img_name = x['image_name']
    typex, ok = Type.objects.get_or_create(name=x['type'])

    product.type = typex

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



