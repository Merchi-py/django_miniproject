from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView

from .models import Order
from .forms import OrderCreationForm

class HomePageView(ListView):
    template_name = "course/home_page.html"

    model = Order
    form_class = OrderCreationForm

class OrderCreationView(CreateView):
    pass
