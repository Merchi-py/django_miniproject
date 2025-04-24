from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('',  views.HomePageView.as_view(), name="home_page"),
    path('',  views.OrderCreationView.as_view(), name="order_create"),
]
