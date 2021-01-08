from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='fridge-home'),
    path('fridge.html', views.fridge, name='fridge-fridge'),
    path('home.html', views.home, name='fridge-home'),
    path('recipy.html', views.recipy, name='fridge-recipy'),
    path('products', views.get_products, name='get_products'),
    path('recipe', views.get_recipe, name='get_recipe'),
    path('recipes', views.get_recipes, name='get_recipes'),
    path('fridge', views.get_products_from_fridge, name='get_products_from_fridge')
]
