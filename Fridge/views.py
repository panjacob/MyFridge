from django.shortcuts import render
from Fridge.models import *


def index(request):
    type = Type(type='fruit')
    type.save()
    print(type)

    return render(request, 'index.html')
