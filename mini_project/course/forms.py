from django import forms
from django.forms import TextInput, EmailInput
from .models import Order, Reviews

class OrderCreationForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["name", "phone", "email"]

        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form_modal",
                "placeholder": "Your name..."
            }),
            "phone": TextInput(attrs={
                "class": "form_modal",
                "placeholder": "Your Phone Number...",
                "label": None
            }),
            "email": EmailInput(attrs={
                "class": "form_modal",
                "placeholder": "Your email..."
            })

        }


class ReviewCreationForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ["review"]


