from django.http import HttpResponse
from django.shortcuts import render
import fridge.models as models
import fridge.utilis as u


def home(request):
    context = {}
    context["title"] = "Home"
    return render(request, 'fridge/home.html', context)


def fridge(request):
    context = {}
    context["title"] = "Fridge"
    return render(request, 'fridge/fridge.html', context)


def fridge_test(request):
    context = {}
    context["title"] = "Fridge test"
    user = request.user
    context["user"] = user
    fridge = models.Fridge.objects.filter(owner=user)
    if len(fridge) == 0:
        fridge = models.Fridge(owner=user)
        fridge.save()
    else:
        fridge = fridge.first()

    fridgeproducts = models.FridgeProduct.objects.filter(fridge=fridge).all()
    context["fridgeproducts_data"] = u.fridgeproducts_to_dictionaries(fridgeproducts)
    fridge_data = { "id": fridge.id }
    context["fridge_data"] = fridge_data
    return render(request, 'fridge/fridge_test.html', context)


def recipy(request):
    context = {}
    context["title"] = "Recipy"
    return render(request, 'fridge/recipy.html', context)


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
        new_products_id = u.get_products_id_from_request(request)
        old_products_id = u.get_products_id_from_fridge(id=fridge_id)

        for new_product in new_products_id:
            if new_product not in old_products_id:
                models.FridgeProduct.objects.create(fridge_id=fridge_id, product_id=new_product).save()
        for old_product in old_products_id:
            if old_product not in new_products_id:
                models.FridgeProduct.objects.get(fridge_id=fridge_id, product_id=old_product).delete()

        print(u.get_products_id_from_fridge(id=fridge_id))

        return HttpResponse({'body': 'OK'}, content_type="text/json-comment-filtered")
    print(request)


# http://127.0.0.1:8000/products
def get_products(request):
    if request.method == 'GET':
        products = models.Product.objects.all()
        products_json = u.products_to_json(products)
        return HttpResponse(products_json, content_type="text/json-comment-filtered")


# http://127.0.0.1:8000/recipe?id=1
def get_recipe(request):
    if request.method == 'GET':
        recipe_id = request.GET.get('id', 1)
        recipe = models.Recipe.objects.get(id=recipe_id)
        recipe_product = models.RecipeProduct.objects.filter(recipe_id=recipe_id)
        recipe_json = u.recipe_to_json(recipe, recipe_product)
        print(recipe_json)
        return HttpResponse(recipe_json, content_type="text/json-comment-filtered")


# http://127.0.0.1:8000/recipes
def get_recipes(request):
    if request.method == 'GET':
        recipes = models.Recipe.objects.all()
        recipes_json = u.recipes_to_json(recipes)
        return HttpResponse(recipes_json, content_type="text/json-comment-filtered")
