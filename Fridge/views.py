from django.shortcuts import render
from Fridge.models import *


def index(request):
    type = Type(type='fruit')
    type.save()
    print(type)

    return render(request, 'Fridge/index.html')

def home(response):
    return render(response, 'Fridge/home.html', {})

def signin(response):
    return render(response, 'Fridge/signin.html', {})

def register(response):
    return render(response, 'Fridge/register.html', {})
