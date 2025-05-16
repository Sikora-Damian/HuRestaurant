from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Dishes, Dish, Tickets, Ticket, Review
from .forms import ContactUs
from itertools import groupby
from operator import attrgetter

# Create your views here.

def index(response, id):
    showDishes = Dishes.objects.get(id=id)
    return render(response, "main/dishes.html", {"showDishes":showDishes})

def home(request):
    dishes = Dish.objects.filter(dishOfTheDay=True).select_related("category").order_by("category__name")
    grouped = [(category, list(food)) for category, food in groupby(dishes, key=attrgetter("category"))]
    reviews = Review.objects.all().order_by('-date')
    return render(request, "main/home.html", {"grouped": grouped, "reviews": reviews})

def dishes(response):
    allDishes = Dish.objects.all()
    return render(response, "main/dishes.html", {"dishes": allDishes})

def dishCategory(request, slug):
    showDishes = get_object_or_404(Dishes, slug=slug)
    return render(request, "main/dishes.html", {"showDishes": showDishes})

def contact(response):
    if response.method == "POST":
        form = ContactUs(response.POST)
        if form.is_valid():
            n = form.cleaned_data["name"]
            e = form.cleaned_data["email"]
            top = form.cleaned_data["topic"]
            msg = form.cleaned_data["message"]
            t = Ticket(name=n, email=e, topic=top, message=msg, user=response.user if response.user.is_authenticated else None)
            t.save()
            form = ContactUs()
            return render(response, "main/contact.html", {"form": form, "success": True})
    else:
        if response.user.is_authenticated:
            initial_data = {
                "name": response.user.username,
                "email": response.user.email,
            }
            form = ContactUs(initial=initial_data)
        else:
            form = ContactUs()
    return render(response, "main/contact.html", {"form":form})

@login_required
def profile(response):
    tickets = Ticket.objects.filter(user=response.user)
    return render(response, "main/profile.html", {"tickets": tickets})
    # return render(response, "main/profile.html", {})