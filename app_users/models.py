from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(AbstractUser):
    email = models.EmailField(max_length=254, unique=True)


class Profile(models.Model):
    address = models.TextField(default='', blank=True)
    phone = models.CharField(max_length=20, default='', blank=True)
    user = models.OneToOneField("app_users.CustomUser", on_delete=models.CASCADE)




