# python manage.py shell < add_products.py
from fridge.models import *

import json

with open('fridge/lib/products.json') as json_file:
    data = json.load(json_file)

fridge, ok = Fridge.objects.get_or_create(id=0)

for x in data:
    print(x)
    product, ok = Product.objects.get_or_create(name=x['name'], ammount=x['ammount'])
    typex, ok = Type.objects.get_or_create(type=" ")
    unit, ok = Unit.objects.get_or_create(unit=x['unit'])
    product.type = typex
    product.unit = unit
    product.save()
    fridge_product, ok = FridgeProduct.objects.get_or_create(product=product, fridge=fridge)
