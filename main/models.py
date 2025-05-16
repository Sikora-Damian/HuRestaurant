from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from datetime import date

# Create your models here.
class Review(models.Model):
    nickname = models.CharField(max_length=100)
    rating = models.IntegerField()
    date = models.DateField(default=date.today)
    content = models.TextField()
    def __str__(self):
        return self.nickname

class Tickets(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Ticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    category = models.ForeignKey(Tickets, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    topic = models.CharField(max_length=100)
    message = models.CharField(max_length=200)
    answered = models.BooleanField(default=False)
    def save(self, *args, **kwargs):
        try:
            if self.answered:
                self.category = Tickets.objects.get(name="Closed")
            else:
                self.category = Tickets.objects.get(name="Open")
        except Tickets.DoesNotExist:
            pass
        super().save(*args, **kwargs)
    def __str__(self):
        return self.name

class Dishes(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, blank=True)
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Dish(models.Model):
    category = models.ForeignKey(Dishes, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    dishOfTheDay = models.BooleanField(default=False)
    vegetarian = models.BooleanField(default=False)
    vegan = models.BooleanField(default=False)

    def priceInZloty(self):
        return f"{self.price} zł"

    def __str__(self):
        return self.name