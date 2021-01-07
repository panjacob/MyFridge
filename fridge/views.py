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


# http://127.0.0.1:8000/fridge
def get_products_from_fridge(request):
    fridge_id = 0 #
    if request.method == 'GET':
        fridge_product = models.FridgeProduct.objects.filter(fridge=fridge_id)
        products = []
        for x in fridge_product:
            products.append(x.product)
        products_json = u.products_to_json(products)
        return HttpResponse(products_json, content_type="text/json-comment-filtered")
    if request.method == 'POST':
        print(request.POST)
        return HttpResponse({}, content_type="text/json-comment-filtered")


def fridge(request):
    context = {}
    context["title"] = "Fridge"
    return render(request, 'fridge/fridge.html', context)


def recipy(request):
    context = {}
    context["title"] = "Recipy"
    return render(request, 'fridge/recipy.html', context)
