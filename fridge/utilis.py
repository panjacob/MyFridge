from rest_framework.utils import json
import fridge.models as models


def products_to_json(products):
    products_arr = []
    for product in products:
        product_json = {}
        product_json['id'] = product.id
        product_json['name'] = product.name
        product_json['type'] = product.type.type
        product_json['img_name'] = product.img_name
        products_arr.append(product_json)
    return json.dumps(products_arr)


def fridgeproducts_to_dictionaries(fridgeproducts):
    result = []
    for fridgeproduct in fridgeproducts:
        tmp = {}
        tmp['amount'] = fridgeproduct.amount
        tmp['unit'] = fridgeproduct.unit.name
        tmp['name'] = fridgeproduct.product.name
        tmp['img_name'] = fridgeproduct.product.img_name
        tmp['type'] = fridgeproduct.product.type.name
        result.append(tmp)
    return result


def get_products_id_from_request(request):
    new_products_id = []
    decoded = request.body.decode('utf-8')
    array = decoded.split(',')
    if array == ['']:
        return []
    for product_id in array:
        new_products_id.append(int(product_id))
    return new_products_id


def get_products_id_from_fridge(id):
    fridge_product = models.FridgeProduct.objects.filter(fridge=id)
    old_products_id = []
    for x in fridge_product:
        old_products_id.append(x.product.id)
    return old_products_id


def recipe_to_json(recipe, recipe_products):
    recipe_json = {"id": recipe.id, "name": recipe.name, "img_name": recipe.img_name,
                   "short_description": recipe.short_description, "long_description": recipe.long_description}

    products = []
    for recipe_product in recipe_products:
        product = {"name": recipe_product.product.name, "img_name": recipe_product.product.img_name,
                   "type": recipe_product.product.type.type}
        products.append(product)
    recipe_json['products'] = products
    return json.dumps(recipe_json, ensure_ascii=False).encode('utf-8')


def recipes_to_json(recipes):
    recipes_json = []
    for recipe in recipes:
        recipe_json = {"id": recipe.id, "name": recipe.name, "short_description": recipe.short_description,
                       "img_name": recipe.img_name}
        recipes_json.append(recipe_json)
    return json.dumps(recipes_json)
