from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from app_general.forms import SubscriptionModelForm


def home(request):
    return render(request, "app_general/home.html")


def about(request):
    return render(request, "app_general/about.html")


def subscription(request):
    form = SubscriptionModelForm(request.POST)
    if request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse("subscription_thankyou"))
    else:
        form = SubscriptionModelForm()
    context = {"form": form}
    return render(request, "app_general/subscription_form.html", context)


def subscription_thankyou(request):
    return render(request, "app_general/subscription_thankyou.html")