from django import forms
from app_foods.models import Food


class SubscriptionForm(forms.Form):
    name = forms.CharField(label="Your Name", max_length=60, required=True)
    email = forms.EmailField(label="Your Email", max_length=60, required=True)
    food_set = forms.ModelMultipleChoiceField(
        label="Your interesting Menu",
        required=True,
        queryset=Food.objects.order_by('-is_premium'),
    )
    accepted = forms.BooleanField(label="Accept Terms and Conditions", required=True)

