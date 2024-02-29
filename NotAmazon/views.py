from django.shortcuts import render
from django.http import HttpResponse

from .models import Item

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

def login(request):
    return render(request, "login.html", {})

def signup(request):
    return render(request, "signup.html", {})




