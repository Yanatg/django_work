from django.db import models

# Create your models here.


class Food(models.Model):

    name = models.CharField(max_length=50)
    price = models.IntegerField()
    special_price = models.IntegerField(null=True)
    is_premium = models.BooleanField(default=False)
    promotion_end_date = models.DateTimeField(null=True)
    description = models.TextField(null=True)

    # def __str__(self):
    #     return self.name