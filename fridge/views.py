from django.shortcuts import render
import fridge.models as models


def home(request):
    context = {}
    context["products"] = models.FridgeProduct.objects.filter(fridge_id=0)
    context["title"] = "Home"
    return render(request, 'fridge/home.html', context)
