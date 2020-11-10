from django.db.models import *


# python manage.py makemigrations Fridge
# python manage.py migrate


class Type(Model):
    type = CharField(max_length=64)


class Unit(Model):
    unit = CharField(max_length=64)


class Product(Model):
    name = CharField(max_length=64)
    type = ForeignKey(Type, on_delete=CASCADE)
    calories = IntegerField()
    carbohydrates = IntegerField()
    fat = IntegerField()
    protein = IntegerField()
    ammount = IntegerField()
    unit = ForeignKey(Unit, on_delete=CASCADE)


class Fridge(Model):
    product = ForeignKey(Product, on_delete=CASCADE)
