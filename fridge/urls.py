from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='fridge-home'),
    path('products', views.get_products_from_fridge, name='get_products_from_fridge')
]