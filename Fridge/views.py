from django.shortcuts import render
from Fridge.models import *


def index(request):
    type = Type(type='fruit')
    type.save()
    print(type)

    return render(request, 'Fridge/index.html')

def home(response):
    return render(response, 'Fridge/home.html', {})
