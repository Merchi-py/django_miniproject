from django import forms
from .models import Order, Reviews

class OrderCreationForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["name", "phone", "email"]

class ReviewCreationForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ["review"]


