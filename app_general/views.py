from django.shortcuts import render
from app_foods.models import Food
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from app_general.forms import SubscriptionForm
from .models import Subscription


def home(request):
    return render(request, "app_general/home.html")


def about(request):
    return render(request, "app_general/about.html")


def subscription(request):
    if request.POST:
        return HttpResponseRedirect(reverse("subscription_thankyou"))
    form = SubscriptionForm()
    context = {"form": form}
    return render(request, "app_general/subscription_form.html", context)


def subscription_thankyou(request):
    return render(request, "app_general/subscription_thankyou.html")