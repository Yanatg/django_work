from django.db import models


class Subscription(models.Model):

    STATUS_CHOICES = [
        ("unapprove", "Unapprove"),
        ("approve", "Approve"),
        ("banned", "Banned"),
    ]
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default="unapprove")
    registered_date = models.DateTimeField(auto_now_add=True)
    food_set = models.ManyToManyField("app_foods.Food")
