from rest_framework.utils import json

def fridgeproduct_to_productsjson(fridge_product):
    products = []
    for i in range(0, len(fridge_product)):
        product = fridge_product[i].product
        product_json = {}
        product_json['name'] = product.name
        product_json['type'] = product.type.type
        product_json['img_name'] = product.img_name
        product_json['ammount'] = product.ammount
        products.append(product_json)
    return json.dumps(products)