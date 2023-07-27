from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from app_users.models import CustomUser
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from app_users.forms import ExtendedProfileForm, RegisterForm, UserProfileForm
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from app_users.utilts.activation_token_generator import activation_token_generator
from django.utils.encoding import force_bytes

# Create your views here.


def register(request: HttpRequest):
    # POST
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            # Register & Login

            # register user
            user: CustomUser = form.save(commit=False)
            user.is_active = False
            user.save()

            # login(request, user)

            # build email body HTML
            context = {
                "protocol": request.scheme,
                "host": request.get_host(),
                "uidb64": urlsafe_base64_encode(force_bytes(user.id)),
                "token": activation_token_generator.make_token(user),
            }
            email_body = render_to_string("app_users/activate_email.html", context)

            # send email
            email = EmailMessage(
                to=[user.email],
                subject="Activate your account",
                body=email_body,
            )
            email.send()
            # redirect to thankyou page
            return HttpResponseRedirect(reverse("register_thankyou"))
    else:
        form = RegisterForm()

    # GET
    context = {"form": form}
    return render(request, "app_users/register.html", context)


def register_thankyou(request: HttpRequest):
    return render(request, "app_users/register_thankyou.html")


def activate(request: HttpRequest, uidb64: str, token: str):
    # decode user id
    id = urlsafe_base64_decode(uidb64).decode()
    title = "Activate your account"
    content = "login to your account"
    try:
        user: CustomUser = CustomUser.objects.get(id=id)
        activated = activation_token_generator.check_token(user, token)
        if not activated:
            raise Exception("Invalid token")
        user.is_active = True
        user.save()
    except:
        print("User not found")
        title = "Invalid activation link"
        content = "Please try again"

    context = {
        "title": title,
        "description": content
    }
    return render(request, "app_users/activate.html", context)


@login_required
def dashboard(request: HttpRequest):
    favourite_food_pivot = request.user.favorite_food_pivot_set.order_by("level")
    context = {"favourite_food_pivot": favourite_food_pivot}
    return render(request, "app_users/dashboard.html", context)


@login_required
def profile(request: HttpRequest):
    user = request.user

    # POST
    if request.method == "POST":
        form = UserProfileForm(request.POST, instance=user)
        is_new_profile = False
        try:
            # Will be updated profile
            extended_form = ExtendedProfileForm(request.POST, instance=user.profile)
        except:
            # Will be created profile
            is_new_profile = True
            extended_form = ExtendedProfileForm(request.POST)

        if form.is_valid() and extended_form.is_valid():
            form.save()
            if is_new_profile:
                # Create profile
                profile = extended_form.save(commit=False)
                profile.user = user
                profile.save()
            else:
                # Update profile
                extended_form.save()
            # return HttpResponseRedirect(reverse("profile"))
            response = HttpResponseRedirect(reverse("profile"))
            response.set_cookie("is_saved", True)
            return response
    else:
        form = UserProfileForm(instance=user)
        try:
            extended_form = ExtendedProfileForm(instance=user.profile)
        except:
            extended_form = ExtendedProfileForm()

    #
    is_saved = request.COOKIES.get("is_saved")
    flash_message = "saved successfully" if is_saved else None
    context = {
        "form": form,
        "extended_form": extended_form,
        "flash_message": flash_message
    }
    if is_saved:
        response = render(request, "app_users/profile.html", context)
        response.delete_cookie("is_saved")
        return response
    return render(request, "app_users/profile.html", context)

