from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from .models import Item

# Creating a register form class
class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model=User
        fields = ["username", "email", "password1", "password2"]




# Create your views here.
def index(request):
    context = {} #dictionary. This is optional information that we can pass from the view
    context["Title"] = "This is a test"
    return render(request, "home.html", context)

def products(request):
    return render(request, "products.html", {})

def shop(request):
    item_list = Item.objects.all()

    context = {"item_list":item_list}
    return render(request, "shop.html", context)

def user_login(request): 
    if request.method == "POST":
        form = AuthenticationForm(request.POST)
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password1=password)

        if user is not None:
            form = login(request, user)

            return redirect("home")
    else:
        form = AuthenticationForm()


    return render(request, "registration/user_login.html", {"form":form})


def user_register(request):
    if request.method =="POST":
        form = RegistrationForm(request.POST)
        if form.isvalid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = RegistrationForm()

    return render(request, "registration/user_register.html", {"form":form})




