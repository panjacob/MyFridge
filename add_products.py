# python manage.py shell < add_products.py
from fridge.models import *

import json

with open('fridge/static/products.json') as json_file:
    data = json.load(json_file)

fridge, ok = Fridge.objects.get_or_create(id=0)

for x in data:
    if not Product.objects.get(name=x['name']).exists():
        product, ok = Product.objects.get_or_create(name=x['name'], ammount=x['ammount'])
        product.img_name = x['image_name']
        typex, ok = Type.objects.get_or_create(type=x['type'])
        unit, ok = Unit.objects.get_or_create(unit=x['unit'])
        product.type = typex
        product.unit = unit
        product.save()
        fridge_product, ok = FridgeProduct.objects.get_or_create(product=product, fridge=fridge)
