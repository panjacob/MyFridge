from django.db.models import *
from django.contrib.auth.models import User


class Type(Model):
    name = CharField(max_length=64)


class Unit(Model):
    name = CharField(max_length=64)


class Product(Model):
    name = CharField(max_length=64)
    type = ForeignKey(Type, null=True, on_delete=CASCADE)
    img_name = CharField(max_length=64, null=True)


class Fridge(Model):
    owner = ForeignKey(User, on_delete=CASCADE, null=True)


class FridgeProduct(Model):
    amount = IntegerField(null=True)
    unit = ForeignKey(Unit,null=True, on_delete=CASCADE)
    fridge = ForeignKey(Fridge, null=True, on_delete=CASCADE)
    product = ForeignKey(Product, null=True, on_delete=CASCADE)


class Recipe(Model):
    name = CharField(max_length=64, null=True)
    short_description = CharField(max_length=256, null=True)
    long_description = CharField(max_length=4096, null=True)
    img_name = CharField(max_length=64, null=True)


class RecipeProduct(Model):
    recipe = ForeignKey(Recipe, null=True, on_delete=CASCADE)
    product = ForeignKey(Product, null=True, on_delete=CASCADE)
