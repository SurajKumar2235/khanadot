from django.forms.models import inlineformset_factory
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import *
import re


class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        max_length=254, help_text="Required. Inform a valid email address."
    )
    name = forms.CharField(max_length=255, required=True)
    phone_number = forms.CharField(max_length=15, required=True)
    address = forms.CharField(widget=forms.Textarea)
    user_type = forms.ChoiceField(choices=User.USER_TYPES, required=True)

    class Meta:
        model = get_user_model()
        fields = (
            "email",
            "username",
            "name",
            "phone_number",
            "address",
            "user_type",
            "password1",
            "password2",
        )


class OrderForm(forms.Form):
    items = forms.MultipleChoiceField(choices=[], widget=forms.CheckboxSelectMultiple)
    delivery_address = forms.CharField(widget=forms.Textarea(attrs={"rows": 4}))

    def __init__(self, restaurant_id, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        menu_items = MenuItem.objects.filter(
            restaurant_id=restaurant_id, availability=True
        )
        self.fields["items"].choices = [
            (item.menu_item_id, f"{item.name} - ${item.price}") for item in menu_items
        ]


class AadhaarValidationForm(forms.Form):
    aadhaar_number = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Enter Aadhaar Number"}),
    )
