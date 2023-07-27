from django.urls import path
from . import views

urlpatterns = [
    path("", views.foods, name="foods"),
    path("<int:food_id>", views.food, name="food"),
    path("<int:food_id>/favourite", views.favourite_food, name="favourite_food"),
    path("<int:food_id>/unfavourite", views.unfavourite_food, name="unfavourite_food"),
]
