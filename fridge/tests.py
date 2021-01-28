from django.test import TestCase
import fridge.models as models


# python manage.py test fridge


class TestFridge(TestCase):
    def test_create(self):
        product = models.Product.objects.create(name="test1")
        product.save()
        assert product.id == 1

    def test_get(self):
        product = models.Product.objects.create(name="test1")
        product.save()
        product_get = models.Product.objects.get(name="test1")
        assert product_get.id == 1

    def test_whole_import(self):
        import json

        with open('fridge/static/products.json') as json_file:
            data = json.load(json_file)
        fridge, ok = models.Fridge.objects.get_or_create(id=0)
        fridge.save()
        for x in data:
            print(x['name'])
            product, ok = models.Product.objects.get_or_create(name=x['name'])
            product.img_name = x['image_name']
            typex, ok = models.Type.objects.get_or_create(name=x['type'])
            product.type = typex
            product.save()

        with open('fridge/static/recipes.json') as json_file:
            data = json.load(json_file)
        for x in data:
            print(x['name'])
            recipe, ok = models.Recipe.objects.get_or_create(name=x['name'])
            recipe.img_name = x['image_name']
            recipe.short_description = x['short_description']
            recipe.long_description = x['long_description']
            recipe.save()
            for product_id in x['products']:
                print(recipe.id, product_id)
                recipe_product, ok = models.RecipeProduct.objects.get_or_create(recipe_id=recipe.id,
                                                                                product_id=product_id)

