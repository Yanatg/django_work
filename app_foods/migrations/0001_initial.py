# Generated by Django 4.2.2 on 2023-06-26 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Food",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("price", models.IntegerField()),
                ("is_premium", models.BooleanField(null=True)),
                ("promotion_end_date", models.DateTimeField(null=True)),
            ],
        ),
    ]
