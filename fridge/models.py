from django.db.models import *


# python manage.py makemigrations Fridge
# python manage.py migrate


class Type(Model):
    type = CharField(max_length=64, null=True)


class Unit(Model):
    unit = CharField(max_length=64, null=True)


class Product(Model):
    name = CharField(max_length=64, null=True)
    type = ForeignKey(Type, null=True, on_delete=CASCADE)
    img_name = CharField(max_length=64, null=True)
    # Narazie nie potrzebne
    # calories = IntegerField()
    # carbohydrates = IntegerField()
    # fat = IntegerField()
    # protein = IntegerField()
    ammount = IntegerField()
    unit = ForeignKey(Unit, null=True, on_delete=CASCADE)


class Fridge(Model):
    pass


class FridgeProduct(Model):
    fridge = ForeignKey(Fridge, null=True, on_delete=CASCADE)
    product = ForeignKey(Product, null=True, on_delete=CASCADE)
