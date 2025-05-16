from django.urls import path
from django.contrib.auth.views import LogoutView

from . import views

urlpatterns = [
    # path("<int:id>", views.index, name="index"),
    path("",views.home, name="home"),
    path("dishes/", views.dishes, name="dishes"),
    path("dishes/<slug:slug>/", views.dishCategory, name="dish_category"),
    path("contact/",views.contact, name="contact"),
    path("profile/",views.profile, name="profile"),
    path("logout/", LogoutView.as_view(), name="logout"),
]