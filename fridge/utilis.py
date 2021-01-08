from rest_framework.utils import json


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

