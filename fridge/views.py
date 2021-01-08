from django.http import HttpResponse
from django.shortcuts import render
import fridge.models as models
import fridge.utilis as u


def home(request):
    context = {}
    context["title"] = "Home"
    return render(request, 'fridge/home.html', context)


# http://127.0.0.1:8000/products
def get_products(request):
    if request.method == 'GET':
        products = models.Product.objects.all()
        products_json = u.products_to_json(products)
        return HttpResponse(products_json, content_type="text/json-comment-filtered")


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


# http://127.0.0.1:8000/fridge
def get_products_from_fridge(request):
    fridge_id = 0
    if request.method == 'GET':
        fridge_product = models.FridgeProduct.objects.filter(fridge=fridge_id)
        products = []
        for x in fridge_product:
            products.append(x.product)
        products_json = u.products_to_json(products)
        return HttpResponse(products_json, content_type="text/json-comment-filtered")
    if request.method == 'POST':
        new_products_id = get_products_id_from_request(request)
        old_products_id = get_products_id_from_fridge(id=fridge_id)

        for new_product in new_products_id:
            if new_product not in old_products_id:
                models.FridgeProduct.objects.create(fridge_id=fridge_id, product_id=new_product).save()
        for old_product in old_products_id:
            if old_product not in new_products_id:
                models.FridgeProduct.objects.get(fridge_id=fridge_id, product_id=old_product).delete()

        print(get_products_id_from_fridge(id=fridge_id))

        return HttpResponse({'body': 'OK'}, content_type="text/json-comment-filtered")
    print(request)


def fridge(request):
    context = {}
    context["title"] = "Fridge"
    return render(request, 'fridge/fridge.html', context)


def recipy(request):
    context = {}
    context["title"] = "Recipy"
    return render(request, 'fridge/recipy.html', context)
