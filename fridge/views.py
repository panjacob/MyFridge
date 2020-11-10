from django.shortcuts import render

# Create your views here.
def home(request):
    context = {}
    context["title"] = "Home"
    return render(request, 'fridge/home.html', context)