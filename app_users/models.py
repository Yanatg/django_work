from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(AbstractUser):
    email = models.EmailField(max_length=254, unique=True)
    favourite_food_set = models.ManyToManyField(
        to="app_foods.Food",
        through="app_users.UserFavoriteFood",
        related_name="favourite_user_set"
    )


class Profile(models.Model):
    address = models.TextField(default='', blank=True)
    phone = models.CharField(max_length=20, default='', blank=True)
    user = models.OneToOneField("app_users.CustomUser", on_delete=models.CASCADE)


class UserFavoriteFood(models.Model):
    levels = [
        (1, 'good'),
        (2, 'like'),
        (3, 'love'),
    ]
    level = models.SmallIntegerField(choices=levels, default=1)
    user = models.ForeignKey(
        "app_users.CustomUser",
        on_delete=models.CASCADE,
        related_name="favorite_food_pivot_set"
    )
    food = models.ForeignKey(
        "app_foods.Food",
        on_delete=models.CASCADE,
        related_name="favorite_user_pivot_set"
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'food'],
                name='unique_user_food'
            )
        ]

    def level_label(self):
        return [l for l in self.levels if l[0] == self.level][0][1]

