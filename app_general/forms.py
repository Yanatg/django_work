from django import forms
from app_foods.models import Food
from .models import Subscription


class FoodMultipleChoiceField(forms.ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        return obj.name


class SubscriptionForm(forms.Form):
    name = forms.CharField(label="Your Name", max_length=60, required=True)
    email = forms.EmailField(label="Your Email", max_length=60, required=True)
    food_set = FoodMultipleChoiceField(
        label="Your interesting Menu",
        required=True,
        queryset=Food.objects.order_by('-is_premium'),
        widget=forms.CheckboxSelectMultiple,
    )
    accepted = forms.BooleanField(label="Accept Terms and Conditions", required=True)


class SubscriptionModelForm(forms.ModelForm):
    food_set = FoodMultipleChoiceField(
        label="Your interesting Menu",
        required=True,
        queryset=Food.objects.order_by('-is_premium'),
        widget=forms.CheckboxSelectMultiple,
    )
    accepted = forms.BooleanField(label="Accept Terms and Conditions", required=True)
    class Meta:
        model = Subscription
        fields = ["name", "email", "food_set"]