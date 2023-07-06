# Generated by Django 4.2.2 on 2023-07-06 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_foods", "0002_food_description_food_special_price_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="food",
            name="image_relative_url",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="food",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="food",
            name="promotion_end_date",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="food",
            name="special_price",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
