from django.db.models import *


class Type(Model):
    type = CharField(max_length=64)


class Unit(Model):
    unit = CharField(max_length=64)


class Product(Model):
    name = CharField(max_length=64)
    type = ForeignKey(Type, null=True, on_delete=CASCADE)
    img_name = CharField(max_length=64, null=True)
    amount = IntegerField(null=True)
    unit = ForeignKey(Unit,null=True, on_delete=CASCADE)


class Fridge(Model):
    # owner = ForeignKey() id usera ktory jest zalogowany
    pass


class FridgeProduct(Model):
    fridge = ForeignKey(Fridge, null=True, on_delete=CASCADE)
    product = ForeignKey(Product, null=True, on_delete=CASCADE)


class Recipe(Model):
    name = CharField(max_length=64, null=True)
    short_description = CharField(max_length=256, null=True)
    long_description = CharField(max_length=4096, null=True)
    img_name = CharField(max_length=64, null=True)


class RecipeProduct(Model):
    recpie = ForeignKey(Recipe, null=True, on_delete=CASCADE)
    product = ForeignKey(Product, null=True, on_delete=CASCADE)
