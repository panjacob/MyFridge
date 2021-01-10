from django.http import HttpResponse
from django.shortcuts import render
import fridge.models as models
import fridge.utilis as u


def home(request):
    context = {}
    context["title"] = "Home"
    user = request.user
    context["user"] = user
    if request.user.is_authenticated:
        fridge = models.Fridge.objects.filter(owner=user).first()
        fridgeproducts = models.FridgeProduct.objects.filter(fridge=fridge).all()
        context["fridgeproducts_data"] = u.fridgeproducts_to_data(fridgeproducts)
        recipes = models.Recipe.objects.all()
        context["recipes_data"] = u.recipes_to_data(recipes)
        fridge_data = { "id": fridge.id }
        context["fridge_data"] = fridge_data
    
    return render(request, 'fridge/home.html', context)


def fridge(request):
    context = {}
    context["title"] = "Fridge"
    user = request.user
    context["user"] = user
    fridge = models.Fridge.objects.filter(owner=user).first()
    products = models.Product.objects.all()
    context["products_data"] = u.products_to_data(products)
    fridgeproducts = models.FridgeProduct.objects.filter(fridge=fridge).all()
    context["fridgeproducts_data"] = u.fridgeproducts_to_data(fridgeproducts)
    fridge_data = { "id": fridge.id }
    context["fridge_data"] = fridge_data
    return render(request, 'fridge/fridge.html', context)


def recipe(request):
    context = {}
    context["title"] = "Recipy"
    recipe_id = request.GET.get('id', 1)
    recipe = models.Recipe.objects.filter(id=recipe_id).first()
    context["recipe_data"] = u.recipe_to_data(recipe)
    return render(request, 'fridge/recipe.html', context)


# http://127.0.0.1:8000/fridge_api
# GET - currently unused
# POST - set specified products (by ids) in the user's fridge
def get_products_from_fridge(request):

    if request.method == 'GET':
        pass
        fridge_product = models.FridgeProduct.objects.filter(fridge=fridge_id)
        products = []
        for x in fridge_product:
            products.append(x.product)
        products_json = u.products_to_json(products)
        return HttpResponse(products_json, content_type="text/json-comment-filtered")

    if request.method == 'POST':
        user = request.user
        new_products_id = u.get_products_id_from_request(request)
        fridge = models.Fridge.objects.filter(owner=user).first()

        # remove all products
        fridgeproducts = models.FridgeProduct.objects.filter(fridge=fridge).all()
        for fridgeproduct in fridgeproducts:
            fridgeproduct.delete()
        
        # add new products
        for new_product_id in new_products_id:
            product = models.Product.objects.filter(id=new_product_id).first()

            # placeholder unit and amount
            unit = models.Unit.objects.filter(name="count").first()
            amount = 1

            fridgeproduct = models.FridgeProduct(amount=amount, unit=unit, fridge=fridge, product=product)
            fridgeproduct.save()

        return HttpResponse({'body': 'OK'}, content_type="text/json-comment-filtered")


# http://127.0.0.1:8000/products_api
# currently unused
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
