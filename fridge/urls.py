from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='fridge_home'),
    path('home', views.home, name='fridge_home'),
    path('fridge', views.fridge, name='fridge_fridge'),
    path('recipe', views.recipe, name='fridge_recipe_details'),
    path('products_api', views.get_products, name='get_products'),
    path('fridge_api', views.get_products_from_fridge, name='get_products_from_fridge'),
]
