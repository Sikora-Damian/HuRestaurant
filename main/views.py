from django.shortcuts import render
from django.http import HttpResponse
from .models import Dishes, Dish, Tickets, Ticket
from .forms import ContactUs

# Create your views here.

def index(response, id):
    showDishes = Dishes.objects.get(id=id)
    return render(response, "main/dishes.html", {"showDishes":showDishes})

def home(response):
    return render(response, "main/home.html", {})

def contact(response):
    if response.method == "POST":
        form = ContactUs(response.POST)
        if form.is_valid():
            n = form.cleaned_data["name"]
            e = form.cleaned_data["email"]
            top = form.cleaned_data["topic"]
            msg = form.cleaned_data["message"]
            cat = Tickets.objects.get(name="Open")
            t = Ticket(name=n, email=e, topic=top, message=msg, category=cat)
            t.save()
            form = ContactUs()
            return render(response, "main/contact.html", {"form": form, "success": True})
    else:
        form = ContactUs()
    return render(response, "main/contact.html", {"form":form})