from django.shortcuts import render
from .models import Food


def foods(request):
    all_foods = Food.objects.all().order_by('-is_premium')
    context = {'foods': all_foods}
    return render(request, "app_foods/foods.html", context)


def food(request, food_id):
    one_food = None
    try:
        one_food = Food.objects.get(id=food_id)
    except Food.DoesNotExist:
        pass
    context = {'food': one_food}
    return render(request, 'app_foods/food.html', context)
