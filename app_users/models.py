from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    address = models.TextField(default='', blank=True)
    phone = models.CharField(max_length=20, default='', blank=True)
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
