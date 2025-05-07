from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView
from django.http import JsonResponse, HttpResponseRedirect

from .models import Order, Reviews
from .forms import OrderCreationForm, ReviewCreationForm

class HomePageView(ListView):
    template_name = "course/home_page.html"
    model = Reviews
    context_object_name = "reviews"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form_order"] = OrderCreationForm()
        context["form_review"] = ReviewCreationForm()
        return context


class OrderCreationView(CreateView):
    http_method_names = ["post"]

    model = Order
    form_class = OrderCreationForm

    def form_valid(self, form):
        self.object = form.save()
        return JsonResponse({"status": "success"}, status=200)

class ReviewCreate(CreateView):
    http_method_names = ["post"]

    model = Reviews
    form_class = ReviewCreationForm

    def form_valid(self, form):
        self.object = form.save()
        return JsonResponse({"status": "success"}, status=200)




