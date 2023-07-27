from django import forms
from app_users.models import UserFavoriteFood


class FavouriteFoodForm(forms.ModelForm):
    class Meta:
        model = UserFavoriteFood
        fields = ["level"]
        widgets = {
            "level": forms.RadioSelect(attrs={"class": "form-control"}),
        }
        labels = {
            "level": "How much do you like this food?",
        }
        help_texts = {
            "level": "Select a level",
        }
