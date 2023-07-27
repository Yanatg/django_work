from django.shortcuts import render
from .models import Food
from .forms import FavouriteFoodForm
from django.contrib.auth.decorators import login_required
from app_users.models import UserFavoriteFood
from django.http import HttpResponseRedirect
from django.urls import reverse


def foods(request):
    all_foods = Food.objects.all().order_by('-is_premium')
    context = {'foods': all_foods}
    return render(request, "app_foods/foods.html", context)


def food(request, food_id):
    one_food = None
    is_favourite_food = False
    try:
        one_food = Food.objects.get(id=food_id)
        if request.user.is_authenticated:
            user_favourite_food = UserFavoriteFood.objects.get(
                user=request.user,
                food=one_food
            )
            is_favourite_food = user_favourite_food is not None
    except UserFavoriteFood.DoesNotExist:
        pass
    form = FavouriteFoodForm()
    context = {
        'food': one_food,
        'form': form,
        'is_favourite_food': is_favourite_food
    }
    return render(request, 'app_foods/food.html', context)


@login_required
def favourite_food(request, food_id):
    if request.method == "POST":
        form = FavouriteFoodForm(request.POST)
        if form.is_valid():
            obj, is_created = UserFavoriteFood.objects.update_or_create(
                user=request.user,
                food_id=food_id,
                defaults={'level': form.cleaned_data['level']}
            )
            print("Created favourite" if is_created else "Updated favourite ")
            return HttpResponseRedirect(request.headers.get('Referer'))

    return HttpResponseRedirect(request.headers.get('Referer'))


@login_required
def unfavourite_food(request, food_id):
    if request.method == "POST":
        request.user.favourite_food_set.remove(Food(id=food_id))
    return HttpResponseRedirect(reverse("dashboard"))
