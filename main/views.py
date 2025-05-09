from django.shortcuts import render
from django.http import HttpResponse
from .models import Dishes, Dish

# Create your views here.

def index(response, id):
    showDishes = Dishes.objects.get(id=id)
    return render(response, "main/dishes.html", {"showDishes":showDishes})

def home(response):
    return render(response, "main/home.html", {})

def contact(response):
    return render(response, "main/contact.html", {})