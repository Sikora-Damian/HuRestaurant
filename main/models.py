from django.db import models

# Create your models here.
class Tickets(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Ticket(models.Model):
    category = models.ForeignKey(Tickets, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    topic = models.CharField(max_length=100)
    message = models.CharField(max_length=200)
    answered = models.BooleanField(default=False)
    def __str__(self):
        return self.name

class Dishes(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Dish(models.Model):
    menu = models.ForeignKey(Dishes, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    dishOfTheDay = models.BooleanField(default=False)

    def __str__(self):
        return self.name