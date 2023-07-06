from django.contrib import admin
from .models import Food

# Register your models here.


class FoodAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'is_premium', 'promotion_end_date']
    search_fields = ['name']
    list_filter = ['is_premium']


admin.site.register(Food, FoodAdmin)
