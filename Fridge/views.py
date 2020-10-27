from django.shortcuts import render
from Fridge.models import *


def index(request):
    print(request.POST)
    try:
        pole1 = request.POST['pole1']
        test = Test(pole1=pole1)
        test.save()
    except:
        pass

    testy = Test.objects.all()
    print(testy)
    return render(request, 'index.html', {'testy': testy})
