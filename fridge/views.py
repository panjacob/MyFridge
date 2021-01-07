from django.http import HttpResponse
from django.shortcuts import render
import fridge.models as models
import fridge.utilis as u


def home(request):
    context = {}
    context["title"] = "Home"
    return render(request, 'fridge/home.html', context)

# http://127.0.0.1:8000/products?id=0
def get_products_from_fridge(request):
    if request.method == 'GET':
        fridge_id = request.GET.get('id', None)
        if id is not None:
            fridge_product = models.FridgeProduct.objects.filter(fridge_id=fridge_id)
            products_json = u.fridgeproduct_to_productsjson(fridge_product)
            return HttpResponse(products_json, content_type="text/json-comment-filtered")

def fridge(request):
    context = {}
    context["title"] = "Fridge"
    return render(request, 'fridge/fridge.html', context)

def recipy(request):
    context = {}
    context["title"] = "Recipy"
    return render(request, 'fridge/recipy.html', context)
