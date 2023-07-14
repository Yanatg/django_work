from django.shortcuts import render
from .forms import RegisterForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required
# Create your views here.

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm


def register(request: HttpRequest):
    # Post request
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the user to the database
            # Log the user in
            login(request, user)
            return HttpResponseRedirect(reverse("home"))
    else:
        form = RegisterForm()

    # Get request
    context = {"form": form}
    return render(request, "app_users/register.html", context)


@login_required
def dashboard(request: HttpRequest):
    return render(request, "app_users/dashboard.html")

