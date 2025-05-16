from django.contrib import admin
from .models import Dishes, Dish, Ticket, Tickets, Review
# Register your models here.
admin.site.register(Review)
admin.site.register(Dishes)
admin.site.register(Dish)
admin.site.register(Ticket)
admin.site.register(Tickets)
