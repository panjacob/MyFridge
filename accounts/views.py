from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from fridge.models import Fridge
from django.contrib.auth.models import User


def register(request):
    context = {}
    context["title"] = "Register"
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Account created for {username}. You may now log in.")

            # add empty fridge
            user = User.objects.filter(username=username).first()
            fridge = Fridge(owner=user)
            fridge.save()

            return redirect("login")
    else:
        form = UserCreationForm()
    context["form"] = form
    return render(request, 'accounts/register.html', context)

