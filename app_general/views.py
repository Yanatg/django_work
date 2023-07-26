from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from app_general.forms import SubscriptionModelForm
from django.http import HttpRequest
from datetime import datetime, timedelta


def home(request: HttpRequest):
    theme = request.COOKIES.get("theme")
    return render(request, "app_general/home.html")


def about(request: HttpRequest):
    return render(request, "app_general/about.html")


def subscription(request: HttpRequest):
    form = SubscriptionModelForm(request.POST)
    if request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse("subscription_thankyou"))
    else:
        form = SubscriptionModelForm()
    context = {"form": form}
    return render(request, "app_general/subscription_form.html", context)


def subscription_thankyou(request: HttpRequest):
    return render(request, "app_general/subscription_thankyou.html")


def change_theme(request: HttpRequest):
    # Referer
    referer = request.headers.get("Referer")
    if referer:
        response = HttpResponseRedirect(referer)
    else:
        response = HttpResponseRedirect(reverse("home"))

    theme = request.GET.get("theme")
    if theme == "dark":
        expired_date = datetime.now() + timedelta(days=30)
        response.set_cookie("theme", "dark", expires=expired_date)
    elif theme == "light":
        response.delete_cookie("theme")

    return response